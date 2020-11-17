# -*- coding: utf-8 -*-

# from odoo import models, fields, api, _
# from odoo.exceptions import UserError

from odoo import api, fields, models, _, SUPERUSER_ID


class EntityFlag(models.Model):
    _name = "entity.flag"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "entity"

    barcode = fields.Char('Barcode', required=True)
    iso = fields.Char('ISO')
    entity = fields.Char('Entity')
    ratio_id = fields.Many2one('flyration.flag', string="Ratio")
    place_holder = fields.Char()




    # def name_get(self):
    #     # name get function for the model executes automatically
    #     res = []
    #     for rec in self:
    #         res.append((rec.id, '%s:%s, %s' % (rec.flyration_left, rec.flyration_right, rec.entity)))
    #     return res


