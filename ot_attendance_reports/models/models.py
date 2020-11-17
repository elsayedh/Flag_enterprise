# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ot_attendance_reports(models.Model):
#     _name = 'ot_attendance_reports.ot_attendance_reports'
#     _description = 'ot_attendance_reports.ot_attendance_reports'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
