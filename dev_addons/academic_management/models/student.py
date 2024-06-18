from odoo import models, fields, api

class Student(models.Model):
    _name = "student"
    _description = "Alumno de la escuela"

    name = fields.Char(string="Nombre", required=True)
    lastname = fields.Char(string="Apellidos", required=True)
    ci = fields.Char(string="Cedula de identidad", required=True)
    birthdate = fields.Date(string="Fecha de nacimiento", required=True)
    rude = fields.Char(string="Codigo RUDE", required=True)
    state = fields.Selection([ ('activo', 'Activo'), ('inactivo', 'Inactivo')], string="Estado", required=True, default='activo')
    phone = fields.Char(string="Telefono", required=False)
    email = fields.Char(string="Correo electronico", required=False)
    address = fields.Char(string="Direccion", required=True)
    gender = fields.Selection([('masculino', 'Masculino'), ('femenino', 'Femenino')], string="Genero", required=True)
    photo = fields.Binary(string="Foto")
    grade_actual = fields.Integer(string="Grado actual", required=False)
    cycle_actual = fields.Integer(string="Ciclo actual", required=False)
    parallel_actual = fields.Integer(string="Paralelo actual", required=False)

    # Relacion con la tabla de cursos
    user_id = fields.Many2one('res.users', string="Usuario", required=False)
    # Relacion con la tabla de guardian
    guardian_ids = fields.Many2many('guardian', "student_guardian_rel", "student_id", "guardian_id", string="Tutores")
    # Relacion con la tabla de inscripcion many many
    enrollment_ids = fields.Many2many('enrollment', "student_enrollment_rel", "student_id", "enrollment_id", string="Inscripciones")

    license_ids = fields.One2many('license', 'student_id', string='Licencias')
    attendance_ids = fields.One2many('attendance', 'student_id', string='Registro de asistencia')
    #attendance_ids = fields.One2many('attendance', 'student_id', string='Asistencias')
    #faltas
    #observaciones
    #calificaciones

    full_name = fields.Char(string="Nombre Completo", compute='_compute_full_name', store=True)
    
    @api.depends('name', 'lastname')
    def _compute_full_name(self):
        for record in self:
            record.full_name = f"{record.name} {record.lastname}"

    _rec_name = 'full_name'


    #Relacion con la tabla report.card
    report_card_ids = fields.One2many('report.card', 'student_id', string='Boletin')

    #Relacion con la tabla grade.book
    grade_book_ids = fields.One2many('grade.book', 'student_id', string='Libreta')

    # Relacion con la tabla announcement
    #announcement_ids = fields.Many2many('announcement', "announcement_student_rel", "student_id", "announcement_id", string="Comunicados")

    
    # Campo computado para concatenar nombre y apellidos
    @api.depends('name', 'lastname')
    def _compute_display_name(self):
        for student in self:
            student.display_name = f"{student.name} {student.lastname}"

    display_name = fields.Char(string="Nombre Completo", compute='_compute_display_name')

    _rec_name = 'display_name'

    #create student and create user
    @api.model
    def create(self, vals):
        # Crear el usuario
        user_vals = {
            'name': f"{vals['name']} {vals['lastname']}",
            'login': vals['email'],
            'email': vals['email']
        }
        user = self.env['res.users'].create(user_vals)
        vals['user_id'] = user.id

        return super(Student, self).create(vals)
    



