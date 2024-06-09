from odoo import models, fields, api

class Attendance(models.Model):
    _name = 'attendance'
    _description = 'Asistencia de alumnos'

    attended = fields.Boolean(string='Asistio', required=True)
    leave = fields.Boolean(string='Licencia', required=True)
    missing = fields.Boolean(string='Falto', required=True)
    observation = fields.Text(string='Observacion')
    student_id = fields.Many2one('student', string='Alumno', required=True)
    register_attendance_id = fields.Many2one('register.attendance', string='Registro de asistencia', required=True)
    #alumnos para la asistencia
    
    #student_ids = fields.Many2many('student', string='Alumnos', required=True, compute='_compute_list_students')

    #@api.depends('grade_id')
    
                
        




        


    
