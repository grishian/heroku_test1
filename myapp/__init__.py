from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seasurf import SeaSurf

db = SQLAlchemy()

migrate = Migrate()

csrf = SeaSurf()


def create_app(config=None):
    app = Flask(__name__)

    csrf.init_app(app)

    app.config['SESSION_TYPE'] = 'memcached'
    app.config['SECRET_KEY'] = 'super secret key'

    app.debug = True

    # hier zou je dan de juiste config nemen(zie google meet file)
    app.config.from_object('configuration.BaseConfiguration')

    db.init_app(app)

    do_register_blueprint(app)
    do_register_error_handlers(app)
    do_register_cli(app)

    migrate.init_app(app, db)
    return app


def do_register_blueprint(flaskapp):
    from myapp.bp_general import bp_general
    from myapp.bp_mushroom import bp_mushroom
    from myapp.bp_grow_run import bp_grow_run
    from myapp.bp_temperature import bp_temperature

    flaskapp.register_blueprint(bp_general)
    flaskapp.register_blueprint(bp_mushroom)
    flaskapp.register_blueprint(bp_grow_run)
    flaskapp.register_blueprint(bp_temperature)


def do_register_error_handlers(flaskapp):
    from myapp.bp_general.views_general import do_not_authorized, do_not_found, do_server_error

    flaskapp.register_error_handler(404, do_not_found)
    flaskapp.register_error_handler(403, do_not_authorized)
    flaskapp.register_error_handler(406, do_not_authorized)
    flaskapp.register_error_handler(500, do_server_error)


def do_register_cli(flaskapp):
    from myapp.bp_general.utils_general import do_create_db

    flaskapp.cli.add_command(do_create_db)

