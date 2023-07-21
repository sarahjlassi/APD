# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Register in website',
    'version': '1.1',
    'category': '',
    'depends' : ['base','website','auth_signup','contacts','portal'],
    'description': """""",
    'data': [
        'views/user_register_form_website.xml',
        'views/res_partner_inherit.xml',
        'views/my_account_details.xml',
    ],
    'demo': [
      
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
