import enum
from ..db import db


class ExecutionState(enum.Enum):
    error = 0
    success = 1


class Language(enum.Enum):
    c_plus_plus = 0
    python = 1
    java = 2


class ErrorReason(enum.Enum):
    tle = 0
    syntax = 1
    run_time = 2


class ExecutionLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    execution_time = db.Column(db.BigInteger, nullable=False)
    state = db.Column(db.Enum(ExecutionState), nullable=False)
    language = db.Column(db.Enum(Language), nullable=False)
    error_reason = db.Column(db.Enum(ErrorReason), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
