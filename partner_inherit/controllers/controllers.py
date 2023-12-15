# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerInherit(http.Controller):
#     @http.route('/partner_inherit/partner_inherit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_inherit/partner_inherit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_inherit.listing', {
#             'root': '/partner_inherit/partner_inherit',
#             'objects': http.request.env['partner_inherit.partner_inherit'].search([]),
#         })

#     @http.route('/partner_inherit/partner_inherit/objects/<model("partner_inherit.partner_inherit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_inherit.object', {
#             'object': obj
#         })
