from odoo import models, fields, api

class SalonBooking(models.Model):
    _inherit = 'salon.booking'

    stage_id = fields.Many2one(
        'salon.stage', string='Stage',
        tracking=True,
        group_expand='_read_group_stage_ids',
        default=lambda self: self.env.ref('sic_salon_management.sic_salon_stage_new', raise_if_not_found=False),
    )

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        return self.env['salon.stage'].search([], order='sequence asc')