from enum import Enum


class TriggerOperationsItem(str, Enum):
    CREATE = "CREATE"
    DELAYED_TRIGGER = "DELAYED_TRIGGER"
    DELETE = "DELETE"
    SHARE = "SHARE"
    UPDATE = "UPDATE"

    def __str__(self) -> str:
        return str(self.value)
