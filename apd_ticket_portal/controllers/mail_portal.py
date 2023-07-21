from odoo.addons.portal.controllers.mail import PortalChatter

from odoo import http, _
from odoo.http import request
from werkzeug.exceptions import Forbidden
from odoo.tools import consteq

from odoo.osv import expression



def _check_special_access(res_model, res_id, token='', _hash='', pid=False):
    record = request.env[res_model].browse(res_id).sudo()
    if _hash and pid:  # Signed Token Case: hash implies token is signed by partner pid
        return consteq(_hash, record._sign_token(pid))
    elif token:  # Token Case: token is the global one of the document
        token_field = request.env[res_model]._mail_post_token_field
        return (token and record and consteq(record[token_field], token))
    else:
        raise Forbidden()




class ExtAuthSignupHome(PortalChatter):


    @http.route('/mail/chatter_init', type='json', auth='public', website=True)
    def portal_chatter_init(self, res_model, res_id, domain=False, limit=False, **kwargs):
        is_user_public = request.env.user.has_group('base.group_public')
        message_data = self.portal_message_fetch(res_model, res_id, domain=domain, limit=limit, **kwargs)
        display_composer = False
        if kwargs.get('allow_composer'):
            display_composer = kwargs.get('token') or not is_user_public

        for msg in message_data['messages']:
           msg['is_internal_user'] = request.env['res.partner'].sudo().browse(msg['author_id'][0]).user_ids.has_group('base.group_user')


        return {
            'messages': message_data['messages'],
            'options': {
                'message_count': message_data['message_count'],
                'parameter_name': request.env['ir.config_parameter'].sudo().search([('key','=','helpdesk_portal.name_of_chatter_for_internal')],limit=1).value or 'APD',
                'is_user_public': is_user_public,
                'is_user_employee': request.env.user.has_group('base.group_user'),
                'is_user_publisher': request.env.user.has_group('website.group_website_publisher'),
                'display_composer': display_composer,
                'partner_id': request.env.user.partner_id.id
            }
        }

    @http.route('/mail/chatter_fetch', type='json', auth='public', website=True)
    def portal_message_fetch(self, res_model, res_id, domain=False, limit=10, offset=0, **kw):
        if not domain:
            domain = []
        # Only search into website_message_ids, so apply the same domain to perform only one search
        # extract domain from the 'website_message_ids' field
        model = request.env[res_model]
        field = model._fields['website_message_ids']
        field_domain = field.get_domain_list(model)
        domain = expression.AND([
            domain,
            field_domain,
            [('res_id', '=', res_id), '|', ('body', '!=', ''), ('attachment_ids', '!=', False)]
        ])

        # Check access
        Message = request.env['mail.message']
        if kw.get('token'):
            access_as_sudo = _check_special_access(res_model, res_id, token=kw.get('token'))
            if not access_as_sudo:  # if token is not correct, raise Forbidden
                raise Forbidden()
            # Non-employee see only messages with not internal subtype (aka, no internal logs)
            if not request.env['res.users'].has_group('base.group_user'):
                domain = expression.AND([Message._get_search_domain_share(), domain])
            Message = request.env['mail.message'].sudo()

        fetch_messages = Message.search(domain, limit=limit, offset=offset).portal_message_format()

        for msg in fetch_messages:
           msg['is_internal_user'] = request.env['res.partner'].sudo().browse(msg['author_id'][0]).user_ids.has_group('base.group_user')


        return {
            'messages': fetch_messages,
            'message_count': Message.search_count(domain)
        }

