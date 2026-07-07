from enum import Enum


class TranscoderUsageSchemaStatus(str, Enum):
    ABORTED = "ABORTED"
    FAILED = "FAILED"
    FINISHED = "FINISHED"

    def __str__(self) -> str:
        return str(self.value)
