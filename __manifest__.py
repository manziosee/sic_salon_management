{
    'name': 'SIC Salon Management',
    'version': '17.0.1.0.0',
    'category': 'Services',
    'summary': 'Salon Management Customizations with Colored Stages',
    'description': """
        Extend salon_management with custom colored stages and stages on bookings and orders.
    """,
    'author': 'SIC Rwanda',
    'website': 'https://www.sicrwanda.com',
    'depends': ['salon_management'],
    'data': [
        'data/salon_stages_data.xml',   
        'views/salon_stage_views.xml',
        'views/salon_booking_views.xml',
        'views/salon_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}