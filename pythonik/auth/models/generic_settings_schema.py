from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.generic_settings_schema_cert_fingerprint_algorithm import (
    GenericSettingsSchemaCertFingerprintAlgorithm,
)
from ..models.generic_settings_schema_digest_algorithm import (
    GenericSettingsSchemaDigestAlgorithm,
)
from ..models.generic_settings_schema_signature_algorithm import (
    GenericSettingsSchemaSignatureAlgorithm,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GenericSettingsSchema")


@_attrs_define
class GenericSettingsSchema:
    """
    Attributes:
        idp_entity_id (str):
        idp_sso_post_url (str):
        name (str):
        cert_fingerprint (str | Unset):
        cert_fingerprint_algorithm (GenericSettingsSchemaCertFingerprintAlgorithm | Unset):
        digest_algorithm (GenericSettingsSchemaDigestAlgorithm | Unset):
        domain_name (str | Unset):
        idp_sls_redirect_url (str | Unset):
        idp_x509cert (str | Unset):
        name_id_encrypted (bool | Unset):
        signature_algorithm (GenericSettingsSchemaSignatureAlgorithm | Unset):
        want_assertions_signed (bool | Unset):
        want_messages_signed (bool | Unset):
    """

    idp_entity_id: str
    idp_sso_post_url: str
    name: str
    cert_fingerprint: str | Unset = UNSET
    cert_fingerprint_algorithm: (
        GenericSettingsSchemaCertFingerprintAlgorithm | Unset
    ) = UNSET
    digest_algorithm: GenericSettingsSchemaDigestAlgorithm | Unset = UNSET
    domain_name: str | Unset = UNSET
    idp_sls_redirect_url: str | Unset = UNSET
    idp_x509cert: str | Unset = UNSET
    name_id_encrypted: bool | Unset = UNSET
    signature_algorithm: GenericSettingsSchemaSignatureAlgorithm | Unset = UNSET
    want_assertions_signed: bool | Unset = UNSET
    want_messages_signed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idp_entity_id = self.idp_entity_id

        idp_sso_post_url = self.idp_sso_post_url

        name = self.name

        cert_fingerprint = self.cert_fingerprint

        cert_fingerprint_algorithm: str | Unset = UNSET
        if not isinstance(self.cert_fingerprint_algorithm, Unset):
            cert_fingerprint_algorithm = self.cert_fingerprint_algorithm.value

        digest_algorithm: str | Unset = UNSET
        if not isinstance(self.digest_algorithm, Unset):
            digest_algorithm = self.digest_algorithm.value

        domain_name = self.domain_name

        idp_sls_redirect_url = self.idp_sls_redirect_url

        idp_x509cert = self.idp_x509cert

        name_id_encrypted = self.name_id_encrypted

        signature_algorithm: str | Unset = UNSET
        if not isinstance(self.signature_algorithm, Unset):
            signature_algorithm = self.signature_algorithm.value

        want_assertions_signed = self.want_assertions_signed

        want_messages_signed = self.want_messages_signed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "idp_entity_id": idp_entity_id,
                "idp_sso_post_url": idp_sso_post_url,
                "name": name,
            }
        )
        if cert_fingerprint is not UNSET:
            field_dict["cert_fingerprint"] = cert_fingerprint
        if cert_fingerprint_algorithm is not UNSET:
            field_dict["cert_fingerprint_algorithm"] = cert_fingerprint_algorithm
        if digest_algorithm is not UNSET:
            field_dict["digest_algorithm"] = digest_algorithm
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name
        if idp_sls_redirect_url is not UNSET:
            field_dict["idp_sls_redirect_url"] = idp_sls_redirect_url
        if idp_x509cert is not UNSET:
            field_dict["idp_x509cert"] = idp_x509cert
        if name_id_encrypted is not UNSET:
            field_dict["name_id_encrypted"] = name_id_encrypted
        if signature_algorithm is not UNSET:
            field_dict["signature_algorithm"] = signature_algorithm
        if want_assertions_signed is not UNSET:
            field_dict["want_assertions_signed"] = want_assertions_signed
        if want_messages_signed is not UNSET:
            field_dict["want_messages_signed"] = want_messages_signed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        idp_entity_id = d.pop("idp_entity_id")

        idp_sso_post_url = d.pop("idp_sso_post_url")

        name = d.pop("name")

        cert_fingerprint = d.pop("cert_fingerprint", UNSET)

        _cert_fingerprint_algorithm = d.pop("cert_fingerprint_algorithm", UNSET)
        cert_fingerprint_algorithm: (
            GenericSettingsSchemaCertFingerprintAlgorithm | Unset
        )
        if isinstance(_cert_fingerprint_algorithm, Unset):
            cert_fingerprint_algorithm = UNSET
        else:
            cert_fingerprint_algorithm = GenericSettingsSchemaCertFingerprintAlgorithm(
                _cert_fingerprint_algorithm
            )

        _digest_algorithm = d.pop("digest_algorithm", UNSET)
        digest_algorithm: GenericSettingsSchemaDigestAlgorithm | Unset
        if isinstance(_digest_algorithm, Unset):
            digest_algorithm = UNSET
        else:
            digest_algorithm = GenericSettingsSchemaDigestAlgorithm(_digest_algorithm)

        domain_name = d.pop("domain_name", UNSET)

        idp_sls_redirect_url = d.pop("idp_sls_redirect_url", UNSET)

        idp_x509cert = d.pop("idp_x509cert", UNSET)

        name_id_encrypted = d.pop("name_id_encrypted", UNSET)

        _signature_algorithm = d.pop("signature_algorithm", UNSET)
        signature_algorithm: GenericSettingsSchemaSignatureAlgorithm | Unset
        if isinstance(_signature_algorithm, Unset):
            signature_algorithm = UNSET
        else:
            signature_algorithm = GenericSettingsSchemaSignatureAlgorithm(
                _signature_algorithm
            )

        want_assertions_signed = d.pop("want_assertions_signed", UNSET)

        want_messages_signed = d.pop("want_messages_signed", UNSET)

        generic_settings_schema = cls(
            idp_entity_id=idp_entity_id,
            idp_sso_post_url=idp_sso_post_url,
            name=name,
            cert_fingerprint=cert_fingerprint,
            cert_fingerprint_algorithm=cert_fingerprint_algorithm,
            digest_algorithm=digest_algorithm,
            domain_name=domain_name,
            idp_sls_redirect_url=idp_sls_redirect_url,
            idp_x509cert=idp_x509cert,
            name_id_encrypted=name_id_encrypted,
            signature_algorithm=signature_algorithm,
            want_assertions_signed=want_assertions_signed,
            want_messages_signed=want_messages_signed,
        )

        generic_settings_schema.additional_properties = d
        return generic_settings_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
