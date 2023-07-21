

{
    "name": "Event Templates Custom",
    "version": "15.0.1.0.0",
    "author": "",
    "license": "AGPL-3",
    "website": "",
    "category": "Tools",
    "depends": ["base",'event','documents', 'mass_mailing'],
    "data": [
        "security/ir.model.access.csv",
        "views/full_page_ticket.xml",
        "views/foldable_badge.xml",
        "views/document_enhance.xml",
        "views/email_marketing_templates.xml",
    ],
    "application": True,
    "installable": True,
    'assets': {
        'web.assets_frontend': [
            'event_template/static/src/scss/event.css',
        ]
    }
}
