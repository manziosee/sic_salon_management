from odoo import models, fields, api

class SalonOrder(models.Model):
    _inherit = 'salon.order'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('invoiced', 'Invoiced'),
        ('done', 'Done')
    ], default='draft', string="Status", tracking=True)

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_invoice(self):
        for rec in self:
            rec.state = 'invoiced'

    def action_done(self):
        for rec in self:
            rec.state = 'done'
