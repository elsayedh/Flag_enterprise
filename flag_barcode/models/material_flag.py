# -*- coding: utf-8 -*-

# from odoo import models, fields, api, _
# from odoo.exceptions import UserError

from odoo import api, fields, models, _, SUPERUSER_ID


class MaterialFlag(models.Model):
    _name = "material.flag"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "material_type"


    barcode = fields.Char('Barcode', required=True)
    material_type = fields.Char('Material Type')
    place_holder = fields.Char()


    # def name_get(self):
    #     # name get function for the model executes automatically
    #     res = []
    #     for rec in self:
    #         res.append((rec.id, '%s, %s' % (rec.material_type, rec.color)))
    #     return res
