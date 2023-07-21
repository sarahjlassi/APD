# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Helpdesk connected to website as ticketing tool 2',
    'version': '1.1',
    'category': '',
    'depends' : ['base','website','helpdesk','apd_registration_website'],
    'description': """""",
    'data': [
        'security/ir.model.access.csv',
       'views/website_contact_us.xml',
       'views/helpdesk_ticket.xml',
       'views/helpdesk_team.xml',
       'views/helpdesk_stages.xml',
       'views/helpdesk_route.xml',
       'views/helpdesk_portal.xml',
    ],
    'demo': [
      
    ],

    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
