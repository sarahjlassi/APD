# -*- coding: utf-8 -*-

import re

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Quiz(models.Model):
    _name = 'registration.quiz'
    _description = 'quiz of registration'

    shop_name = fields.Char(string='اسم المتجر')
    shop_type = fields.Selection([('retail_sector', 'قطاع التجزئة '), ('online_shop', 'متجر الكتروني')], required="1",
                                 string='هل انت')
    shop_code = fields.Integer(required="1", string='رقم التسجيل')
    shop_link = fields.Char(required="1", string='الرابط الالكتروني للمتجر')
    shop_representer = fields.Char(required="1", string='اسم ممثل المتجر')
    shop_number = fields.Char(required="1", string='رقم التواصل')
    shop_email = fields.Char(widget="email", required="1", string='البريد الالكتروني')
    shop_localisation = fields.Char(required="1", string='مكان تواجد المتجر او حدود تغطية المتجر للشحن')
    branches_number = fields.Integer(required="1", string='عدد الفروع')
    city = fields.Char(required="1", string='المدينة/المدن')
    shop_logo = fields.Binary(required="1", string='شعار المتجر')
    discount = fields.Char(required="1", string='مقدار الخصم')
    discount_type = fields.Selection([('code', 'APD تفعيل الكود من خلال المتجر'),
                                      ('card',
                                       'من خلال ابراز بطاقة التسهيلات المرورية او بطاقة تخفيض اجور الاركابللاشخاص دوي الاعاقة و زيارة احد فروع المتجر'),
                                      ('email', 'ارغب بتقديم طلب استثنائي و ساتواصل على البريد : PS@apd.gov.sa'), ],
                                     required="1", string='طريقة الإستفادة من الخصم')
    category_ids = fields.Many2one("shop.category", required="1", string='التصنيفات')
    state = fields.Selection([("new", "New"), ("approved", "Approved"), ("rejected", "Rejected")], default='new',
                             required="1", string='حالة نموذج التسجيل')

    def action_new(self):
        self.state = 'new'
        return True

    def action_approved(self):
        self.state = 'approved'
        mail_template = self.env.ref('apd.approved_email_template')
        # print(mail_template)
        for rec in self:
            if rec.shop_email:

                mail_template.send_mail(rec.id, force_send=True)
        shop_card_values = {
            'name': self.shop_name,
            'logo': self.shop_logo,
            'discount': self.discount,
            'discount_type': self.discount_type,
            'website': self.shop_link,
        }
        self.env['shop.card'].create(shop_card_values)
        print(shop_card_values)
        return True

    def action_rejected(self):
        self.state = 'rejected'
        #mail_template = self.env.ref('auth_signup.mail_template_data_unregistered_users')
        # print(mail_template)
        for rec in self:
            if rec.shop_email:
                pass
            # mail_template.send_mail(rec.id, force_send=True)
        return True

    @api.constrains('shop_email')
    def check_shop_code(self):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        for rec in self:
            if not bool(re.match(email_regex, rec.shop_email)):
                raise ValidationError(_("Please verify your email adress ! "))

    @api.constrains('shop_link')
    def check_shop_link(self):
        website_regex = "^(http(s)?://)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+(/\S*)?$"
        for rec in self:
            if not bool(re.match(website_regex, rec.shop_link)):
                raise ValidationError(_("Please verify your website link ! "))

    @api.constrains('shop_number')
    def check_shop_number(self):
        for rec in self:
            if not rec.shop_number.isdigit() or len(rec.shop_number) != 10:
                raise ValidationError(_("Your phone shop number must contains only 10 numbers ! "))
