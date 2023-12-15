# -*- coding: utf-8 -*-
from odoo import http, models, fields, _
from odoo.http import request
from odoo.addons.website.controllers.main import Website
from odoo.addons.portal.controllers.portal import pager as portal_pager

class advanced_search(Website):
    @http.route([
        '/website/search',
        '/website/search/page/<int:page>',
        '/website/search/<string:search_type>',
        '/website/search/<string:search_type>/page/<int:page>',
    ], type='http', auth="public", website=True, sitemap=False)
    def hybrid_list(self, page=1, search='', ordre='',ordred='', type='', search_type='all', search_ad='',date_begin='', date_end='',
                    siteweb=True, **kw):
        print('site web', siteweb)
        if not search:
            values = {'siteweb': siteweb }
            return request.render("website.list_hybrid", values)

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

        if search_ad=='':
            search_ad=search


            data = self.autocomplete(search_type=type, term=search, order='name ' + ordre, limit=500, max_nb_chars=200,
                                 options=options)
        else:

            data = self.autocomplete(search_type=type, term=search_ad, order='name ' + ordred, limit=500, max_nb_chars=200,
                                     options=options)

            search=search_ad
            ordre=ordred


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
            'search_ad':search_ad,
            'ordred':ordred

        }
        return request.render("website.list_hybrid", values)
