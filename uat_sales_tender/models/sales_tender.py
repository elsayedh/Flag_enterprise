# -*- coding: utf-8 -*-

# from odoo import models, fields, api, _
# from odoo.exceptions import UserError


from odoo import api, fields, models, _, SUPERUSER_ID
# from odoo.osv import expression
# from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.exceptions import UserError
# from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES


_STATES = [
    ('draft', 'Draft'),
    ('approve', 'Approved'),
    ('print', 'Printed'),
    ('confirm', 'Confirmed'),
    ('cancel', 'Canceled'),
]

class SalesTender(models.Model):
    _name = "sales.tender"
    _inherit = "mail.thread"


    name = fields.Char(string='Tender Reference', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))

    # Department = fields.Many2one()
    tender_ids = fields.One2many("sales.tender.lines", "tender_id")

    state = fields.Selection(selection=_STATES,
                             string='Status',
                             index=True,
                             track_visibility='onchange',
                             required=True,
                             copy=False,
                             default='draft')

    # samples_att = fields.Many2many('ir.attachment', 'doc_attach_rel', 'doc_id', 'attach_id', string="Samples Attachment")
    # contract_att = fields.Many2many('ir.attachment', 'doc_attach_rel', 'doc_id', 'attach_id', string="Contract Attachment")

    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    partner_id = fields.Many2one('res.partner', string="Partner", domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]")

    ordering_date = fields.Date(string="Ordering Date", tracking=True)
    delivery_date = fields.Date(string='Delivery Date', tracking=True)

    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    c_state = fields.Many2one("res.country.state", string='State', ondelete='restrict')
    country = fields.Many2one('res.country', string='Country', ondelete='restrict')
    website = fields.Char()


    @api.model
    def create(self, vals):
        # assigning the sequence for the record
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('sales.tender') or _('New')
        res = super(SalesTender, self).create(vals)
        return res


    def create_tender_so(self):
        self.button_confirm()
        tender_id = self.env['sale.order']

        tender_obj = tender_id.create({
            'partner_id': self.partner_id.id,
            'company_id': self.company_id.id,
            'order_line': [
                (0, 0, {
                    'product_id': tender.product_id.id,
                    'product_uom_qty': tender.quantity,
                    'price_unit': tender.price,
                }) for tender in self.tender_ids]
        })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Sales Tender',
            'res_model': 'sale.order',
            'res_id': tender_obj.id,
            'view_mode': 'form',
            'target': 'current',
        }


    def print_report_action(self):
        return self.env.ref('uat_sales_tender.sales_tender_report_id').report_action(self)

    def button_approve(self):
        return self.write({'state': 'approve'})

    def button_confirm(self):
        return self.write({'state': 'confirm'})

    def button_cancel(self):
        return self.write({'state': 'cancel'})

    def button_to_draft(self):
        return self.write({'state': 'draft'})


    def _document_count(self):
        for each in self:
            document_ids = self.env['tender.document'].sudo().search([('tender_ref', '=', each.id)])
            each.document_count = len(document_ids)

    def document_view(self):
        self.ensure_one()
        domain = [
            ('tender_ref', '=', self.id)]
        return {
            'name': _('Documents'),
            'domain': domain,
            'res_model': 'tender.document',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                           Click to Create for New Documents
                        </p>'''),
            'limit': 80,
            'context': "{'default_tender_ref': '%s'}" % self.id
        }

    document_count = fields.Integer(compute='_document_count', string='# Documents')



    # def create_tender_so(self):
    #     tender_id = self.env['sale.order']
    #
    #     tender_obj = tender_id.create({
    #         'partner_id': self.partner_id.id,
    #         'company_id': self.company_id.id,
    #     })
    #     for line in tender_id.order_line:
    #         line.create({
    #             'product_id': self.tender_ids.product_id.id,
    #         })
    #
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Sales Tender',
    #         'res_model': 'sales.tender',
    #         'res_id': tender_obj.id,
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'target': 'current',
    #     }


# class AccountTAxes(models.Model):
#     _inherit = "account.tax"
#
#     tender_id = fields.Many2one("sales.tender.lines")


class SalesTenderLines(models.Model):
    _name = "sales.tender.lines"


    tender_id = fields.Many2one("sales.tender")

    product_id = fields.Many2one("product.product")
    description = fields.Text(string="Description", related='product_id.description', readonly=False)
    product_uom_id = fields.Many2one('uom.uom', related='product_id.uom_id', readonly=True, String='UnitMeasure')
    quantity = fields.Float(string="Quantity")
    price = fields.Float(string="Price", related='product_id.lst_price',readonly=False)
    note = fields.Char()
    total = fields.Float(compute="compute_total_price")
    sequence = fields.Integer()


    @api.depends('quantity', 'price')
    def compute_total_price(self):
        for record in self:
            record.total = record.quantity * record.price


    def _document_count2(self):
        for each in self:
            document_idss = self.env['product.tender.document'].sudo().search([('product_ref', '=', each.id)])
            each.document_count2 = len(document_idss)

    def document_view2(self):
        self.ensure_one()
        domain = [
            ('product_ref', '=', self.id)]
        return {
            'name': _('Documents'),
            'domain': domain,
            'res_model': 'product.tender.document',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'view_type': 'form',
            'help': _('''<p class="oe_view_nocontent_create">
                           Click to Create for New Documents
                        </p>'''),
            'limit': 80,
            'context': "{'default_product_ref': '%s'}" % self.id
        }

    document_count2 = fields.Integer(compute='_document_count2', string='# Documents')

    # state = fields.Selection(selection=[('close', 'close'), ('open', 'open')], compute='compute_tender_state')
    # @api.depends('balance')
    # def compute_tender_state(self):
    #     for record in self:
    #         if record.balance <= 0:
    #             record.state = 'close'
    #         else:
    #             record.state = 'open'
