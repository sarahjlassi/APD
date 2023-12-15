# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class TestApd(http.Controller):
    @http.route(['/purple-saturday-2023'], type='http', auth="public", website=True)
    def card_data(self, all_cards=True, special_cards=False, clicks_cards=False, discount_cards=False, **kwargs, ):
        categories_data = request.env['shop.category'].sudo().search([])
        city_cards = request.env['shop.card'].sudo().search([])
        cities = city_cards.mapped('city')
        cities = list(set(cities))
        record_ids = request.env['shop.card'].search([], order='clicks DESC')
        discount_records = request.env['shop.card'].search([], order='discount DESC')
        env = request.env(context=dict(request.env.context, show_address=True, no_tag_br=True))
        shop_cards = env['shop.card'].sudo()

        search_string = ''
        search_name = ''
        search_city = ''
        search_discount_type = ''

        if kwargs.get('search'):
            search_string = kwargs.get('search', None)
        print('search', search_string)
        if kwargs.get('search_name'):
            search_name = kwargs.get('search_name', None)
        print('search_name', search_name)

        if kwargs.get('search_city'):
            search_city = kwargs.get('search_city', None)

        if kwargs.get('search_discount_type'):
            search_discount_type = kwargs.get('search_discount_type', None)

        domain = ['|', '|', '|',
                  ('name', 'ilike', search_string), ('discount', 'ilike', search_string),
                  ("discount_types", 'ilike', search_string), ('website', 'ilike', search_string),
                  ]

        if search_name:
            domain += [('category', 'ilike', search_name)]
        if search_city:
            domain += [('city', 'ilike', search_city)]
        if search_discount_type:
            domain += [('discount_type', 'ilike', search_discount_type)]
        cards_ids = shop_cards.sudo().search(domain).ids
        cards = shop_cards.sudo().browse(cards_ids)

        if special_cards == 'True':
            all_cards = False
        if clicks_cards == 'True':
            all_cards = False
            special_cards = False
        if discount_cards == 'True':
            all_cards = False
            special_cards = False
            clicks_cards = False

        values = {
            'records': cards,
            'all_cards': bool(all_cards),
            'special_cards': bool(special_cards),
            'clicks_cards': bool(clicks_cards),
            'discount_cards': bool(discount_cards),
            'categories': categories_data,
            'cities': cities,
            'search_name': search_name,
            'search_city': search_city,
            'clicks_records': record_ids,
            'discount_records': discount_records,

        }

        return request.render("test_apd.tmp_cards_data", values)

    @http.route(['/ps-registration'], type='http', methods=['POST', 'GET'], auth="public", website=True)
    def registration(self,  **kwargs, ):
        categories_data = request.env['shop.category'].sudo().search([])

        if request.httprequest.method == 'POST':
            # request.env['registration.quiz'].create({"shop_name": kwargs.get("name"),
            #                                          "shop_type": kwargs.get("type"),
            #                                          "description": kwargs.get("descritpion"),
            #                                          "shop_code": kwargs.get("number"),
            #                                          "shop_link": kwargs.get("website"),
            #                                          "shop_representer": kwargs.get("representer"),
            #                                          "shop_number": kwargs.get("phone"),
            #                                          "shop_email": kwargs.get("mail"),
            #                                          "branches_number": kwargs.get("details"),
            #                                          "city": kwargs.get("city"),
            #                                          "shop_logo": kwargs.get("upload"),
            #                                          "discount": kwargs.get("discount"),
            #                                          "discount_type": kwargs.get("discountType"),
            #                                          "category_ids": int(kwargs.get("selected_category")),
            #
            #                                          })
            print("kawaargs....", kwargs)

        values = {
            'categories': categories_data,


        }
        return request.render("test_apd.tmp_registration", values)
