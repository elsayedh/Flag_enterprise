# -*- coding: utf-8 -*-


from odoo import api, exceptions, fields, models, _

from datetime import date, datetime


class MailActivity(models.Model):
    """ An actual activity to perform. Activities are linked to
    documents using res_id and res_model_id fields. Activities have a deadline
    that can be used in kanban view to display a status. Once done activities
    are unlinked and a message is posted. This message has a new activity_type_id
    field that indicates the activity linked to the message. """
    _inherit = 'mail.activity'

    date_deadline = fields.Date('Due Date', index=True, default=fields.Date.context_today)
    date_due = fields.Datetime('Due Date', index=True, required=True,default=fields.Datetime.now)


class AccountInvoice(models.Model):
    _inherit = "account.move"

    current_date = fields.Date()
    recipients_of_email = fields.Many2many(comodel_name='res.partner',relation='customer',column1='partner_id',column2='partner_name',string = "Recipients of the Email")
    subject = fields.Text('Subject')
    email_content = fields.Text('Email Content')

    @api.model
    def send_email_from_customer(self):
        # date_now = fields.Datetime.now()
        today_date = date.today()
        context = self._context
        current_uid = context.get('uid')
        current_login_user = self.env['res.users'].search([])
        for recUser in current_login_user:
            obj = self.env['mail.activity'].search([('user_id','=',recUser.id)])
            print(obj)

            if obj:
                context = self._context
                current_uid = context.get('uid')
                partner = recUser.partner_id
                print(partner)
                activities = {}
                email_to = []
                for record in partner:
                    if record.email:
                        email_to.append(record)
                count=0
                list=[]
                task_description = ""
                for invoice in obj:
                    if invoice.date_due.date()==today_date:
                        print(invoice.date_due.date())
                        count=count+1

                        activities.update({'Activity': invoice.activity_type_id.name,'Date': invoice.date_due,'Summary': invoice.summary,'Note': invoice.note})
                        list.append(activities)
                        task_description += "<tr>   <td  align=""center""> <font size=""2"">{0}</font></td>" \
                                            "<td  align=""center""> <font size=""2"">{1}</font></td>" \
                                            "<td  align=""center""> <font size=""2"">{2}</font></td>    " \
                                            "<td  align=""center""> <font size=""2"">{3}</font></td>  </tr>"\
                            .format(str(invoice.date_due.strftime("%d-%m-%Y %H:%M:%S")), str(invoice.activity_type_id.name), str(invoice.summary), str(invoice.note))


                        status_table = " <font size=""2"">   <p> Hello, </p>    <p> Today’s Activity Summary: </p>" \
                                       "<table style=""width:80%"" border="" 1px solid black"">" \
                                       "<tr> <th><font size=""2"">Date Time</font> </th>    " \
                                       "<th><font size=""2""> Activity</font> </th>    " \
                                       "<th><font size=""2"">Summary</font> </th>    " \
                                       "<th><font size=""2""> Body </font> </th>    </tr>{0}" \
                                       "<tr> <td colspan=""3"" align=""right""><font size=""2""> Total </font></td>" \
                                       "<td  align=""center""><font size=""2""> {5} </font> </td>   </table>" \
                                       "<p> <p>Regards,</p> </font>"\
                            .format(task_description, invoice.date_due, invoice.activity_type_id.name, invoice.summary,invoice.note,count)

                        mail = {
                            'subject': "Daily Activities",
                            'email_from': partner.email,
                            'recipient_ids': [(6, 0, [v.id for v in email_to])],
                            'body_html': status_table,
                        }
                mail_create = recUser.env['mail.mail'].create(mail)
                if mail_create:
                    mail_create.send()
                    self.mail_id = mail_create