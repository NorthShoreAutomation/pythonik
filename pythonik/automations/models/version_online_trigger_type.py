from enum import Enum


class VersionOnlineTriggerType(str, Enum):
    VERSION_ONLINE = "VERSION_ONLINE"

    def __str__(self) -> str:
        return str(self.value)
