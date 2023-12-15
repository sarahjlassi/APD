from odoo import models, fields, api
from odoo.http import request


class Shop_card(models.Model):
    _name = 'shop.card'
    _description = 'shop.card'

    name = fields.Char(string='اسم المتجر')
    logo = fields.Image(string='شعار المتجر')
    discount = fields.Integer(string="الخصم")
    # discount_type = fields.Selection([('code', 'APD تفعيل الكود من خلال الم   تجر'),
    #                                   ('card', 'من خلال ابراز بطاقة التسهيلات المرورية او بطاقة تخفيض اجور الاركابللاشخاص دوي الاعاقة و زيارة احد فروع المتجر'),
    #                                   ('email', 'ارغب بتقديم طلب استثنائي و ساتواصل على البريد : PS@apd.gov.sa') ,],
    #                                  string='طريقة الإستفادة من الخصم')
    discount_types = fields.Char(string='طريقة الإستفادة من الخصم')
    website = fields.Char(string='رابط المتجر')
    category = fields.Char(string='التصنيف')
    city = fields.Char(string='المدينة/المدن')
    special_offer = fields.Boolean(string="عرض مميز", default=False)
    clicks = fields.Integer(string='عدد الزيارات')

    @api.model
    def most_visited_cards(self, record_id):
        print(" cqrd   id", record_id )
        record = self.browse(record_id)
        record.clicks += 1

        return True





