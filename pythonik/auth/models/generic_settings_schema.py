from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

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
        cert_fingerprint (None | str | Unset):
        cert_fingerprint_algorithm (GenericSettingsSchemaCertFingerprintAlgorithm | None | Unset):
        digest_algorithm (GenericSettingsSchemaDigestAlgorithm | None | Unset):
        domain_name (None | str | Unset):
        idp_sls_redirect_url (None | str | Unset):
        idp_x509cert (None | str | Unset):
        name_id_encrypted (bool | None | Unset):
        signature_algorithm (GenericSettingsSchemaSignatureAlgorithm | None | Unset):
        want_assertions_signed (bool | None | Unset):
        want_messages_signed (bool | None | Unset):
    """

    idp_entity_id: str
    idp_sso_post_url: str
    name: str
    cert_fingerprint: None | str | Unset = UNSET
    cert_fingerprint_algorithm: (
        GenericSettingsSchemaCertFingerprintAlgorithm | None | Unset
    ) = UNSET
    digest_algorithm: GenericSettingsSchemaDigestAlgorithm | None | Unset = UNSET
    domain_name: None | str | Unset = UNSET
    idp_sls_redirect_url: None | str | Unset = UNSET
    idp_x509cert: None | str | Unset = UNSET
    name_id_encrypted: bool | None | Unset = UNSET
    signature_algorithm: GenericSettingsSchemaSignatureAlgorithm | None | Unset = UNSET
    want_assertions_signed: bool | None | Unset = UNSET
    want_messages_signed: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idp_entity_id = self.idp_entity_id

        idp_sso_post_url = self.idp_sso_post_url

        name = self.name

        cert_fingerprint: None | str | Unset
        if isinstance(self.cert_fingerprint, Unset):
            cert_fingerprint = UNSET
        else:
            cert_fingerprint = self.cert_fingerprint

        cert_fingerprint_algorithm: None | str | Unset
        if isinstance(self.cert_fingerprint_algorithm, Unset):
            cert_fingerprint_algorithm = UNSET
        elif isinstance(
            self.cert_fingerprint_algorithm,
            GenericSettingsSchemaCertFingerprintAlgorithm,
        ):
            cert_fingerprint_algorithm = self.cert_fingerprint_algorithm.value
        else:
            cert_fingerprint_algorithm = self.cert_fingerprint_algorithm

        digest_algorithm: None | str | Unset
        if isinstance(self.digest_algorithm, Unset):
            digest_algorithm = UNSET
        elif isinstance(self.digest_algorithm, GenericSettingsSchemaDigestAlgorithm):
            digest_algorithm = self.digest_algorithm.value
        else:
            digest_algorithm = self.digest_algorithm

        domain_name: None | str | Unset
        if isinstance(self.domain_name, Unset):
            domain_name = UNSET
        else:
            domain_name = self.domain_name

        idp_sls_redirect_url: None | str | Unset
        if isinstance(self.idp_sls_redirect_url, Unset):
            idp_sls_redirect_url = UNSET
        else:
            idp_sls_redirect_url = self.idp_sls_redirect_url

        idp_x509cert: None | str | Unset
        if isinstance(self.idp_x509cert, Unset):
            idp_x509cert = UNSET
        else:
            idp_x509cert = self.idp_x509cert

        name_id_encrypted: bool | None | Unset
        if isinstance(self.name_id_encrypted, Unset):
            name_id_encrypted = UNSET
        else:
            name_id_encrypted = self.name_id_encrypted

        signature_algorithm: None | str | Unset
        if isinstance(self.signature_algorithm, Unset):
            signature_algorithm = UNSET
        elif isinstance(
            self.signature_algorithm, GenericSettingsSchemaSignatureAlgorithm
        ):
            signature_algorithm = self.signature_algorithm.value
        else:
            signature_algorithm = self.signature_algorithm

        want_assertions_signed: bool | None | Unset
        if isinstance(self.want_assertions_signed, Unset):
            want_assertions_signed = UNSET
        else:
            want_assertions_signed = self.want_assertions_signed

        want_messages_signed: bool | None | Unset
        if isinstance(self.want_messages_signed, Unset):
            want_messages_signed = UNSET
        else:
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

        def _parse_cert_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cert_fingerprint = _parse_cert_fingerprint(d.pop("cert_fingerprint", UNSET))

        def _parse_cert_fingerprint_algorithm(
            data: object,
        ) -> GenericSettingsSchemaCertFingerprintAlgorithm | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cert_fingerprint_algorithm_type_1 = (
                    GenericSettingsSchemaCertFingerprintAlgorithm(data)
                )

                return cert_fingerprint_algorithm_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                GenericSettingsSchemaCertFingerprintAlgorithm | None | Unset, data
            )

        cert_fingerprint_algorithm = _parse_cert_fingerprint_algorithm(
            d.pop("cert_fingerprint_algorithm", UNSET)
        )

        def _parse_digest_algorithm(
            data: object,
        ) -> GenericSettingsSchemaDigestAlgorithm | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                digest_algorithm_type_1 = GenericSettingsSchemaDigestAlgorithm(data)

                return digest_algorithm_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GenericSettingsSchemaDigestAlgorithm | None | Unset, data)

        digest_algorithm = _parse_digest_algorithm(d.pop("digest_algorithm", UNSET))

        def _parse_domain_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        domain_name = _parse_domain_name(d.pop("domain_name", UNSET))

        def _parse_idp_sls_redirect_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        idp_sls_redirect_url = _parse_idp_sls_redirect_url(
            d.pop("idp_sls_redirect_url", UNSET)
        )

        def _parse_idp_x509cert(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        idp_x509cert = _parse_idp_x509cert(d.pop("idp_x509cert", UNSET))

        def _parse_name_id_encrypted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        name_id_encrypted = _parse_name_id_encrypted(d.pop("name_id_encrypted", UNSET))

        def _parse_signature_algorithm(
            data: object,
        ) -> GenericSettingsSchemaSignatureAlgorithm | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                signature_algorithm_type_1 = GenericSettingsSchemaSignatureAlgorithm(
                    data
                )

                return signature_algorithm_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GenericSettingsSchemaSignatureAlgorithm | None | Unset, data)

        signature_algorithm = _parse_signature_algorithm(
            d.pop("signature_algorithm", UNSET)
        )

        def _parse_want_assertions_signed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        want_assertions_signed = _parse_want_assertions_signed(
            d.pop("want_assertions_signed", UNSET)
        )

        def _parse_want_messages_signed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        want_messages_signed = _parse_want_messages_signed(
            d.pop("want_messages_signed", UNSET)
        )

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
