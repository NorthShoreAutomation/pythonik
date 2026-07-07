from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataFieldMappingUpdateSchema")


@_attrs_define
class MetadataFieldMappingUpdateSchema:
    """
    Attributes:
        mapped_field_name (str):
        field_type (str | Unset):
        name (str | Unset):
    """

    mapped_field_name: str
    field_type: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mapped_field_name = self.mapped_field_name

        field_type = self.field_type

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mapped_field_name": mapped_field_name,
            }
        )
        if field_type is not UNSET:
            field_dict["field_type"] = field_type
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mapped_field_name = d.pop("mapped_field_name")

        field_type = d.pop("field_type", UNSET)

        name = d.pop("name", UNSET)

        metadata_field_mapping_update_schema = cls(
            mapped_field_name=mapped_field_name,
            field_type=field_type,
            name=name,
        )

        metadata_field_mapping_update_schema.additional_properties = d
        return metadata_field_mapping_update_schema

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
