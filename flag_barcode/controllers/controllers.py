# -*- coding: utf-8 -*-
from odoo import http

# class FlagBarcode(http.Controller):
#     @http.route('/flag_barcode/flag_barcode/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flag_barcode/flag_barcode/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('flag_barcode.listing', {
#             'root': '/flag_barcode/flag_barcode',
#             'objects': http.request.env['flag_barcode.flag_barcode'].search([]),
#         })

#     @http.route('/flag_barcode/flag_barcode/objects/<model("flag_barcode.flag_barcode"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flag_barcode.object', {
#             'object': obj
#         })