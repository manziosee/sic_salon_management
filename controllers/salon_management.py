import json
import pytz
from datetime import datetime, time
from odoo import fields, http
from odoo.http import request

class SalonBookingWeb(http.Controller):
    """Handles all salon web operations"""

    @http.route('/salon/chairs', type="json", auth="public")
    def get_salon_chair(self, products_per_slide=3):
        """Returns chairs for dashboard"""
        chairs = []
        for chair in request.env['salon.chair'].sudo().search([]):
            orders_count = request.env['salon.order'].search_count([
                ("chair_id", "=", chair.id),
                ("state", "in", ['confirmed', 'ongoing'])
            ])
            chairs.append({
                'name': chair.name,
                'id': chair.id,
                'orders': orders_count
            })
        return chairs

    @http.route('/page/salon_details', type='json', auth='public', website=True, csrf=False)
    def salon_details(self, name, date, salon_time, phone, email, chair, number, list_service):
        """Create new booking from website"""
        service_lists = [service['item'] for service in list_service]
        dates_time = f"{date} {salon_time}:00"
        user_tz = request.env.user.tz or 'UTC'
        local_tz = pytz.timezone(user_tz)
        date_and_time = local_tz.localize(
            datetime.strptime(dates_time, '%Y-%m-%d %H:%M:%S')
        ).astimezone(pytz.UTC).replace(tzinfo=None)
        
        booking = request.env['salon.booking'].create({
            'name': name,
            'phone': phone,
            'time': date_and_time,
            'email': email,
            'chair_id': chair,
            'service_ids': [(6, 0, service_lists)],
            'state': 'new_request'
        })
        return {'result': True}

    @http.route('/page/salon_check_date', type='json', auth="public", website=True)
    def salon_check(self, **kwargs):
        """Check chair availability"""
        year, month, day = map(int, kwargs['check_date'].split('-'))
        user_tz = request.env.user.tz or 'UTC'
        local_tz = pytz.timezone(user_tz)
        date_start = local_tz.localize(
            datetime(year, month, day, hour=0, minute=0, second=0)
        ).astimezone(pytz.UTC).replace(tzinfo=None)
        date_end = local_tz.localize(
            datetime(year, month, day, hour=23, minute=59, second=59)
        ).astimezone(pytz.UTC).replace(tzinfo=None)
        
        orders = request.env['salon.order'].search([
            ('chair_id.active_booking_chairs', '=', True),
            ('state', 'in', ['new_request', 'confirmed', 'ongoing']),
            ('start_time', '>=', date_start),
            ('start_time', '<=', date_end)
        ])
        
        result = {}
        for order in orders:
            start_time = fields.Datetime.to_string(
                pytz.UTC.localize(order.start_time).astimezone(local_tz).replace(tzinfo=None)
            )[11:16]
            end_time = fields.Datetime.to_string(
                pytz.UTC.localize(order.end_time).astimezone(local_tz).replace(tzinfo=None)
            )[11:16]
            
            if order.chair_id.id not in result:
                result[order.chair_id.id] = {
                    'name': order.chair_id.name,
                    'orders': [{
                        'number': order.id,
                        'start_time_only': start_time,
                        'end_time_only': end_time
                    }],
                }
            else:
                result[order.chair_id.id]['orders'].append({
                    'number': order.id,
                    'start_time_only': start_time,
                    'end_time_only': end_time
                })
        return result

    @http.route('/page/salon_management/salon_booking_thank_you', type='http', auth="public", website=True, csrf=False)
    def return_thank_you(self, **post):
        """Thank you page after booking"""
        return request.render('salon_management.salon_booking_thank_you', {})

    @http.route('/salon_booking_form', type='http', auth="public", website=True)
    def chair_info(self, **post):
        """Booking form with all required data"""
        date_check = datetime.today().date()
        user_tz = request.env.user.tz or 'UTC'
        local_tz = pytz.timezone(user_tz)
        date_start = local_tz.localize(
            datetime.combine(date_check, time.min)
        ).astimezone(pytz.UTC).replace(tzinfo=None)
        date_end = local_tz.localize(
            datetime.combine(date_check, time.max)
        ).astimezone(pytz.UTC).replace(tzinfo=None)
        
        orders = request.env['salon.order'].search([
            ('chair_id.active_booking_chairs', '=', True),
            ('state', 'in', ['new_request', 'confirmed', 'ongoing']),
            ('start_time', '>=', date_start),
            ('start_time', '<=', date_end)
        ])
        
        return request.render(
            'salon_management.salon_booking_form', {
                'chair_details': request.env['salon.chair'].search([]),
                'order_details': orders,
                'salon_services': request.env['salon.service'].search([]),
                'date_search': date_check,
                'holiday': request.env['salon.holiday'].search([('holiday', '=', True)]),
                'working_time': request.env['salon.working.hours'].search([])
            }
        )