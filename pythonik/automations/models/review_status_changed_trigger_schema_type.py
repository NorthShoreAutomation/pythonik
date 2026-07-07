from enum import Enum


class ReviewStatusChangedTriggerSchemaType(str, Enum):
    REVIEW_STATUS_CHANGED = "REVIEW_STATUS_CHANGED"

    def __str__(self) -> str:
        return str(self.value)
