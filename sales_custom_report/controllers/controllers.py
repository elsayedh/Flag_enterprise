# -*- coding: utf-8 -*-
# from odoo import http


# class SalesCustomReport(http.Controller):
#     @http.route('/sales_custom_report/sales_custom_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_custom_report/sales_custom_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_custom_report.listing', {
#             'root': '/sales_custom_report/sales_custom_report',
#             'objects': http.request.env['sales_custom_report.sales_custom_report'].search([]),
#         })

#     @http.route('/sales_custom_report/sales_custom_report/objects/<model("sales_custom_report.sales_custom_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_custom_report.object', {
#             'object': obj
#         })
