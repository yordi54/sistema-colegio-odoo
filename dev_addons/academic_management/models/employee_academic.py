from odoo import models, fields, api
from odoo.exceptions import UserError
class EmployeeAcademic(models.Model):
    _inherit = 'hr.employee'

    schedule_ids = fields.One2many('schedule', 'teacher_id', string='Horarios')
        
        
           


    