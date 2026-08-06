from enum import Enum


class LogsRecipientSchemaMethod(str, Enum):
    AMAZON = "AMAZON"
    GOOGLE = "GOOGLE"

    def __str__(self) -> str:
        return str(self.value)
