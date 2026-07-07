from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.watermark_options_type_show_for_groups import (
    WatermarkOptionsTypeShowForGroups,
)
from ..models.watermark_options_type_show_in_context import (
    WatermarkOptionsTypeShowInContext,
)
from ..models.watermark_options_type_text_appearance import (
    WatermarkOptionsTypeTextAppearance,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="WatermarkOptionsType")


@_attrs_define
class WatermarkOptionsType:
    """
    Attributes:
        custom_text (str | Unset):
        groups (list[UUID] | None | Unset):
        include_custom_text (bool | Unset):
        include_date_time (bool | Unset):
        include_email (bool | Unset):
        include_ip_address (bool | Unset):
        shadow_opacity (float | Unset):
        show_for_groups (WatermarkOptionsTypeShowForGroups | Unset):
        show_in_context (WatermarkOptionsTypeShowInContext | Unset):
        show_watermark (bool | Unset):
        text_appearance (WatermarkOptionsTypeTextAppearance | Unset):
        text_opacity (float | Unset):
    """

    custom_text: str | Unset = UNSET
    groups: list[UUID] | None | Unset = UNSET
    include_custom_text: bool | Unset = UNSET
    include_date_time: bool | Unset = UNSET
    include_email: bool | Unset = UNSET
    include_ip_address: bool | Unset = UNSET
    shadow_opacity: float | Unset = UNSET
    show_for_groups: WatermarkOptionsTypeShowForGroups | Unset = UNSET
    show_in_context: WatermarkOptionsTypeShowInContext | Unset = UNSET
    show_watermark: bool | Unset = UNSET
    text_appearance: WatermarkOptionsTypeTextAppearance | Unset = UNSET
    text_opacity: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_text = self.custom_text

        groups: list[str] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = []
            for groups_type_0_item_data in self.groups:
                groups_type_0_item = str(groups_type_0_item_data)
                groups.append(groups_type_0_item)

        else:
            groups = self.groups

        include_custom_text = self.include_custom_text

        include_date_time = self.include_date_time

        include_email = self.include_email

        include_ip_address = self.include_ip_address

        shadow_opacity = self.shadow_opacity

        show_for_groups: str | Unset = UNSET
        if not isinstance(self.show_for_groups, Unset):
            show_for_groups = self.show_for_groups.value

        show_in_context: str | Unset = UNSET
        if not isinstance(self.show_in_context, Unset):
            show_in_context = self.show_in_context.value

        show_watermark = self.show_watermark

        text_appearance: str | Unset = UNSET
        if not isinstance(self.text_appearance, Unset):
            text_appearance = self.text_appearance.value

        text_opacity = self.text_opacity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_text is not UNSET:
            field_dict["custom_text"] = custom_text
        if groups is not UNSET:
            field_dict["groups"] = groups
        if include_custom_text is not UNSET:
            field_dict["include_custom_text"] = include_custom_text
        if include_date_time is not UNSET:
            field_dict["include_date_time"] = include_date_time
        if include_email is not UNSET:
            field_dict["include_email"] = include_email
        if include_ip_address is not UNSET:
            field_dict["include_ip_address"] = include_ip_address
        if shadow_opacity is not UNSET:
            field_dict["shadow_opacity"] = shadow_opacity
        if show_for_groups is not UNSET:
            field_dict["show_for_groups"] = show_for_groups
        if show_in_context is not UNSET:
            field_dict["show_in_context"] = show_in_context
        if show_watermark is not UNSET:
            field_dict["show_watermark"] = show_watermark
        if text_appearance is not UNSET:
            field_dict["text_appearance"] = text_appearance
        if text_opacity is not UNSET:
            field_dict["text_opacity"] = text_opacity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_text = d.pop("custom_text", UNSET)

        def _parse_groups(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = []
                _groups_type_0 = data
                for groups_type_0_item_data in _groups_type_0:
                    groups_type_0_item = UUID(groups_type_0_item_data)

                    groups_type_0.append(groups_type_0_item)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))

        include_custom_text = d.pop("include_custom_text", UNSET)

        include_date_time = d.pop("include_date_time", UNSET)

        include_email = d.pop("include_email", UNSET)

        include_ip_address = d.pop("include_ip_address", UNSET)

        shadow_opacity = d.pop("shadow_opacity", UNSET)

        _show_for_groups = d.pop("show_for_groups", UNSET)
        show_for_groups: WatermarkOptionsTypeShowForGroups | Unset
        if isinstance(_show_for_groups, Unset):
            show_for_groups = UNSET
        else:
            show_for_groups = WatermarkOptionsTypeShowForGroups(_show_for_groups)

        _show_in_context = d.pop("show_in_context", UNSET)
        show_in_context: WatermarkOptionsTypeShowInContext | Unset
        if isinstance(_show_in_context, Unset):
            show_in_context = UNSET
        else:
            show_in_context = WatermarkOptionsTypeShowInContext(_show_in_context)

        show_watermark = d.pop("show_watermark", UNSET)

        _text_appearance = d.pop("text_appearance", UNSET)
        text_appearance: WatermarkOptionsTypeTextAppearance | Unset
        if isinstance(_text_appearance, Unset):
            text_appearance = UNSET
        else:
            text_appearance = WatermarkOptionsTypeTextAppearance(_text_appearance)

        text_opacity = d.pop("text_opacity", UNSET)

        watermark_options_type = cls(
            custom_text=custom_text,
            groups=groups,
            include_custom_text=include_custom_text,
            include_date_time=include_date_time,
            include_email=include_email,
            include_ip_address=include_ip_address,
            shadow_opacity=shadow_opacity,
            show_for_groups=show_for_groups,
            show_in_context=show_in_context,
            show_watermark=show_watermark,
            text_appearance=text_appearance,
            text_opacity=text_opacity,
        )

        watermark_options_type.additional_properties = d
        return watermark_options_type

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
