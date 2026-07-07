from enum import Enum


class JobStepUpdateBulkSchemaStatus(str, Enum):
    DONE = "DONE"
    FAILED = "FAILED"
    IN_PROGRESS = "IN_PROGRESS"
    SKIPPED = "SKIPPED"
    WAITING = "WAITING"

    def __str__(self) -> str:
        return str(self.value)
