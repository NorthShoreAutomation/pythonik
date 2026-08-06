from enum import Enum


class EdgeTranscodeWorkerSchemaStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def __str__(self) -> str:
        return str(self.value)
