# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
import logging

from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.addons.website.controllers.main import Website

from odoo import http
from odoo.http import request

logger = logging.getLogger(__name__)

# Completely arbitrary limits
MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT = IMAGE_LIMITS = (1024, 768)
LOC_PER_SITEMAP = 45000
SITEMAP_CACHE_TIME = datetime.timedelta(hours=12)


# class EventCalendar(http.Controller):
#
#     @http.route('/get_events', type='json', auth='public')
#     def get_events(self, **kw):
#         events = request.env['event.event'].search([('website_published','=',True)])  # Fetch events from the model
#         event_data = []
#         for event in events:
#             #print('event',event.name)
#             #print('start',event.date_begin)
#             event_data.append({
#                 'title': event.name,
#                 'start': event.date_begin.date(),
#                 'end': event.date_end.date(),
#                 'url': f'/event/{event.id}'
#             })
#         return event_data

class WebsiteInherit(Website):
    @http.route([
        '/website/search',
        '/website/search/page/<int:page>',
        '/website/search/<string:search_type>',
        '/website/search/<string:search_type>/page/<int:page>',
    ], type='http', auth="public", website=True, sitemap=False)
    def hybrid_list(self, page=1, search='', ordre='', ordred='', type='', search_type='all', search_ad='',
                    date_begin='', date_end='',
                    siteweb=True, **kw):
        if not search:
            return request.render("website.list_hybrid")

        options = {
            'displayDescription': True,
            'displayDetail': True,
            'displayExtraDetail': True,
            'displayExtraLink': True,
            'displayImage': True,
            'allowFuzzy': not kw.get('noFuzzy'),
            'date_begin': date_begin,
            'date_end': date_end,
        }

        print("ordre", ordre)
        if ordre == '':
            ordre = "asc"
        if type == '':
            type = 'all'

        if search_ad == '':

            data = self.autocomplete(search_type=type, term=search, order='name ' + ordre, limit=500, max_nb_chars=200,
                                     options=options)
        else:

            data = self.autocomplete(search_type=type, term=search_ad, order='name ' + ordred, limit=500,
                                     max_nb_chars=200,
                                     options=options)

            search = search_ad
            ordre = ordred

        results = data.get('results', [])
        search_count = len(results)
        parts = data.get('parts', {})

        step = 50
        pager = portal_pager(
            url="/website/search/%s" % type,
            url_args={'search': search},
            total=search_count,
            page=page,
            step=step
        )

        results = results[(page - 1) * step:page * step]

        values = {
            'pager': pager,
            'results': results,
            'parts': parts,
            'search': search,
            'fuzzy_search': data.get('fuzzy_search'),
            'search_count': search_count,
            'ordre': ordre,
            'type': type,
            'siteweb': siteweb,
            'date_begin': date_begin,
            'date_end': date_end,
            'search_ad': search_ad,
            'ordred': ordred

        }
        return request.render("website.list_hybrid", values)


