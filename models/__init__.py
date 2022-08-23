#!/usr/bin/env python3
from models.base import Base
#from models.criterion import Criterion
from models.criterion_option import CriterionOption
#from models.criterion_statement import CriterionStatement
#from models.general_statement import GeneralStatement
from models.general_statement_option import GeneralStatementOption
#from models.general_question import GeneralQuestion
from models.criterion_evaluation import CriterionEvaluation
from models.general_statement_evaluation import GeneralStatementEvaluation
from models.general_question_evaluation import GeneralQuestionEvaluation
from models.student_evaluated_course import StudentEvaluatedCourse
#from models.student import Student
#from models.lecturer import Lecturer
#from models.program_course import ProgramCourse
#from models.lecturer_course import LecturerCourse
#from models.course import Course
from models.level import Level
from models.semester import Semester
#from models.program import Program


classes = {#Criterion.__name__: Criterion,
           CriterionOption.__name__: CriterionOption,
           #CriterionStatement.__name__: CriterionStatement,
           #GeneralStatement.__name__: GeneralStatement,
           GeneralStatementOption.__name__: GeneralStatementOption,
           #GeneralQuestion.__name__: GeneralQuestion,
           #GeneralQuestionAnswer.__name__: GeneralQuestionAnswer,
           CriterionEvaluation.__name__: CriterionEvaluation,
           GeneralStatementEvaluation.__name__: GeneralStatementEvaluation,
           GeneralQuestionEvaluation.__name__: GeneralQuestionEvaluation,
           StudentEvaluatedCourse.__name__: StudentEvaluatedCourse,
           #Student.__name__: Student, Lecturer.__name__: Lecturer,
           #ProgramCourse.__name__: ProgramCourse,
           #LecturerCourse.__name__: LecturerCourse,
           #Course.__name__: Course, Program.__name__: Program,
           Level.__name__: Level, Semester.__name__: Semester}

from models.filestorage.filestorage import Storage
storage = Storage()
from models.program_course import ProgramCourse
from models.criterion import Criterion
from models.criterion_statement import CriterionStatement
from models.general_statement import GeneralStatement
from models.general_question import GeneralQuestion
from models.student import Student
from models.lecturer import Lecturer
from models.lecturer_course import LecturerCourse
from models.course import Course
from models.program import Program

classes[Program.__name__] = Program
classes[Course.__name__] = Course
classes[LecturerCourse.__name__] = LecturerCourse
classes[Lecturer.__name__] = Lecturer
classes[Student.__name__] = Student
classes[GeneralQuestion.__name__] = GeneralQuestion
classes[GeneralStatement.__name__] = GeneralStatement
classes[Criterion.__name__] = Criterion
classes[CriterionStatement.__name__] = CriterionStatement
classes[ProgramCourse.__name__] = ProgramCourse
storage.reload()
