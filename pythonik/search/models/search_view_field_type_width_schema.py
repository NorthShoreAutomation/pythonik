from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchViewFieldTypeWidthSchema")


@_attrs_define
class SearchViewFieldTypeWidthSchema:
    """
    Attributes:
        auto_resize (bool | Unset):
        current (int | Unset):
        fixed (int | Unset):
        max_ (int | Unset):
        min_ (int | Unset):
    """

    auto_resize: bool | Unset = UNSET
    current: int | Unset = UNSET
    fixed: int | Unset = UNSET
    max_: int | Unset = UNSET
    min_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_resize = self.auto_resize

        current = self.current

        fixed = self.fixed

        max_ = self.max_

        min_ = self.min_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_resize is not UNSET:
            field_dict["auto_resize"] = auto_resize
        if current is not UNSET:
            field_dict["current"] = current
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        auto_resize = d.pop("auto_resize", UNSET)

        current = d.pop("current", UNSET)

        fixed = d.pop("fixed", UNSET)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        search_view_field_type_width_schema = cls(
            auto_resize=auto_resize,
            current=current,
            fixed=fixed,
            max_=max_,
            min_=min_,
        )

        search_view_field_type_width_schema.additional_properties = d
        return search_view_field_type_width_schema

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
