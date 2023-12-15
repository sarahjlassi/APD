# -*- coding: utf-8 -*-
{
    'name': "test_apd",

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
    'sequence': 1,



    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'mail'],

    # always loaded
    'data': [

        'security/ir.model.access.csv',
        'data/approved_email_template.xml',
        'security/security.xml',
        'views/templates.xml',
        'views/menus.xml',
        'views/category_view.xml',
        'views/card_view.xml',
        'views/quiz_view.xml',
        'views/dash.xml',
        'views/registration.xml',

    ],

    'assets': {

        'web.assets_frontend': [
            "test_apd/static/src/js/most_viseted_cards.js",
            "test_apd/static/src/js/registration_validation.js",
            # "apd_test/static/js/filter_script.js",

        ],

    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
