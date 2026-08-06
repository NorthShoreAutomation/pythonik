from enum import Enum


class BulkSetApprovalSchemaStatus(str, Enum):
    APPROVED = "APPROVED"
    NOT_APPROVED = "NOT_APPROVED"

    def __str__(self) -> str:
        return str(self.value)
