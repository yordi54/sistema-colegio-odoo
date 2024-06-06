from odoo import models, fields

class Parallel(models.Model):
    _name = "parallel"
    _description = "Paralelos escolares"

    name = fields.Char(string="Nombre", required=True)
    
    # Relacion con la tabla grade
    grade_ids = fields.One2many('grade', 'parallel_id', string='Cursos')