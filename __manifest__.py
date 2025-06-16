# -*- coding: utf-8 -*-
{
    'name': 'SIC Salon Management',
    'version': '1.0.0',
    'category': 'Services',
    'summary': 'Salon Management Customizations with Colored Stages',
    'description': """
        Extend salon_management with custom colored stages (via decorations) 
        and limited stage workflow display on bookings and orders.
    """,
    'author': 'SIC Rwanda',
    'website': 'https://www.sicrwanda.com',
    'depends': ['salon_management'],
    'data': [
        'data/salon_stages_data.xml',
        'views/salon_stage_views.xml',
        'views/salon_booking_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}