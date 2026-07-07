from enum import Enum


class ModifiedAtTransitionTriggerSchemaType(str, Enum):
    MODIFIED_AT_TRANSITION = "MODIFIED_AT_TRANSITION"

    def __str__(self) -> str:
        return str(self.value)
