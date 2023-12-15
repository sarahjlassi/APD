# -*- coding: utf-8 -*-
###############################################################################
#
#   Copyright (C) 2004-today OpenERP SA (<http://www.openerp.com>)
#   Copyright (C) 2016-today Geminate Consultancy Services (<http://geminatecs.com>).
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': 'Weather Forecast',
    "version": "15.0.0.1",
    'category': 'Web',
    'summary': ''' Geminate comes with a feature of weather information, weather notification and alerts based on natural calamities. weather information mainly covers current precipitation, humidity, wind, sunset, sunrise and temperature of current logged in user's location. it also provides information of daily, hourly weather apart from the current climate. ''',
    'website': 'www.geminatecs.com',
    'author': 'Geminate Consultancy Services',
    'license': 'Other proprietary',
    'depends': ['mail','base_geolocalize'],
    "description": """Geminate comes with a feature of weather information, weather notification and alerts based on natural calamities. weather information mainly covers current precipitation, humidity, wind, sunset, sunrise and temperature of current logged in user's location. it also provides information of daily, hourly weather apart from the current climate.""",
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/res_user_views.xml',
    ],
    'images': ['static/description/weather_forecast.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'assets': {
        'web.assets_backend': [
            'web_weather_forecast/static/src/css/weather_forecast.css',
            'web_weather_forecast/static/src/js/*',
        ],
        'web.assets_qweb': [
            'web_weather_forecast/static/src/xml/*',
        ],
    },
    'price': 54.99,
    'currency': 'EUR',
}
