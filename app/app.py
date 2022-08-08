#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = b'chitown'

if __name__ == '__main__':
    from app.views.login import *
    from app.views.home import *
    from app.views.admin.evaluation_statements_creation_form import *
    from app.views.admin.criterion_creation import *
    from app.views.admin.general_statement_creation import *
    from app.views.admin.general_question_creation import *
    app.run(debug=True)
