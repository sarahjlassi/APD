# Copyright 2015 Grupo ESOC Ingeniería de Servicios, S.L.U. - Jairo Llopis
# Copyright 2019 Tecnativa - Cristina Martin R.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    "name": "Website Breadcrumbs",
    "summary": "Let you have breadcrumbs in website pages",
    "version": "13.0.1.0.0",
    "category": "Website",
    "website": "https://github.com/OCA/website",
    "author": "Grupo ESOC Ingeniería de Servicios, Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": ["website","web"],
    "data": ["views/templates.xml", "views/layout.xml"],
    "assets": {
        'web.assets_frontend': [
            'website_breadcrumb/static/src/css/bootstrap.css',

        ],
    }
}
