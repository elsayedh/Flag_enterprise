# -*- coding: utf-8 -*-

# from odoo import models, fields, api, _
# from odoo.exceptions import UserError

from odoo import api, fields, models, _, SUPERUSER_ID


class FlagCategory(models.Model):
    _name = "flag.category"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "category"

    barcode = fields.Char('Barcode', required=True)
    category = fields.Char('Category')
    place_holder = fields.Char()

