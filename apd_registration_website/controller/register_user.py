

import logging
from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request
from odoo.exceptions import UserError
import werkzeug
from odoo.addons.auth_signup.models.res_users import SignupError

from odoo.addons.portal.controllers.portal import CustomerPortal as CustomerPortal




_logger = logging.getLogger(__name__)


class ExtAuthSignupHome(AuthSignupHome):
    def get_auth_signup_qcontext(self):
        """ Shared helper returning the rendering context for signup and reset password """
        qcontext = {k: v for (k, v) in request.params.items()
                    if k in {'db', 'login', 'debug', 'token', 'message', 'error', 'scope', 'mode',
                          'redirect', 'redirect_hostname', 'email', 'name', 'partner_id',
                          'password', 'confirm_password', 'city', 'country_id', 'lang','id_number','phone'}
                    }
        default_country = request.env['ir.config_parameter'].sudo().get_param(
            'ejad_eservices_m_features.registeration_default_country_id')
        if not default_country:
            default_country = request.env.company.country_id

        qcontext['states'] = request.env['res.country.state'].sudo().search(
            [('country_id', '=', int(default_country.id))])

        qcontext.update(self.get_auth_signup_config())
        if not qcontext.get('token') and request.session.get('auth_signup_token'):
            qcontext['token'] = request.session.get('auth_signup_token')
        if qcontext.get('token'):
            try:
                # retrieve the user info (name, login or email) corresponding to a signup token
                token_infos = request.env['res.partner'].sudo().signup_retrieve_info(qcontext.get('token'))
                for k, v in token_infos.items():
                    qcontext.setdefault(k, v)

            except:
                qcontext['error'] = _("Invalid signup token")
                qcontext['invalid_token'] = True
        return qcontext

    def _prepare_signup_values(self, qcontext):
        #passing new inputs in sending context to signup
        values = { key: qcontext.get(key) for key in ('login', 'name', 'password','id_number','phone') }
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
        lang = request.context.get('lang', '')
        if lang in supported_lang_codes:
            values['lang'] = lang
        return values

    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = {key: qcontext.get(key) for key in ('login', 'name', 'password','id_number','phone')}
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
        lang = request.context.get('lang', '').split('_')[0]
        if lang in supported_lang_codes:
            values['lang'] = lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()


class InheritedCustomerPortal(CustomerPortal):
    """Updated the Optional fields list to stop the unkown fields error."""

    OPTIONAL_BILLING_FIELDS = ["zipcode", "state_id", "vat", "company_name","street", "city", "country_id","id_number"]
    MANDATORY_BILLING_FIELDS = ["name", "phone", "email", ]







