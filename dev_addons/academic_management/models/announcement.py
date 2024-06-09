from odoo import models, fields, api

class Announcement(models.Model):
    _name = "announcement"
    _description = "Comunicados"

    reason = fields.Char(string="Motivo", required=True)
    description = fields.Char(string="Descripcion", required=True)
    # Campo de selección para definir el tipo de destinatario del comunicado
    state = fields.Selection([
        ('cycle', 'Ciclo'),
        ('student', 'Alumno'),
        ('grade', 'Curso')
    ], string="Selección", required=True)

    # Relacion con la tabla student
    student_ids = fields.Many2many('student', string='Alumno', required=False)
    # Relacion con la tabla grade
    grade_ids = fields.Many2many('grade', string='Curso', required=False)
    # Relacion con la tabla cycle
    cycle_ids = fields.Many2many('cycle', string='Ciclo', required=False)

    @api.onchange('state')
    def _onchange_state(self):
        if self.state != 'student':
            self.student_ids = [(5, 0, 0)]  # Elimina todas las selecciones de alumnos
        if self.state != 'grade':
            self.grade_ids = [(5, 0, 0)]  # Elimina todas las selecciones de cursos
        if self.state != 'cycle':
            self.cycle_ids = [(5, 0, 0)]  # Elimina todas las selecciones de ciclos