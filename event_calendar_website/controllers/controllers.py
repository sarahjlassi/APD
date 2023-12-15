# -*- coding: utf-8 -*-
from odoo.http import request
from odoo import http, models, fields, _

class EventCalendar(http.Controller):

    @http.route('/get_events', type='json', auth='public')
    def get_events(self, **kw):
        events = request.env['event.event'].search([('website_published','=',True)])  # Fetch events from the model
        event_data = []
        for event in events:
            #print('event',event.name)
            #print('start',event.date_begin)
            event_data.append({
                'title': event.name,
                'start': event.date_begin.date(),
                'end': event.date_end.date(),
                'url': f'/event/{event.id}'
            })
        return event_data
