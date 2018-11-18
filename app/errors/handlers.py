from app.errors import bp
from flask import render_template

@bp.app_errorhandler(404)
def pageNotFound(error):
    print("wp")
    return render_template('errors/404.html'), 404

@bp.route('/hi')
def hi():
    return 'Hi'