# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ticket chat customizations',
    'version': '1.1',
    'category': '',
    'depends': ['base', 'portal'],
    'description': """""",
    'data': [
        'views/helpdesk_parameter.xml',
    ],
    'demo': [

    ],
    'assets': {
        'web.assets_frontend': [
            'apd_ticket_portal/static/src/js/demo_example.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
