import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


migrate = Migrate()
login_manager = LoginManager()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='mysql://devusr:789123as@127.0.0.1/devdb',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        MYSQL_DATABASE_CHARSET='utf8',
    )

    # initialize the database connection
    from welldata.models import db
    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)

    if test_config is None:
        # load the instace config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # import blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    with app.app_context():
        return app
