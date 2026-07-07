from enum import Enum


class NotificationSettingSchemaProtocol(str, Enum):
    EMAIL = "email"
    PUSH = "push"
    WEB = "web"

    def __str__(self) -> str:
        return str(self.value)
