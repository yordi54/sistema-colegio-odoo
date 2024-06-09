from odoo import fields, models, api
from odoo.exceptions import UserError

class Period(models.Model):
    _name = 'period'
    _description = 'Periodo académico en un año académico'
   
    
    number = fields.Char(string='Numero', required=True)
    description = fields.Text(string='Descripción')
    type_period = fields.Selection([
        ('bimestre', 'Bimestre'),
        ('trimestre', 'Trimestre'),
        ('semestre', 'Semestre')
    ], string='Tipo de periodo', required=True)
    date_start = fields.Date(string='Fecha de inicio', required=True)
    date_end = fields.Date(string='Fecha de fin', required=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('in_progress', 'En Curso'),
        ('done', 'Finalizado')
    ], string='Estado', default='draft', required=True)
    management_id = fields.Many2one('management', string='Gestión', required=True)

    name = fields.Char(string='Nombre del Periodo', compute='_compute_name', store=True)

    #campo computado para el nombre del periodo academico en un año academico
    @api.depends('number', 'management_id.year')
    def _compute_name(self):
        for record in self:
            if record.management_id:
                record.name = f"{record.number}-{record.management_id.year}"

    _rec_name = 'name'

    enrollment_ids = fields.One2many('enrollment', 'period_id', string='Inscripciones')

    #campos de solo lectura
    #year = fields.Char(related='management_id.year', string='Año Academico', readonly=True)
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
         #   if record.state == 'done':
          #      raise UserError('No se puede pasar a Borrador si el estado es Finalizado.')
           # record.state = 'draft'


    #def write(self, vals):
     #   for record in self:
      #      if record.state == 'done':
       #         raise UserError('No se puede editar un periodo finalizada.')
       # return super(Period, self).write(vals)


    #Relacion con la tabla report.card
    report_card_ids = fields.One2many('report.card', 'period_id', string='Boletin')