from odoo import api, fields, models

class Website_Blog_Blog_Blog(models.Model):
    _inherit = 'blog.blog'

    type_of_news = fields.Selection(string="Type Of News", selection=[('all', 'General News'), ('emp', 'Employees News'), ], required=False, )

