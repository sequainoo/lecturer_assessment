#!/usr/bin/env python3
from models import Base, storage


class Lecturer(Base):
    name = ''

    def __init__(self, **kwargs):
        if 'name' not in kwargs:
            raise AttributeError('name attr not provided')
        if type(kwargs['name']) is not str:
            raise TypeError('name must be a str')
        super().__init__(**kwargs)

    @property
    def courses(self):
        """returns courses related to  lecturer"""
        lecturer_course_list = storage.filter('LecturerCourse',
                                              lecturer_id=self.id)
        course_list = [storage.get('Course', lecturer_course.course_id)
                       for lecturer_course in lecturer_course_list]
        return course_list

    def add_course(self, course):
        lecturer_course = LecturerCourse(lecturer_id=self.id,
                                         course_id=course.id)

    def get_general_question_evaluations(self, course):
        q_evaluations = storage.filter('GeneralQuestionEvaluation',
                                       course_id=course.id,
                                       lecturer_id=self.id)
        grouped_by_question_id = {}
        for q_eval in q_evaluations:
            if q_eval.general_question_id not in grouped_by_question_id:
                grouped_by_question_id[q_eval.general_question_id] = []
            grouped_by_question_id[q_eval.general_question_id].append(
                    q_eval
            )
        organized = []
        for q_id, q_evals in grouped_by_question_id.items():
            question = {'general_question_id': q_id,
                        'text': storage.get('GeneralQuestion',
                                            q_id).text,
                        'evaluations': [q_eval.to_dict()
                                        for q_eval in q_evals]}
            organized.append(question)
        return organized

    def get_general_statement_evaluations(self, course):
        g_evaluations = storage.filter('GeneralStatementEvaluation',
                                       course_id=course.id,
                                       lecturer_id=self.id)
        group = {}
        for g_evaluation in g_evaluations:
            if g_evaluation.general_statement_id not in group:
                group[g_evaluation.general_statement_id] = []
            group[g_evaluation.general_statement_id].append(g_evaluation)

        organized = []
        for g_stmnt_id, g_evaluations in group.items():
            avg_ratings = 0
            statement = {'general_statement_id': g_stmnt_id,
                         'text': storage.get('GeneralStatement',
                                             g_stmnt_id).text,
                         'evaluations': []}
            for g_evaluation in g_evaluations:
                choice = storage.get(
                        'GeneralEvaluationOption',
                        g_evaluation.general_evaluation_option_id
                )
                # track avg_rating
                avg_ratings += choice.value
                eval_dict = g_evaluation.to_dict()
                eval_dict['text'] = choice.text
                eval_dict['value'] = choice.value
                
                statement['evaluations'].append(eval_dict)
            
            # avg ratings
            avg_ratings /= len(statement['evaluations'])
            statement['avg_ratings'] = avg_ratings
            
            organized.append(statement)
        return organized

    def get_criterion_evaluations(self, course):
        # get criterion evaluations on this course for thsi liecturer
        c_evaluations = storage.filter('CriterionEvaluation',
                                       course_id=course.id,
                                       lecturer_id=self.id)
        # group into criteria
        c_group = {}
        for c_eval in c_evaluations:
            if c_eval.criterion_id not in c_group:
                c_group[c_eval.criterion_id] = {c_eval.statement_id: []}
            c_group[c_eval.criterion_id][c_eval.statement_id].append(c_eval)
        # oorganize
        organized_data = []
        for criterion_id, value in c_group.items():
            criterion = {'criterion_id': criterion_id,
                         'text': storage.get('Criterion',
                                             criterion_id).text,
                         'statements': []}
            for statement_id, evaluations in value.items():
                avg_ratings = 0
                statement = {'statement_id': statement_id,
                             'text': storage.get('CriterionStatement',
                                                 statement_id).text,
                             'evaluations': []}
                for evaluation in evaluations:
                    eval_dict = evaluation.to_dict()
                    criterion_option = storage.get(
                            'CriterionOption',
                            evaluation.criterion_option_id
                    )
                    # track avg ratings
                    avg_ratings += criterion_option.value

                    eval_dict['value'] = criterion_option.value
                    eval_dict['text'] = criterion_option.text
                    # put into evaluations
                    statement['evaluations'].append(eval_dict)
                # avg ratings
                avg_ratings /= len(statement['evaluations'])
                statement['avg_ratings'] = avg_ratings

                criterion['statements'].append(statement)
            organized_data.append(criterion)
        return organized_data
