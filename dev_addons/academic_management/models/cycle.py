from odoo import models, fields

class Cycle(models.Model):
    _name = "cycle"
    _description = "Ciclos escolares"

    name = fields.Char(string="Nombre", required=True)
    description = fields.Char(string="Descripcion", required=True)
    duration = fields.Integer(string="Duracion", required=False)
    state = fields.Selection([ ('activo', 'Activo'), ('inactivo', 'Inactivo')], string="Estado", required=True, default='activo')

    # Relacion con la tabla de colegio
    company_id = fields.Many2one('res.company', string="Colegio", required=True)
    # Relacion con la tabla grade
    grade_ids = fields.One2many('grade', 'cycle_id', string='Cursos')