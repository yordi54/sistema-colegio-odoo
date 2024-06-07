from odoo import models, fields, api

class Grade(models.Model):
    _name = "grade"
    _description = "Cursos escolares"

    name = fields.Char(string="Nombre", required=True)

    # Relacion con la tabla Parallel
    parallel_id = fields.Many2one('parallel', string="Paralelo", required=True)
    # Relacion con la tabla Cycle
    cycle_id = fields.Many2one('cycle', string="Ciclo", required=True)

    # # Campo computado para los cursos paralelos
    # parallel_grade_ids = fields.One2many('grade', string="Cursos Paralelos", compute="_compute_parallel_grades")

    # @api.depends('cycle_id')
    # def _compute_parallel_grades(self):
    #     for grade in self:
    #         if grade.cycle_id:
    #             grade.parallel_grade_ids = self.env['grade'].search([
    #                 ('cycle_id', '=', grade.cycle_id.id),
    #                 ('id', '!=', grade.id if grade.id else 0)  # Evitar NewId durante la creación
    #             ])
    #         else:
    #             grade.parallel_grade_ids = self.env['grade'].browse([])