# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'APD Recuritment',
    'version': '1.1',
    'category': '',
    'depends' : ['base','website_hr_recruitment','hr_recruitment', 'ejad_nafath'],
    'description': """""",
    'data': [
        'security/ir.model.access.csv',
        'views/apply_job.xml',
        'views/hr_applicant.xml',
        'views/d_type.xml',
        'views/degree_degree.xml',
    ],
    'demo': [
      
    ],
    'assets': {
        'web.assets_frontend': [
            # '/apd_recruitment/static/src/scss/style.css',
            '/apd_recruitment/static/src/scss/custom.scss',
            '/apd_recruitment/static/src/js/degree_applicant.js',
            '/apd_recruitment/static/src/js/jquery.steps.js',
            '/apd_recruitment/static/src/js/steps.js',
        ],
    },

    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
