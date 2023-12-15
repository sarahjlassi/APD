import logging
import passlib

from odoo import _, api, fields, models
from odoo.exceptions import AccessDenied, UserError

_logger = logging.getLogger(__name__)


class Respartners(models.Model):
    _inherit = 'res.partner'

    gender = fields.Selection(
        string='Gender', default="M",
        selection=[('M', 'Male'), ('F', 'Female')])

    id_issue_date=fields.Char("ID Issue Date")
    id_expiry_date=fields.Char("ID Expiry Date")
    nationality=fields.Char(string="Nationality code")
    language=fields.Char(string="Language")
    nationality_country=fields.Char(string="Nationality")
    dob=fields.Char(string="Date of birth")
    card_issue_place=fields.Char(string="Card Issue Place")
