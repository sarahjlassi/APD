# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import os
import odoo
from odoo import exceptions,Command, http, tools, _, SUPERUSER_ID, api, registry as registry_get
from odoo.addons.web.controllers.main import (
    Home,
    ensure_db,
    login_and_redirect,
    set_cookie_and_redirect,
)
from odoo.http import request

import werkzeug.utils
import requests
import logging
import json
import time
from jose import jwt

_logger = logging.getLogger(__name__)


class AuthSignupHome(Home):

    @http.route('/signin/nafath', type='http', auth='public', website=True, sitemap=False)
    def web_auth_signin_nafath(self, *args, **kw):
        print("*** Sign In With Nafath ***")

        data = {
            'show_id_number': True,
            'show_random_number': False,
        }
        return request.render("ejad_nafath.nafath_login_template", data)

    @http.route('/nafath/sendID', type='http', auth='public', website=True, sitemap=False)
    def nafath_send_id(self, **kw):
        print('** :', kw)
        sp_api_key = request.env['ir.config_parameter'].sudo().get_param('ejad_nafath.sp_api_key', False)
        print('sp_api_key :', sp_api_key)
        nafath_url = request.env['ir.config_parameter'].sudo().get_param('ejad_nafath.nafath_url', False)

        user_info_url = request.env['ir.config_parameter'].sudo().get_param('ejad_nafath.user_info', False)
        if user_info_url:
            url_info = user_info_url+"/identityServices/userInfo"
        else:
            url_info = "https://api.id.gov.sa/identityServices/userInfo"


        if nafath_url:
            url = nafath_url
        else:
            url = "https://www.iam.sa/nafath/"

        headers = {
            'Content-Type': 'application/json',
            'Authorization': sp_api_key
        }
        if kw.get('NAT_ID', False):
            national_id = kw.get('NAT_ID', False)
            payload = json.dumps({
                "Action": "SpRequest",
                "Parameters": {
                    "service": "AdvancedLogin",
                    "id": national_id
                }
            })
            random = ''
            transId = ''
            try:
                response = requests.request("POST", url, headers=headers, data=payload)
                content = response.json()
                print('content : ', content)
                #_logger.error("Content %s" % content)
                transId = content.get('transId', False)
                random = content.get('random', False)
            except:
                #_logger.error("Error during the request %s" % e)
                print('1st Step ..')
                pass
            print('transId : ', transId)
            print('random : ', random)
            if transId and random:
                registry = registry_get(request.session.db)
                with registry.cursor() as cr:
                    env = api.Environment(cr, SUPERUSER_ID, {})
                    ## for old user who already has login
                    if kw.get('old_user_id', False):
                        user = env["res.users"].search([('id', '=', kw['old_user_id'])])
                        user.write({'national_id': national_id})
                    else:
                        user = env["res.users"].search([('national_id', '=', national_id)])
                        print('User : ', user)

                    if user:
                        print('User Found: Login OK')
                        user.write({'nafath_secret': transId, 'nafath_callback_success': False})
                    else:
                        print('User Not Found: Create One')
                        SudoUser = env['res.users'].sudo().with_context(no_reset_password=True)
                        grp_internal = env.ref('base.group_user')
                        grp_portal = env.ref('base.group_portal')
                        grp_public = env.ref('base.group_public')

                        user_data = {
                            'name': national_id,
                            'national_id': national_id,
                            'login': national_id,
                            'nafath_secret': transId,
                            'nafath_callback_success': False,
                            'nafath_enabled': False,
                            'active': True,
                            'sel_groups_%s_%s_%s' % (grp_internal.id, grp_portal.id, grp_public.id): grp_portal.id,
                        }
                        new_user = SudoUser.create(user_data)
                        print('New User : ', new_user, ' login: ', new_user.login)
                data = {
                    'show_id_number': False,
                    'show_random_number': True,
                    'nationalId': national_id,
                    'random': random,
                    'transId': transId,
                    'redirect_url':kw.get('redirect_url', False)
                }
                return request.render("ejad_nafath.nafath_login_template", data)
            else:
                url = "/web/login"
                redirect = werkzeug.utils.redirect(url, 303)
                redirect.autocorrect_location_header = False
                return redirect
        if kw.get('random', False) and kw.get('transId', False):
            national_id = kw.get('nationalId', False)
            transId = kw.get('transId', False)
            random_number = kw.get('random', False)

            payload = json.dumps({
                "Action": "CheckSpRequest",
                "Parameters": {
                    "transId": transId,
                    "id": national_id,
                    "random": random_number
                }
            })

            dbname = request.session.db
            count = 1
            status = 'REJECTED'
            accessToken=''
            arFullName = ''
            while count < 60:
                try:
                    response2 = requests.request("POST", url, headers=headers, data=payload)
                    content2 = response2.json()
                    print('content2 : ', content2)
                    status = content2.get('status', False)
                    person = content2.get('person', False)
                    accessToken = content2.get('accessToken', False)
                    #_logger.info("accessToken %s" % accessToken)
                    arFullName = person['arFullName']
                except:
                    print('2nd Step ..')
                    pass
                print("**** status : ", status)
                print("**** : ", count)
                time.sleep(1)
                count += 1
                if status == 'COMPLETED' and accessToken!=False:

                    headers_info = {
                        'Content-Type': 'application/json',
                        'Authorization': "Bearer " + accessToken
                    }
                    _logger.info(100*"++")
                    _logger.info(os.getcwd())
                    try:
                        response = requests.request("GET", url_info, headers=headers_info)
                        _logger.info("response %s" % response)
                        jwt_token = response.text
                        _logger.info("jwt_token %s" % jwt_token)

                        # Decode the JWT token
                        try:
                            #decoded_token = jwt.decode(jwt_token, 'secret', algorithms=['RS256'])
                            decoded_token=jwt.get_unverified_claims(jwt_token)
                            _logger.info("decoded_token %s" % decoded_token)
                        except Exception as e:
                            # Handle decoding error
                            _logger.error("error during jwt decoding %s" % e)
                            decoded_token = None
                        payload_jwt = ""
                        if decoded_token:
                            # Access the payload data
                            payload_jwt = decoded_token

                        registry = registry_get(request.session.db)

                        with registry.cursor() as cr:
                            try:
                                env = api.Environment(cr, SUPERUSER_ID, {})
                                user = env["res.users"].search([('nafath_secret', '=', transId)])
                                _logger.info("user exists",user.name)
                                if user:
                                    if user:
                                        _logger.info("start writing user info", payload_jwt.get('user_info', False).get('full_name#ar',False))
                                        user.write({
                                        'name': payload_jwt.get('user_info', False).get('full_name#ar', False),
                                        'nafath_enabled': True
                                        })
                                        _logger.info("user was written we are going to update the partner")
                                        user.partner_id.sudo().write({
                                            'name': payload_jwt.get('user_info', False).get('full_name#ar', False),
                                            'gender':payload_jwt.get('user_info', False).get('gender', False),
                                            'id_issue_date': payload_jwt.get('user_info', False).get('id_issue_date#g', False),
                                            'id_expiry_date': payload_jwt.get('user_info', False).get('id_expiry_date#g', False),
                                            'nationality': payload_jwt.get('user_info', False).get('nationality', False),
                                            'language': payload_jwt.get('user_info', False).get('language', False),
                                            'nationality_country': payload_jwt.get('user_info', False).get('nationality#en', False),
                                            'dob': payload_jwt.get('user_info', False).get('dob#g', False),
                                            'card_issue_place': payload_jwt.get('user_info', False).get('card_issue_place#en', False),

                                        })
                                        env.cr.commit()

                                    if user.login == user.national_id:
                                        url = "/update_user_info"
                                    else:
                                        if kw.get('redirect_url', False):
                                            url = kw.get('redirect_url', False)
                                        else:
                                            url = "/web"

                                    return login_and_redirect(dbname, user.login, transId, redirect_url=url)
                            except odoo.exceptions.AccessDenied:
                                url = "/web/login"
                                redirect = werkzeug.utils.redirect(url, 303)
                                redirect.autocorrect_location_header = False
                                return redirect
                        return set_cookie_and_redirect(url)

                    except requests.exceptions.ConnectionError as e:
                        _logger.error("Error during the request %s" % e)






                if status in ['EXPIRED', 'REJECTED']:
                    url = "/web/login"
                    redirect = werkzeug.utils.redirect(url, 303)
                    redirect.autocorrect_location_header = False
                    return redirect

        if kw.get('random', False) and kw.get('transId', False):
            national_id = kw.get('nationalId', False)
            transId = kw.get('transId', False)
            random_number = kw.get('random', False)

            dbname = request.session.db
            count = 1
            status = 'REJECTED'
            arFullName = ''
            while count < 60:
                print("**** status : ", status)
                print("**** : ", count)
                time.sleep(1)
                count += 1

                registry = registry_get(request.session.db)

                with registry.cursor() as cr:
                    try:
                        env = api.Environment(cr, SUPERUSER_ID, {})
                        user = env["res.users"].search([('nafath_secret', '=', transId)])
                        if user and user.nafath_callback_success:

                            if user.login == user.national_id:
                                url = "/update_user_info"
                            else:
                                if kw.get('redirect_url', False):
                                    url = kw.get('redirect_url', False)
                                else:
                                    url = "/web"

                            return login_and_redirect(dbname, user.login, transId, redirect_url=url)
                    except odoo.exceptions.AccessDenied:
                        url = "/web/login"
                        redirect = werkzeug.utils.redirect(url, 303)
                        redirect.autocorrect_location_header = False
                        return redirect

            url = "/web/login"
            redirect = werkzeug.utils.redirect(url, 303)
            redirect.autocorrect_location_header = False
            return redirect

    # @http.route('/nafath/callback', type='json', auth='public', website=True, sitemap=False)
    # def nafath_callback(self, **kw):
    #
    #     _logger.info("Hello nafath_callback******")
    #     user_info_url = request.env['ir.config_parameter'].sudo().get_param('ejad_nafath.user_info', False)
    #     if user_info_url:
    #         url = user_info_url+"/identityServices/userInfo"
    #     else:
    #         url = "https://api.id.gov.sa/identityServices/userInfo"
    #     all_data = json.loads(http.request.httprequest.data.decode('utf-8'))
    #     # all_data = kw
    #     _logger.info("REQUEST_DATA******")
    #     print("all_data ==", all_data)
    #     print("kw ==", kw)
    #     if 'response' in all_data:
    #         _logger.info("REQUEST_DATA Has response")
    #         response_encoded_data = all_data['response']
    #     else:
    #         _logger.info("REQUEST_DATA Has NOOO response")
    #         return {'result': 'no response'}
    #
    #     final_data = jwt.get_unverified_claims(response_encoded_data)
    #
    #     if 'status' in final_data and final_data.get('status') == 'COMPLETED' and final_data.get('transId', False):
    #         _logger.info("nafath Entered If Condition")
    #         access_token=final_data.get('accessToken')
    #         headers = {
    #             'Content-Type': 'application/json',
    #             'Authorization': "Bearer " + access_token
    #         }
    #
    #         try :
    #             response = requests.request("GET", url, headers=headers)
    #             jwt_token = response.text
    #
    #             # Decode the JWT token
    #             try:
    #                 decoded_token = jwt.decode(jwt_token, 'secret',algorithms=['RS256'])
    #             except Exception as e:
    #                 # Handle decoding error
    #                 print("JWT decoding error",e)
    #                 decoded_token = None
    #             payload=""
    #             if decoded_token:
    #                 # Access the payload data
    #                 payload = decoded_token
    #
    #             registry = registry_get(request.session.db)
    #
    #             with registry.cursor() as cr:
    #                 try:
    #                     env = api.Environment(cr, SUPERUSER_ID, {})
    #                     user = env["res.users"].search([('nafath_secret', '=', final_data.get('transId'))])
    #                     if user:
    #                         if not user.nafath_enabled:
    #                             user.write({
    #                                 'name': payload.get('full_name#ar', False),
    #                                 'nafath_enabled': True,
    #                                 'nafath_callback_success': True
    #                             })
    #                         else:
    #                             user.write({
    #                                 'nafath_callback_success': True
    #                             })
    #
    #                         env.cr.commit()
    #                         print("nafath Successfully")
    #                         _logger.info("nafath Successfully")
    #                         return {'result': True}
    #                     else:
    #                         print("nafath Failed")
    #                         _logger.info("nafath Failed No user found")
    #                         return {'result': "No user found"}
    #                 except:
    #                     _logger.info("nafath FAILED")
    #                     return {'result': False}
    #         except requests.exceptions.ConnectionError  as e:
    #             _logger.error("Error during the request %s" % e)
    #
    #
    #
    #     else:
    #         _logger.info("nafath NOT Entered If Condition")
    #         return {'result': "No Status or no transId or status not completed"}



    @http.route('/nafath/callback', type='json', auth='public', website=True, sitemap=False)
    def nafath_callback(self, **kw):
        _logger.info("Hello nafath_callback******")
        all_data = json.loads(http.request.httprequest.data.decode('utf-8'))
        # all_data = kw
        _logger.info("REQUEST_DATA******")
        print("all_data ==", all_data)
        print("kw ==", kw)
        if 'response' in all_data:
            _logger.info("REQUEST_DATA Has response")
            response_encoded_data = all_data['response']
        else:
            _logger.info("REQUEST_DATA Has NOOO response")
            return {'result': 'no response'}

        final_data = jwt.get_unverified_claims(response_encoded_data)

        if 'status' in final_data and final_data.get('status') == 'COMPLETED' and final_data.get('transId', False):
            _logger.info("nafath Entered If Condition")
            registry = registry_get(request.session.db)

            with registry.cursor() as cr:
                try:
                    env = api.Environment(cr, SUPERUSER_ID, {})
                    user = env["res.users"].search([('nafath_secret', '=', final_data.get('transId'))])
                    if user:
                        if not user.nafath_enabled:
                            user.write({
                                'name': final_data.get('person', False).get('ArFullName', False),
                                'nafath_enabled': True,
                                'nafath_callback_success': True
                            })
                        else:
                            user.write({
                                'nafath_callback_success': True
                            })

                        env.cr.commit()
                        print("nafath Successfully")
                        _logger.info("nafath Successfully")
                        return {'result': True}
                    else:
                        print("nafath Failed")
                        _logger.info("nafath Failed No user found")
                        return {'result': "No user found"}
                except:
                    _logger.info("nafath FAILED")
                    return {'result': False}
        else:
            _logger.info("nafath NOT Entered If Condition")
            return {'result': "No Status or no transId or status not completed"}
