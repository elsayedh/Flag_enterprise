from odoo import api, fields, models, _


# class AccountInvoiceReport(models.Model):
#     _inherit = 'account.invoice.report'
#
#     price_total_tax = fields.Float(string='Total with Tax', readonly=True)
#
#     def _select(self):
#         return super(AccountInvoiceReport, self)._select() + ", sub.price_total as price_total_tax"
#
#     def _group_by(self):
#         return super(AccountInvoiceReport, self)._group_by() + ",  sub.price_total"

class AccountAccount(models.Model):
    _inherit = 'res.partner'

    def _invoice_total(self):
        account_invoice_report = self.env['account.move']
        if not self.ids:
            return True

        user_currency_id = self.env.company.currency_id.id
        all_partners_and_children = {}
        all_partner_ids = []
        for partner in self:
            # price_total is in the company currency
            all_partners_and_children[partner] = self.with_context(active_test=False).search(
                [('id', 'child_of', partner.id)]).ids
            all_partner_ids += all_partners_and_children[partner]

        # searching account.invoice.report via the ORM is comparatively expensive
        # (generates queries "id in []" forcing to build the full table).
        # In simple cases where all invoices are in the same currency than the user's company
        # access directly these elements

        # generate where clause to include multicompany rules
        where_query = account_invoice_report._where_calc([
            ('partner_id', 'in', all_partner_ids), ('state', 'not in', ['draft', 'cancel']),
            ('type', 'in', ('out_invoice', 'out_refund'))
        ])

        account_invoice_report._apply_ir_rules(where_query, 'read')
        from_clause, where_clause, where_clause_params = where_query.get_sql()
        # print("hi",where_clause)
        where_clause=where_clause.replace('"account_move".','')
        # print("hiw", where_clause)
        # price_total is in the company currency
        query = """
                    SELECT SUM(amount_total) as total, partner_id
                      FROM account_move account_invoice_report 
                     WHERE %s
                     GROUP BY partner_id
                  """ % where_clause
        print(query)
        print(where_clause_params)
        self.env.cr.execute(query, where_clause_params)
        price_totals = self.env.cr.dictfetchall()
        for partner, child_ids in all_partners_and_children.items():
            partner.total_invoiced = sum(price['total'] for price in price_totals if price['partner_id'] in child_ids)
