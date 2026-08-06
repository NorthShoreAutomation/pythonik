from enum import Enum


class NotifyOTPConfigurationChangedSchemaMessageType(str, Enum):
    OTP_DISABLED = "otp_disabled"
    OTP_ENABLED = "otp_enabled"
    TOTP_DISABLED = "totp_disabled"
    TOTP_ENABLED = "totp_enabled"

    def __str__(self) -> str:
        return str(self.value)
