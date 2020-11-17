# -*- coding: utf-8 -*-
# from odoo import http


# class OtAttendanceReports(http.Controller):
#     @http.route('/ot_attendance_reports/ot_attendance_reports/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ot_attendance_reports/ot_attendance_reports/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ot_attendance_reports.listing', {
#             'root': '/ot_attendance_reports/ot_attendance_reports',
#             'objects': http.request.env['ot_attendance_reports.ot_attendance_reports'].search([]),
#         })

#     @http.route('/ot_attendance_reports/ot_attendance_reports/objects/<model("ot_attendance_reports.ot_attendance_reports"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ot_attendance_reports.object', {
#             'object': obj
#         })
