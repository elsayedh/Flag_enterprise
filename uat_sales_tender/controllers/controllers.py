# -*- coding: utf-8 -*-
# from odoo import http


# class UatSalesTender(http.Controller):
#     @http.route('/uat_sales_tender/uat_sales_tender/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/uat_sales_tender/uat_sales_tender/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('uat_sales_tender.listing', {
#             'root': '/uat_sales_tender/uat_sales_tender',
#             'objects': http.request.env['uat_sales_tender.uat_sales_tender'].search([]),
#         })

#     @http.route('/uat_sales_tender/uat_sales_tender/objects/<model("uat_sales_tender.uat_sales_tender"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('uat_sales_tender.object', {
#             'object': obj
#         })
