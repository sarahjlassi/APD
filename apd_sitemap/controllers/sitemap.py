from odoo import http
from odoo.http import request

class custom_website_Sitemap(http.Controller):

    @http.route(['/sitemap'], type='http', auth="public", website=True)
    def sitemap_page(self, **kwargs):
        if  request.env.user.id == request.env.ref('base.public_user').id or request.env.user.has_group('base.group_portal') :
            return request.render("apd_sitemap.sitemap_page_tempalte_for_public_and_not_login_user", {})
        else:
            return request.render("apd_sitemap.sitemap_page_tempalte", {})

