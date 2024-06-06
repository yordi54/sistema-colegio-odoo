from odoo import models, fields

class Grade(models.Model):
    _name = "grade"
    _description = "Cursos escolares"

    name = fields.Char(string="Nombre", required=True)

    # Relacion con la tabla Parallel
    parallel_id = fields.Many2one('parallel', string="Paralelo", required=True)
    # Relacion con la tabla Cycle
    cycle_id = fields.Many2one('cycle', string="Ciclo", required=True)