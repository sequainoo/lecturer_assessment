#!/usr/bin/env python3
import math

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

        print('working')
        for course in course_list:
            for lecturer_course in lecturer_course_list:
                if course.id == lecturer_course.course_id:
                    course.year = lecturer_course.year
                    print(course.year)
                    continue
        return course_list

    def add_course(self, course):
        lecturer_course = LecturerCourse(lecturer_id=self.id,
                                         course_id=course.id)
        storage.add(lecturer_course)
        storage.save()

    def remove_course(self, course):
        """disassociate course from lecturer"""
        lecturer_courses = storage.filter('LecturerCourse',
                                          lecturer_id=self.id,
                                          course_id=course.id)
        for lecturer_course in lecturer_courses:
            storage.remove(lecturer_course)
        storage.save()
        
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
                                            q_id).question,
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
        sum_statement_avg_ratings = 0

        for g_stmnt_id, g_evaluations in group.items():
            sum_statement_evaluation = 0
            statement = {'general_statement_id': g_stmnt_id,
                         'text': storage.get('GeneralStatement',
                                             g_stmnt_id).text,
                         'evaluations': []}
            for g_evaluation in g_evaluations:
                print(g_evaluation.to_dict())
                choice = storage.get(
                        'GeneralStatementOption',
                        g_evaluation.general_statement_option_id
                )
                # track avg_rating
                sum_statement_evaluation += choice.value
                eval_dict = g_evaluation.to_dict()
                eval_dict['text'] = choice.text
                eval_dict['value'] = choice.value
                
                statement['evaluations'].append(eval_dict)
            
            # avg ratings
            avg = round(sum_statement_evaluation / len(statement['evaluations']), 1)
            statement['avg_rating'] = avg
            
            avg_option = storage.filter('GeneralStatementOption',
                                        value=int(avg),
                                        general_statement_id=g_stmnt_id)

            statement['avg_option'] = avg_option[0].text
            # add statement avg to accumulated sum of all statement averages
            sum_statement_avg_ratings += avg
            organized.append(statement)

        general_statement_evaluation_avg = 0
        if len(organized):
            general_statement_evaluation_avg = sum_statement_avg_ratings / len(organized)
        return organized, round(general_statement_evaluation_avg, 1)

    def get_criterion_evaluations(self, course):
        # get criterion evaluations on this course for thsi liecturer
        c_evaluations = storage.filter('CriterionEvaluation',
                                       course_id=course.id,
                                       lecturer_id=self.id)
        # group into criteria
        c_group = {}
        for c_eval in c_evaluations:
            if c_eval.criterion_id not in c_group:
                c_group[c_eval.criterion_id] = {}
            if c_eval.statement_id not in c_group[c_eval.criterion_id]:
                c_group[c_eval.criterion_id][c_eval.statement_id] = []
            c_group[c_eval.criterion_id][c_eval.statement_id].append(c_eval)
        # oorganize
        organized_data = []
        sum_criteria_avg_ratings = 0

        for criterion_id, value in c_group.items():
            criterion = {'criterion_id': criterion_id,
                         'text': storage.get('Criterion',
                                             criterion_id).name,
                         'statements': []}
            sum_statement_eval_avg = 0 # track avg for a criterion

            for statement_id, evaluations in value.items():
                sum_statement_eval_value = 0 # sum of evaluation value to track avg ratings
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
                    # track avg ratings for statement
                    sum_statement_eval_value += criterion_option.value

                    eval_dict['value'] = criterion_option.value
                    eval_dict['text'] = criterion_option.text
                    # put into evaluations
                    statement['evaluations'].append(eval_dict)
                
                # calculate statement avgerage ratings
                avg = round(sum_statement_eval_value / len(statement['evaluations']), 1)
                statement['avg_rating'] = avg
                # use average to get the average criterion option selected
                avg_option = storage.filter('CriterionOption', value=int(avg))
                if avg_option:
                    statement['avg_option'] = avg_option[0].text

                criterion['statements'].append(statement)
                sum_statement_eval_avg += avg
            # calcute averge across statements
            avg = round(sum_statement_eval_avg / len(criterion['statements']), 1)
            criterion['avg_rating'] = avg
            avg_option = storage.filter('CriterionOption', value=int(avg))
            if  avg_option:
               criterion['avg_option'] = avg_option[0].text
            organized_data.append(criterion)
            sum_criteria_avg_ratings += avg
        length = len(organized_data)
        if not length:
            length = 1

        return organized_data, round(sum_criteria_avg_ratings / length, 1)
