
from odoo import models,api,fields,_

class FormRegistrasi(models.Model):
    _name = 'form.registrasi'
    _rec_name = 'first_name'

    first_name = fields.Char("Firstname", required=True)
    last_name = fields.Char("Lastname", required=True)
    gender = fields.Selection([('m',"Male"),('f', "Female")], string="Gender", required=True)
    address = fields.Text("Addres", required=True)