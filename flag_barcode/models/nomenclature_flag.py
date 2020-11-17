# -*- coding: utf-8 -*-

# from odoo import models, fields, api, _
# from odoo.exceptions import UserError

from odoo import api, fields, models, _, SUPERUSER_ID


class NomenclatureFlag(models.Model):
    _name = "nomenclature.flag"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "nomenclature"

    barcode = fields.Char('Barcode', required=True)
    height = fields.Float('Height')
    height_stored = fields.Float('Standard Height')
    ration = fields.Float('Ration')
    width = fields.Float('Width', store=True, compute="_calc_width")
    nomenclature = fields.Char('Nomenclature')
    place_holder = fields.Char()

    def btn_bolean(self):
        msg = self.env['sh.message.wizard'].sudo().search([])
        print(msg)
        msg.unlink()
        self.height_stored = self.height
        message_id = self.env['sh.message.wizard'].create({'name': _("Successfully changed standard height")})
        return {
            'name': _('Success'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'sh.message.wizard',
            # pass the id
            'res_id': message_id.id,
            'target': 'new'
        }

    @api.model
    def create(self, vals):
        vals['height_stored'] = vals['height']
        result = super(NomenclatureFlag, self).create(vals)
        return result

    @api.depends("height", "ration")
    def _calc_width(self):
        self.width = self.height * self.ration


    # def name_get(self):
    #     # name get function for the model executes automatically
    #     res = []
    #     for rec in self:
    #         res.append((rec.id, '%s, %s (%s x %s)' % (rec.nomenclature, rec.ration, rec.height, rec.width)))
    #     return res


