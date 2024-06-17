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


    @api.model
    def create(self, vals):
        record = super(Schedule, self).create(vals)
        if 'grade_id' in vals:
            grade = self.env['grade'].browse(vals['grade_id'])
            grade._compute_subject_ids()
        return record

    def write(self, vals):
        grade_ids = self.mapped('grade_id').ids
        result = super(Schedule, self).write(vals)
        new_grade_ids = self.mapped('grade_id').ids
        for grade_id in set(grade_ids + new_grade_ids):
            grade = self.env['grade'].browse(grade_id)
            grade._compute_subject_ids()
        return result

    def unlink(self):
        grade_ids = self.mapped('grade_id').ids
        result = super(Schedule, self).unlink()
        for grade_id in grade_ids:
            grade = self.env['grade'].browse(grade_id)
            grade._compute_subject_ids()
        return result