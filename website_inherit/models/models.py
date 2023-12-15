# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.base.models.assetsbundle import AssetsBundle
from odoo.addons.base.models.assetsbundle import JavascriptAsset
from odoo.addons.base.models.assetsbundle import StylesheetAsset

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


class testfinal(models.AbstractModel):
    """ QWeb object for rendering stuff in the website context """

    _inherit = 'ir.qweb'



    def get_asset_bundle(self, xmlid, files, env=None, css=True, js=True):
        return FixdeferBug(xmlid, files, env=env)

class website_inherit(models.Model):
    _name = 'rating.page'
    _description = 'rating.page'

    # visite = fields.Selection(
    #     [('first', 'الزيارة الأولى'), ('daily', 'يوميا'),('monthly','شهريا'), ('sometimes','ليس دائما')
    #
    #      ], default='first', string='عدد زياراتك للبوابة الإلكترونية')
    #
    # ease = fields.Selection(
    #     [('very_easy', 'سهلة جدا'), ('easy', 'سهلة'), ('neutral', 'محايد'), ('difficult', 'صعبة'), ('very_difficult','صعبة جدا')
    #
    #      ], default='very_easy', string='سهولة تصفح البوابة الإلكترونية')
    # clarity =fields.Selection(
    #     [('very_clear', 'واضحة تماما'), ('clear', 'واضحة'), ('neutral', 'محايد'), ('not_clear', 'غير واضحة'), ('not_clear_at_all','غير واضحة اطلاقا')
    #
    #      ], default='very_clear', string='مدى وضوح البوابة الإلكترونية وتنظيمها')
    # satisfaction = fields.Selection(
    #     [('very_satisfied', 'راضي بشدة'), ('satisfied', 'راضي'), ('neutral', 'محايد'), ('not_satisfied', 'غير راضي'), ('not_satisfied_at_all','غير راضي اطلاقا')
    #
    #      ], default='very_satisfied', string='مدى رضاك عن تصميم البوابة لإلكترونية')


    cas_yes = fields.Selection(
        [('utile', 'كانت مفيدة'), ('liaison', 'الإجابات كانت مرتبطة'),('good','مكتوبة بشكل جيد'), ('facile','التصميم جعله من السهل قراءته'), ('autre_yes', 'أخرى')

         ], default='عutile', string='السبب')


    cas_no = fields.Selection(
        [('problem', 'توجد مشكلة تقنية'), ('manque', 'لم استطع إيجاد إجابة ذات صلة'),('bad','مكتوبة بشكل سيء'), ('difficile','التصميم جعله من الصعب قراءته'), ('autre_no', 'أخرى')

         ], default='problem', string='السبب')

    utile = fields.Selection(
        [('yes', 'مفيد'), ('no', 'غير مفيد')

         ], default='yes', string='هل وجدت هذا المحتوى مفيدا')

    path = fields.Char("الصفحة")
    page_name = fields.Char("اسم الصفحة")
    rating = fields.Integer(string="التقييم")

    comment_yes=fields.Text("التعليق")
    comment_no = fields.Text("التعليق")

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
