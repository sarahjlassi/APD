from odoo import api, fields, models


class HR_Applicant_Model_inherit(models.Model):
    _inherit = 'hr.applicant'

    gender_custom = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female'), ], required=False, )
    p_with_d = fields.Selection(string="Person With Disability", selection=[('yes', 'Yes'), ('no', 'NO'), ], required=False, )
    experience = fields.Selection(string="Experience", selection=[('yes', 'Yes'), ('no', 'NO'), ], required=False, )
    nationality_c = fields.Char(string="Nationality", required=False,translate=True )
    state_id = fields.Many2one(comodel_name="res.country.state", string="City", )
    dis_id = fields.Many2one(comodel_name="d.type", string="Disability Type ", )
    accom = fields.Text(string="accommodations", required=False, translate=True)
    employer = fields.Char(string="Employer", required=False, translate=True)
    job_title_custom = fields.Char(string="Job Title", required=False, translate=True)
    ex_years = fields.Char(string="Years Of Experience", required=False, translate=True)
    linkedin_pro = fields.Char(string="Linkedin Profile", required=False, translate=True)
    birthday_c = fields.Date(string="Birthday", required=False, )
    degree_id_c = fields.Many2one(comodel_name="degree.degree", string="Degree", required=False, )
    special_c = fields.Char(string="Specialization", required=False,translate=True )
    grade_degree = fields.Char(string="Graduation Year", required=False,translate=True )
    gpa = fields.Char(string="GPA", required=False, translate=True)
    accept_terms = fields.Boolean('Accept Terms?', default=True)
    resume=fields.Many2many('ir.attachment', 'attach_rel', 'doc_id', 'attach_id', string="Attachment", help='You can upload your document', copy=False)

class Disapility_type(models.Model):
    _name = 'd.type'
    _rec_name = 'name'
    _description = 'Disability Type'

    name = fields.Char(string="Disability Name", required=False,translate=True )


class Degree_MOdel(models.Model):
    _name = 'degree.degree'
    _rec_name = 'name'
    _description = 'Aplicant Degree'

    name = fields.Char(string="Name", required=False,translate=True )
    is_collage_degree_or_higher = fields.Boolean(string="", )


class Attachment(models.Model):
    _inherit = 'ir.attachment'
    attach_rel = fields.Many2many('hr.applicant', 'attachment', 'attachment_id', 'document_id', string = "Attachment")
