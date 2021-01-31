from app.app import app
from flask_sqlalchemy import SQLAlchemy
from ..model.execution_logs import ExecutionLog

db = SQLAlchemy(app)
db.create_all()
