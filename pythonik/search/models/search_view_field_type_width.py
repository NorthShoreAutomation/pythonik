from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchViewFieldTypeWidth")


@_attrs_define
class SearchViewFieldTypeWidth:
    """
    Attributes:
        auto_resize (bool | None | Unset):
        current (int | None | Unset):
        fixed (int | None | Unset):
        max_ (int | None | Unset):
        min_ (int | None | Unset):
    """

    auto_resize: bool | None | Unset = UNSET
    current: int | None | Unset = UNSET
    fixed: int | None | Unset = UNSET
    max_: int | None | Unset = UNSET
    min_: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_resize: bool | None | Unset
        if isinstance(self.auto_resize, Unset):
            auto_resize = UNSET
        else:
            auto_resize = self.auto_resize

        current: int | None | Unset
        if isinstance(self.current, Unset):
            current = UNSET
        else:
            current = self.current

        fixed: int | None | Unset
        if isinstance(self.fixed, Unset):
            fixed = UNSET
        else:
            fixed = self.fixed

        max_: int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        min_: int | None | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
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

        def _parse_auto_resize(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_resize = _parse_auto_resize(d.pop("auto_resize", UNSET))

        def _parse_current(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        current = _parse_current(d.pop("current", UNSET))

        def _parse_fixed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        fixed = _parse_fixed(d.pop("fixed", UNSET))

        def _parse_max_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        def _parse_min_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))

        search_view_field_type_width = cls(
            auto_resize=auto_resize,
            current=current,
            fixed=fixed,
            max_=max_,
            min_=min_,
        )

        search_view_field_type_width.additional_properties = d
        return search_view_field_type_width

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
