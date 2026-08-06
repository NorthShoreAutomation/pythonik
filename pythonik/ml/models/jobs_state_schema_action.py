from enum import Enum


class JobsStateSchemaAction(str, Enum):
    ABORT = "ABORT"
    RESTART = "RESTART"

    def __str__(self) -> str:
        return str(self.value)
