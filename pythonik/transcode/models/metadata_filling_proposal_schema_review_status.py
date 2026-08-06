from enum import Enum


class MetadataFillingProposalSchemaReviewStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    PENDING_USER = "PENDING_USER"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
