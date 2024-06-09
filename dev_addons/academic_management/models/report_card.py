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

    @api.model
    def create(self, vals):
        # Buscar la libreta del estudiante
        student_id = vals.get('student_id')
        if student_id:
            grade_book = self.env['grade.book'].search([('student_id', '=', student_id)], limit=1)
            if grade_book:
                vals['grade_book_id'] = grade_book.id
        
        # Crear el registro del boletín
        record = super(ReportCard, self).create(vals)
        
        # Generar el código del boletín
        record.code = f"{record.student_id.rude}{record.period_id.name}"
        return record

    _rec_name = 'code'