class RatingController(http.Controller):
    @http.route('/rating/rate', type='http', auth="public", methods=['POST'], website=True)
    def rate(self, **kw):
        choice = request.params.get('choice')
        print("choice", choice)
        print('path', kw.get('path'))
        page = request.env['website.page'].sudo().search([('url', '=', kw.get('path'))])
        if len(page) != 0:
            pagename = page[0].name
        else:
            pagename = kw.get('path')
        if kw.get('rating') == '':
            r = 0
        else:
            r = int(kw.get('rating'))

        rating = request.env['rating.page'].sudo().create({
            'utile': kw.get('choice'),
            'cas_yes': kw.get('radio-choice_yes'),
            'cas_no': kw.get('radio-choice_no'),
            #  'visite': kw.get('visite'),
            # 'ease': kw.get('ease'),
            # 'clarity': kw.get('clarity'),
            'path': kw.get('path'),
            'page_name': pagename,
            # 'satisfaction': kw.get('satisfaction'),
            'rating': r,
            'comment_yes': kw.get('comment_yes'),
            'comment_no': kw.get('comment_no')

        })

        # Do whatever you want with the form data and the rating value
        # For example, save it in a model or process it in any way you need

        # Redirect to a success page or return a response
        return request.render("website_inherit.feedback_sent", {})

    def _get_month_name(self, month):
        month_names = ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر",
                       "نوفمبر", "ديسمبر"];

        return month_names[month - 1]

    @http.route(['/e-portalresults', '/e-portalresults/best_by_month', '/e-portalresults/worst_by_month'], type='http',
                auth="public", website=True)
    def dashboard(self, **kw):

        selectedMonth = int(kw.get('selectedMonth', datetime.datetime.now().month))

        latest_months = []

        # Generate list of last 12 months
        for i in range(12):
            month = (selectedMonth - i + 12) % 12
            latest_months.append((month, self._get_month_name(month)))

        selectedMonth1 = int(kw.get('selectedMonth1', datetime.datetime.now().month))

        latest_months1 = []

        # Generate list of last 12 months
        for i in range(12):
            month = (selectedMonth1 - i + 12) % 12
            latest_months1.append((month, self._get_month_name(month)))

        if len(request.env['rating.page'].sudo().search([])) == 0:
            denom = 1
        else:
            denom = len(request.env['rating.page'].sudo().search([]))

        a1 = (len(request.env['rating.page'].sudo().search([('utile', '=', 'yes')])) / denom) * 100
        a2 = (len(request.env['rating.page'].sudo().search([('utile', '=', 'no')])) / denom) * 100

        # a3 = (len(request.env['rating.page'].sudo().search([('visite', '=', 'monthly')])) / denom) * 100

        # a4 = (len(request.env['rating.page'].sudo().search([('visite', '=', 'sometimes')])) / denom) * 100

        # value1 = '{"labels":["الزيارة الأولى","يوميا ","شهريا","ليس دائما "],"datasets":[{"label":"One","data":[' + '"' + str(a1) + '"' + "," + '"' + str(a2) + '"' + ',' + '"' + str(a3) + '"' + ',' + '"' + str(a4) + '"' + '],"backgroundColor":["#1AA684","#FFB259","#99FCFF","#94BD7B"],"borderColor":["","","",""]}]}'

        value1 = '{"labels":["غير مفيد","مفيد"],"datasets":[{"label":"","data":[' + '"' + str(
            a1) + '"' + "," + '"' + str(a2) + '"' + '],"backgroundColor":["#1AA684","#FFB259"],"borderColor":["",""]}]}'

        b1 = len(request.env['rating.page'].sudo().search([('utile', '=', 'yes')]))
        b2 = len(request.env['rating.page'].sudo().search([('utile', '=', 'no')]))

        # b1 = (len(request.env['rating.page'].sudo().search([('ease', '=', 'very_easy')])) / denom) * 100
        #
        # b2 = (len(request.env['rating.page'].sudo().search([('ease', '=', 'easy')])) / denom) * 100
        #
        # b3 = (len(request.env['rating.page'].sudo().search([('ease', '=', 'neutral')])) / denom) * 100
        #
        # b4 = (len(request.env['rating.page'].sudo().search([('ease', '=', 'difficult')])) / denom) * 100
        # b5 = (len(request.env['rating.page'].sudo().search([('ease', '=', 'very_difficult')])) / denom) * 100
        #
        #
        value2 = '{"labels":["غير مفيد","مفيد"],"datasets":[{"label":"","data":[' + '"' + str(
            b1) + '"' + "," + '"' + str(b2) + '"' + '],"backgroundColor":["#99FCFF","#94BD7B"],"borderColor":["",""]}]}'

        c1 = len(request.env['rating.page'].sudo().search([('cas_yes', '=', 'utile')]))

        c2 = len(request.env['rating.page'].sudo().search([('cas_yes', '=', 'liaison')]))

        c3 = len(request.env['rating.page'].sudo().search([('cas_yes', '=', 'good')]))
        c4 = len(request.env['rating.page'].sudo().search([('cas_yes', '=', 'facile')]))
        c5 = len(request.env['rating.page'].sudo().search([('cas_yes', '=', 'autre_yes')]))

        value3 = '{"labels":["أخرى","التصميم جعله من السهل قراءته","مكتوبة بشكل جيد","الإجابات كانت مرتبطة","كانت مفيدة "],"datasets":[{"label":" ","data":[' + '"' + str(
            c1) + '"' + "," + '"' + str(c2) + '"' + ',' + '"' + str(c3) + '"' + ',' + '"' + str(
            c4) + '"' + ',' + '"' + str(c5) + '"' + '],"backgroundColor":"#1AA684","borderColor":"o-color-1"}]}'

        d1 = len(request.env['rating.page'].sudo().search([('cas_no', '=', 'problem')]))

        d2 = len(request.env['rating.page'].sudo().search([('cas_no', '=', 'manque')]))

        d3 = len(request.env['rating.page'].sudo().search([('cas_no', '=', 'bad')]))

        d4 = len(request.env['rating.page'].sudo().search([('cas_no', '=', 'difficile')]))
        d5 = len(request.env['rating.page'].sudo().search([('cas_no', '=', 'autre_no')]))

        value4 = '{"labels":["أخرى","التصميم جعله من الصعب قراءته","مكتوبة بشكل سيء","لم استطع إيجاد إجابة ذات صلة","توجد مشكلة تقنية"],"datasets":[{"label":"","data":[' + '"' + str(
            d1) + '"' + "," + '"' + str(d2) + '"' + ',' + '"' + str(d3) + '"' + ',' + '"' + str(
            d4) + '"' + ',' + '"' + str(d5) + '"' + '],"backgroundColor":"#1AA684","borderColor":"o-color-1"}]}'

        if len(request.env['rating.page'].sudo().search([])) == 0:
            value5 = '{"labels":["","","","",""],"datasets":[{"label":"","data":[' + '"' + str(
                0) + '"' + "," + '"' + str(0) + '"' + ',' + '"' + str(0) + '"' + ',' + '"' + str(
                0) + '"' + ',' + '"' + str(0) + '"' + '],"backgroundColor":"#1AA684","borderColor":"o-color-1"}]}'
        else:
            RatingPage = request.env['rating.page'].sudo()
            rating_records = RatingPage.search([])

            path_ratings = {}
            for record in rating_records:
                if record.create_date.month == selectedMonth:
                    path = record.page_name
                    rating = record.rating
                    if path in path_ratings:
                        path_ratings[path].append(rating)
                    else:
                        path_ratings[path] = [rating]

            path_averages = {}
            for path, ratings in path_ratings.items():
                average_rating = sum(ratings) / len(ratings)
                path_averages[path] = (average_rating / 5) * 100

            sorted_paths = sorted(path_averages.items(), key=lambda x: x[1], reverse=True)[:5]

            top_path_list = []
            for path, rating_percentage in sorted_paths:
                top_path_list.append((path, rating_percentage))

            while len(top_path_list) < 5:
                top_path_list.append(("", 0))

            path_ratings1 = {}
            for record in rating_records:
                if record.create_date.month == selectedMonth1:
                    path = record.page_name
                    rating = record.rating
                    if path in path_ratings1:
                        path_ratings1[path].append(rating)
                    else:
                        path_ratings1[path] = [rating]

            path_averages1 = {}
            for path, ratings in path_ratings1.items():
                average_rating = sum(ratings) / len(ratings)
                path_averages1[path] = (average_rating / 5) * 100

            sorted_paths1 = sorted(path_averages1.items(), key=lambda x: x[1], reverse=False)[:5]

            top_path_list1 = []
            for path, rating_percentage in sorted_paths1:
                top_path_list1.append((path, rating_percentage))

            while len(top_path_list1) < 5:
                top_path_list1.append(("", 0))

            print('dictionnaire', top_path_list)
            print('dictionnaire', top_path_list)

            value5 = '{"labels":["' + top_path_list[0][0] + '","' + top_path_list[1][0] + '","' + top_path_list[2][
                0] + '","' + top_path_list[3][0] + '","' + top_path_list[4][
                         0] + '"],"datasets":[{"label":"","data":[' + '"' + str(
                top_path_list[0][1]) + '"' + "," + '"' + str(top_path_list[1][1]) + '"' + ',' + '"' + str(
                top_path_list[2][1]) + '"' + ',' + '"' + str(
                top_path_list[3][1]) + '"' + ',' + '"' + str(
                top_path_list[4][1]) + '"' + '],"backgroundColor":"#1AA684","borderColor":"o-color-1"}]}'

            value6 = '{"labels":["' + top_path_list1[0][0] + '","' + top_path_list1[1][0] + '","' + top_path_list1[2][
                0] + '","' + top_path_list1[3][0] + '","' + top_path_list1[4][
                         0] + '"],"datasets":[{"label":"","data":[' + '"' + str(
                top_path_list1[0][1]) + '"' + "," + '"' + str(top_path_list1[1][1]) + '"' + ',' + '"' + str(
                top_path_list1[2][1]) + '"' + ',' + '"' + str(
                top_path_list1[3][1]) + '"' + ',' + '"' + str(
                top_path_list1[4][1]) + '"' + '],"backgroundColor":"#1AA684","borderColor":"o-color-1"}]}'

        return request.render("website_inherit.dash", {

            'value1': value1,
            'value2': value2,
            'value3': value3,
            'value4': value4,
            'value5': value5,
            'value6': value6,
            'selected_month': selectedMonth,
            'latest_months': latest_months,

            'selected_month1': selectedMonth1,
            'latest_months1': latest_months1,
            # 'month_best':calendar.month_name[selectedMonth]

        })

    @http.route('/rating/calculate_length', type='json', auth='public')
    def calculate_length(self, **kw):
        path = kw.get('path')
        print("path test", path)
        # length_cal = len(http.request.env['rating.page'].sudo().search([('path', '=', path)]))
        # print('length_cal',length_cal)
        ratings = http.request.env['rating.page'].sudo().search([('path', '=', path)])

        count = ratings.search_count([('path', '=', path)])

        # Calculate the average rating
        average_rating = 0
        if count:
            total_rating = sum(ratings.mapped('rating'))
            average_rating = int(total_rating / count)
        return average_rating

    @http.route('/rating/calculate_nb_comment', type='json', auth='public')
    def calculate_nb_comment(self, **kw):
        path = kw.get('path')
        print("path test", path)

        ratings = http.request.env['rating.page'].sudo().search([('path', '=', path)])
        nb_cmt = 0
        for r in ratings:
            if r.comment_yes != '' or r.comment_no != 0:
                nb_cmt += 1

        return nb_cmt


class accountInherit(CustomerPortal):
    @http.route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        values.update({
            'error': {},
            'error_message': [],
        })

        if post and request.httprequest.method == 'POST':
            error, error_message = self.details_form_validate(post)
            values.update({'error': error, 'error_message': error_message})
            values.update(post)
            if not error:
                values = {key: post[key] for key in self.MANDATORY_BILLING_FIELDS}
                values.update({key: post[key] for key in self.OPTIONAL_BILLING_FIELDS if key in post})
                for field in set(['country_id', 'state_id']) & set(values.keys()):
                    try:
                        values[field] = int(values[field])
                    except:
                        values[field] = False
                values.update({'zip': values.pop('zipcode', '')})
                partner.sudo().write(values)
                if redirect:
                    return request.redirect(redirect)
                return request.redirect('/my/account')

        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])

        values.update({
            'partner': partner,
            'countries': countries,
            'states': states,
            'has_check_vat': hasattr(request.env['res.partner'], 'check_vat'),
            'redirect': redirect,
            'page_name': 'my_details',
        })

        response = request.render("portal.portal_my_details", values)
        response.headers['X-Frame-Options'] = 'DENY'
        return response
