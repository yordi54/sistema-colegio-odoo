from odoo import models, fields, api
class Enrollment(models.Model):
    _name = 'enrollment'
    _description = 'Inscripcion de alumnos'


    student_ids = fields.Many2many('student', string='Alumno', required=True)
    grade_id = fields.Many2one('grade', string='Curso', required=True)
    date_start = fields.Date(string='Fecha de Inicio', required=True)
    date_end = fields.Date(string='Fecha de fin', required=True)
    period_id = fields.Many2one('period', string='Periodo', required=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('in_progress', 'En Curso'),
        ('done', 'Finalizado')
    ], string='Estado', default='draft', required=True)

    def action_in_progress(self):
        self.state = 'in_progress'
    
    
    def action_done(self):
        self.state = 'done'


    def action_draft(self):
        self.state = 'draft'



    
    


            



    

