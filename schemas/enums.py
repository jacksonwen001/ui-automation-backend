from enum import Enum


class Status(Enum):
    RUNNING = 'RUNNING'
    SUCCEED = 'SUCCEED'
    FAILED  = 'FAILED'
    CANCELLED = 'CANCELLED'

class Env(Enum):
    QA = 'QA'
    UAT = 'UAT'  