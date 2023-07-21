odoo.define('web_weather_forecast.WeatherForecast', function (require) {
"use strict";

var core = require('web.core');
var session = require('web.session');

var SystrayMenu = require('web.SystrayMenu');
var Widget = require('web.Widget');
var rpc = require('web.rpc');
var QWeb = core.qweb;

var Dialog = require('web.Dialog');
var _t = core._t;

	var WeatherForecast = Widget.extend({
	    name: 'weather_menu_bar',
	    template:'web_weather_forecast.systray.WeatherForecast',
	    events: {
			'show.bs.dropdown': '_onWeatherDropdownShow',
			"click .toggle_hourly_daily span.daily_tab": "_onDailyTabClick",
			"click .toggle_hourly_daily span.hourly_tab": "_onHourlyTabClick",
			"click .daily_prev" : "_onDailyPrevClick",
			"click .daily_next" : "_onDailyNextClick",
			"click .hourly_prev" : "_onHourlyPrevClick",
			"click .hourly_next" : "_onHourlyNextClick",
			"click .daily" : "_onDailyClick",
			"click .hour" : "_onHourlyClick",
			"click .weather_container" : "_onClickWeatherContainer",
			"hashchange window" : 'checkWeatherAlert',
		},

	    start: function () {
		   var self = this;
	       this._$weatherPreview = this.$('.o_weather_forecast_systray_dropdown_items');
	       this.checkWeatherAlert();
	       window.setInterval(this.checkWeatherAlert.bind(this), (18000));
	       this._super.apply(this, arguments)
	    },

	    checkWeatherAlert : function(){
	    	var self = this;
	    	rpc.query({
	    		model : 'user.weather.alert',
	    		method : 'check_for_alert',
	    		args : [,session.user_context.uid]
	    	}).then(function(data){
	    		if(data) {
	    			var alerts = []
	    			self.alerts = data
					self.$el.find('.o_weather_alert_counter').text($(data).find('table.alert_table').length)
					self.$el.find('a i.fa-cloud').hide();
	    			self.$el.find('a img').show();
					if(!session['mute_weather_alert']) {
						self.$el.find('a').addClass('alert_blink')
					}
	    		}
	    		else {
	    			self.alerts = false
					self.$el.find('a').removeClass('alert_blink')
					self.$el.find('a i.fa-cloud').show();
	    			self.$el.find('a img').hide();
	    			self.$el.find('.o_weather_alert_counter').text('')
	    		}
	    	})
	    },

	    _onDailyPrevClick : function (ev) {
	    	ev.preventDefault();
	    	ev.stopPropagation();
	    	this._$weatherPreview.find("#dailyWeatherControls").carousel("prev");
	    },

	    _onDailyNextClick : function (ev) {
	    	ev.preventDefault();
	    	ev.stopPropagation();
	    	this._$weatherPreview.find("#dailyWeatherControls").carousel("next");
	    },

	    _onHourlyPrevClick : function (ev) {
	    	ev.preventDefault();
	    	ev.stopPropagation();
	    	this._$weatherPreview.find("#hourlyWeatherControls").carousel("prev");
	    },

	    _onHourlyNextClick : function (ev) {
	    	ev.preventDefault();
	    	ev.stopPropagation();
	    	this._$weatherPreview.find("#hourlyWeatherControls").carousel("next");
	    },

	    _onDailyClick : function (ev) {
	    	ev.preventDefault();
	    	ev.stopPropagation();
	    	var dailyid = $(ev.currentTarget).attr('id');
	    	dailyid = dailyid.split('daily_')[1];
	    	this._$weatherPreview.find("#dailyWeatherControls").carousel(parseInt(dailyid));
	    },

	    _onHourlyClick : function (ev) {
	    	ev.preventDefault();
	    	ev.stopPropagation();
	    	var hourlyid = $(ev.currentTarget).attr('id');
	    	hourlyid = hourlyid.split('hourly_')[1];
	    	this._$weatherPreview.find("#hourlyWeatherControls").carousel(parseInt(hourlyid));
	    },

	    _onClickWeatherContainer : function (ev) {
	    	ev.preventDefault();
	    	ev.stopPropagation();
	    },

	    _onWeatherDropdownShow : function () {
	    	this._updateWeatherPreview();
	    },

	    _onDailyTabClick : function (event) {
	    	event.preventDefault();
            event.stopPropagation();
            var self = this;
            $(event.currentTarget).removeClass('inactive_forecast').addClass('active_forecast')
            this._$weatherPreview.find('.hourly_tab').removeClass('active_forecast').addClass('inactive_forecast')
            this._$weatherPreview.find('.hourly_weather').hide()
            this._$weatherPreview.find('.daily_weather').show()
	    },

	    _onHourlyTabClick : function (event) {
	    	event.preventDefault();
            event.stopPropagation();
            var self = this;
            $(event.currentTarget).removeClass('inactive_forecast').addClass('active_forecast')
            this._$weatherPreview.find('.daily_tab').removeClass('active_forecast').addClass('inactive_forecast')
            this._$weatherPreview.find('.daily_weather').hide()
            this._$weatherPreview.find('.hourly_weather').show()
	    },

	    _updateWeatherPreview : function(){
	    	var self = this;
	    	var params_val = '';

	    	if(session['openweather_api_key'])
	    		self.openweather_api_key = session['openweather_api_key']
	    	else
	    		self.openweather_api_key = false

			if(session['user_city']) {
				params_val += session['user_city'] + ','
	    		self.user_city = session['user_city']
			}
	    	else
	    		self.user_city = false

			if(session['user_state']) {
				params_val += session['user_state'] + ','
	    		self.user_state = session['user_state']
			}
	    	else
	    		self.user_state = false

	    	if(session['user_country']) {
	    		params_val += session['user_country']
	    		self.user_country = session['user_country']
	    	}
	    	else
	    		self.user_country = false


	    	if(params_val.charAt(params_val.length - 1) == ',') {
	    		params_val = params_val.splice(-1)
	    	}

	    	if(self.alerts && self.openweather_api_key) {
	    		self._$weatherPreview.html(QWeb.render('web_weather_forecast.systray.Previews', {
	            	widget: self
		        }));

	    		rpc.query({
	    			'model' : 'user.weather.alert',
	    			'method' : 'clear_alert_data',
	    			'args' : [,session.user_context.uid],
	    		}).then(function(){
	    			self.$el.find('.o_weather_alert_counter').text('')
					self.$el.find('a').removeClass('alert_blink')
					self.$el.find('a i.fa-cloud').show();
	    			self.$el.find('a img').hide();
					self.alerts = false;
	    		})
	    	}

	    	else if(self.openweather_api_key){
	    		var current_weather_url = "http://api.openweathermap.org/data/2.5/onecall?lat=" + session['partner_latitude'] + '&lon=' + session['partner_longitude'] +  '&units=metric&appid=' + self.openweather_api_key + '&lang=' + session.user_context.lang.split('_')[0]
				$.getJSON(current_weather_url,function(json){

		            var celsius,fahrenheit,humidity,sunrise,sunset,max_temp,min_temp,pressure,wind_speed,wind_deg,weather_description,weather_icon;

		            if(json.current) {
		            	self.celsius = Math.round(json.current.temp)
	        			self.fahrenheit = Math.round(((self.celsius * (9/5)) + 32))
						self.humidity = json.current.humidity
						self.pressure = json.current.pressure
						self.wind_deg = json.current.wind_deg
						self.wind_speed = Math.round((json.current.wind_speed * 2.237 * 1.609))

		            	var risedateObj = new Date(json.current.sunrise * 1000);
		                var setdateObj = new Date(json.current.sunset * 1000);
		            	self.sunrise = risedateObj.toLocaleTimeString("en-US", {timeZone: session['user_context'].tz,hour: '2-digit', minute:'2-digit'})
	        			self.sunset = setdateObj.toLocaleTimeString("en-US", {timeZone: session['user_context'].tz,hour: '2-digit', minute:'2-digit'})
		            }

		            if(json.current.weather.length > 0) {
		            	self.weather_description = json.current.weather[0].description
	        			self.weather_icon = json.current.weather[0].icon
		            }

		            if(json.hourly.length > 0) {
		            	self.hourly_data = []
	        			var hourly_cnt = 0
		            	_.each(json.hourly,function(hourdata){
		            		var hourdateObj = new Date(hourdata.dt * 1000);
		            		var hourdatestr = hourdateObj.toLocaleDateString("en-US", {timeZone: session['user_context'].tz,day: '2-digit', month:'2-digit',year : '2-digit'})
	        				var hourtimestr = hourdateObj.toLocaleTimeString("en-US", {timeZone: session['user_context'].tz,hour: '2-digit', minute:'2-digit'})

	        				self.hourly_data.push({
		            			'celsius' : Math.round(hourdata.temp),
		            			'fahrenheit': Math.round((hourdata.temp * (9/5) + 32)),
		            			'wind_speed' : Math.round((hourdata.wind_speed * 2.237 * 1.609)),
		            			'humidity' : hourdata.humidity,
		            			'pressure' : hourdata.pressure,
		            			'weather_description' : hourdata.weather[0].description,
		            			'weather_icon' : hourdata.weather[0].icon,
		            			'date' : hourdatestr,
		            			'time' : hourtimestr,
		            			'id' : hourly_cnt,
	        				})
	        				hourly_cnt += 1
		            	});
		            }

		            if(json.daily.length > 0) {
		            	self.daily_data = []
		            	var daily_cnt = 0
		            	_.each(json.daily,function(dailydata){
		            		var sunrisedateObj = new Date(dailydata.sunrise * 1000);
		            		var sunsetdateObj = new Date(dailydata.sunset * 1000);

		            		var sunrisedatestr = sunrisedateObj.toLocaleDateString("en-US", {timeZone: session['user_context'].tz,day: '2-digit', month:'2-digit',year : '2-digit'})
	        				var sunrisetimestr = sunrisedateObj.toLocaleTimeString("en-US", {timeZone: session['user_context'].tz,hour: '2-digit', minute:'2-digit'})

							var sunsetdatestr = sunsetdateObj.toLocaleDateString("en-US", {timeZone: session['user_context'].tz,day: '2-digit', month:'2-digit',year : '2-digit'})
	        				var sunsettimestr = sunsetdateObj.toLocaleTimeString("en-US", {timeZone: session['user_context'].tz,hour: '2-digit', minute:'2-digit'})

	        				var currentdateobj = new Date(dailydata.dt * 1000);

		            		var currentdatestr = currentdateobj.toLocaleDateString("en-US", {timeZone: session['user_context'].tz,day: '2-digit', month:'2-digit',year : '2-digit'})

	        				self.daily_data.push({
		            			'wind_speed' : Math.round((dailydata.wind_speed * 2.237 * 1.609)),
		            			'humidity' : dailydata.humidity,
		            			'pressure' : dailydata.pressure,
		            			'weather_description' : dailydata.weather[0].description,
		            			'weather_icon' : dailydata.weather[0].icon,
		            			'sunrise_date' :  sunrisedatestr,
		            			'sunrise_time' : sunrisetimestr,
		            			'sunset_date' : sunsetdatestr,
		            			'sunset_time' : sunsettimestr,
		            			'min_celsius' : Math.round(dailydata.temp.min),
		            			'min_fahrenheit': Math.round((dailydata.temp.min * (9/5) + 32)),
		            			'max_celsius' : Math.round(dailydata.temp.max),
		            			'max_fahrenheit': Math.round((dailydata.temp.max * (9/5) + 32)),
		            			'date' : currentdatestr,
		            			'id' : daily_cnt,
	        				})
	        				daily_cnt += 1
		            	});
		            }
		            self._$weatherPreview.html(QWeb.render('web_weather_forecast.systray.Previews', {
			             widget: self
			        }));
		        }).fail(function(error) {
		        	self.json_error = error.statusText + " : " + error.responseJSON.message
	        		self._$weatherPreview.html(QWeb.render('web_weather_forecast.systray.Previews', {
	            		widget: self
		        	}));
		        });
	    	}
	    	else{
	    		self._$weatherPreview.html(QWeb.render('web_weather_forecast.systray.Previews', {
	            	widget: self
		        }));
	    	}

	    },

	})

	SystrayMenu.Items.push(WeatherForecast);

	return WeatherForecast;

});
