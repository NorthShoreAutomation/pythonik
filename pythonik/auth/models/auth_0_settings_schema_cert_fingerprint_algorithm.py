from enum import Enum


class Auth0SettingsSchemaCertFingerprintAlgorithm(str, Enum):
    HTTPWWW_W3_ORG200009XMLDSIGSHA1 = "http://www.w3.org/2000/09/xmldsig#sha1"
    HTTPWWW_W3_ORG200104XMLDSIG_MORESHA384 = (
        "http://www.w3.org/2001/04/xmldsig-more#sha384"
    )
    HTTPWWW_W3_ORG200104XMLENCSHA256 = "http://www.w3.org/2001/04/xmlenc#sha256"
    HTTPWWW_W3_ORG200104XMLENCSHA512 = "http://www.w3.org/2001/04/xmlenc#sha512"

    def __str__(self) -> str:
        return str(self.value)
