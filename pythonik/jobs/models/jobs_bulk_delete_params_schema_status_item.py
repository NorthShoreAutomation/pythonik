from enum import Enum


class JobsBulkDeleteParamsSchemaStatusItem(str, Enum):
    ABORTED = "ABORTED"
    DISCARDED = "DISCARDED"
    FAILED = "FAILED"
    FINISHED = "FINISHED"
    FINISHED_WITH_WARNING = "FINISHED_WITH_WARNING"
    SKIPPED = "SKIPPED"

    def __str__(self) -> str:
        return str(self.value)
