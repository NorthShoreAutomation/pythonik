from enum import Enum


class SystemSettingSchemaWatermark(str, Enum):
    NONE = "none"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
