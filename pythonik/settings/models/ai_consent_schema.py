from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_consent_schema_origin import AIConsentSchemaOrigin
from ..models.ai_consent_schema_status import AIConsentSchemaStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIConsentSchema")


@_attrs_define
class AIConsentSchema:
    """
    Attributes:
        date_created (datetime.datetime | None | Unset):
        date_revoked (datetime.datetime | None | Unset):
        document_id (None | str | Unset):
        document_url (None | str | Unset):
        evidence (None | str | Unset):
        origin (AIConsentSchemaOrigin | None | Unset):
        status (AIConsentSchemaStatus | None | Unset):
        version (None | str | Unset):
    """

    date_created: datetime.datetime | None | Unset = UNSET
    date_revoked: datetime.datetime | None | Unset = UNSET
    document_id: None | str | Unset = UNSET
    document_url: None | str | Unset = UNSET
    evidence: None | str | Unset = UNSET
    origin: AIConsentSchemaOrigin | None | Unset = UNSET
    status: AIConsentSchemaStatus | None | Unset = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_revoked: None | str | Unset
        if isinstance(self.date_revoked, Unset):
            date_revoked = UNSET
        elif isinstance(self.date_revoked, datetime.datetime):
            date_revoked = self.date_revoked.isoformat()
        else:
            date_revoked = self.date_revoked

        document_id: None | str | Unset
        if isinstance(self.document_id, Unset):
            document_id = UNSET
        else:
            document_id = self.document_id

        document_url: None | str | Unset
        if isinstance(self.document_url, Unset):
            document_url = UNSET
        else:
            document_url = self.document_url

        evidence: None | str | Unset
        if isinstance(self.evidence, Unset):
            evidence = UNSET
        else:
            evidence = self.evidence

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        elif isinstance(self.origin, AIConsentSchemaOrigin):
            origin = self.origin.value
        else:
            origin = self.origin

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, AIConsentSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_revoked is not UNSET:
            field_dict["date_revoked"] = date_revoked
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if document_url is not UNSET:
            field_dict["document_url"] = document_url
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if origin is not UNSET:
            field_dict["origin"] = origin
        if status is not UNSET:
            field_dict["status"] = status
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_revoked(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_revoked_type_0 = datetime.datetime.fromisoformat(data)

                return date_revoked_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_revoked = _parse_date_revoked(d.pop("date_revoked", UNSET))

        def _parse_document_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_id = _parse_document_id(d.pop("document_id", UNSET))

        def _parse_document_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_url = _parse_document_url(d.pop("document_url", UNSET))

        def _parse_evidence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        evidence = _parse_evidence(d.pop("evidence", UNSET))

        def _parse_origin(data: object) -> AIConsentSchemaOrigin | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_1 = AIConsentSchemaOrigin(data)

                return origin_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AIConsentSchemaOrigin | None | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        def _parse_status(data: object) -> AIConsentSchemaStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = AIConsentSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AIConsentSchemaStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        ai_consent_schema = cls(
            date_created=date_created,
            date_revoked=date_revoked,
            document_id=document_id,
            document_url=document_url,
            evidence=evidence,
            origin=origin,
            status=status,
            version=version,
        )

        ai_consent_schema.additional_properties = d
        return ai_consent_schema

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
