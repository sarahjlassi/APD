# -*- coding: utf-8 -*-
{
    'name': "website_inherit",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/card_view.xml',
        'views/templates.xml',
        'views/dash.xml',
        'views/event_calendar.xml'
    ],

    'assets': {

        'web.assets_frontend': [

            # "website_inherit/static/src/js/rating.js",
            "website_inherit/static/src/js/index.global.min.js",
            "website_inherit/static/src/js/locales-all.global.min.js",
            "website_inherit/static/src/js/event_calendar.js",
            #           "website_inherit/static/src/css/rating.css",
            "website_inherit/static/src/css/calendar.css"
        ],

    },

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
