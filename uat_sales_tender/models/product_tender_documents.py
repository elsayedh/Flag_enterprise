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


class ProductTenderDocument(models.Model):
    _name = 'product.tender.document'
    _description = 'Product Tender Documents'
    _inherit = ['mail.thread']
    _rec_name = "supplier_id"


    supplier_id = fields.Many2one('supplier.tender')
    supplier_doc_ids = fields.One2many('supplier.tender.document','supplier_prod_id')


    description = fields.Text(string='Description', copy=False)
    product_ref = fields.Many2one('sales.tender.lines', invisible=1, copy=False)
    doc_attachment_idss = fields.Many2many('ir.attachment', 'doc_attach_relss', 'docum_id', 'attach_id33',
                                         string="Attachment", help='You can attach the copy of your document', copy=False)
    date = fields.Date(string='Date', default=fields.Datetime.now, index=True)

