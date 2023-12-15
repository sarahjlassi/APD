from odoo import models, fields, api

class Shop_card(models.Model):
    _name = 'shop.card'
    _description = 'shop.card'


    name = fields.Char(string='اسم المتجر')
    logo = fields.Binary(string='شعار المتجر')
    discount = fields.Char(string="الخصم")
    discount_type = fields.Selection([('code', 'APD تفعيل الكود من خلال المتجر'),
                                      ('card', 'من خلال ابراز بطاقة التسهيلات المرورية او بطاقة تخفيض اجور الاركابللاشخاص دوي الاعاقة و زيارة احد فروع المتجر'),
                                      ('email', 'ارغب بتقديم طلب استثنائي و ساتواصل على البريد : PS@apd.gov.sa') ,],
                                     string='طريقة الإستفادة من الخصم')
    website = fields.Char(string='رابط المتجر')
