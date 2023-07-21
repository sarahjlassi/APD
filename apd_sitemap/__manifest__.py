# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Website Sitemap',
    'version': '1.1',
    'category': '',
    'depends' : ['base','website'],
    'description': """""",
    'data': [
       'views/sitemap.xml',
       'views/sitemap_front.xml',

    ],
    'demo': [
      
    ],
    'assets': {
        'web.assets_frontend': [
            'apd_sitemap/static/src/css/sitemap.css',
        ]
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
