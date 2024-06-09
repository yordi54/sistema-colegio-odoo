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
    phone = fields.Char(string="Telefono", required=True)
    email = fields.Char(string="Correo electronico", required=False, unique=True)
    address = fields.Char(string="Direccion", required=True)
    gender = fields.Selection([('masculino', 'Masculino'), ('femenino', 'Femenino')], string="Genero", required=True)
    photo = fields.Binary(string="Foto")

    # Relacion con la tabla de cursos
    user_id = fields.Many2one('res.users', string="Usuario", required=True)

    #Relacion con la tabla report.card
    report_card_ids = fields.One2many('report.card', 'student_id', string='Boletin')

    #Relacion con la tabla grade.book
    grade_book_ids = fields.One2many('grade.book', 'student_id', string='Libreta')

    # Relacion con la tabla announcement
    announcement_ids = fields.Many2many('announcement', "announcement_student_rel", "student_id", "announcement_id", string="Comunicados")

    
    # Campo computado para concatenar nombre y apellidos
    @api.depends('name', 'lastname')
    def _compute_display_name(self):
        for student in self:
            student.display_name = f"{student.name} {student.lastname}"

    display_name = fields.Char(string="Nombre Completo", compute='_compute_display_name')

    _rec_name = 'display_name'
    



