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

    @api.model
    def create(self, vals):
        record = super(GradeBook, self).create(vals)
        record.code = f"{record.student_id.rude}-{record.management_id.year}"
        return record

    _rec_name = 'code'