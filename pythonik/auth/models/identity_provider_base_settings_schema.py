from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.identity_provider_base_settings_schema_cert_fingerprint_algorithm import (
    IdentityProviderBaseSettingsSchemaCertFingerprintAlgorithm,
)
from ..models.identity_provider_base_settings_schema_digest_algorithm import (
    IdentityProviderBaseSettingsSchemaDigestAlgorithm,
)
from ..models.identity_provider_base_settings_schema_signature_algorithm import (
    IdentityProviderBaseSettingsSchemaSignatureAlgorithm,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentityProviderBaseSettingsSchema")


@_attrs_define
class IdentityProviderBaseSettingsSchema:
    """
    Attributes:
        cert_fingerprint (str | Unset):
        cert_fingerprint_algorithm (IdentityProviderBaseSettingsSchemaCertFingerprintAlgorithm | Unset):
        digest_algorithm (IdentityProviderBaseSettingsSchemaDigestAlgorithm | Unset):
        domain_name (str | Unset):
        idp_x509cert (str | Unset):
        signature_algorithm (IdentityProviderBaseSettingsSchemaSignatureAlgorithm | Unset):
    """

    cert_fingerprint: str | Unset = UNSET
    cert_fingerprint_algorithm: (
        IdentityProviderBaseSettingsSchemaCertFingerprintAlgorithm | Unset
    ) = UNSET
    digest_algorithm: IdentityProviderBaseSettingsSchemaDigestAlgorithm | Unset = UNSET
    domain_name: str | Unset = UNSET
    idp_x509cert: str | Unset = UNSET
    signature_algorithm: (
        IdentityProviderBaseSettingsSchemaSignatureAlgorithm | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cert_fingerprint = self.cert_fingerprint

        cert_fingerprint_algorithm: str | Unset = UNSET
        if not isinstance(self.cert_fingerprint_algorithm, Unset):
            cert_fingerprint_algorithm = self.cert_fingerprint_algorithm.value

        digest_algorithm: str | Unset = UNSET
        if not isinstance(self.digest_algorithm, Unset):
            digest_algorithm = self.digest_algorithm.value

        domain_name = self.domain_name

        idp_x509cert = self.idp_x509cert

        signature_algorithm: str | Unset = UNSET
        if not isinstance(self.signature_algorithm, Unset):
            signature_algorithm = self.signature_algorithm.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cert_fingerprint is not UNSET:
            field_dict["cert_fingerprint"] = cert_fingerprint
        if cert_fingerprint_algorithm is not UNSET:
            field_dict["cert_fingerprint_algorithm"] = cert_fingerprint_algorithm
        if digest_algorithm is not UNSET:
            field_dict["digest_algorithm"] = digest_algorithm
        if domain_name is not UNSET:
            field_dict["domain_name"] = domain_name
        if idp_x509cert is not UNSET:
            field_dict["idp_x509cert"] = idp_x509cert
        if signature_algorithm is not UNSET:
            field_dict["signature_algorithm"] = signature_algorithm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cert_fingerprint = d.pop("cert_fingerprint", UNSET)

        _cert_fingerprint_algorithm = d.pop("cert_fingerprint_algorithm", UNSET)
        cert_fingerprint_algorithm: (
            IdentityProviderBaseSettingsSchemaCertFingerprintAlgorithm | Unset
        )
        if isinstance(_cert_fingerprint_algorithm, Unset):
            cert_fingerprint_algorithm = UNSET
        else:
            cert_fingerprint_algorithm = (
                IdentityProviderBaseSettingsSchemaCertFingerprintAlgorithm(
                    _cert_fingerprint_algorithm
                )
            )

        _digest_algorithm = d.pop("digest_algorithm", UNSET)
        digest_algorithm: IdentityProviderBaseSettingsSchemaDigestAlgorithm | Unset
        if isinstance(_digest_algorithm, Unset):
            digest_algorithm = UNSET
        else:
            digest_algorithm = IdentityProviderBaseSettingsSchemaDigestAlgorithm(
                _digest_algorithm
            )

        domain_name = d.pop("domain_name", UNSET)

        idp_x509cert = d.pop("idp_x509cert", UNSET)

        _signature_algorithm = d.pop("signature_algorithm", UNSET)
        signature_algorithm: (
            IdentityProviderBaseSettingsSchemaSignatureAlgorithm | Unset
        )
        if isinstance(_signature_algorithm, Unset):
            signature_algorithm = UNSET
        else:
            signature_algorithm = IdentityProviderBaseSettingsSchemaSignatureAlgorithm(
                _signature_algorithm
            )

        identity_provider_base_settings_schema = cls(
            cert_fingerprint=cert_fingerprint,
            cert_fingerprint_algorithm=cert_fingerprint_algorithm,
            digest_algorithm=digest_algorithm,
            domain_name=domain_name,
            idp_x509cert=idp_x509cert,
            signature_algorithm=signature_algorithm,
        )

        identity_provider_base_settings_schema.additional_properties = d
        return identity_provider_base_settings_schema

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
