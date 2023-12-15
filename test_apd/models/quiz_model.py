# -*- coding: utf-8 -*-

import re

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Quiz(models.Model):
    _name = 'registration.quiz'
    _description = 'quiz of registration'

    shop_logo = fields.Image(required="1", string='شعار المتجر')
    shop_name = fields.Char(string='الاسم التجاري أو اسم المتجر')
    shop_type = fields.Selection([('retail_sector', 'قطاع التجزئة /مركز خدمة'), ('online_shop', 'متجر الكتروني')],
                                 required="1",
                                 string='هل انت')
    description = fields.Char(required="1", string='نبذة عن النشاط/ المركز/ الخدمة')
    shop_code = fields.Integer(required="1", string='رقم السجل التجاري')
    shop_link = fields.Char(required="1", string='الموقع الالكتروني')
    shop_representer = fields.Char(required="1", string='اسم ممثل الشركة/ المؤسسة/ المجموعة')
    shop_number = fields.Char(required="1", string='رقم التواصل')
    shop_email = fields.Char(widget="email", required="1", string='البريد الالكتروني')
    # shop_localisation = fields.Char(string='تصنيف النشاط')
    branches_number = fields.Char(string=' تفاصيل الفروع ان وجدت')
    city = fields.Char(string='المدينة/المدن')
    discount = fields.Selection([('10','10'), ('20','20'), ('30','30'), ('40','40'),('50','50'),('60','60'),('70','70'),('80','80'),('90','90'),('100','100')], required="1", string='مقدار الخصم')
    discount_type = fields.Selection([('code', 'APD2024 كود خصم'),
                                      ('card',
                                       'ابراز بطاقة التسهيلات المرورية/اركاب/اثبات الاعاقة.'),
                                     ],
                                     required="1", string='طريقة الإستفادة من الخصم')
    category_ids = fields.Many2one("shop.category", required="1", string='تصنيف النشاط')
    state = fields.Selection([("new","جديد"),("approved", "موافقة"), ("rejected", "رفض")], default='new',
                             string='حالة نموذج التسجيل')

    def action_approved(self):
        self.state = 'approved'
        mail_template = self.env.ref('test_apd.samedi_approval')
        print(mail_template)
        for rec in self:
            if rec.shop_email:
                mail_template.send_mail(rec.id, force_send=True)
        if self.discount_type == 'code':
            result = 'APD تفعيل الكود من خلال الم   تجر'
        if self.discount_type == 'email':
            result = 'ارغب بتقديم طلب استثنائي و ساتواصل على البريد : PS@apd.gov.sa'
        if self.discount_type == 'card':
            result = 'من خلال ابراز بطاقة التسهيلات المرورية او بطاقة تخفيض اجور الاركاب للاشخاص ذوي الاعاقة و زيارة احد فروع المتجر'
        shop_card_values = {
            'name': self.shop_name,
            'logo': self.shop_logo,
            'discount': self.discount,
            'discount_types': result,
            'website': self.shop_link,
            'category': self.category_ids.name,
            'city': self.city
        }
        self.env['shop.card'].create(shop_card_values)
        print('shop_card_values', shop_card_values)
        return True

    def action_rejected(self):
        self.state = 'rejected'
        # mail_template = self.env.ref('test_apd.samedi_approval')
        # print(mail_template)
        for rec in self:
            if rec.shop_email:
                pass
            # mail_template.send_mail(rec.id, force_send=True)
        return True

    # @api.constrains('shop_email')
    # def check_shop_code(self):
    #     email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #     for rec in self:
    #         if not bool(re.match(email_regex, rec.shop_email)):
    #             raise ValidationError(_("Please verify your email adress ! "))
    #
    # @api.constrains('shop_link')
    # def check_shop_link(self):
    #     website_regex = "^(http(s)?://)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+(/\S*)?$"
    #     for rec in self:
    #         if not bool(re.match(website_regex, rec.shop_link)):
    #             raise ValidationError(_("Please verify your website link ! "))
    #
    # @api.constrains('shop_number')
    # def check_shop_number(self):
    #     for rec in self:
    #         if not rec.shop_number.isdigit() or len(rec.shop_number) != 9:
    #             raise ValidationError(_("Your phone shop number must contains only 9 numbers !"))
    #
    # @api.constrains('description')
    # def check_description(self):
    #     for rec in self:
    #         if len(rec.shop_number) > 180:
    #             raise ValidationError(_("This description is too long, you have reached 180 characters !"))
    #
    # @api.constrains('discount')
    # def check_discount_format(self):
    #     for rec in self:
    #         if rec.discount and not re.match(r'^\d+(\.\d+)?%?$', rec.discount):
    #             raise ValidationError("Invalid discount format. Please enter a valid number or percentage.")
