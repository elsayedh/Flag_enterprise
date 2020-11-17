# -*- coding: utf-8 -*-

# from odoo import models, fields, api, _
# from odoo.exceptions import UserError

from odoo import api, fields, models, _, SUPERUSER_ID


class FacesFlag(models.Model):
    _name = "faces.flag"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "faces"

    barcode = fields.Char('Barcode', required=True)
    faces = fields.Char('Face')
    place_holder = fields.Char()

