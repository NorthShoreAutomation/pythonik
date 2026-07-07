from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageMagickSettingsSchema")


@_attrs_define
class ImageMagickSettingsSchema:
    """
    Attributes:
        data (str | Unset):
        exclude_patterns (list[str] | Unset):
        height (int | Unset):
        include_patterns (list[str] | Unset):
        local (bool | Unset):
        overlay_coordinates (None | str | Unset):
        overlay_url (None | str | Unset):
        priority (int | None | Unset):
        width (int | Unset):
    """

    data: str | Unset = UNSET
    exclude_patterns: list[str] | Unset = UNSET
    height: int | Unset = UNSET
    include_patterns: list[str] | Unset = UNSET
    local: bool | Unset = UNSET
    overlay_coordinates: None | str | Unset = UNSET
    overlay_url: None | str | Unset = UNSET
    priority: int | None | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        exclude_patterns: list[str] | Unset = UNSET
        if not isinstance(self.exclude_patterns, Unset):
            exclude_patterns = self.exclude_patterns

        height = self.height

        include_patterns: list[str] | Unset = UNSET
        if not isinstance(self.include_patterns, Unset):
            include_patterns = self.include_patterns

        local = self.local

        overlay_coordinates: None | str | Unset
        if isinstance(self.overlay_coordinates, Unset):
            overlay_coordinates = UNSET
        else:
            overlay_coordinates = self.overlay_coordinates

        overlay_url: None | str | Unset
        if isinstance(self.overlay_url, Unset):
            overlay_url = UNSET
        else:
            overlay_url = self.overlay_url

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if exclude_patterns is not UNSET:
            field_dict["exclude_patterns"] = exclude_patterns
        if height is not UNSET:
            field_dict["height"] = height
        if include_patterns is not UNSET:
            field_dict["include_patterns"] = include_patterns
        if local is not UNSET:
            field_dict["local"] = local
        if overlay_coordinates is not UNSET:
            field_dict["overlay_coordinates"] = overlay_coordinates
        if overlay_url is not UNSET:
            field_dict["overlay_url"] = overlay_url
        if priority is not UNSET:
            field_dict["priority"] = priority
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = d.pop("data", UNSET)

        exclude_patterns = cast(list[str], d.pop("exclude_patterns", UNSET))

        height = d.pop("height", UNSET)

        include_patterns = cast(list[str], d.pop("include_patterns", UNSET))

        local = d.pop("local", UNSET)

        def _parse_overlay_coordinates(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overlay_coordinates = _parse_overlay_coordinates(
            d.pop("overlay_coordinates", UNSET)
        )

        def _parse_overlay_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        overlay_url = _parse_overlay_url(d.pop("overlay_url", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        width = d.pop("width", UNSET)

        image_magick_settings_schema = cls(
            data=data,
            exclude_patterns=exclude_patterns,
            height=height,
            include_patterns=include_patterns,
            local=local,
            overlay_coordinates=overlay_coordinates,
            overlay_url=overlay_url,
            priority=priority,
            width=width,
        )

        image_magick_settings_schema.additional_properties = d
        return image_magick_settings_schema

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
