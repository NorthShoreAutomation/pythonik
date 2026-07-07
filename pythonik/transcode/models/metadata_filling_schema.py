from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MetadataFillingSchema")


@_attrs_define
class MetadataFillingSchema:
    """
    Attributes:
        field_names (list[str]):
        view_id (UUID):
    """

    field_names: list[str]
    view_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_names = self.field_names

        view_id = str(self.view_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_names": field_names,
                "view_id": view_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_names = cast(list[str], d.pop("field_names"))

        view_id = UUID(d.pop("view_id"))

        metadata_filling_schema = cls(
            field_names=field_names,
            view_id=view_id,
        )

        metadata_filling_schema.additional_properties = d
        return metadata_filling_schema

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
