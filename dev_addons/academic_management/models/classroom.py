from odoo import models, fields, api

class Classroom(models.Model):
    _name = 'classroom'
    _description = 'Aulas'
    name = fields.Char(string='Aula', required=True)
    capacity = fields.Integer(string='Capacidad', required=True)
    classroom_type = fields.Selection([ ('aula', 'Aula'), ('laboratorio', 'Laboratorio')], string='Tipo de aula', required=True)
    state = fields.Selection([ ('disponible', 'Disponible'), ('cerrado', 'Cerrado')], string='Estado', required=True, default='disponible')