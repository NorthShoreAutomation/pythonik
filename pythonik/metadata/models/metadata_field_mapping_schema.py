from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataFieldMappingSchema")


@_attrs_define
class MetadataFieldMappingSchema:
    """
    Attributes:
        mapped_field_name (str):
        name (str):
        field_type (None | str | Unset):
    """

    mapped_field_name: str
    name: str
    field_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mapped_field_name = self.mapped_field_name

        name = self.name

        field_type: None | str | Unset
        if isinstance(self.field_type, Unset):
            field_type = UNSET
        else:
            field_type = self.field_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mapped_field_name": mapped_field_name,
                "name": name,
            }
        )
        if field_type is not UNSET:
            field_dict["field_type"] = field_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mapped_field_name = d.pop("mapped_field_name")

        name = d.pop("name")

        def _parse_field_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field_type = _parse_field_type(d.pop("field_type", UNSET))

        metadata_field_mapping_schema = cls(
            mapped_field_name=mapped_field_name,
            name=name,
            field_type=field_type,
        )

        metadata_field_mapping_schema.additional_properties = d
        return metadata_field_mapping_schema

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
