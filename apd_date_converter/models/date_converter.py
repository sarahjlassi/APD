from odoo import api, fields, models,_
# from hijri_converter import Hijri, Gregorian
from .d_convert.convert import Hijri, Gregorian
import datetime
from odoo.exceptions import UserError
from deep_translator import GoogleTranslator



class Date_Converter(models.TransientModel):
    _name = 'date.convert'


    converter = fields.Selection(string="Converter", selection=[('g_to_h', 'Gregorian To Hijri'), ('h_to_g', 'Hijri To Gregorian '), ], required=False, )

#######################################################################################################################

    @api.onchange('g_day','g_month','g_year')
    def get_hijri_date(self):
        for rec in self:
            if rec.g_day and rec.g_month and rec.g_year:
                g_daaay = ""
                g_month = ""

                kay_val_dict_g_day = dict(self._fields['g_day'].selection)
                for key, val in kay_val_dict_g_day.items():
                    if key == rec.g_day:
                       g_daaay = val

                kay_val_dict_g_day = dict(self._fields['g_month'].selection)
                for key, val in kay_val_dict_g_day.items():
                    if key == rec.g_month:
                        g_month = val

                date_string = rec.g_year + "-" + g_month + "-"+ g_daaay

                date_format = '%Y-%m-%d'

                try:

                    dateObject = datetime.datetime.strptime(date_string, date_format)
                    try:
                        um = Gregorian(dateObject.year, dateObject.month, dateObject.day).to_hijri()
                        rec.h_result = um.day_name() + " " +str(um)
                    except:
                        raise UserError(_('Date Out Of Range'))
                except ValueError:
                    raise UserError(_('Invalid Date'))


            else:
                rec.h_result = ""

    @api.depends('h_result')
    def get_arabic_hijri(self):
        for rec in self:
            if rec.h_result:
                rec.h_result_arabic = GoogleTranslator(source='auto', target='ar').translate(rec.h_result)
            else:
                rec.h_result_arabic = " "



    g_day = fields.Selection(string="Day", selection=[('one', '1'), ('two', '2'), ('three', '3'), ('four', '4'), ('five', '5'),
                                        ('six', '6'), ('seven', '7'), ('eight', '8'), ('nine', '9'), ('ten', '10'),
                                        ('eleven', '11'), ('twelve', '12'), ('thidteen', '13'), ('fourteen', '14'),
                                        ('fifteen', '15'), ('sixteen', '16'), ('seventeen', '17'), ('Eighteen', '18'),
                                        ('ninteen', '19'), ('twenty', '20'), ('twnty_1', '21'), ('twnty_2', '22'),
                                        ('twnty_3', '23'), ('twnty_4', '24'), ('twnty_5', '25'), ('twnty_6', '26'),
                                        ('twnty_7', '27'), ('twnty_8', '28'), ('twnty_9', '29'),
                                        ('thirty', '30'),('thirty_1','31')
                                                   ], required=False, )
    g_month = fields.Selection(string="Month", selection=[('jan', '1'), ('feb', '2'),('mar', '3'), ('apr', '4'),('may', '5'), ('june', '6'),('july', '7'), ('aug', '8'),('sep', '9'), ('oct', '10'),('nov', '11'), ('dec', '12'),
                                                     ], required=False, )

    g_year = fields.Char(string="Year", required=False, )

    h_result = fields.Char(string="Hijri date",readonly=1)
    h_result_arabic = fields.Char(string="Arabic Hijri date ",compute=get_arabic_hijri,store=True)
#######################################################################################################################


    @api.onchange('h_day','h_month','h_year')
    def get_gregorian_date(self):
        for rec in self:
            if rec.h_day and rec.h_month and rec.h_year :
                try:
                    hijri = Hijri(int(rec.h_year), int(rec.h_month), int(rec.h_day))
                    try:
                        um = hijri.to_gregorian()
                        rec.g_result = hijri.day_name() + " " +str(um)
                    except:
                        raise UserError(_('Date Out Of Range'))
                except ValueError:
                    raise UserError(_('Invalid Hijri Date'))

            else:
                rec.g_result = " "

    @api.depends('g_result')
    def get_gregorian_date_from_english(self):
        for rec in self:
            if rec.g_result:
                rec.g_result_arabic = GoogleTranslator(source='auto', target='ar').translate(rec.g_result)
            else:
                rec.g_result_arabic = " "





    h_day = fields.Selection(string="Day",
                             selection=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), (
    '10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'),
    ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), (
    '23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'),
    ('30', '30'),
                                        ], required=False, )


    h_month = fields.Selection(string="Month",
                               selection=[('1', 'Muharram'), ('2', 'Safar'), ('3', 'Rabi-I'), ('4', 'Rabi-II'), ('5', 'Jumada-I'),
                                          ('6', 'Jumada-II'), ('7', 'Rajab'), ('8', 'Shaban'), ('9', 'Ramadan'), ('10', 'Shawwal'),
                                          ('11', 'Dhul-Qadah'), ('12', 'Dhul-Hijjah'),
                                          ], required=False, )

    h_year = fields.Char(string="Year", required=False, )

    g_result = fields.Char(string="Gregorian date",readonly=1 )
    g_result_arabic = fields.Char(string="Arabic Gregorian date",compute=get_gregorian_date_from_english,store=True )




