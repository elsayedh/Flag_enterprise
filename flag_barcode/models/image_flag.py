# -*- coding: utf-8 -*-

# from odoo import models, fields, api, _
# from odoo.exceptions import UserError

from odoo import api, fields, models, _, SUPERUSER_ID


class ImageFlag(models.Model):
    _name = "image.flag"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "image"

    barcode = fields.Char('Barcode', required=True)
    image = fields.Char('Image')
    place_holder = fields.Char()

