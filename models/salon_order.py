from odoo import models, fields, api

class SalonOrder(models.Model):
    _inherit = 'salon.order'

    stage_id = fields.Many2one(
        'salon.stage', string='Stage',
        default=lambda self: self.env.ref('sic_salon_management.salon_stage_new_request', raise_if_not_found=False),
        group_expand='_read_group_stage_ids',
        tracking=True,
    )

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        return self.env['salon.stage'].search([]).sorted('sequence')