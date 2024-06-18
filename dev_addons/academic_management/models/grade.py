from odoo import models, fields, api

class Grade(models.Model):
    _name = "grade"
    _description = "Cursos escolares"

    name = fields.Char(string="Nombre", required=True)

    # Relacion con la tabla Parallel
    parallel_id = fields.Many2one('parallel', string="Paralelo", required=True)
    # Relacion con la tabla Cycle
    cycle_id = fields.Many2one('cycle', string="Ciclo", required=True)
    # Relacion con la tabla announcement
    #announcement_ids = fields.Many2many('announcement', "announcement_grade_rel", "grade_id", "announcement_id", string="Comunicados")

    # campo computado para concatenar el nombre del curso con el nombre del ciclo y el nombre del paralelo
    @api.depends('name', 'cycle_id', 'parallel_id')
    def _compute_full_name(self):
        for record in self:
            record.full_name = f"{record.name} - {record.cycle_id.name} - {record.parallel_id.name}"
    
    full_name = fields.Char(string="Nombre Completo", compute='_compute_full_name', store=True)
    _rec_name = 'full_name'

    enrollment_ids = fields.One2many('enrollment', 'grade_id', string='Inscripciones')
    #license_ids = fields.One2many('license', 'grade_id', string='Licencias')
    schedule_ids = fields.One2many('schedule', 'grade_id', string='Horarios')
    register_attendance_ids = fields.One2many('register.attendance', 'grade_id', string='Registro de asistencia')
    subject_ids = fields.Many2many('subject', string='Materias', compute='_compute_subject_ids', store=True)

    #obtener los materias de un curso
    @api.depends('schedule_ids')
    def _compute_subject_ids(self):
        for record in self:
            subjects = record.get_subjects()
            record.subject_ids = [(6, 0, subjects.ids)]

    def get_subjects(self):
        self.ensure_one()
        schedules = self.env['schedule'].search([('grade_id', '=', self.id)])
        subject_ids = schedules.mapped('subject_id')
        return subject_ids
    


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

    # lista de alumnos de un curso y añadir los datos de asistencia 
 
    
        



