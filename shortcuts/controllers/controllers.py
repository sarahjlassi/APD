# -*- coding: utf-8 -*-
# from odoo import http


# class Shortcuts(http.Controller):
#     @http.route('/shortcuts/shortcuts', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shortcuts/shortcuts/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('shortcuts.listing', {
#             'root': '/shortcuts/shortcuts',
#             'objects': http.request.env['shortcuts.shortcuts'].search([]),
#         })

#     @http.route('/shortcuts/shortcuts/objects/<model("shortcuts.shortcuts"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shortcuts.object', {
#             'object': obj
#         })
