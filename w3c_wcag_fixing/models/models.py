# -*- coding: utf-8 -*-



from odoo import models, fields, api
from odoo.addons.base.models.assetsbundle import AssetsBundle
class FixdeferBug(AssetsBundle):

    def to_node(self, css=True, js=True, debug=False, async_load=False, defer_load=False, lazy_load=False):
        #print('heritage')
        response = super(FixdeferBug, self).to_node(css, js, debug, async_load, defer_load, lazy_load)

        # Modify the response list to change the attribute name from "data-src" to "src"
        for index, (tag_name, attributes, content) in enumerate(response):
            if tag_name == "script" and attributes.get("data-src"):
                attributes["src"] = attributes.pop("data-src")
        #print('response',response)

        return response


class Fixbug(models.AbstractModel):
    """ QWeb object for rendering stuff in the website context """

    _inherit = 'ir.qweb'



    def get_asset_bundle(self, xmlid, files, env=None, css=True, js=True):
        return FixdeferBug(xmlid, files, env=env)
