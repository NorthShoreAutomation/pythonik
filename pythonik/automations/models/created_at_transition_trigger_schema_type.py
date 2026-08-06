from enum import Enum


class CreatedAtTransitionTriggerSchemaType(str, Enum):
    CREATED_AT_TRANSITION = "CREATED_AT_TRANSITION"

    def __str__(self) -> str:
        return str(self.value)
