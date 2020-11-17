# -*- coding: utf-8 -*-

# from odoo import models, fields, api, _
# from odoo.exceptions import UserError


from odoo import api, fields, models, _, SUPERUSER_ID
# from odoo.osv import expression
# from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.exceptions import UserError
# from odoo.addons.stock.models.stock_move import PROCUREMENT_PRIORITIES


class SuppliersTender(models.Model):
    _name = "supplier.tender"
    _inherit = "mail.thread"

    supplier_prod_id = fields.Many2one('product.tender.document')
    name = fields.Char(string='Supplier Reference', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    d_name = fields.Char()
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    mobile = fields.Char()
    email = fields.Char()
    image = fields.Binary()

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
            vals['name'] = self.env['ir.sequence'].next_by_code('supplier.tender') or _('New')
        res = super(SuppliersTender, self).create(vals)
        return res


    def name_get(self):
        # name get function for the model executes automatically
        res = []
        for rec in self:
            if self.env.user.has_group('uat_sales_tender.group_sales_tender_manager'):
                print("MANAGERRRRRRRRRRRRRRR")
                res.append((rec.id, '%s - %s' % (rec.name, rec.d_name)))
            else:
                print("USSSSSSSSSSSSSSSSSSER")
                res.append((rec.id, '%s' % (rec.name)))
        return res