# -*- coding: utf-8 -*-
{
    'name': "ejad_nafath_features",

    'summary': """
        NEw features for ejad_nafath module""",

    'description': """
        1- if who login is person redirect to nafath
    """,
    'category': 'Uncategorized',
    'version': '15.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'ejad_nafath'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/update_user_info.xml',
    ],
}
