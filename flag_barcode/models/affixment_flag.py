# -*- coding: utf-8 -*-

# from odoo import models, fields, api, _
# from odoo.exceptions import UserError

from odoo import api, fields, models, _, SUPERUSER_ID


class AffixmentFlag(models.Model):
    _name = "affixment.flag"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "affixment"

    barcode = fields.Char('Barcode', required=True)
    affixment = fields.Char('Affixment')
    place_holder = fields.Char()
