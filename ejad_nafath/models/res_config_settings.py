# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sp_api_key = fields.Char(string="SP API Key")
    nafath_url = fields.Char(string="Nafath URL")
    user_info=fields.Char(string="User Info Server URL")

    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param('ejad_nafath.sp_api_key', self.sp_api_key)
        self.env['ir.config_parameter'].sudo().set_param('ejad_nafath.nafath_url', self.nafath_url)
        self.env['ir.config_parameter'].sudo().set_param('ejad_nafath.user_info', self.user_info)
        super(ResConfigSettings, self).set_values()

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['sp_api_key'] = self.env['ir.config_parameter'].sudo().get_param('ejad_nafath.sp_api_key', False)
        res['nafath_url'] = self.env['ir.config_parameter'].sudo().get_param('ejad_nafath.nafath_url', False)
        res['user_info'] = self.env['ir.config_parameter'].sudo().get_param('ejad_nafath.user_info', False)
        return res
