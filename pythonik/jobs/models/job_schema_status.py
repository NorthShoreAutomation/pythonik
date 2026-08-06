from enum import Enum


class JobSchemaStatus(str, Enum):
    ABORTED = "ABORTED"
    ABORT_PENDING = "ABORT_PENDING"
    DISCARDED = "DISCARDED"
    FAILED = "FAILED"
    FINISHED = "FINISHED"
    FINISHED_WITH_WARNING = "FINISHED_WITH_WARNING"
    PAUSED = "PAUSED"
    PENDING_USER = "PENDING_USER"
    READY = "READY"
    SKIPPED = "SKIPPED"
    STARTED = "STARTED"
    WAITING = "WAITING"

    def __str__(self) -> str:
        return str(self.value)
