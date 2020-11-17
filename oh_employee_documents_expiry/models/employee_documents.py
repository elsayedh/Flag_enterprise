# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta
from odoo import models, fields, api, _
from odoo.exceptions import Warning


class HrEmployeeDocument(models.Model):
    _name = 'hr.employee.document'
    _description = 'HR Employee Documents'
    _inherit = ['mail.thread']

    # @api.multi
    # def server_do_action(self):
    #
    #     groups = self.env['res.groups'].search([('name', '=', 'Employees / Administrator')])
    #     print(groups)
    #     recipient_partners = []
    #     for group in groups:
    #         for recipient in group.users:
    #             if recipient.partner_id.id not in recipient_partners:
    #                 recipient_partners.append(recipient.partner_id.id)
    #
    #     if len(recipient_partners):
    #         self.message_post(body='There is No enough QTY',
    #                             subtype='mt_comment',
    #                             subject='Minimum Qty',
    #                             partner_ids=recipient_partners,
    #                             message_type='comment')
    @api.model
    def mail_reminder(self):
        """Sending document expiry notification to employees."""

        obj = self.env['hr.employee.document'].search([])
        groups = self.env['res.groups'].search([('id', '=', '12')])

        print(groups)
        recipient_partners = []
        for group in groups:
            for recipient in group.users:
                if recipient.partner_id.id not in recipient_partners:
                    recipient_partners.append(recipient.partner_id.id)
                print(recipient_partners)

                for recUser in obj:
                    print(obj)

                    if obj:
                        partner = recipient
                        print(partner)
                        activities = {}
                        email_to = []
                        for record in partner:
                            if record.email:
                                email_to.append(record)
                        count = 0
                        list = []
                        task_description = ""
                        for invoice in obj:
                            count = count + 1

                            activities.update(
                                {'Employee': invoice.employee_ref.name, 'Expiry Date': invoice.expiry_date,
                                 'Description': invoice.description, 'Document Type': invoice.document_type.name})
                            list.append(activities)
                            task_description += "<tr>   <td  align=""center""> <font size=""2"">{3}</font></td>" \
                                                "<td  align=""center""> <font size=""2"">{2}</font></td>" \
                                                "<td  align=""center""> <font size=""2"">{1}</font></td>    " \
                                                "<td  align=""center""> <font size=""2"">{0}</font></td>  </tr>" \
                                .format(str(invoice.document_type.name), str(invoice.employee_ref.name),
                                        str(invoice.expiry_date), str(invoice.description), )

                            print(task_description)

                            status_table = " <font size=""2"">   <p> Hello: {6}</p>    <p>Here You Are Our Employee Expired Documents Dates: </p>" \
                                           "<table style=""width:80%"" border="" 1px solid black"">" \
                                           "<tr> <th><font size=""2"">Description</font> </th>    " \
                                           "<th><font size=""2"">Expiry Date</font> </th>    " \
                                           "<th><font size=""2"">Employee</font> </th>    " \
                                           "<th><font size=""2"">Document Type</font> </th>    </tr>{0}" \
                                           "<tr> <td colspan=""3"" align=""right""><font size=""2""> Total </font></td>" \
                                           "<td  align=""center""><font size=""2""> {5} </font> </td>   </table>" \
                                           "<p> <p>Regards,</p> </font>" \
                                .format(task_description, invoice.employee_ref.name, invoice.description,
                                        invoice.expiry_date, invoice.document_type.name, count,
                                        recipient.partner_id.name)
                            print(status_table)
                            mail = {
                                'subject': "Expired Dates",
                                'email_from': partner.email,
                                'recipient_ids': [(6, 0, [v.id for v in email_to])],
                                'body_html': status_table,
                            }

                            if not invoice.document_type.name:
                                invoice.document_type.name = ''
                            if not invoice.employee_ref.name:
                                invoice.employee_ref.name = ''
                            if not invoice.expiry_date:
                                invoice.expiry_date = ''
                            if not invoice.description:
                                invoice.description = ''

                mail_create = recUser.env['mail.mail'].create(mail)
                if mail_create:
                    mail_create.send()
                    self.mail_id = mail_create

        # for i in match:
        #     if i.expiry_date:
        #         mail_content = "Hello  " + i.employee_ref.name + ",<br>Your Document " \
        #                        + i.name + "is going to expire on " + \
        #                        str(i.expiry_date) + ". Please renew it before expiry date"
        #         main_content = {
        #             'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
        #             'author_id': self.env.user.partner_id.id,
        #             'body_html': mail_content,
        #             'email_to': i.employee_ref.work_email,
        #         }
        #         print(main_content)
        #         if len(recipient_partners):
        #             i.message_post(body=mail_content,
        #                            subtype='mt_comment',
        #                            subject=_('Document-%s Expired On %s') % (i.name, i.expiry_date),
        #                            partner_ids=recipient_partners,
        #                            message_type='comment')
        #         print(i.message_post)

        groups = self.env['res.groups'].search([('id', '=', '12')])
        print(groups)
        recipient_partners = []
        for group in groups:
            for recipient in group.users:
                if recipient.partner_id.id not in recipient_partners:
                    recipient_partners.append(recipient.partner_id.id)
        print(recipient_partners)

        now = datetime.now() + timedelta(days=1)
        date_now = now.date()
        match = self.search([])

        for i in match:
            if i.expiry_date:
                if i.notification_type == 'single':
                    exp_date = fields.Date.from_string(i.expiry_date)
                    if date_now == exp_date:
                        mail_content = "Hello  " + i.employee_ref.name + ",<br>Your Document " \
                                       + i.name + "is going to expire on " + \
                                       str(i.expiry_date) + ". Please renew it before expiry date"
                        main_content = {
                            'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
                            'author_id': self.env.user.partner_id.id,
                            'body_html': mail_content,
                            'email_to': i.employee_ref.work_email,
                        }
                        if len(recipient_partners):
                            i.message_post(body=mail_content,
                                           subtype='mt_comment',
                                           subject=_('Document-%s Expired On %s') % (i.name, i.expiry_date),
                                           partner_ids=recipient_partners,
                                           message_type='comment')
                        self.env['mail.mail'].create(main_content).send()
                elif i.notification_type == 'multi':
                    exp_date = fields.Date.from_string(i.expiry_date) - timedelta(days=i.before_days)
                    if date_now == exp_date or date_now == i.expiry_date:
                        mail_content = "Hello  " + i.employee_ref.name + ",<br>Your Document " \
                                       + i.name + "is going to expire on " + \
                                       str(i.expiry_date) + ". Please renew it before expiry date"
                        main_content = {
                            'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
                            'author_id': self.env.user.partner_id.id,
                            'body_html': mail_content,
                            'email_to': i.employee_ref.work_email,
                        }
                        if len(recipient_partners):
                            i.message_post(body=mail_content,
                                           subtype='mt_comment',
                                           subject=_('Document-%s Expired On %s') % (i.name, i.expiry_date),
                                           partner_ids=recipient_partners,
                                           message_type='comment')
                        self.env['mail.mail'].create(main_content).send()
                elif i.notification_type == 'everyday':
                    exp_date = fields.Date.from_string(i.expiry_date) - timedelta(days=i.before_days)
                    if date_now >= exp_date and date_now == i.expiry_date:
                        mail_content = "Hello  " + i.employee_ref.name + ",<br>Your Document " \
                                       + i.name + "is going to expire on " + \
                                       str(i.expiry_date) + ". Please renew it before expiry date"
                        main_content = {
                            'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
                            'author_id': self.env.user.partner_id.id,
                            'body_html': mail_content,
                            'email_to': i.employee_ref.work_email,
                        }
                        if len(recipient_partners):
                            i.message_post(body=mail_content,
                                           subtype='mt_comment',
                                           subject=_('Document-%s Expired On %s') % (i.name, i.expiry_date),
                                           partner_ids=recipient_partners,
                                           message_type='comment')
                        self.env['mail.mail'].create(main_content).send()
                elif i.notification_type == 'everyday_after':
                    exp_date = fields.Date.from_string(i.expiry_date) + timedelta(days=i.before_days)
                    if date_now == exp_date and date_now == i.expiry_date:
                        mail_content = "Hello  " + i.employee_ref.name + ",<br>Your Document " \
                                       + i.name + "is going to expire on " + \
                                       str(i.expiry_date) + ". Please renew it before expiry date"
                        main_content = {
                            'subject': _('Document-%s Expired On %s') % (i.name, i.expiry_date),
                            'author_id': self.env.user.partner_id.id,
                            'body_html': mail_content,
                            'email_to': i.employee_ref.work_email,
                        }
                        if len(recipient_partners):
                            i.message_post(body=mail_content,
                                           subtype='mt_comment',
                                           subject=_('Document-%s Expired On %s') % (i.name, i.expiry_date),
                                           partner_ids=recipient_partners,
                                           message_type='comment')
                        self.env['mail.mail'].create(main_content).send()

    @api.constrains('expiry_date')
    def check_expr_date(self):
        for each in self:
            if each.expiry_date:
                exp_date = fields.Date.from_string(each.expiry_date)
                if exp_date < date.today():
                    raise Warning('Your Document Is Expired.')

    name = fields.Char(string='Document Number', required=True, copy=False, help='You can give your'
                                                                                 'Document number.')
    description = fields.Text(string='Description', copy=False, help="Description")
    expiry_date = fields.Date(string='Expiry Date', copy=False, help="Date of expiry")
    employee_ref = fields.Many2one('hr.employee', invisible=1, copy=False)
    doc_attachment_id = fields.Many2many('ir.attachment', 'doc_attach_rel', 'doc_id', 'attach_id3', string="Attachment",
                                         help='You can attach the copy of your document', copy=False)
    issue_date = fields.Date(string='Issue Date', default=fields.datetime.now(), help="Date of issue", copy=False)
    document_type = fields.Many2one('document.type', string="Document Type", help="Document type")
    before_days = fields.Integer(string="Days", help="How many number of days before to get the notification email")
    notification_type = fields.Selection([
        ('single', 'Notification on expiry date'),
        ('multi', 'Notification before few days'),
        ('everyday', 'Everyday till expiry date'),
        ('everyday_after', 'Notification on and after expiry')
    ], string='Notification Type',
        help="""
        Notification on expiry date: You will get notification only on expiry date.
        Notification before few days: You will get notification in 2 days.On expiry date and number of days before date.
        Everyday till expiry date: You will get notification from number of days till the expiry date of the document.
        Notification on and after expiry: You will get notification on the expiry date and continues upto Days.
        If you did't select any then you will get notification before 7 days of document expiry.""")


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    def _document_count(self):
        for each in self:
            document_ids = self.env['hr.employee.document'].sudo().search([('employee_ref', '=', each.id)])
            each.document_count = len(document_ids)

    def document_view(self):
        self.ensure_one()
        domain = [
            ('employee_ref', '=', self.id)]
        return {
            'name': _('Documents'),
            'domain': domain,
            'res_model': 'hr.employee.document',
            'type': 'ir.actions.act_window',
            'view_id': False,
            'view_mode': 'tree,form',
            'help': _('''<p class="oe_view_nocontent_create">
                           Click to Create for New Documents
                        </p>'''),
            'limit': 80,
            'context': "{'default_employee_ref': %s}" % self.id
        }

    document_count = fields.Integer(compute='_document_count', string='# Documents')


class HrEmployeeAttachment(models.Model):
    _inherit = 'ir.attachment'

    doc_attach_rel = fields.Many2many('hr.employee.document', 'doc_attachment_id', 'attach_id3', 'doc_id',
                                      string="Attachment", invisible=1)
    attach_rel = fields.Many2many('hr.document', 'attach_id', 'attachment_id3', 'document_id',
                                  string="Attachment", invisible=1)
