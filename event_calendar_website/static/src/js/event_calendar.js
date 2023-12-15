odoo.define('event_calendar_website.event_calendar_widget', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');
    var core = require('web.core');

   publicWidget.registry.EventCalendarWidget = publicWidget.Widget.extend({
        selector: '#event_container',

        events: {
            'click #toggleCardView': '_onShowCardClick',
            'click #toggleCalendarView': '_onShowCalendarClick',
        },

        init: function () {
        console.log('init')
            this._super.apply(this, arguments);
            this.language = document.getElementById('current_lang').value;
            this.userTimezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
            console.log(this.language)
        },

        start: function () {
        console.log('start')

            this.renderCalendar();
            return this._super.apply(this, arguments);
            console.log('end start')
        },

        renderCalendar: function () {
        var $calendarEl=this.$('#calendar')[0];
            if ($calendarEl) {
                var localeLang;
                if (this.language === 'en_US') {
                    localeLang = 'en';
                } else if (this.language === 'ar_001') {
                    localeLang = 'ar';
                }
                //console.log('calendar',$calendarEl)
                //console.log('lang',localeLang)

                this.calendar = new FullCalendar.Calendar($calendarEl, {
                    timeZone: this.userTimezone,
                    initialView: 'dayGridMonth',


                    locale: localeLang,
                    events: function (fetchInfo, successCallback, failureCallback) {
                        ajax.jsonRpc('/get_events', 'call', {}).then(function (data) {
                            var events = data.map(function (event) {
                                return {
                                    title: event.title,
                                    start: event.start,
                                    end: event.end,
                                    url: event.url
                                };
                            });
                            console.log('events',events)
                            successCallback(events);
                        }).catch(function (error) {
                            console.error('Error fetching events:', error);
                        });
                    }
                });
                console.log('calendar va',calendar)

                console.log('calendar before rendering',calendar)


                this.calendar.render();
                console.log('calendar after rendering',calendar)
            }
        },

        _onShowCardClick: function (ev) {
            console.log('card toggle clicked');

            const $link = $(ev.currentTarget);
            const $cardViewContainer = this.$('#cardViewContainer');
            const $calendarViewContainer = this.$('#calendarViewContainer');
            $cardViewContainer.attr({'style': 'display:block'});
            $calendarViewContainer.attr({'style': 'display:none'});

        },

        _onShowCalendarClick: function (ev) {
            console.log('calendar toggle clicked');

            const $link = $(ev.currentTarget);
            const $cardViewContainer = this.$('#cardViewContainer');
            const $calendarViewContainer = this.$('#calendarViewContainer');
            $cardViewContainer.attr({'style': 'display:none'});
            $calendarViewContainer.attr({'style': 'display:block'});

            this.calendar.render();
        },
    });

    return publicWidget.registry.EventCalendarWidget;
});
