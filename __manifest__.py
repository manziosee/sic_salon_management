# -*- coding: utf-8 -*-
{
    'name': 'SIC Salon Management',
    'version': '1.0.0',
    'category': 'Services',
    'summary': 'Custom colored stages and workflow for salon bookings',
    'description': """
        Extends salon_management by adding colored stages with Cancel and custom workflow on salon bookings.
        Adds views for stages since base module has none.
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