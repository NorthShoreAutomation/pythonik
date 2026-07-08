from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_setting_schema_protocol import (
    NotificationSettingSchemaProtocol,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_setting_schema_settings_type_0 import (
        NotificationSettingSchemaSettingsType0,
    )


T = TypeVar("T", bound="NotificationSettingSchema")


@_attrs_define
class NotificationSettingSchema:
    """
    Attributes:
        enabled (bool):
        event_type (str):
        object_type (str):
        protocol (None | NotificationSettingSchemaProtocol | Unset):
        recipient_id (None | Unset | UUID):
        settings (None | NotificationSettingSchemaSettingsType0 | Unset):
        sub_object_type (None | str | Unset):
        system_domain_id (None | Unset | UUID):
    """

    enabled: bool
    event_type: str
    object_type: str
    protocol: None | NotificationSettingSchemaProtocol | Unset = UNSET
    recipient_id: None | Unset | UUID = UNSET
    settings: None | NotificationSettingSchemaSettingsType0 | Unset = UNSET
    sub_object_type: None | str | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.notification_setting_schema_settings_type_0 import (
            NotificationSettingSchemaSettingsType0,
        )

        enabled = self.enabled

        event_type = self.event_type

        object_type = self.object_type

        protocol: None | str | Unset
        if isinstance(self.protocol, Unset):
            protocol = UNSET
        elif isinstance(self.protocol, NotificationSettingSchemaProtocol):
            protocol = self.protocol.value
        else:
            protocol = self.protocol

        recipient_id: None | str | Unset
        if isinstance(self.recipient_id, Unset):
            recipient_id = UNSET
        elif isinstance(self.recipient_id, UUID):
            recipient_id = str(self.recipient_id)
        else:
            recipient_id = self.recipient_id

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, NotificationSettingSchemaSettingsType0):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        sub_object_type: None | str | Unset
        if isinstance(self.sub_object_type, Unset):
            sub_object_type = UNSET
        else:
            sub_object_type = self.sub_object_type

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "event_type": event_type,
                "object_type": object_type,
            }
        )
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if recipient_id is not UNSET:
            field_dict["recipient_id"] = recipient_id
        if settings is not UNSET:
            field_dict["settings"] = settings
        if sub_object_type is not UNSET:
            field_dict["sub_object_type"] = sub_object_type
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_setting_schema_settings_type_0 import (
            NotificationSettingSchemaSettingsType0,
        )

        d = dict(src_dict)
        enabled = d.pop("enabled")

        event_type = d.pop("event_type")

        object_type = d.pop("object_type")

        def _parse_protocol(
            data: object,
        ) -> None | NotificationSettingSchemaProtocol | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                protocol_type_1 = NotificationSettingSchemaProtocol(data)

                return protocol_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NotificationSettingSchemaProtocol | Unset, data)

        protocol = _parse_protocol(d.pop("protocol", UNSET))

        def _parse_recipient_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recipient_id_type_0 = UUID(data)

                return recipient_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        recipient_id = _parse_recipient_id(d.pop("recipient_id", UNSET))

        def _parse_settings(
            data: object,
        ) -> None | NotificationSettingSchemaSettingsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = NotificationSettingSchemaSettingsType0.from_dict(data)

                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | NotificationSettingSchemaSettingsType0 | Unset, data)

        settings = _parse_settings(d.pop("settings", UNSET))

        def _parse_sub_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_object_type = _parse_sub_object_type(d.pop("sub_object_type", UNSET))

        def _parse_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_id_type_0 = UUID(data)

                return system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

        notification_setting_schema = cls(
            enabled=enabled,
            event_type=event_type,
            object_type=object_type,
            protocol=protocol,
            recipient_id=recipient_id,
            settings=settings,
            sub_object_type=sub_object_type,
            system_domain_id=system_domain_id,
        )

        notification_setting_schema.additional_properties = d
        return notification_setting_schema

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
