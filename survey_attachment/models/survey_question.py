# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.exceptions import AccessError, MissingError, ValidationError, UserError
import base64



class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    question_attachment = fields.Binary('Question attachment')
    # type = fields.Selection([
    #     ('free_text', 'Multiple Lines Text Box'),
    #     ('textbox', 'Single Line Text Box'),
    #     ('numerical_box', 'Numerical Value'),
    #     ('date', 'Date'),
    #     ('upload_file', 'Upload file'),
    #     ('simple_choice', 'Multiple choice: only one answer'),
    #     ('multiple_choice', 'Multiple choice: multiple answers allowed'),
    #     ('matrix', 'Matrix')], string='Type of Question', default='free_text', required=True)

    question_type = fields.Selection(selection_add=[('upload_file', 'Upload file')])


class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    def save_lines(self, question, answer, comment=None):
        """ Save answers to questions, depending on question type

            If an answer already exists for question and user_input_id, it will be
            overwritten (or deleted for 'choice' questions) (in order to maintain data consistency).
        """
        old_answers = self.env['survey.user_input.line'].search([
            ('user_input_id', '=', self.id),
            ('question_id', '=', question.id)
        ])

        if question.question_type in ['char_box', 'text_box', 'numerical_box', 'date', 'datetime']:
            self._save_line_simple_answer(question, old_answers, answer)
            if question.save_as_email and answer:
                self.write({'email': answer})
            if question.save_as_nickname and answer:
                self.write({'nickname': answer})

        elif question.question_type in ['simple_choice', 'multiple_choice']:
            self._save_line_choice(question, old_answers, answer, comment)
        elif question.question_type == 'matrix':
            self._save_line_matrix(question, old_answers, answer, comment)
        elif question.question_type == 'upload_file':
            self._save_line_upload_file(question, old_answers, answer)
        else:
            return super(SurveyUserInput, self).save_lines(question, answer, comment=None)
            # raise AttributeError(question.question_type + ": This type of question has no saving function")

    @api.model
    def _save_line_upload_file(self, question, old_answers, answer):
        print("question: ", question)
        print("old_answers: ", old_answers)
        print("answer: ", answer)

        # vals = {
        #     'user_input_id': self.id,
        #     'question_id': question.id,
        #     'survey_id': question.survey_id.id,
        #     'skipped': False
        # }
        # file_name = str(post[answer_tag])
        # file_type = file_name.find("('application/pdf')")
        # image_type = file_name.find("('image/png')")
        # if file_type > -1:
        #     vals.update({'file_type': 'pdf'})
        # if image_type > -1:
        #     vals.update({'file_type': 'image'})
        #
        # if question.constr_mandatory:
        #     file = base64.encodebytes(post[answer_tag].read())
        # else:
        #     file = base64.encodebytes(post[answer_tag].read()) if post[answer_tag] else None
        # if answer_tag in post:
        #     vals.update({'answer_type': 'upload_file', 'file': file})
        # else:
        #     vals.update({'answer_type': None, 'skipped': True})
        # old_uil = self.search([
        #     ('user_input_id', '=', user_input_id),
        #     ('survey_id', '=', question.survey_id.id),
        #     ('question_id', '=', question.id)
        # ])
        # if old_uil:
        #     old_uil.write(vals)
        # else:
        #     old_uil.create(vals)
        # return True


class SurveyUserInputLine(models.Model):
    _inherit = 'survey.user_input.line'

    answer_type = fields.Selection(selection_add=[
        ('upload_file', 'Upload file'),
        ('list', 'List box'),
        ('matrix_models', 'Matrix models')])

    file = fields.Binary('Upload file')
    file_type = fields.Selection([('image', 'image'), ('pdf', 'pdf')])

