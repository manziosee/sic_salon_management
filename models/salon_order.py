from odoo import models

class SalonOrder(models.Model):
    _inherit = ['salon.order', 'mail.thread', 'mail.activity.mixin']
