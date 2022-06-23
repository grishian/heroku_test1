from flask import render_template
from myapp.bp_general import bp_general


@bp_general.route('/')
@bp_general.route('/index')
def do_home():
    return render_template('general/home.html', title='Home')


def do_not_found(error):
    return render_template('general/errors.html', code=404, error=error)


def do_not_authorized(error):
    return render_template('general/errors.html', code=403, error=error)


def do_server_error(error):
    return render_template('general/errors.html', code=500, error=error)
