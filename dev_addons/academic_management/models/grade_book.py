from odoo import models, fields, api

class GradeBook(models.Model):
    _name = "grade.book"
    _description = "Libretas escolares"

    code = fields.Char(string="Código", required=False)
     
    #Relacion con la tabla report.card
    report_card_ids = fields.One2many('report.card', 'grade_book_id', string='Boletin')

    # Relacion con la tabla student
    student_id = fields.Many2one('student', string="Alumno", required=True)

    # Relacion con la tabla management
    management_id = fields.Many2one('management', string="Gestión", required=True)

    grade_name = fields.Char(string="Curso", readonly=True)

    #cuando selecciono un estudiante que me muestre el nombre de curso en el que esta inscrito
    """ @api.onchange('student_id')
    def _onchange_student_id(self):
        if self.student_id:
            #buscar el curso en el que esta inscrito el estudiante y mostrar su nombre
            grade_name = self.env['grade'].search([('id', '=', self.student_id.grade_actual)], limit=1)
            self.grade_name = grade_name.full_name """
    @api.onchange('student_id')
    def _onchange_student_id(self):
        if self.student_id:
            #buscar el curso en el que esta inscrito el estudiante y mostrar su nombre
            grade_name = self.env['grade'].search([('id', '=', self.student_id.grade_actual)], limit=1)
            self.grade_name = grade_name.full_name
    #cargar boletines de un estudiante
    
    def action_load_report_cards(self):
        for record in self:
            if record.student_id and record.management_id:
                new_report_cards = self.env['report.card'].search([
                    ('student_id', '=', record.student_id.id),
                    ('period_id.management_id', '=', record.management_id.id)
                ])
                # Limpiar todos los boletines actuales y luego agregar los nuevos
                record.report_card_ids = [(5, 0, 0)]  # Eliminar todos los registros actuales
                record.report_card_ids = [(4, report_card.id) for report_card in new_report_cards]



    @api.model
    def create(self, vals):
        # Crear el registro de la libreta
        if 'student_id' in vals:
            # Obtener el estudiante
            student = self.env['student'].browse(vals['student_id'])
            if student.grade_actual:
            # Obtener el nombre completo del grado del estudiante
                grade = self.env['grade'].search([('id', '=', student.grade_actual)], limit=1)
                if grade:
                    vals['grade_name'] = grade.full_name

            # Obtener el número de gestión del periodo
            if 'management_id' in vals:
                management = self.env['management'].browse(vals['management_id'])
                vals['code'] = f"{student.rude}{management.year}"

        return super(GradeBook, self).create(vals)


    
    @api.model
    def write(self, vals):
        # Crear el registro de la libreta
        if 'student_id' in vals:
            # Obtener el estudiante
            student = self.env['student'].browse(vals['student_id'])
            if student.grade_actual:
            # Obtener el nombre completo del grado del estudiante
                grade = self.env['grade'].search([('id', '=', student.grade_actual)], limit=1)
                if grade:
                    vals['grade_name'] = grade.full_name

            # Obtener el número de gestión del periodo
            if 'management_id' in vals:
                management = self.env['management'].browse(vals['management_id'])
                vals['code'] = f"{student.rude}{management.year}"

        return super(GradeBook, self).write(vals)

    _rec_name = 'code'