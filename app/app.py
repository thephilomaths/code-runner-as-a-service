import os

from flask import Flask

from app.config.routes import routes
from app import setup

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{os.environ['DATABASE_USERNAME']}:" + \
                                        f"{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_HOST']}/" + \
                                        f"{os.environ['DATABASE_NAME']}"
app.config['SQLALCHEMY_ECHO'] = True

app.register_blueprint(routes)


@app.route('/', methods=['GET'])
def handler():
    return 'HELLo'
