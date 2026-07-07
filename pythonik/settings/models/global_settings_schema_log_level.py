from enum import Enum


class GlobalSettingsSchemaLogLevel(str, Enum):
    CRITICAL = "CRITICAL"
    DEBUG = "DEBUG"
    ERROR = "ERROR"
    INFO = "INFO"
    NOTSET = "NOTSET"
    WARNING = "WARNING"

    def __str__(self) -> str:
        return str(self.value)
