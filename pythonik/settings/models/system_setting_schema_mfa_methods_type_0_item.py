from enum import Enum


class SystemSettingSchemaMfaMethodsType0Item(str, Enum):
    MAIL_2SV = "MAIL_2SV"
    TOTP = "TOTP"

    def __str__(self) -> str:
        return str(self.value)
