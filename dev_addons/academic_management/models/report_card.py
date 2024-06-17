from odoo import models, fields, api

class ReportCard(models.Model):
    _name = "report.card"
    _description = "Boletin de un periodo de un alumno"

    code = fields.Char(string="Código", required=False)
    
    #Relacion con la tabla mark
    mark_ids = fields.One2many('mark', 'report_card_id', string='Nota')

    # Relacion con la tabla period
    period_id = fields.Many2one('period', string="Periodo", required=True)

    # Relacion con la tabla student
    student_id = fields.Many2one('student', string="Alumno", required=True)

    # Relacion con la tabla grade.book
    grade_book_id = fields.Many2one('grade.book', string="Libreta", required=False)

    grade_name = fields.Char(string="Curso", readonly=True)

    #cuando selecciono un estudiante que me muestre el nombre de curso en el que esta inscrito
    @api.onchange('student_id')
    def _onchange_student_id(self):
        if self.student_id:
            #buscar el curso en el que esta inscrito el estudiante y mostrar su nombre
            grade_name = self.env['grade'].search([('id', '=', self.student_id.grade_actual)], limit=1)
            self.grade_name = grade_name.full_name

            

    @api.model
    def create(self, vals):
    # Crear el registro de la libreta
        if 'student_id' in vals:
        # Obtener el nombre completo del grado del estudiante
            student = self.env['student'].browse(vals['student_id'])
            if student.grade_actual:
                grade = self.env['grade'].search([('id', '=', student.grade_actual)], limit=1)
                if grade:
                    vals['grade_name'] = grade.full_name

                # Obtener el número del periodo
            if 'period_id' in vals:
                period = self.env['period'].browse(vals['period_id'])
                if period:
                    vals['code'] = f"{student.rude}{period.name}"

        return super(ReportCard, self).create(vals)
    
    
    @api.model
    def write(self, vals):
        for record in self:
        # Verificar si se ha modificado el estudiante
            if 'student_id' in vals:
            # Obtener el nombre completo del grado del estudiante
                student = self.env['student'].browse(vals['student_id'])
                if student.grade_actual:
                    grade = self.env['grade'].search([('id', '=', student.grade_actual)], limit=1)
                    if grade:
                        vals['grade_name'] = grade.full_name

        # Verificar si se ha modificado el periodo
            if 'period_id' in vals:
                period = self.env['period'].browse(vals['period_id'])
                if period:
                    vals['code'] = f"{record.student_id.rude}{period.name}"

        return super(ReportCard, self).write(vals)

    _rec_name = 'code'