# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016-Today Geminate Consultancy Services (<http://geminatecs.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    openweather_api_key = fields.Char(string='Api Key')
    

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        urlconfig = self.env['ir.config_parameter'].sudo()
        api_key = urlconfig.get_param('web_weather_forecast.api_key')
        if api_key == False:
            self.env['ir.config_parameter'].sudo().set_param('web_weather_forecast.api_key', 'False')
            res.update(
                openweather_api_key=False
            )
        elif api_key == 'False':
            self.env['ir.config_parameter'].sudo().set_param('web_weather_forecast.api_key', 'False')
            res.update(
                openweather_api_key=False
            )
        else:
            res.update(
                openweather_api_key=str(api_key)
            )
        return res

    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param('web_weather_forecast.api_key', str(self.openweather_api_key))
        super(ResConfigSettings, self).set_values()
        
        
        