from odoo import models, fields


class Category(models.Model):
    _name = 'shop.category'
    _description = 'categories of shops'

    name = fields.Char(string='اسم التصنيف')
    # quest_id = fields.One2many("registration.quiz", 'category_ids',string='')

