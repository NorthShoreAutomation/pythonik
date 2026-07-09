from enum import Enum


class DeviceTokenSchemaPushService(str, Enum):
    APNS = "apns"
    FCM = "fcm"

    def __str__(self) -> str:
        return str(self.value)
