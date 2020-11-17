# -*- coding: utf-8 -*-

from odoo import api, fields, models



class SaleOrderDemoReport(models.Model):
    _inherit = "sale.order"

    stamp_img = fields.Binary("Stamp Image")
    # default_sales_tax = fields.Char(compute="get_default_sales_tax")

    # @api.depends('partner_invoice_id')
    # def get_default_sales_tax(self):
    #     print('test')
    #     res_conf = self.env['res.config.settings'].sudo()
    #     max_manager = res_conf.get_values()
    #     print(max_manager)

    # supply_duration = fields.Char('Supply Duration', translate=True)
    # validate_duration = fields.Char('Validate', translate=True)
    # total_all = fields.Char('Total', translate=True)

class CompanyDemoReport(models.Model):
    _inherit = "res.company"

    stamp_img = fields.Binary("Stamp Image")
    company_chief_ar = fields.Char('Chief Executive AR')
    company_chief_en = fields.Char('Chief Executive EN')



class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    parent_product_categ_id = fields.Many2one('product.category', string='Parent Product Category', readonly=True)


    @api.model
    def _select(self):
        res = super(AccountInvoiceReport, self)._select()
        res +=", template_categ.parent_id  AS parent_product_categ_id "
        # print("res select ", res)
        return res

    @api.model
    def _from(self):
        res = super(AccountInvoiceReport, self)._from()
        res += " LEFT JOIN  product_category template_categ ON template_categ.id=template.categ_id  "
        res += " LEFT JOIN  product_category template_parent ON template_categ.parent_id=template_parent.id "
        # print("res from ",res)
        return res
    # def _from(self):
    #     res = super(AccountInvoiceReport, self)._from()
    #     print("from:", res)
    #     return res

    @api.model
    def _group_by(self):
        res = super(AccountInvoiceReport, self)._group_by()
        res += ", template_categ.parent_id "
        # print("res by ", res)
        return res


