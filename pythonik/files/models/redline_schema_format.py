from enum import Enum


class RedlineSchemaFormat(str, Enum):
    APPLE_PRORES = "Apple ProRes"
    QT_TRANSCODE = "QT transcode"
    VALUE_0 = ""

    def __str__(self) -> str:
        return str(self.value)
