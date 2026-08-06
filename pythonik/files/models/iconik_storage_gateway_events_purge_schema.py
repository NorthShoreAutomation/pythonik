from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="IconikStorageGatewayEventsPurgeSchema")


@_attrs_define
class IconikStorageGatewayEventsPurgeSchema:
    """
    Attributes:
        event_ids (list[UUID]):
    """

    event_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_ids = []
        for event_ids_item_data in self.event_ids:
            event_ids_item = str(event_ids_item_data)
            event_ids.append(event_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_ids": event_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_ids = []
        _event_ids = d.pop("event_ids")
        for event_ids_item_data in _event_ids:
            event_ids_item = UUID(event_ids_item_data)

            event_ids.append(event_ids_item)

        iconik_storage_gateway_events_purge_schema = cls(
            event_ids=event_ids,
        )

        iconik_storage_gateway_events_purge_schema.additional_properties = d
        return iconik_storage_gateway_events_purge_schema

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
