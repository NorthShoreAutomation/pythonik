from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.automation_stats_object_schema_type import AutomationStatsObjectSchemaType

T = TypeVar("T", bound="AutomationStatsObjectSchema")


@_attrs_define
class AutomationStatsObjectSchema:
    """
    Attributes:
        name (str):
        system_domain_id (UUID):
        type_ (AutomationStatsObjectSchemaType):
        value (int):
    """

    name: str
    system_domain_id: UUID
    type_: AutomationStatsObjectSchemaType
    value: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        system_domain_id = str(self.system_domain_id)

        type_ = self.type_.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "system_domain_id": system_domain_id,
                "type": type_,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        system_domain_id = UUID(d.pop("system_domain_id"))

        type_ = AutomationStatsObjectSchemaType(d.pop("type"))

        value = d.pop("value")

        automation_stats_object_schema = cls(
            name=name,
            system_domain_id=system_domain_id,
            type_=type_,
            value=value,
        )

        automation_stats_object_schema.additional_properties = d
        return automation_stats_object_schema

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
