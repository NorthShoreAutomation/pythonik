from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThemeTypographySchema")


@_attrs_define
class ThemeTypographySchema:
    """
    Attributes:
        font_family (None | str | Unset):
        font_size_base (None | str | Unset):
        heading_font_family (None | str | Unset):
    """

    font_family: None | str | Unset = UNSET
    font_size_base: None | str | Unset = UNSET
    heading_font_family: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        font_family: None | str | Unset
        if isinstance(self.font_family, Unset):
            font_family = UNSET
        else:
            font_family = self.font_family

        font_size_base: None | str | Unset
        if isinstance(self.font_size_base, Unset):
            font_size_base = UNSET
        else:
            font_size_base = self.font_size_base

        heading_font_family: None | str | Unset
        if isinstance(self.heading_font_family, Unset):
            heading_font_family = UNSET
        else:
            heading_font_family = self.heading_font_family

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if font_family is not UNSET:
            field_dict["font_family"] = font_family
        if font_size_base is not UNSET:
            field_dict["font_size_base"] = font_size_base
        if heading_font_family is not UNSET:
            field_dict["heading_font_family"] = heading_font_family

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_font_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        font_family = _parse_font_family(d.pop("font_family", UNSET))

        def _parse_font_size_base(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        font_size_base = _parse_font_size_base(d.pop("font_size_base", UNSET))

        def _parse_heading_font_family(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        heading_font_family = _parse_heading_font_family(
            d.pop("heading_font_family", UNSET)
        )

        theme_typography_schema = cls(
            font_family=font_family,
            font_size_base=font_size_base,
            heading_font_family=heading_font_family,
        )

        theme_typography_schema.additional_properties = d
        return theme_typography_schema

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
