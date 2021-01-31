import os

from flask import Flask
from . import setup

from .config.routes import routes


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_ENDPOINT']

app.register_blueprint(routes)

if __name__ == "__main__":
  app.run("0.0.0.0", 5000, debug=True, threaded=True)