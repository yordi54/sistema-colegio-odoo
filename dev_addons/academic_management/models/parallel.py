from odoo import models, fields

class Parallel(models.Model):
    _name = "parallel"
    _description = "Paralelos escolares"

    name = fields.Char(string="Nombre", required=True)
    
