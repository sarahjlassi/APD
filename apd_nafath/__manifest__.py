# -*- coding: utf-8 -*-
{
    'name': "apd_nafath",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        apd integration with nafath
    """,
    'version': '15.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'ejad_nafath'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/card_view.xml',
    ],
}
