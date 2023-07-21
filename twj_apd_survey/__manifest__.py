# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'Custom Survey',
    'version': '1.1',
    'category': '',
    'depends' : ['base','survey','web'],
    'description': """""",
    'data': [
        'views/survey_view.xml',
       'views/survey_temp.xml',
       'views/powered_by.xml',
    ],
    'demo': [
      
    ],
    'assets' : {
        'survey.survey_assets' : [
            'twj_apd_survey/static/src/js/servey_form.js',
        ]
    },
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
