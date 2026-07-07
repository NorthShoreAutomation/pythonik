from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FacetFilterSchema")


@_attrs_define
class FacetFilterSchema:
    """
    Attributes:
        name (str):
        value_in (list[str] | Unset):
    """

    name: str
    value_in: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value_in: list[str] | Unset = UNSET
        if not isinstance(self.value_in, Unset):
            value_in = self.value_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if value_in is not UNSET:
            field_dict["value_in"] = value_in

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value_in = cast(list[str], d.pop("value_in", UNSET))

        facet_filter_schema = cls(
            name=name,
            value_in=value_in,
        )

        facet_filter_schema.additional_properties = d
        return facet_filter_schema

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
