from enum import Enum


class RequestReviewActionType(str, Enum):
    REQUEST_REVIEW = "REQUEST_REVIEW"

    def __str__(self) -> str:
        return str(self.value)
