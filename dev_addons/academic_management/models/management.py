from odoo import fields, models, api
from odoo.exceptions import UserError
import logging
class Management(models.Model):
    _name = 'management'
    _description = 'Gestion anual académico'
    _rec_name = 'year'  # Define year as the name field


    year = fields.Char(string='Año', required=True)
    description = fields.Text(string='Descripción')
    state = fields.Selection([
    ('draft', 'Borrador'),
    ('in_progress', 'En Curso'),
    ('done', 'Finalizado')
], string='Estado', default='draft', required=True)
    date_start = fields.Date(string='Fecha de inicio', required=True)
    date_end = fields.Date(string='Fecha de fin', required=True)
    period_ids = fields.One2many('period', 'management_id', string='Periodos')
    # reescribir el campo name_get
    def name_get(self):
        result = []
        for record in self:
            name = record.year
            result.append((record.id, name))
        return result

    def action_in_progress(self):
        self.state = 'in_progress'
        #for record in self:
         #   if record.state == 'done':
          #      raise UserError('No se puede cambiar de Finalizado a En Curso.')
           # record.state = 'in_progress'
    
    def action_done(self):
        self.state = 'done'


    def action_draft(self):
        self.state = 'draft'
        #for record in self:
          #  if record.state == 'done':
         #       raise UserError('No se puede pasar a Borrador si el estado es Finalizado.')
        #    record.state = 'draft'
    #si es finalizado que no se pueda editar
   
    #def write(self, vals):
    #    for record in self:
     #       if record.state == 'done':
      #          raise UserError('No se puede editar una gestion finalizada.')
       # return super(Management, self).write(vals)

    
    
        
        
        

    #Relacion con la tabla grade.book
    grade_book_ids = fields.One2many('grade.book', 'management_id', string='Libreta')




