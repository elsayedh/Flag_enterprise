# -*- coding: utf-8 -*-

# from odoo import models, fields, api, _
# from odoo.exceptions import UserError

from odoo import api, fields, models, _, SUPERUSER_ID


class FlyRationFlag(models.Model):
    _name = "flyration.flag"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "ratio_related"

    barcode = fields.Char('Barcode', required=True)
    ratio_related = fields.Float("Ratio")
    place_holder = fields.Char()




    # def name_get(self):
    #     # name get function for the model executes automatically
    #     res = []
    #     for rec in self:
    #         res.append((rec.id, '%s:%s' % (rec.flyration_left, rec.flyration_right)))
    #     return res
