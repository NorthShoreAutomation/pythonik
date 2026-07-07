from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiscoveryViewSettingsSchema")


@_attrs_define
class DiscoveryViewSettingsSchema:
    """
    Attributes:
        entity_ids (list[UUID]):
        id (UUID | Unset):
        system_domain_id (UUID | Unset):
    """

    entity_ids: list[UUID]
    id: UUID | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entity_ids = []
        for entity_ids_item_data in self.entity_ids:
            entity_ids_item = str(entity_ids_item_data)
            entity_ids.append(entity_ids_item)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entity_ids": entity_ids,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_ids = []
        _entity_ids = d.pop("entity_ids")
        for entity_ids_item_data in _entity_ids:
            entity_ids_item = UUID(entity_ids_item_data)

            entity_ids.append(entity_ids_item)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        discovery_view_settings_schema = cls(
            entity_ids=entity_ids,
            id=id,
            system_domain_id=system_domain_id,
        )

        discovery_view_settings_schema.additional_properties = d
        return discovery_view_settings_schema

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
