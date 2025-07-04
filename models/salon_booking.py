from odoo import models, fields
from odoo.exceptions import UserError

class SalonBooking(models.Model):
    _inherit = 'salon.booking'

    stage_id = fields.Many2one('salon.stage', string='Stage', index=True, tracking=True)

    def action_approve(self):
        Stage = self.env['salon.stage']
        Order = self.env['salon.order']
        stage_confirmed = Stage.search([('name', '=', 'Confirmed')], limit=1)
        if not stage_confirmed:
            raise UserError('Cannot approve salon booking because the "Confirmed" stage is missing.')

        for booking in self.filtered(lambda b: b.state != 'approved'):
            order_vals = {
                'name': self.env['ir.sequence'].next_by_code('salon.order') or 'New',
                'customer_name': booking.name,
                'time_start': booking.datetime,
                'salon_chair_id': booking.salon_chair_id.id,
                'phone': booking.phone,
                'email': booking.email,
                'stage_id': stage_confirmed.id,
            }
            Order.create(order_vals)
            booking.stage_id = stage_confirmed
            booking.state = 'approved'

        return True