# -*- coding: utf-8 -*-
{
    'name': "Rating APD",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Asma Ben Brahem",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/security.xml',
         'security/ir.model.access.csv',
        'views/card_view.xml',
        'views/templates.xml',
        'views/dash.xml',
    ],
  'assets': {

        'web.assets_frontend': [

"rating_apd/static/src/js/rating.js",

            "rating_apd/static/src/css/rating.css",

        ],

    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
