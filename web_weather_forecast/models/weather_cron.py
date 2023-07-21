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
import requests
import json
from datetime import datetime
import pytz

class IrCron(models.Model):
    _inherit = 'ir.cron'

    is_weather_scheduler = fields.Boolean(default=False,string="Is Weather Scheduler")

class ResConfigUsers(models.Model):
    _inherit = 'res.users'

    weather_enable = fields.Boolean(string='Weather Alert',copy=False)
    mute_weather_alert = fields.Boolean(string = 'Mute Weather Alert')

    def __init__(self, pool, cr):
        """Override of __init__ to add access rights.
        Access rights are disabled by default, but allowed on some specific
        fields defined in self.SELF_{READ/WRITE}ABLE_FIELDS.
        """
        super(ResConfigUsers, self).__init__(pool, cr)
        # duplicate list to avoid modifying the original reference
        type(self).SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        type(self).SELF_WRITEABLE_FIELDS.extend(["weather_enable"])
        # duplicate list to avoid modifying the original reference
        type(self).SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
        type(self).SELF_READABLE_FIELDS.extend(["weather_enable"])
        # duplicate list to avoid modifying the original reference
        type(self).SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        type(self).SELF_WRITEABLE_FIELDS.extend(["mute_weather_alert"])
        # duplicate list to avoid modifying the original reference
        type(self).SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
        type(self).SELF_READABLE_FIELDS.extend(["mute_weather_alert"])

    def prepare_alert_html_content(self,alerts,tz):
        html_content = ''
        for alert in range(len(alerts)):

            user_timezone = pytz.timezone(tz)

            timezone_start_date = datetime.fromtimestamp(alerts[alert].get('start')).replace(tzinfo=pytz.UTC).astimezone(pytz.timezone(tz))
            timezone_end_date = datetime.fromtimestamp(alerts[alert].get('end')).replace(tzinfo=pytz.UTC).astimezone(pytz.timezone(tz))

            
            changed_description = alerts[alert].get('description').replace("\n", "<br/>")
            html_content += '''
                                <table border="0" cellpadding="0" cellspacing="0" bgcolor="#F0F0F0" style="width:100%">
                                  <tr>
                                    <td align="center" valign="top" bgcolor="#F0F0F0" style="background-color: #F0F0F0;">
                                      <br>
                                      <table border="0" width="600" cellpadding="0" cellspacing="0" class="container alert_table">
                                        <tr>
                                          <td class="container-padding header" align="left" style="font-family:Helvetica, Arial, sans-serif;font-size:24px;font-weight:bold;padding-bottom:12px;color:#DF4726;padding-left:24px;padding-right:24px">
                                            '''+alerts[alert].get('event')+'''
                                          </td>
                                        </tr>
                                        <tr>
                                          <td class="container-padding content" align="left" style="padding-left:24px;padding-right:24px;padding-top:12px;padding-bottom:12px;background-color:#ffffff">
                                            <br>

                                <div class="title" style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;color:#374550">By : '''+alerts[alert].get('sender_name')+'''</div>
                                <div class="title" style="font-family:Helvetica, Arial, sans-serif;font-size:18px;font-weight:600;color: #1f7eca;font-size: small;">From : '''+timezone_start_date.strftime("%d/%m/%Y, %H:%M:%S")+'''&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;To : '''+ timezone_end_date.strftime("%d/%m/%Y, %H:%M:%S")+'''</div>
                                <br>

                                <div class="body-text" style="font-family:Helvetica, Arial, sans-serif;font-size:14px;line-height:20px;text-align:left;color:#333333">
                                  '''+changed_description+'''
                                </div>
                                </td></tr><tr><td><div style="height:10px;"></div></td></tr></tbody></table></td></tr><tr><td><div style="height:10px;"></div></td></tr></tbody></table>'''
        return html_content

    def sync_scheduled_weather(self,user_id):
        ir_config = self.env['ir.config_parameter'].sudo()
        res_user = self.sudo().browse(user_id)
        api_key = ir_config.get_param('web_weather_forecast.api_key')
        if res_user:
            user_lat= res_user.partner_id.partner_latitude
            user_long = res_user.partner_id.partner_longitude
            if api_key and api_key != 'False':
                alert_url = 'http://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&units=metric&appid=%s&lang=%s'%(user_lat,user_long,api_key,res_user.lang.split('_')[0])
                alert_response = requests.get(alert_url)
                alert_json_response = alert_response.json()

                if 'alerts' in alert_json_response:
                    html_content = self.prepare_alert_html_content(alert_json_response.get('alerts'),res_user.tz)

                    if not res_user.mute_weather_alert:
                        mail_values = {
                            'subject': "Notification regarding weather alert on your location",
                            'email_from': self.company_id.partner_id.email_formatted if self.company_id else self.env.user.email_formatted,
                            'email_to': res_user.login,
                            'body_html': html_content,
                            'auto_delete': True,
                        }
                        mail = self.env['mail.mail'].sudo().create(mail_values).send(raise_exception=False)

                    user_weather_alert_data = self.env['user.weather.alert'].search([('user_id','=',res_user.id)])
                    if user_weather_alert_data:
                        user_weather_alert_data.write({'check_for_weather' : True,'weather_data' : html_content})
                    else:
                        user_weather_alert_id = self.env['user.weather.alert'].create({
                                                    'user_id' : res_user.id,
                                                    'check_for_weather' : True,
                                                    'weather_data' : html_content,
                                                })


    def write(self, values):
        res = super(ResConfigUsers, self).write(values)
        if 'weather_enable' in values:
            for user in self:
                user.update_weather_scheduler(user.id,user.name,values.get('weather_enable'))
        return res


    @api.model
    def create(self,values):
        res = super(ResConfigUsers, self).create(values)
        for user in res:
            if 'weather_enable' in values and values.get('weather_enable') and user.has_group('base.group_user'):
                user.create_weather_scheduler(res.id,res.name,values.get('weather_enable'))
        return res

    def unlink(self):
        for user in self:
            s_name = "National Weather Alert Notification_"+str(user.id)+"_"+user.name;
            alert_cron = self.env['ir.cron'].sudo().search([('name','=',s_name),('active','=',False)], limit=1)
            if not alert_cron:
                alert_cron = self.env['ir.cron'].sudo().search([('name','=',s_name),('active','=',True)], limit=1)
            if alert_cron:
                alert_cron.unlink()
        return super(ResConfigUsers,self).unlink()

    def create_weather_scheduler(self,res_id,res_name,res_weather_enable):
        modelOBJ = self.env['ir.model'].sudo()
        model_id = modelOBJ.search([('model','=','res.users')],limit=1)
        value = {
                 'name':"National Weather Alert Notification_" + str(res_id) + "_" + res_name,
                 'model_id':model_id.id,
                 'state':'code',
                 'active':res_weather_enable,
                 'interval_number':1,
                 'interval_type':'hours',
                 'numbercall' : -1,
                  }
        create_scheduled_id = self.env['ir.cron'].sudo().create(value)
        create_scheduled_id.is_weather_scheduler = True
        model_name = "res.users"
        automation_code = "env['res.users'].browse(" + str(res_id) +  ").sync_scheduled_weather("+str(res_id)+")"

        if automation_code:
            create_scheduled_id.write({'code':automation_code})

    def update_weather_scheduler(self,id,name,weather_enable):
        s_name = "National Weather Alert Notification_"+str(id)+"_"+name;
        res = self.env['ir.cron'].sudo().search([('name','=',s_name),('active','=',False)], limit=1)
        if not res:
            res = self.env['ir.cron'].sudo().search([('name','=',s_name),('active','=',True)], limit=1)
        if res:
            res.is_weather_scheduler = True
            res.active = weather_enable
        else:
            self.create_weather_scheduler(id,name,weather_enable)
