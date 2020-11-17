# -*- coding: utf-8 -*-

# from odoo import models, fields, api, _
# from odoo.exceptions import UserError

from odoo import api, fields, models, _, SUPERUSER_ID


class MaterialColorFlag(models.Model):
    _name = "material.color.flag"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "color"


    barcode = fields.Char('Barcode', required=True)
    color = fields.Char('Material Color')
    place_holder = fields.Char()


    # def name_get(self):
    #     # name get function for the model executes automatically
    #     res = []
    #     for rec in self:
    #         res.append((rec.id, '%s, %s' % (rec.material_type, rec.color)))
    #     return res




