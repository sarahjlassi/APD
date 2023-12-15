# -*- coding: utf-8 -*-
# from odoo import http


# class -TestApd(http.Controller):
#     @http.route('/test_apd/test_apd', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/test_apd/test_apd/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('test_apd.listing', {
#             'root': '/test_apd/test_apd',
#             'objects': http.request.env['test_apd.test_apd'].search([]),
#         })

#     @http.route('/test_apd/test_apd/objects/<model("test_apd.test_apd"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('test_apd.object', {
#             'object': obj
#         })
