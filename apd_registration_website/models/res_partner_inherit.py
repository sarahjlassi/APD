# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner_Inherit(models.Model):
    _inherit = "res.partner"

    #add fields to set value of signup users in (res.partner)
    id_number = fields.Char("National ID")
