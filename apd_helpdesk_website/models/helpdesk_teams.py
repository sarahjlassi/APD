from odoo import fields, models


class Helpdesk_Teams_Inherit(models.Model):
    _inherit = 'helpdesk.team'

    ticket_type_custom = fields.Selection(string="Ticket Type", selection=[('sugg', 'اقتراح'),('inquiry','استفسار'),('requ_open_data','طلب بيانات مفتوحة') ], required=False, )
    team_managers_ids = fields.Many2many(comodel_name="res.users", relation="rel3", column1="custom_manager", column2="users_id1", string="Team Managers", )
    team_members_ids = fields.Many2many(comodel_name="res.users", relation="rel4", column1="member_id_custom", column2="users_id2", string="Team Members", )