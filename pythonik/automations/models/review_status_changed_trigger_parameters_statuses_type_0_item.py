from enum import Enum


class ReviewStatusChangedTriggerParametersStatusesType0Item(str, Enum):
    APPROVED = "APPROVED"
    MIXED = "MIXED"
    NA = "N/A"
    NOT_APPROVED = "NOT_APPROVED"
    REQUESTED = "REQUESTED"

    def __str__(self) -> str:
        return str(self.value)
