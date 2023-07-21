# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Create New Type of news to add employees News',
    'version': '1.1',
    'category': '',
    'depends' : ['base','website_blog'],
    'description': """""",
    'data': [
       'views/emp_news.xml',
       'views/blog_blog.xml',
    ],
    'demo': [
      
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    "assets": {
        'web.assets_frontend': [
            'twj_employees_news/static/src/css/index.css',

        ],
    }
}
