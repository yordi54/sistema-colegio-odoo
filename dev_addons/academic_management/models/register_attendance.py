from odoo import models, fields, api

class RegisterAttendance(models.Model):
    _name = 'register.attendance'
    _description = 'Registro de asistencia'
    name = fields.Char(string='Titulo', required=True)
    date = fields.Date(string='Fecha', required=True)
    grade_id = fields.Many2one('grade', string='Curso', required=True)
    attendance_ids = fields.One2many('attendance', 'register_attendance_id', string='Asistencia de alumnos')
    color = fields.Char(string='Color') 


    #al crear generar la asistencia de los alumnos en base al grade_id
   
    

    

    #generar la asistencia de los alumnos en base al grade_id y que no se repita cuando genere un alumno   
    def generate_attendance_records(self):
        for record in self:
            students = self.env['student']
            if record.grade_id:
                for enrollment in record.grade_id.enrollment_ids:
                    students |= enrollment.student_ids
            
            existing_attendance = self.env['attendance'].search([
                ('register_attendance_id', '=', record.id),
            ])
            
            existing_attendance.unlink()  # Eliminar las asistencias existentes
            
            for student in students:
                self.env['attendance'].create({
                    'student_id': student.id,
                    'register_attendance_id': record.id,
                    'attended': False,
                    'leave': False,
                    'missing': False,
                })
    
    

