from odoo import models, fields, api
class Schedule(models.Model):
    _name = 'schedule'
    _description = 'Horario de clases'

    start_time = fields.Char(string='Hora de inicio', required=True)
    end_time = fields.Char(string='Hora de fin', required=True)
    day = fields.Selection([ ('lunes', 'Lunes'), ('martes', 'Martes'), ('miercoles', 'Miercoles'), ('jueves', 'Jueves'), ('viernes', 'Viernes'), ('sabado', 'Sabado')], string='Dia', required=True)
    grade_id = fields.Many2one('grade', string='Curso', required=True)
    subject_id = fields.Many2one('subject', string='Materia', required=True)
    classroom_id = fields.Many2one('classroom', string='Aula', required=True)

    ##  listar los empleado id de tipo puesto de trabajo es profesor
    teacher_id = fields.Many2one('hr.employee', string='Profesor', required=True, domain=[('job_title', '=', 'Profesor')])