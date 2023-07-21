from odoo.addons.website_hr_recruitment.controllers.main import WebsiteHrRecruitment
from odoo import http
from odoo.http import request
import werkzeug
import base64

class Custom_Rcruit(WebsiteHrRecruitment):
    @http.route('''/jobs/apply/<model("hr.job"):job>''', type='http', auth="public", website=True, sitemap=True)
    def jobs_apply(self, job, **kwargs):
        if request.env.user.id == request.env.ref('base.public_user').id:
            return request.render("ejad_nafath.nafath_login_template",
                                  {'redirect_url': request.httprequest.url, 'show_id_number': True})
            # return request.redirect('/signin/nafath')
        default_country = request.env.company.country_id
        states = request.env['res.country.state'].sudo().search(
            [('country_id', '=', int(default_country.id))])

        disability_types = request.env['d.type'].sudo().search([])
        degrees = request.env['degree.degree'].sudo().search([])



        error = {}
        default = {}
        if 'website_hr_recruitment_error' in request.session:
            error = request.session.pop('website_hr_recruitment_error')
            default = request.session.pop('website_hr_recruitment_default')
        return request.render("website_hr_recruitment.apply", {
            'partner': request.env.user.partner_id,
            'job': job,
            'error': error,
            'default': default,
            'states': states,
            'disability_types': disability_types,
            'degrees': degrees,
        })

    @http.route(['/is_collage_degree'], type='json', auth="public", methods=['POST'], website=True)
    def is_collage_degree_func(self, degree_id_c, **kw):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^", degree_id_c)
        if degree_id_c:
            collage_orhigher_degree = http.request.env['degree.degree'].sudo().search(
                [('id', '=', int(degree_id_c))])
            if collage_orhigher_degree and collage_orhigher_degree.is_collage_degree_or_higher :
                print("Collage Or Higher TRUE")
                return True
            else:
                print("Not Collage Or Higher")
                return False

        return False


    @http.route(['/jobs/application/submit'], type="http", auth='user', methods=['POST'], website=True)
    def application_submit(self, **kw):
        application = request.env['hr.applicant'].sudo().create({
            'job_id': kw.get('job_id', False),
            'name': kw.get('partner_name', False),
            'birthday_c': kw.get('birthday_c', False),
            'gender_custom': kw.get('gender_custom', False),
            'nationality_c': kw.get('nationality_c', False),
            'state_id': kw.get('state_id', False),
            'p_with_d': kw.get('p_with_d', False),
            'dis_id': kw.get('dis_id', False),
            'accom': kw.get('accom', False),
            'description': kw.get('description', False),
            'department_id': kw.get('department_id', False),
            'degree_id_c': kw.get('degree_id_c', False),
            'special_c': kw.get('special_c', False),
            'gpa': kw.get('gpa', False),
            'grade_degree': kw.get('grade_degree', False),
            'experience': kw.get('experience', False),
            'employer': kw.get('employer', False),
            'job_title_custom': kw.get('job_title_custom', False),
            'ex_years': kw.get('ex_years', False),
            'email_from': kw.get('email_from', False),
            'partner_phone': kw.get('partner_phone', False),
            'linkedin_pro': kw.get('linkedin_pro', False),
            'accept_terms': kw.get('accept_terms', False) == 'yes',
        })
    
        file_name = kw.get('resume').filename
        file = kw.get('resume')
        attachment_id = request.env['ir.attachment'].sudo().create({
        'name': file_name,
        'type': 'binary',
        'datas': base64.b64encode(file.read()),
        'res_model': application._name,
        'res_id': application.id
        })

        application.update({
            'resume': [(4, attachment_id.id)],
        })

        # return request.render("website_hr_recruitment.thankyou", {})
        return request.render("apd_recruitment.job_application_feedback", {})
    

    
    @http.route(['/my/job-applications'], type="http", auth='user', website=True)
    def view_job_applications(self, **kw):
        #TODO: link jobs with contact id rather than name
        user = request.env.user
        jobs = request.env['hr.applicant'].sudo().search([('name','=',user.partner_id.name)])
        return request.render("apd_recruitment.job_application_view", {'jobs': jobs})
    