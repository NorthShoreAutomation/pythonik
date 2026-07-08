from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.okta_settings_schema_cert_fingerprint_algorithm import (
    OktaSettingsSchemaCertFingerprintAlgorithm,
)
from ..models.okta_settings_schema_digest_algorithm import (
    OktaSettingsSchemaDigestAlgorithm,
)
from ..models.okta_settings_schema_signature_algorithm import (
    OktaSettingsSchemaSignatureAlgorithm,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OktaSettingsSchema")


@_attrs_define
class OktaSettingsSchema:
    """
    Attributes:
        okta_name (str):
        cert_fingerprint (None | str | Unset):
        cert_fingerprint_algorithm (None | OktaSettingsSchemaCertFingerprintAlgorithm | Unset):
        digest_algorithm (None | OktaSettingsSchemaDigestAlgorithm | Unset):
        domain_name (None | str | Unset):
        idp_x509cert (None | str | Unset):
        okta_app_id (None | str | Unset):
        okta_preview (bool | None | Unset):
        okta_sso (None | str | Unset):
        signature_algorithm (None | OktaSettingsSchemaSignatureAlgorithm | Unset):
    """

    okta_name: str
    cert_fingerprint: None | str | Unset = UNSET
    cert_fingerprint_algorithm: (
        None | OktaSettingsSchemaCertFingerprintAlgorithm | Unset
    ) = UNSET
    digest_algorithm: None | OktaSettingsSchemaDigestAlgorithm | Unset = UNSET
    domain_name: None | str | Unset = UNSET
    idp_x509cert: None | str | Unset = UNSET
    okta_app_id: None | str | Unset = UNSET
    okta_preview: bool | None | Unset = UNSET
    okta_sso: None | str | Unset = UNSET
    signature_algorithm: None | OktaSettingsSchemaSignatureAlgorithm | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        okta_name = self.okta_name

        cert_fingerprint: None | str | Unset
        if isinstance(self.cert_fingerprint, Unset):
            cert_fingerprint = UNSET
        else:
            cert_fingerprint = self.cert_fingerprint

        cert_fingerprint_algorithm: None | str | Unset
        if isinstance(self.cert_fingerprint_algorithm, Unset):
            cert_fingerprint_algorithm = UNSET
        elif isinstance(
            self.cert_fingerprint_algorithm, OktaSettingsSchemaCertFingerprintAlgorithm
        ):
            cert_fingerprint_algorithm = self.cert_fingerprint_algorithm.value
        else:
            cert_fingerprint_algorithm = self.cert_fingerprint_algorithm

        digest_algorithm: None | str | Unset
        if isinstance(self.digest_algorithm, Unset):
            digest_algorithm = UNSET
        elif isinstance(self.digest_algorithm, OktaSettingsSchemaDigestAlgorithm):
            digest_algorithm = self.digest_algorithm.value
        else:
            digest_algorithm = self.digest_algorithm

        domain_name: None | str | Unset
        if isinstance(self.domain_name, Unset):
            domain_name = UNSET
        else:
            domain_name = self.domain_name

        idp_x509cert: None | str | Unset
        if isinstance(self.idp_x509cert, Unset):
            idp_x509cert = UNSET
        else:
            idp_x509cert = self.idp_x509cert

        okta_app_id: None | str | Unset
        if isinstance(self.okta_app_id, Unset):
            okta_app_id = UNSET
        else:
            okta_app_id = self.okta_app_id

        okta_preview: bool | None | Unset
        if isinstance(self.okta_preview, Unset):
            okta_preview = UNSET
        else:
            okta_preview = self.okta_preview

        okta_sso: None | str | Unset
        if isinstance(self.okta_sso, Unset):
            okta_sso = UNSET
        else:
            okta_sso = self.okta_sso

        signature_algorithm: None | str | Unset
        if isinstance(self.signature_algorithm, Unset):
            signature_algorithm = UNSET
        elif isinstance(self.signature_algorithm, OktaSettingsSchemaSignatureAlgorithm):
            signature_algorithm = self.signature_algorithm.value
        else:
            signature_algorithm = self.signature_algorithm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "okta_name": okta_name,
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
        if idp_x509cert is not UNSET:
            field_dict["idp_x509cert"] = idp_x509cert
        if okta_app_id is not UNSET:
            field_dict["okta_app_id"] = okta_app_id
        if okta_preview is not UNSET:
            field_dict["okta_preview"] = okta_preview
        if okta_sso is not UNSET:
            field_dict["okta_sso"] = okta_sso
        if signature_algorithm is not UNSET:
            field_dict["signature_algorithm"] = signature_algorithm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        okta_name = d.pop("okta_name")

        def _parse_cert_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cert_fingerprint = _parse_cert_fingerprint(d.pop("cert_fingerprint", UNSET))

        def _parse_cert_fingerprint_algorithm(
            data: object,
        ) -> None | OktaSettingsSchemaCertFingerprintAlgorithm | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cert_fingerprint_algorithm_type_1 = (
                    OktaSettingsSchemaCertFingerprintAlgorithm(data)
                )

                return cert_fingerprint_algorithm_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OktaSettingsSchemaCertFingerprintAlgorithm | Unset, data)

        cert_fingerprint_algorithm = _parse_cert_fingerprint_algorithm(
            d.pop("cert_fingerprint_algorithm", UNSET)
        )

        def _parse_digest_algorithm(
            data: object,
        ) -> None | OktaSettingsSchemaDigestAlgorithm | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                digest_algorithm_type_1 = OktaSettingsSchemaDigestAlgorithm(data)

                return digest_algorithm_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OktaSettingsSchemaDigestAlgorithm | Unset, data)

        digest_algorithm = _parse_digest_algorithm(d.pop("digest_algorithm", UNSET))

        def _parse_domain_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain_name = _parse_domain_name(d.pop("domain_name", UNSET))

        def _parse_idp_x509cert(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        idp_x509cert = _parse_idp_x509cert(d.pop("idp_x509cert", UNSET))

        def _parse_okta_app_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        okta_app_id = _parse_okta_app_id(d.pop("okta_app_id", UNSET))

        def _parse_okta_preview(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        okta_preview = _parse_okta_preview(d.pop("okta_preview", UNSET))

        def _parse_okta_sso(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        okta_sso = _parse_okta_sso(d.pop("okta_sso", UNSET))

        def _parse_signature_algorithm(
            data: object,
        ) -> None | OktaSettingsSchemaSignatureAlgorithm | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signature_algorithm_type_1 = OktaSettingsSchemaSignatureAlgorithm(data)

                return signature_algorithm_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OktaSettingsSchemaSignatureAlgorithm | Unset, data)

        signature_algorithm = _parse_signature_algorithm(
            d.pop("signature_algorithm", UNSET)
        )

        okta_settings_schema = cls(
            okta_name=okta_name,
            cert_fingerprint=cert_fingerprint,
            cert_fingerprint_algorithm=cert_fingerprint_algorithm,
            digest_algorithm=digest_algorithm,
            domain_name=domain_name,
            idp_x509cert=idp_x509cert,
            okta_app_id=okta_app_id,
            okta_preview=okta_preview,
            okta_sso=okta_sso,
            signature_algorithm=signature_algorithm,
        )

        okta_settings_schema.additional_properties = d
        return okta_settings_schema

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
