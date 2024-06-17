from odoo import models, fields, api

class License(models.Model):
    _name = 'license'
    _description = 'Licencia para un dia de clases'
    # que el name sea el nombre del alumno y el titulo de la licencia
    name = fields.Char(string='Titulo', required=True)
    date_start = fields.Date(string='Fecha de inicio', required=True)
    date_end = fields.Date(string='Fecha de fin', required=True)
    reason = fields.Text(string='Motivo', required=True)
    #grade_id = fields.Many2one('grade', string='Curso', required=True)
    student_id = fields.Many2one('student', string='Alumno', required=True)
    color = fields.Char(string='Color') 
   
    # que el name sea el nombre del alumno y el titulo de la licencia, despues de la creacion
    @api.model
    def create(self, vals):
        record = super(License, self).create(vals)
        record.name = f"{record.student_id.full_name} - {record.name}"
        return record
    

