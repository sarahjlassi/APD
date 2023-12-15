# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rating_website(models.Model):
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




# class webpage_inherit(models.Model):
#     _inherit ='website.page'

