import logging
import sys
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask

from code_runner.extensions import db, limiter
from . import code


def create_app(config_object='code_runner.settings'):
    """Creates and returns flask app instance as well as register all the extensions and blueprints"""
    app = Flask(__name__)
    register_environment()
    app.config.from_object(config_object)
    register_blueprints(app=app)
    register_views(app=app)
    register_extensions(app=app)
    configure_logger(app=app)
    return app


def register_blueprints(app):
    """Registers the blueprints"""
    app.register_blueprint(code.views.blueprint)


def register_views(app):
    """Registers the pluggable views"""
    run_view = code.views.RunCode.as_view('run')
    run_async_view = code.views.RunCodeAsync.as_view('run-async')
    app.add_url_rule('/run', view_func=run_view, methods=['POST'])
    app.add_url_rule('/run-async', view_func=run_async_view, methods=['POST'])
    app.add_url_rule('/get-result/<string:task_id>', view_func=run_async_view, methods=['GET'])


def register_extensions(app):
    """Register Flask extensions"""
    with app.app_context():
        db.init_app(app=app)
        db.create_all()
        limiter.init_app(app=app)


def register_environment():
    """Register environment"""
    dotenv_path = Path('./') / '.env.development.local'
    load_dotenv(dotenv_path=dotenv_path)


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
