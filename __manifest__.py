{
    "name": "Inouk Notifications",
    "summary": """Send real time notifications to users using Odoo message bus.""",
    "version": "13.0.0.0.0",
    "license": "LGPL-3",
    "author": "Cyril MORISSE (@cmorisse)",
    "website": "https://github.com/cmorisse/inouk_notifications",
    "depends": [
        "base",
        "bus", 
        "web", 
    ],
    "data": [
        'assets_loader.xml',
        "views/res_users_views.xml"
    ],
}
