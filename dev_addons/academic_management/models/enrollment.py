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


    #modificar create , cada estudiante poner el curso y periodo que se inscribio
    @api.model
    def create(self, values):
        enrollment = super(Enrollment, self).create(values)
        for student in enrollment.student_ids:
            if 'grade_id' in values:
                data_grade = self.env['grade'].search([('id', '=', values['grade_id'])])
                student.grade_actual = data_grade.id
                student.cycle_actual = data_grade.cycle_id.id
                student.parallel_actual = data_grade.parallel_id.id
        return enrollment
    
    #modificar write, si se cambia el curso o periodo de la inscripcion, cambiar el curso y periodo del estudiante
    def write(self, values):
        enrollment = super(Enrollment, self).write(values)
        if 'grade_id' in values:
            new_grade = self.env['grade'].browse(values['grade_id'])
            for student in self.student_ids:
                student.write({
                    'grade_actual': new_grade.id,
                    'cycle_actual': new_grade.cycle_id.id,
                    'parallel_actual': new_grade.parallel_id.id,
                })

        return enrollment



    def action_in_progress(self):
        self.state = 'in_progress'
    
    
    def action_done(self):
        self.state = 'done'


    def action_draft(self):
        self.state = 'draft'



    
    


            



    

