from odoo import models, fields
from odoo.exceptions import UserError

class SalonStage(models.Model):
    _inherit = "salon.stage"

    color = fields.Integer(string="Color")  # Define the missing color field

    def unlink(self):
        linked_order = self.env['salon.order'].search([('stage_id', 'in', self.ids)])
        for stage in self:
            if stage in linked_order.mapped('stage_id'):
                raise UserError(
                    f'Cannot delete stage "{stage.name}" because it is linked to existing salon order(s). Please archive it instead.'
                )
        return super(SalonStage, self).unlink()