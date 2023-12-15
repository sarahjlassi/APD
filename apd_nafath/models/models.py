# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class apd_nafath(models.Model):
#     _name = 'apd_nafath.apd_nafath'
#     _description = 'apd_nafath.apd_nafath'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
