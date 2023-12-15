# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import passlib

from odoo import _, api, fields, models
from odoo.exceptions import AccessDenied, UserError

_logger = logging.getLogger(__name__)


class ResUsers(models.Model):
    _inherit = 'res.users'

    nafath_enabled = fields.Boolean(string="Nafath authentication")
    nafath_secret = fields.Char(copy=False)
    national_id = fields.Char(copy=False)
    nafath_callback_success = fields.Boolean(string="Nafath Callback Success")

    def _check_credentials(self, password, env):
        try:
            # Attempt a regular login (via other auth addons) first.
            return super()._check_credentials(password, env)

        except (AccessDenied, passlib.exc.PasswordSizeError):
            # since normal auth did not succeed we now try to find if the user
            # has an active token attached to his uid
            token = (
                self.env["res.users"].sudo().search([("nafath_secret", "=", password)])
            )
            if token:
                return
            raise AccessDenied() from None
