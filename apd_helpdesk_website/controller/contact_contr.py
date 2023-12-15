from odoo import http
from odoo.http import request
import base64


class custom_website_helpdesk(http.Controller):

    @http.route(['/contactus/helpdesk/new'], type='http', auth="public", website=True)
    def contact_us_team_first_page(self, team=None, **kwargs):
        if request.env.user.id == request.env.ref('base.public_user').id:

            return request.render("ejad_nafath.nafath_login_template",{'redirect_url':request.httprequest.url,'show_id_number':True})
            # return request.redirect('/signin/nafath')
        return request.render("apd_helpdesk_website.contactus_first_page", {})

    # pass values of ticket_type ans sub_ticket_type from tickettype (1st) form to helpdesk_ticket_form (2nd)
    @http.route(['/contactus/helpdesk'], type='http', auth="user", website=True)
    def contact_us_team(self, team=None, **kwargs):

        default_values = {}
        submited_ticket_type = ''
        lst_of_ticket_types = ['sugg','inquiry','requ_open_data']
        if any((match := item) == kwargs.get('ticket_type') for item in lst_of_ticket_types):
            submited_ticket_type =match

        # team = http.request.env['helpdesk.team'].sudo().search(
        #     [('id', '=', request.env.ref('helpdesk.helpdesk_team1').id)], limit=1)
        # ticket_types = request.env['helpdesk.ticket.type'].sudo().search([('helpdesk_team_id', '=', team.id)])
        log_in_user = request.env.user
        related_partner_to_login_user = log_in_user.partner_id
        partner_data = {
            'name': related_partner_to_login_user.name,
            'n_id':related_partner_to_login_user.id_number,
            'phone':related_partner_to_login_user.phone,
        }

        default_country = request.env.company.country_id
        states = request.env['res.country.state'].sudo().search(
            [('country_id', '=', int(default_country.id))])

        team = None
        ticket_types = request.env['helpdesk.ticket.type'].sudo().search([])
        default_values.update({'ticket_types': ticket_types})

        return request.render("apd_helpdesk_website.contactus", {'team': team, 'default_values': default_values,
                                                             'partner_data':partner_data,
                                                             'states':states,
                                                             'ticket_type':submited_ticket_type,})


    @http.route(['/contactus_type/submit'], type='http', methods=['POST'], auth="user", website=True)
    def contactus_submit(self, **kwargs):
        #Create New Ticket with the data from website and update record with attachment
        new_ticket = request.env['helpdesk.ticket'].sudo().create({
            'ticket_type_custom':kwargs.get('ticket_type',False),
            'team_id':request.env['helpdesk.team'].sudo().search([('ticket_type_custom','=',kwargs.get('ticket_type'))],limit=1).id or 1,
            'name':kwargs.get('subject') or 'No Subject',
            'n_id':kwargs.get('n_id',False) ,
            'partner_id':request.env.user.partner_id.id or False,
            'partner_name':request.env.user.partner_id.name or False,
            'partner_email':request.env.user.partner_id.email or False,
            'partner_phone':kwargs.get('phone',False) ,
            'state_id': request.env['res.country.state'].browse(kwargs.get('state_id')).id or False,
            'description':kwargs.get('descrip',False),
            'disability_person':kwargs.get('disability',False),
            'beneficiary':kwargs.get('beneficiary',False) ,
        })

        if kwargs.get('attachments', False):
            Attachment = request.env['ir.attachment']
            file_name = kwargs.get('attachments').filename
            file = kwargs.get('attachments')
            attachment_id = Attachment.sudo().create({
                'name': file_name,
                'type': 'binary',
                'datas': base64.b64encode(file.read()),
                'res_model': 'helpdesk.ticket',
                'res_id': new_ticket.id
            })
            request.env['helpdesk.ticket'].search([('id','=',new_ticket.id)]).sudo().update({
                'attach_ids': [(4, attachment_id.id)],
            })

        return request.render("apd_helpdesk_website.ticket_success_page", {
            'new_ticket':new_ticket
        })