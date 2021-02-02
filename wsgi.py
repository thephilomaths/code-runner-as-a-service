from app.app import app
from app.db import db
from app.models.execution_logs import ExecutionLog

db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
