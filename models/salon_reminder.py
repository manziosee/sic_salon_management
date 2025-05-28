from odoo import models, fields, api

class SalonReminder(models.Model):
    _name = 'salon.reminder'
    _description = 'Salon Reminder'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Reminder Subject", required=True)
    booking_id = fields.Many2one('salon.booking', string="Booking")
    order_id = fields.Many2one('salon.order', string="Order")
    recipient_id = fields.Many2one('res.partner', string="Recipient", required=True)
    send_time = fields.Datetime(string="Send Time", required=True)
    sent = fields.Boolean(string="Sent", default=False)
    message = fields.Text(string="Message")
    method = fields.Selection([
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('both', 'Both')
    ], string="Delivery Method", default='email')
    
    def send_reminder(self):
        for reminder in self:
            if not reminder.sent and reminder.send_time <= fields.Datetime.now():
                if reminder.method in ('email', 'both'):
                    template = self.env.ref('sic_salon_management.mail_template_salon_reminder')
                    template.with_context(
                        reminder_message=reminder.message
                    ).send_mail(reminder.id, force_send=True)
                
                if reminder.method in ('sms', 'both'):
                    # SMS implementation would go here
                    pass
                
                reminder.sent = True
                reminder.message_post(body="Reminder sent successfully")
    
    def cron_send_reminders(self):
        """Automatically send pending reminders"""
        pending_reminders = self.search([
            ('sent', '=', False),
            ('send_time', '<=', fields.Datetime.now())
        ])
        pending_reminders.send_reminder()