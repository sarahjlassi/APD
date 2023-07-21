from odoo import api, fields, models,_


class Helpdesk_stage_Inherit(models.Model):
    _inherit = 'helpdesk.stage'

    custom_users_ids = fields.Many2many(comodel_name="res.users", string="Allowed Users", )
    allowed_members_managers = fields.Selection(string="Allowed Managers/Members", selection=[('mang', 'Teams Managers'), ('mem', 'Teams Members'), ], required=False, )

class Stage_Routes(models.Model):
    _name = 'stage.route'

    stage_id = fields.Many2one(comodel_name="helpdesk.stage", string="Stage", required=True, )
    next_stages_ids = fields.Many2many(comodel_name="helpdesk.stage", relation="rel1", column1="helpdesk_stage_id", column2="stage_route_id", string="Next Stages", )
    previous_stages_ids = fields.Many2many(comodel_name="helpdesk.stage", relation="rel2", column1="helpdesk_stage_id_2", column2="stage_route_id_2", string="Previous Stages", )