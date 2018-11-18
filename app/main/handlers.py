from app.main import bp

from flask import render_template, request, make_response, session, escape, current_app

@bp.route('/test', methods = ['GET'])
def test():

    if 'User' in session:
        return session['User']
    return "No User"

@bp.route('/out', methods = ['GET'])
def out():

    return session.pop('User', '')


@bp.route('/', methods = ['GET'])
def main():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    response =  make_response(render_template('index.html'))
    response.set_cookie('User','Laotiemeimaobing', max_age=60, domain=".wchen1999.me")

    session['User'] = 'Jctest'

    current_app.logger.info(f"{session['User']} just accessed")

    return response
