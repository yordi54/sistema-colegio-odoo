from odoo import models, fields

class Mark(models.Model):
    _name = "mark"
    _description = "Nota de una materia"

    number = fields.Integer(string="Calificación", required=True)
    
    # Relacion con la tabla subject
    subject_id = fields.Many2one('subject', string="Materia", required=True)

    # Relacion con la tabla report.card
    report_card_id = fields.Many2one('report.card', string="Boletin", required=True)