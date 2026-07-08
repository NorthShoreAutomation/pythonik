from enum import Enum


class SystemNotificationSchemaStatus(str, Enum):
    QUEUED = "QUEUED"
    READ = "READ"
    SENT = "SENT"

    def __str__(self) -> str:
        return str(self.value)
