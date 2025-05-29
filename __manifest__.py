{
    'name': 'SIC Salon Management',
    'version': '1.0.1',
    'category': 'Services',
    'summary': 'Extended salon management with reminders and enhanced status tracking',
    'description': """
        Extends salon management with:
        - Enhanced status tracking with colors
        - Appointment reminders
        - Improved workflow
    """,
    'author': 'SIC Rwanda',
    'website': 'https://www.sicrwanda.com',
    'depends': ['salon_management'],
    'data': [
        'security/ir.model.access.csv',
        'data/salon_management_mail_template.xml',
        'data/salon_stages_data.xml',
        'views/salon_booking_views.xml',
        'views/salon_order_views.xml',
        'views/salon_management_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'sic_salon_management/static/src/js/salon_dashboard.js',
            'sic_salon_management/static/src/xml/salon_dashboard.xml',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
