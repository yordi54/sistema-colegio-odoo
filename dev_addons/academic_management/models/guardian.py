from odoo import models, fields, api

class Guardian(models.Model):
    _name = 'guardian'
    _description = 'Tutor Alumno'

    name = fields.Char(string='Nombre', required=True)
    lastname = fields.Char(string='Apellidos', required=True)
    ci = fields.Char(string='CI', required=True)    
    email = fields.Char(string='Correo')
    phone = fields.Char(string='Telefono', required=True)
    address = fields.Char(string='Direccion', required=True)
    student_ids = fields.Many2many('student', 'student_guardian_rel', 'guardian_id', 'student_id', string='Alumnos')
    user_id = fields.Many2one('res.users', string='Usuario', required=False)



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

        return super(Guardian, self).create(vals)