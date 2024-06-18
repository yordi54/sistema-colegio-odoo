import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging
from odoo import models, fields, api


def initialize_firebase():
    cred = credentials.Certificate('/mnt/extra-addons/academic_management/static/firebase.json')
    firebase_admin.initialize_app(cred)

initialize_firebase()

def send_message_to_device(token, title, body):
    
    message = messaging.Message(
        notification=messaging.Notification(title=title, body=body),
        token=token,
    )
    messaging.send(message)



class Announcement(models.Model):
    _name = "announcement"
    _description = "Comunicados"

    reason = fields.Char(string="Motivo", required=True)
    description = fields.Char(string="Descripcion", required=True)
 

    @api.model
    def create(self, vals):
        #enviar mensaje notificacion
        record = super(Announcement, self).create(vals)
        send_message_to_device("d8SrTu8cTrumyxqX4D0T9X:APA91bFoDgMpHkuIRcUhAxwxVfk6Q1tu90cptUnHA94DfsizyzUhIPYrYvHeAJBXpKo7rdOt03P4bsweXXeg5TP6httZbL5C3KLGtNL1rbFhPaZZb3D5oE-g-HHqOTZ3yORvIqtxWOF_", record.reason, record.description)
        return record


