
from odoo import api, fields, models

class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    max_length = fields.Integer(string="Max Length",default=0 )
    min_length = fields.Integer(string="Minimum Length",default=0 )
    start_with = fields.Char(string="Starts With",default="")
