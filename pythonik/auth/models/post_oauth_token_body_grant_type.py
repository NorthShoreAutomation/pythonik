from enum import Enum


class PostOauthTokenBodyGrantType(str, Enum):
    AUTHORIZATION_CODE = "authorization_code"
    CLIENT_CREDENTIALS = "client_credentials"

    def __str__(self) -> str:
        return str(self.value)
