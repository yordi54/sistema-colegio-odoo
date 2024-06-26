from odoo import models, fields

class School(models.Model):
    _inherit = 'res.company'

    # Añadimos un campo nuevo, is school
    is_school = fields.Boolean(string="Es escuela", default=True)

    # Relacion con la tabla cycles
    cycle_ids = fields.One2many('cycle', 'company_id', string='Ciclos')