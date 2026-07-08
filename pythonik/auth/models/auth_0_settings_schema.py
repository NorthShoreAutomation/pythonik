from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_0_settings_schema_cert_fingerprint_algorithm_type_1 import (
        Auth0SettingsSchemaCertFingerprintAlgorithmType1,
    )
    from ..models.auth_0_settings_schema_digest_algorithm_type_1 import (
        Auth0SettingsSchemaDigestAlgorithmType1,
    )
    from ..models.auth_0_settings_schema_signature_algorithm_type_1 import (
        Auth0SettingsSchemaSignatureAlgorithmType1,
    )


T = TypeVar("T", bound="Auth0SettingsSchema")


@_attrs_define
class Auth0SettingsSchema:
    """
    Attributes:
        auth0_client_id (str):
        auth0_name (str):
        auth0_region (str):
        cert_fingerprint (None | str | Unset):
        cert_fingerprint_algorithm (Auth0SettingsSchemaCertFingerprintAlgorithmType1 | None | Unset):
        digest_algorithm (Auth0SettingsSchemaDigestAlgorithmType1 | None | Unset):
        domain_name (None | str | Unset):
        idp_x509cert (None | str | Unset):
        signature_algorithm (Auth0SettingsSchemaSignatureAlgorithmType1 | None | Unset):
    """

    auth0_client_id: str
    auth0_name: str
    auth0_region: str
    cert_fingerprint: None | str | Unset = UNSET
    cert_fingerprint_algorithm: (
        Auth0SettingsSchemaCertFingerprintAlgorithmType1 | None | Unset
    ) = UNSET
    digest_algorithm: Auth0SettingsSchemaDigestAlgorithmType1 | None | Unset = UNSET
    domain_name: None | str | Unset = UNSET
    idp_x509cert: None | str | Unset = UNSET
    signature_algorithm: Auth0SettingsSchemaSignatureAlgorithmType1 | None | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.auth_0_settings_schema_cert_fingerprint_algorithm_type_1 import (
            Auth0SettingsSchemaCertFingerprintAlgorithmType1,
        )
        from ..models.auth_0_settings_schema_digest_algorithm_type_1 import (
            Auth0SettingsSchemaDigestAlgorithmType1,
        )
        from ..models.auth_0_settings_schema_signature_algorithm_type_1 import (
            Auth0SettingsSchemaSignatureAlgorithmType1,
        )

        auth0_client_id = self.auth0_client_id

        auth0_name = self.auth0_name

        auth0_region = self.auth0_region

        cert_fingerprint: None | str | Unset
        if isinstance(self.cert_fingerprint, Unset):
            cert_fingerprint = UNSET
        else:
            cert_fingerprint = self.cert_fingerprint

        cert_fingerprint_algorithm: dict[str, Any] | None | Unset
        if isinstance(self.cert_fingerprint_algorithm, Unset):
            cert_fingerprint_algorithm = UNSET
        elif isinstance(
            self.cert_fingerprint_algorithm,
            Auth0SettingsSchemaCertFingerprintAlgorithmType1,
        ):
            cert_fingerprint_algorithm = self.cert_fingerprint_algorithm.to_dict()
        else:
            cert_fingerprint_algorithm = self.cert_fingerprint_algorithm

        digest_algorithm: dict[str, Any] | None | Unset
        if isinstance(self.digest_algorithm, Unset):
            digest_algorithm = UNSET
        elif isinstance(self.digest_algorithm, Auth0SettingsSchemaDigestAlgorithmType1):
            digest_algorithm = self.digest_algorithm.to_dict()
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

        signature_algorithm: dict[str, Any] | None | Unset
        if isinstance(self.signature_algorithm, Unset):
            signature_algorithm = UNSET
        elif isinstance(
            self.signature_algorithm, Auth0SettingsSchemaSignatureAlgorithmType1
        ):
            signature_algorithm = self.signature_algorithm.to_dict()
        else:
            signature_algorithm = self.signature_algorithm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "auth0_client_id": auth0_client_id,
                "auth0_name": auth0_name,
                "auth0_region": auth0_region,
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
        if signature_algorithm is not UNSET:
            field_dict["signature_algorithm"] = signature_algorithm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_0_settings_schema_cert_fingerprint_algorithm_type_1 import (
            Auth0SettingsSchemaCertFingerprintAlgorithmType1,
        )
        from ..models.auth_0_settings_schema_digest_algorithm_type_1 import (
            Auth0SettingsSchemaDigestAlgorithmType1,
        )
        from ..models.auth_0_settings_schema_signature_algorithm_type_1 import (
            Auth0SettingsSchemaSignatureAlgorithmType1,
        )

        d = dict(src_dict)
        auth0_client_id = d.pop("auth0_client_id")

        auth0_name = d.pop("auth0_name")

        auth0_region = d.pop("auth0_region")

        def _parse_cert_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cert_fingerprint = _parse_cert_fingerprint(d.pop("cert_fingerprint", UNSET))

        def _parse_cert_fingerprint_algorithm(
            data: object,
        ) -> Auth0SettingsSchemaCertFingerprintAlgorithmType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cert_fingerprint_algorithm_type_1 = (
                    Auth0SettingsSchemaCertFingerprintAlgorithmType1.from_dict(data)
                )

                return cert_fingerprint_algorithm_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                Auth0SettingsSchemaCertFingerprintAlgorithmType1 | None | Unset, data
            )

        cert_fingerprint_algorithm = _parse_cert_fingerprint_algorithm(
            d.pop("cert_fingerprint_algorithm", UNSET)
        )

        def _parse_digest_algorithm(
            data: object,
        ) -> Auth0SettingsSchemaDigestAlgorithmType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                digest_algorithm_type_1 = (
                    Auth0SettingsSchemaDigestAlgorithmType1.from_dict(data)
                )

                return digest_algorithm_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Auth0SettingsSchemaDigestAlgorithmType1 | None | Unset, data)

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

        def _parse_signature_algorithm(
            data: object,
        ) -> Auth0SettingsSchemaSignatureAlgorithmType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                signature_algorithm_type_1 = (
                    Auth0SettingsSchemaSignatureAlgorithmType1.from_dict(data)
                )

                return signature_algorithm_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Auth0SettingsSchemaSignatureAlgorithmType1 | None | Unset, data)

        signature_algorithm = _parse_signature_algorithm(
            d.pop("signature_algorithm", UNSET)
        )

        auth_0_settings_schema = cls(
            auth0_client_id=auth0_client_id,
            auth0_name=auth0_name,
            auth0_region=auth0_region,
            cert_fingerprint=cert_fingerprint,
            cert_fingerprint_algorithm=cert_fingerprint_algorithm,
            digest_algorithm=digest_algorithm,
            domain_name=domain_name,
            idp_x509cert=idp_x509cert,
            signature_algorithm=signature_algorithm,
        )

        auth_0_settings_schema.additional_properties = d
        return auth_0_settings_schema

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
