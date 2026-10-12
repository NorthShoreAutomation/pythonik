from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ai_consent_event_schema_action import AIConsentEventSchemaAction
from ..types import UNSET, Unset

T = TypeVar("T", bound="AIConsentEventSchema")


@_attrs_define
class AIConsentEventSchema:
    """
    Attributes:
        acting_as_user_id (None | Unset | UUID):
        action (AIConsentEventSchemaAction | None | Unset):
        app_id (None | Unset | UUID):
        date_created (datetime.datetime | None | Unset):
        document_id (None | str | Unset):
        document_url (None | str | Unset):
        document_version (None | str | Unset):
        evidence (None | str | Unset):
        id (None | Unset | UUID):
        ip (None | str | Unset):
        origin (None | str | Unset):
        user_email (None | str | Unset):
        user_id (None | Unset | UUID):
    """

    acting_as_user_id: None | Unset | UUID = UNSET
    action: AIConsentEventSchemaAction | None | Unset = UNSET
    app_id: None | Unset | UUID = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    document_id: None | str | Unset = UNSET
    document_url: None | str | Unset = UNSET
    document_version: None | str | Unset = UNSET
    evidence: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    ip: None | str | Unset = UNSET
    origin: None | str | Unset = UNSET
    user_email: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acting_as_user_id: None | str | Unset
        if isinstance(self.acting_as_user_id, Unset):
            acting_as_user_id = UNSET
        elif isinstance(self.acting_as_user_id, UUID):
            acting_as_user_id = str(self.acting_as_user_id)
        else:
            acting_as_user_id = self.acting_as_user_id

        action: None | str | Unset
        if isinstance(self.action, Unset):
            action = UNSET
        elif isinstance(self.action, AIConsentEventSchemaAction):
            action = self.action.value
        else:
            action = self.action

        app_id: None | str | Unset
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        elif isinstance(self.app_id, UUID):
            app_id = str(self.app_id)
        else:
            app_id = self.app_id

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

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

        document_version: None | str | Unset
        if isinstance(self.document_version, Unset):
            document_version = UNSET
        else:
            document_version = self.document_version

        evidence: None | str | Unset
        if isinstance(self.evidence, Unset):
            evidence = UNSET
        else:
            evidence = self.evidence

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        ip: None | str | Unset
        if isinstance(self.ip, Unset):
            ip = UNSET
        else:
            ip = self.ip

        origin: None | str | Unset
        if isinstance(self.origin, Unset):
            origin = UNSET
        else:
            origin = self.origin

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if acting_as_user_id is not UNSET:
            field_dict["acting_as_user_id"] = acting_as_user_id
        if action is not UNSET:
            field_dict["action"] = action
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if document_url is not UNSET:
            field_dict["document_url"] = document_url
        if document_version is not UNSET:
            field_dict["document_version"] = document_version
        if evidence is not UNSET:
            field_dict["evidence"] = evidence
        if id is not UNSET:
            field_dict["id"] = id
        if ip is not UNSET:
            field_dict["ip"] = ip
        if origin is not UNSET:
            field_dict["origin"] = origin
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_acting_as_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acting_as_user_id_type_0 = UUID(data)

                return acting_as_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        acting_as_user_id = _parse_acting_as_user_id(d.pop("acting_as_user_id", UNSET))

        def _parse_action(data: object) -> AIConsentEventSchemaAction | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                action_type_1 = AIConsentEventSchemaAction(data)

                return action_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AIConsentEventSchemaAction | None | Unset, data)

        action = _parse_action(d.pop("action", UNSET))

        def _parse_app_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                app_id_type_0 = UUID(data)

                return app_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        app_id = _parse_app_id(d.pop("app_id", UNSET))

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

        def _parse_document_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        document_version = _parse_document_version(d.pop("document_version", UNSET))

        def _parse_evidence(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        evidence = _parse_evidence(d.pop("evidence", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip = _parse_ip(d.pop("ip", UNSET))

        def _parse_origin(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        ai_consent_event_schema = cls(
            acting_as_user_id=acting_as_user_id,
            action=action,
            app_id=app_id,
            date_created=date_created,
            document_id=document_id,
            document_url=document_url,
            document_version=document_version,
            evidence=evidence,
            id=id,
            ip=ip,
            origin=origin,
            user_email=user_email,
            user_id=user_id,
        )

        ai_consent_event_schema.additional_properties = d
        return ai_consent_event_schema

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
