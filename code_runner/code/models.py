import enum

from code_runner.database import Model, db


class ExecutionState(enum.Enum):
    error = 0
    success = 1


class Language(enum.Enum):
    cpp = 0
    python = 1
    java = 2


class ErrorReason(enum.Enum):
    no_error = -1
    tle = 0
    syntax_or_runtime = 1


class ExecutionLog(Model):
    execution_time = db.Column(db.BigInteger, nullable=False, default=-1)
    state = db.Column(db.Enum(ExecutionState), nullable=False)
    language = db.Column(db.Enum(Language), nullable=False)
    error_reason = db.Column(db.Enum(ErrorReason), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
