from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_setting_schema_protocol import (
    NotificationSettingSchemaProtocol,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_setting_schema_settings import (
        NotificationSettingSchemaSettings,
    )


T = TypeVar("T", bound="NotificationSettingSchema")


@_attrs_define
class NotificationSettingSchema:
    """
    Attributes:
        enabled (bool):
        event_type (str):
        object_type (str):
        protocol (NotificationSettingSchemaProtocol | Unset):
        recipient_id (UUID | Unset):
        settings (NotificationSettingSchemaSettings | Unset):
        sub_object_type (str | Unset):
        system_domain_id (UUID | Unset):
    """

    enabled: bool
    event_type: str
    object_type: str
    protocol: NotificationSettingSchemaProtocol | Unset = UNSET
    recipient_id: UUID | Unset = UNSET
    settings: NotificationSettingSchemaSettings | Unset = UNSET
    sub_object_type: str | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        event_type = self.event_type

        object_type = self.object_type

        protocol: str | Unset = UNSET
        if not isinstance(self.protocol, Unset):
            protocol = self.protocol.value

        recipient_id: str | Unset = UNSET
        if not isinstance(self.recipient_id, Unset):
            recipient_id = str(self.recipient_id)

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        sub_object_type = self.sub_object_type

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

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
        from ..models.notification_setting_schema_settings import (
            NotificationSettingSchemaSettings,
        )

        d = dict(src_dict)
        enabled = d.pop("enabled")

        event_type = d.pop("event_type")

        object_type = d.pop("object_type")

        _protocol = d.pop("protocol", UNSET)
        protocol: NotificationSettingSchemaProtocol | Unset
        if isinstance(_protocol, Unset):
            protocol = UNSET
        else:
            protocol = NotificationSettingSchemaProtocol(_protocol)

        _recipient_id = d.pop("recipient_id", UNSET)
        recipient_id: UUID | Unset
        if isinstance(_recipient_id, Unset):
            recipient_id = UNSET
        else:
            recipient_id = UUID(_recipient_id)

        _settings = d.pop("settings", UNSET)
        settings: NotificationSettingSchemaSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = NotificationSettingSchemaSettings.from_dict(_settings)

        sub_object_type = d.pop("sub_object_type", UNSET)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

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
