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
        value_in (list[str] | None | Unset):
    """

    name: str
    value_in: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value_in: list[str] | None | Unset
        if isinstance(self.value_in, Unset):
            value_in = UNSET
        elif isinstance(self.value_in, list):
            value_in = self.value_in

        else:
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

        def _parse_value_in(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                value_in_type_0 = cast(list[str], data)

                return value_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        value_in = _parse_value_in(d.pop("value_in", UNSET))

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
