from odoo import models, fields


class Category(models.Model):
    _name = 'shop.category'
    _description = 'categories of shops'

    name = fields.Char(string='اسم التصنيف')

