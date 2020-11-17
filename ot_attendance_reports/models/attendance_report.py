from odoo import models, fields, api
from collections import OrderedDict
from collections import Counter

class AttendanceReportWizard(models.TransientModel):
    _name = 'attendance.report.wizard'

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True, default=fields.Date.today)

    def get_attendance_report(self):
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'start_date': self.start_date,
                'end_date': self.end_date,
            },
        }
        return self.env.ref('ot_attendance_reports.attendance_report').report_action(self, data=data)


class AttendanceReportReport(models.AbstractModel):
    _name = "report.ot_attendance_reports.attendance_report_view"
    _description = "Attendance Report"

    def group_list(self,lst):
        res = [(el, lst.count(el)) for el in lst]
        return list(OrderedDict(res).items())

    @api.model
    def _get_report_values(self, docids, data=None):
        date_start = data['form']['start_date']
        date_end = data['form']['end_date']
        docs = []
        Attendances = self.env['hr.attendance'].search([('check_in', '>=', data['form']['start_date']),
                                                        ('check_in', '<=', data['form']['end_date'])])
        for atten in Attendances:
            docs.append({
                'employee': atten.employee_id.name,
                'check_in': atten.check_in,
                'check_out': atten.check_out,
                'worked_hours': int(atten.worked_hours),
            })

        return {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'date_start': date_start,
            'date_end': date_end,
            'docs': docs,
        }

