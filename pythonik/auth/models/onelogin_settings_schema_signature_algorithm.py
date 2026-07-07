from enum import Enum


class OneloginSettingsSchemaSignatureAlgorithm(str, Enum):
    HTTPWWW_W3_ORG200009XMLDSIGDSA_SHA1 = "http://www.w3.org/2000/09/xmldsig#dsa-sha1"
    HTTPWWW_W3_ORG200009XMLDSIGRSA_SHA1 = "http://www.w3.org/2000/09/xmldsig#rsa-sha1"
    HTTPWWW_W3_ORG200104XMLDSIG_MORERSA_SHA256 = (
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"
    )
    HTTPWWW_W3_ORG200104XMLDSIG_MORERSA_SHA384 = (
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha384"
    )
    HTTPWWW_W3_ORG200104XMLDSIG_MORERSA_SHA512 = (
        "http://www.w3.org/2001/04/xmldsig-more#rsa-sha512"
    )

    def __str__(self) -> str:
        return str(self.value)
