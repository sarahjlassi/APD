from odoo import api, fields, models
from deep_translator import GoogleTranslator


class Res_Partner_Inhert(models.Model):
    _inherit = 'res.partner'

    # @api.depends('name')
    # def get_english_name(self):
    #     for rec in self:
    #         if rec.name:
    #             rec.en_name = GoogleTranslator(source='auto', target='en').translate(rec.name)

    #         else:
    #             rec.en_name = " "

    # def inverse_for_english_name(self):
    #     pass

    en_name = fields.Char(string="English Name")
