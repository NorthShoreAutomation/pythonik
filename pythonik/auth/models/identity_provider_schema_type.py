from enum import Enum


class IdentityProviderSchemaType(str, Enum):
    AUTH0_COM = "auth0.com"
    GENERIC = "GENERIC"
    OKTA_COM = "okta.com"
    ONELOGIN_COM = "onelogin.com"

    def __str__(self) -> str:
        return str(self.value)
