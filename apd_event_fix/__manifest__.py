# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Event Website  Custom',
    'version': '1.1',
    'category': '',
    'depends': ['base', 'website_event'],
    'description': """""",
    'data': [
        'views/website_event_register.xml',
        'views/res_partner.xml',
    ],
    'demo': [

    ],
    'external_dependencies': {
        'python': ['deep_translator']
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
