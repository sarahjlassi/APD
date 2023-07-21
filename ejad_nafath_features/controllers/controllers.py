# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.web.controllers.main import Home as Homeweb
from odoo.http import request
from odoo.addons.web.controllers.main import (
    Home,
    ensure_db,
    login_and_redirect,
    set_cookie_and_redirect,
)


class HomeWeb(Homeweb):

    @http.route()
    def web_login(self, redirect=None, *args, **kw):
        print("kw : ",kw )
        print("args : ", args)
        login = kw.get('login', False)
        user = None
        if login:
            user = request.env['res.users'].sudo().search([('login', '=', login)])
        if user and user.partner_id.company_type == 'person' and user.has_group('base.group_portal'):
            data = {
                'show_id_number': True,
                'show_random_number': False,
                'old_user_id': user.id,
            }
            return request.render("ejad_nafath.nafath_login_template", data)
            # return request.redirect('/signin/nafath')
        else:
            res = super(HomeWeb, self).web_login(redirect=redirect, *args, **kw)
            return res
        # otp_signin_auth = request.env['ir.default'].sudo().get('res.config.settings', 'signin_auth')
        # if request.params['login_success'] and otp_signin_auth and request.env.user.mobile and not request.session.get(
        #         'otp_auth_success', False):
        #     return request.redirect('/web/login/totp')
        # print("LOGIN HERE ########")
        # if request.session.uid:
        #     user = request.env['res.users'].browse(request.session.uid)
        #     print("login_user ==", user)
        #     if user and user.partner_id.company_type == 'person':
        #         request.session.logout(keep_db=True)
        #         data = {
        #             'show_id_number': True,
        #             'show_random_number': False,
        #         }
        #         request.redirect('/signin/nafath')
        #         request.csrf_token()
        #         return request.render("ejad_nafath.nafath_login_template", data)
        #
        #
        #

    @http.route('/update_user_info', type='http', auth='public', website=True, sitemap=False)
    def update_user_info(self, **kw):
        # print("*** Update User Info ***")
        user = request.env['res.users'].search([('id', '=', request.session.uid)])
        data = {
            'nafath_user_id': request.session.uid,
            'user_email': user.email,
            'user_mobile': user.mobile,
        }
        # print("DATA ==", data)
        return request.render("ejad_nafath_features.nafath_update_user_info", data)

    @http.route('/nafath_save_user_info', type='http', auth='public', website=True, sitemap=False)
    def save_user_info(self, **kw):
        # print("*** SAVING User Info ***")
        # print("$$$$ ==", kw)
        user_id = kw.get('user_id', False)
        if user_id:
            user = request.env['res.users'].search([('id', '=', user_id)])
            transId = user.nafath_secret
            user.partner_id.sudo().write({'email': kw.get('user_email', False),
                                          'mobile': kw.get('user_mobile', False),
                                          'phone': kw.get('user_mobile', False),
                                          'id_number': user.national_id})
            user.sudo().write({'login': kw.get('user_email', False)})
            request.env.cr.commit()
            # return request.redirect('/web')
            dbname = request.session.db
            return login_and_redirect(dbname, kw.get('user_email', False), transId, redirect_url='/web')
