from enum import Enum


class DeviceTokenSchemaPlatform(str, Enum):
    ANDROID = "android"
    IOS = "ios"

    def __str__(self) -> str:
        return str(self.value)
