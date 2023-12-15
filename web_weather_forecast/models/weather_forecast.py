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
from odoo import api, models,fields,_
import requests
import json

class UserWeatherAlert(models.Model):
    
    _name = 'user.weather.alert'
    
    user_id = fields.Many2one("res.users",string="User")
    weather_data = fields.Html('Weather Alert Data')
    check_for_weather = fields.Boolean('Check For Weather',default=False)
    
    def check_for_alert(self,user_id):
        res_user_id = self.sudo().search([('user_id','=',self.env.user.id)])
        if res_user_id.check_for_weather:
            return res_user_id.weather_data
        else:
            return False
        
    def clear_alert_data(self,user_id):
        res_user_id = self.sudo().search([('user_id','=',user_id)])
        if res_user_id:
            res_user_id.check_for_weather = False
            res_user_id.weather_data = False

        
class Http(models.AbstractModel):
    _inherit = 'ir.http'
    
    def session_info(self):
        session_info = super(Http,self).session_info()
        if self.env.user.partner_id and self.env.user.partner_id.country_id:
            country_name= self.env.user.partner_id.country_id.code
            session_info.update({'user_country':country_name})
            
        if self.env.user.partner_id and self.env.user.partner_id.state_id:   
            state_name = self.env.user.partner_id.state_id.code
            session_info.update({'user_state':state_name})
            
        if self.env.user.partner_id and self.env.user.partner_id.city:   
            city = self.env.user.partner_id.city
            session_info.update({'user_city':city})
            
        if self.env.user.partner_id:   
            partner_latitude = self.env.user.partner_id.partner_latitude
            partner_longitude = self.env.user.partner_id.partner_longitude
            session_info.update({
                'partner_latitude' : partner_latitude,
                'partner_longitude' : partner_longitude,
                'mute_weather_alert' : self.env.user.mute_weather_alert
            })
            
        ir_config = self.env['ir.config_parameter'].sudo()
        api_key = ir_config.get_param('web_weather_forecast.api_key')
        if api_key and api_key != 'False':
            session_info.update({'openweather_api_key':api_key})
        else:
            session_info.update({'openweather_api_key':False})   
          
        return session_info


    
    