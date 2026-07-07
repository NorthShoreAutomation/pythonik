from enum import Enum


class LogsRecipientReadSchemaMethod(str, Enum):
    AMAZON = "AMAZON"
    GOOGLE = "GOOGLE"

    def __str__(self) -> str:
        return str(self.value)
