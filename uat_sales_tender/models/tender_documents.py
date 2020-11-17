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


class TenderDocument(models.Model):
    _name = 'tender.document'
    _description = 'Tender Documents'
    _inherit = ['mail.thread']

    @api.model
    def create(self, vals):
        # assigning the sequence for the record
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('tender.document') or _('New')
        res = super(TenderDocument, self).create(vals)
        return res

    name = fields.Char(string='Document Reference', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))

    description = fields.Text(string='Description', copy=False)
    tender_ref = fields.Many2one('sales.tender', invisible=1, copy=False)
    doc_attachment_ids = fields.Many2many('ir.attachment', 'doc_attach_rels', 'doc_id', 'attach_id3',
                                         string="Attachment", help='You can attach the copy of your document', copy=False)
    date = fields.Date(string='Date', default=fields.Datetime.now, index=True)
    type = fields.Selection([
        ('sample', 'Sample'),
        ('contract', 'Contract'),
        ('other', 'Other')
    ],required=True,tracking=True)


class TenderAttachment(models.Model):
    _inherit = 'ir.attachment'

    doc_attach_rels = fields.Many2many('tender.document', 'doc_attachment_ids', 'attach_id3', 'doc_id',
                                      string="Attachment", invisible=1)
    doc_attach_relss = fields.Many2many('product.tender.document', 'doc_attachment_idss', 'attach_id33', 'docum_id',
                                      string="Attachment", invisible=1)
    doc_attach_rels_supp = fields.Many2many('supplier.tender', 'doc_attachment_ids_supp', 'attach_id_supp', 'docum_id_supp',
                                      string="Attachment", invisible=1)

