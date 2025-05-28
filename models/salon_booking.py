from odoo import models, fields, api

class SalonBooking(models.Model):
    _name = 'salon.booking'
    _description = 'Salon Booking'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Customer Name", required=True, tracking=True)
    phone = fields.Char(string="Phone Number", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    time = fields.Datetime(string="Appointment Time", tracking=True)

    service_ids = fields.Many2many('salon.service', string="Services", tracking=True)
    chair_id = fields.Many2one('salon.chair', string="Stylist Chair", tracking=True)

    state = fields.Selection([
        ('New Request', 'New Request'),
        ('Confirmed', 'Confirmed'),
        ('Ongoing', 'Ongoing'),
        ('Done', 'Done')
    ], default='draft', string="Status", tracking=True)

    # Optional method to approve booking
    def action_approve(self):
        for rec in self:
            rec.state = 'approved'
            template = self.env.ref('salon_management.mail_template_salon_approved')
            if template and rec.email:
                template.send_mail(rec.id, force_send=True)

    # Optional method to reject booking
    def action_reject(self):
        for rec in self:
            rec.state = 'rejected'
            template = self.env.ref('salon_management.mail_template_salon_rejected')
            if template and rec.email:
                template.send_mail(rec.id, force_send=True)
