from odoo import models, fields

class SalonStage(models.Model):
    _inherit = 'salon.stage'

    color = fields.Integer(string="Color")