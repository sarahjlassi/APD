from odoo import  fields, models,_
from odoo.exceptions import ValidationError


class Helpdesk_Ticket_Inherit(models.Model):
    _inherit = 'helpdesk.ticket'

    def name_get(self):
        result = []
        for ticket in self:
            new_origin_id = str(ticket._origin.id).zfill(6)
            result.append((ticket.id, "#%s" % (new_origin_id)))
        return result

    def write(self, values):
        if 'stage_id' in values:
            allowed_next_stages = self.env['stage.route'].search([('stage_id','=',self.current_stage_id.id)],limit=1).next_stages_ids.ids
            allowed_previous_stages = self.env['stage.route'].search([('stage_id','=',self.current_stage_id.id)],limit=1).previous_stages_ids.ids
            allowed_user_to_move_stage = self.env['helpdesk.stage'].search([('id','=',self.current_stage_id.id)],limit=1).custom_users_ids.ids
            allowd_stages = allowed_previous_stages + allowed_next_stages
            if allowd_stages:
                if self.current_stage_id.custom_users_ids:
                    if values.get('stage_id') not in allowd_stages or self.env.user.id not in allowed_user_to_move_stage:
                        raise ValidationError(_('You are not allowed to move ticket to this stage'))

                if values.get('stage_id') in allowd_stages:
                    if self.current_stage_id.allowed_members_managers == 'mang':
                        lst_of_all_team_managers = []
                        allowed_teams_as_managers = self.env['helpdesk.team'].search_read([('id','in',self.current_stage_id.team_ids.ids)],['team_managers_ids'])
                        for user_manager in allowed_teams_as_managers:
                            lst_of_all_team_managers += user_manager['team_managers_ids']
                        if self.env.user.id not in lst_of_all_team_managers:
                            raise ValidationError(_('you are not allowed to move ticket to this stage'))

                    if self.current_stage_id.allowed_members_managers == 'mem':
                        lst_of_all_team_members_allowed = []
                        allowed_teams_as_members = self.env['helpdesk.team'].search_read([('id','in',self.current_stage_id.team_ids.ids)],['team_members_ids'])
                        for user_team_member in allowed_teams_as_members:
                            lst_of_all_team_members_allowed += user_team_member['team_members_ids']

                        if self.env.user.id not in lst_of_all_team_members_allowed:
                            raise ValidationError(_('you are not allowed to move ticket to this Stage'))
                else:
                    raise ValidationError(_('You are not allowed to move ticket to this Stage'))
            else:
                raise ValidationError(_('Please Check Allowed stages from stages routes Menu'))
        return super(Helpdesk_Ticket_Inherit, self).write(values)

    ticket_type_custom = fields.Selection(string="Ticket Type", selection=[('sugg', 'اقتراح'),('inquiry','استفسار'),('requ_open_data','طلب بيانات مفتوحة') ], required=False, )
    n_id = fields.Char(string="National ID",)
    state_id = fields.Many2one(comodel_name="res.country.state", string="City", )
    disability_person = fields.Selection(string="Type Of Creator", selection=[('dis_apility', 'a person with a disability'), ('parents', 'In loco parentis'),
                                                                              ('s_provider','Service Provider'),('d_other','Other'),], required=False, )
    beneficiary = fields.Selection(string="Beneficiary Type", selection=[('social', 'Ministry Of Human Resources And Social Development'), ('education', 'Ministry Of Education'),
                                                                         ('health','Ministry Of Health'),('b_other','Other')], required=False, )

    attach_ids = fields.Many2many(string="Main Attachment", comodel_name='ir.attachment',  copy=False)

    current_stage_id = fields.Many2one(comodel_name="helpdesk.stage", string="Current Stage", readonly=True,related='stage_id' )

