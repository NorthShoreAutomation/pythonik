from enum import Enum


class JobsStateSchemaAction(str, Enum):
    ABORT = "ABORT"
    PAUSE = "PAUSE"
    RESTART = "RESTART"
    RESUME = "RESUME"

    def __str__(self) -> str:
        return str(self.value)
