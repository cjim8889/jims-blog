import os

baseDir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('FLASK_KEY')
    TRAP_HTTP_EXCEPTIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(baseDir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False