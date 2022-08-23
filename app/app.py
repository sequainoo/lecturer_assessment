#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = b'chitown'

if __name__ == '__main__':
    from app.views.login import *
    from app.views.logout import *
    from app.views.home import *
    from app.views.evaluation import *
    from app.views.admin.evaluation_statements_creation_form import *
    from app.views.admin.criterion import *
    from app.views.admin.general_statement import *
    from app.views.admin.general_question import *
    from app.views.admin.admin import *
    from app.views.admin.course import *
    from app.views.admin.program import *
    from app.views.admin.level import *
    from app.views.admin.semester import *
    from app.views.admin.student import *
    from app.views.admin.lecturer import *
    from app.views.admin.program_course import *
    from app.views.admin.lecturer_course import *
    app.run(debug=True)
