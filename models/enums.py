from enum import Enum


class Status(Enum):
    RUNNING = "RUNNING"
    CANCELLED = "CANCELLED"
    SUCCEED = "SUCCEED"
    FAILED = "FAILED"

class Env(Enum):
    QA = "QA"
    UAT = "UAT"

class Position(Enum):
    BEFORE = "BEFORE"
    PROCESS = "PROCESS"
    AFTER = "AFTER"