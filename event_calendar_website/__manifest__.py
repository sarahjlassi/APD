# -*- coding: utf-8 -*-
{
    'name': "event_calendar_website",

    'summary': """
        This module integrated full calendar javascript library to allow the user to switch between calendar view and defaut card view in the event website page""",

    'description': """
         This module integrated full calendar javascript library to allow the user to switch between calendar view and defaut card view in the event website page

    """,

    'author': "Asma Ben Brahem",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website_event'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/card_view.xml',
        'views/templates.xml',
    ],

    'assets': {

        'web.assets_frontend': [


"event_calendar_website/static/src/js/index.global.min.js",
"event_calendar_website/static/src/js/locales-all.global.min.js",
"event_calendar_website/static/src/js/event_calendar.js",

            "event_calendar_website/static/src/css/calendar.css"
        ],

    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
