from odoo import models, fields, api

class SalonBooking(models.Model):
    _inherit = 'salon.booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    state = fields.Selection([
        ('new_request', 'New Request'),
        ('confirmed', 'Confirmed'),
        ('ongoing', 'Ongoing'),
        ('done', 'Done')
    ], default='new_request', string="Status", tracking=True)

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'
            template = self.env.ref('sic_salon_management.mail_template_salon_approved')
            if template and rec.email:
                template.send_mail(rec.id, force_send=True)

    def action_start(self):
        for rec in self:
            rec.state = 'ongoing'
            template = self.env.ref('sic_salon_management.mail_template_salon_ongoing')
            if template and rec.email:
                template.send_mail(rec.id, force_send=True)
            

    def action_done(self):
        for rec in self:
            rec.state = 'done'
            template = self.env.ref('sic_salon_management.mail_template_salon_done')
            if template and rec.email:
                template.send_mail(rec.id, force_send=True)
                
