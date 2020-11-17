# -*- coding: utf-8 -*-
###################################################################################
#    A part of Open HRMS Project <https://www.openhrms.com>
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Cybrosys Technologies (<https://www.cybrosys.com>).
#    Author: Nilmar Shereef (<https://www.cybrosys.com>)
#
#    This program is free software: you can modify
#    it under the terms of the GNU Affero General Public License (AGPL) as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################
from datetime import datetime, date, timedelta
from odoo import models, fields, api, _
from odoo.exceptions import Warning


class SupplierDocument(models.Model):
    _name = 'supplier.tender.document'
    _description = 'Tender Supplier Documents'
    _inherit = ['mail.thread']

    supplier_prod_id = fields.Many2one('product.tender.document')

    @api.model
    def create(self, vals):
        # assigning the sequence for the record
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('supplier.tender.document') or _('New')
        res = super(SupplierDocument, self).create(vals)
        return res

    name = fields.Char(string='Document Reference', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))

    description = fields.Text(string='Description', copy=False)
    doc_attachment_ids_supp = fields.Many2many('ir.attachment', 'doc_attach_rels_supp', 'docum_id_supp', 'attach_id_supp',
                                         string="Attachment", help='You can attach the copy of your document', copy=False)
    date = fields.Date(string='Date', default=fields.Datetime.now, index=True)
    type = fields.Selection([
        ('sample', 'Sample'),
        ('contract', 'Contract'),
        ('other', 'Other')
    ],required=True,tracking=True)

