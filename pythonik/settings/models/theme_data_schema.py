from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.theme_data_schema_base import ThemeDataSchemaBase
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.theme_colors_schema import ThemeColorsSchema
    from ..models.theme_typography import ThemeTypography


T = TypeVar("T", bound="ThemeDataSchema")


@_attrs_define
class ThemeDataSchema:
    """
    Attributes:
        base (None | ThemeDataSchemaBase | Unset):
        colors (None | ThemeColorsSchema | Unset):
        typography (None | ThemeTypography | Unset):
    """

    base: None | ThemeDataSchemaBase | Unset = UNSET
    colors: None | ThemeColorsSchema | Unset = UNSET
    typography: None | ThemeTypography | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.theme_colors_schema import ThemeColorsSchema
        from ..models.theme_typography import ThemeTypography

        base: None | str | Unset
        if isinstance(self.base, Unset):
            base = UNSET
        elif isinstance(self.base, ThemeDataSchemaBase):
            base = self.base.value
        else:
            base = self.base

        colors: dict[str, Any] | None | Unset
        if isinstance(self.colors, Unset):
            colors = UNSET
        elif isinstance(self.colors, ThemeColorsSchema):
            colors = self.colors.to_dict()
        else:
            colors = self.colors

        typography: dict[str, Any] | None | Unset
        if isinstance(self.typography, Unset):
            typography = UNSET
        elif isinstance(self.typography, ThemeTypography):
            typography = self.typography.to_dict()
        else:
            typography = self.typography

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base is not UNSET:
            field_dict["base"] = base
        if colors is not UNSET:
            field_dict["colors"] = colors
        if typography is not UNSET:
            field_dict["typography"] = typography

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.theme_colors_schema import ThemeColorsSchema
        from ..models.theme_typography import ThemeTypography

        d = dict(src_dict)

        def _parse_base(data: object) -> None | ThemeDataSchemaBase | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                base_type_1 = ThemeDataSchemaBase(data)

                return base_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ThemeDataSchemaBase | Unset, data)

        base = _parse_base(d.pop("base", UNSET))

        def _parse_colors(data: object) -> None | ThemeColorsSchema | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                colors_type_1 = ThemeColorsSchema.from_dict(data)

                return colors_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ThemeColorsSchema | Unset, data)

        colors = _parse_colors(d.pop("colors", UNSET))

        def _parse_typography(data: object) -> None | ThemeTypography | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                typography_type_1 = ThemeTypography.from_dict(data)

                return typography_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ThemeTypography | Unset, data)

        typography = _parse_typography(d.pop("typography", UNSET))

        theme_data_schema = cls(
            base=base,
            colors=colors,
            typography=typography,
        )

        theme_data_schema.additional_properties = d
        return theme_data_schema

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
