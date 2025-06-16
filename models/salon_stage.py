from odoo import models, fields

class SalonStage(models.Model):
    _inherit = 'salon.stage'

    # Restore color field to avoid frontend errors
    color = fields.Integer(string='Color')