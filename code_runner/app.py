import logging
import sys
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask

from code_runner.extensions import db
from . import code


def create_app(config_object='code_runner.settings'):
    app = Flask(__name__)
    register_environment()
    app.config.from_object(config_object)
    register_blueprints(app=app)
    register_extensions(app=app)
    configure_logger(app=app)
    return app


def register_blueprints(app):
    app.register_blueprint(code.views.blueprint)


def register_extensions(app):
    """Register Flask extensions"""
    with app.app_context():
        db.init_app(app=app)
        db.create_all()


def register_environment():
    """Register environment"""
    dotenv_path = Path('./') / '.env.development.local'
    load_dotenv(dotenv_path=dotenv_path)


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
