from enum import Enum


class PostOauthTokenBodyGrantType(str, Enum):
    AUTHORIZATION_CODE = "authorization_code"
    CLIENT_CREDENTIALS = "client_credentials"
    REFRESH_TOKEN = "refresh_token"

    def __str__(self) -> str:
        return str(self.value)
