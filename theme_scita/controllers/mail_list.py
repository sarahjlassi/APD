from odoo import http,_
from odoo.http import request


class custom_website_add_to_mail_list(http.Controller):

    #subscribe and create for logged in user in mail list
    @http.route(['/subscrube/m_list'], type='http',methods=['POST'], auth="user",csrf=False, website=True)
    def subscribe_in_mail_list_confirm(self,**kwargs):

        current_user= request.env.user
        exist_email = request.env['mailing.contact'].sudo().search([('email', '=',current_user.partner_id.email)])
        if not exist_email :
            data_for_current_user = {
                'name': current_user.partner_id.name,
                'email': current_user.partner_id.email,
                'company_name': current_user.partner_id.company_id.name,
                'country_id': current_user.partner_id.country_id.id,
            }
            # create in maillist
            mail_list = request.env['mailing.contact'].sudo().create(data_for_current_user)
