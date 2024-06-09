from odoo import models, fields

class Subject(models.Model):
    _name = "subject"
    _description = "Materias escolares"

    name = fields.Char(string="Nombre", required=True)
    initials = fields.Char(string="Sigla", required=True)
    description = fields.Char(string="Descripcion", required=False)

    schedule_ids = fields.One2many('schedule', 'subject_id', string='Horarios')
    