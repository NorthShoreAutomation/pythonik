from enum import Enum


class UserByEmailAndLoginTypeSchemaLoginType(str, Enum):
    PASSWORD = "PASSWORD"
    SSO = "SSO"

    def __str__(self) -> str:
        return str(self.value)
