from enum import Enum


class TriggerCustomActionType(str, Enum):
    CUSTOM_ACTION = "CUSTOM_ACTION"

    def __str__(self) -> str:
        return str(self.value)
