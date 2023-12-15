# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ejad_nafath_features(models.Model):
#     _name = 'ejad_nafath_features.ejad_nafath_features'
#     _description = 'ejad_nafath_features.ejad_nafath_features'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
