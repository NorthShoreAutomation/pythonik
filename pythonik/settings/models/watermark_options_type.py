from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.watermark_options_type_show_for_groups_type_1 import (
        WatermarkOptionsTypeShowForGroupsType1,
    )
    from ..models.watermark_options_type_show_in_context_type_1 import (
        WatermarkOptionsTypeShowInContextType1,
    )
    from ..models.watermark_options_type_text_appearance_type_1 import (
        WatermarkOptionsTypeTextAppearanceType1,
    )


T = TypeVar("T", bound="WatermarkOptionsType")


@_attrs_define
class WatermarkOptionsType:
    """
    Attributes:
        custom_text (None | str | Unset):
        groups (list[UUID] | None | Unset):
        include_custom_text (bool | None | Unset):
        include_date_time (bool | None | Unset):
        include_email (bool | None | Unset):
        include_ip_address (bool | None | Unset):
        shadow_opacity (float | None | Unset):
        show_for_groups (None | Unset | WatermarkOptionsTypeShowForGroupsType1):
        show_in_context (None | Unset | WatermarkOptionsTypeShowInContextType1):
        show_watermark (bool | None | Unset):
        text_appearance (None | Unset | WatermarkOptionsTypeTextAppearanceType1):
        text_opacity (float | None | Unset):
    """

    custom_text: None | str | Unset = UNSET
    groups: list[UUID] | None | Unset = UNSET
    include_custom_text: bool | None | Unset = UNSET
    include_date_time: bool | None | Unset = UNSET
    include_email: bool | None | Unset = UNSET
    include_ip_address: bool | None | Unset = UNSET
    shadow_opacity: float | None | Unset = UNSET
    show_for_groups: None | Unset | WatermarkOptionsTypeShowForGroupsType1 = UNSET
    show_in_context: None | Unset | WatermarkOptionsTypeShowInContextType1 = UNSET
    show_watermark: bool | None | Unset = UNSET
    text_appearance: None | Unset | WatermarkOptionsTypeTextAppearanceType1 = UNSET
    text_opacity: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.watermark_options_type_show_for_groups_type_1 import (
            WatermarkOptionsTypeShowForGroupsType1,
        )
        from ..models.watermark_options_type_show_in_context_type_1 import (
            WatermarkOptionsTypeShowInContextType1,
        )
        from ..models.watermark_options_type_text_appearance_type_1 import (
            WatermarkOptionsTypeTextAppearanceType1,
        )

        custom_text: None | str | Unset
        if isinstance(self.custom_text, Unset):
            custom_text = UNSET
        else:
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

        include_custom_text: bool | None | Unset
        if isinstance(self.include_custom_text, Unset):
            include_custom_text = UNSET
        else:
            include_custom_text = self.include_custom_text

        include_date_time: bool | None | Unset
        if isinstance(self.include_date_time, Unset):
            include_date_time = UNSET
        else:
            include_date_time = self.include_date_time

        include_email: bool | None | Unset
        if isinstance(self.include_email, Unset):
            include_email = UNSET
        else:
            include_email = self.include_email

        include_ip_address: bool | None | Unset
        if isinstance(self.include_ip_address, Unset):
            include_ip_address = UNSET
        else:
            include_ip_address = self.include_ip_address

        shadow_opacity: float | None | Unset
        if isinstance(self.shadow_opacity, Unset):
            shadow_opacity = UNSET
        else:
            shadow_opacity = self.shadow_opacity

        show_for_groups: dict[str, Any] | None | Unset
        if isinstance(self.show_for_groups, Unset):
            show_for_groups = UNSET
        elif isinstance(self.show_for_groups, WatermarkOptionsTypeShowForGroupsType1):
            show_for_groups = self.show_for_groups.to_dict()
        else:
            show_for_groups = self.show_for_groups

        show_in_context: dict[str, Any] | None | Unset
        if isinstance(self.show_in_context, Unset):
            show_in_context = UNSET
        elif isinstance(self.show_in_context, WatermarkOptionsTypeShowInContextType1):
            show_in_context = self.show_in_context.to_dict()
        else:
            show_in_context = self.show_in_context

        show_watermark: bool | None | Unset
        if isinstance(self.show_watermark, Unset):
            show_watermark = UNSET
        else:
            show_watermark = self.show_watermark

        text_appearance: dict[str, Any] | None | Unset
        if isinstance(self.text_appearance, Unset):
            text_appearance = UNSET
        elif isinstance(self.text_appearance, WatermarkOptionsTypeTextAppearanceType1):
            text_appearance = self.text_appearance.to_dict()
        else:
            text_appearance = self.text_appearance

        text_opacity: float | None | Unset
        if isinstance(self.text_opacity, Unset):
            text_opacity = UNSET
        else:
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
        from ..models.watermark_options_type_show_for_groups_type_1 import (
            WatermarkOptionsTypeShowForGroupsType1,
        )
        from ..models.watermark_options_type_show_in_context_type_1 import (
            WatermarkOptionsTypeShowInContextType1,
        )
        from ..models.watermark_options_type_text_appearance_type_1 import (
            WatermarkOptionsTypeTextAppearanceType1,
        )

        d = dict(src_dict)

        def _parse_custom_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        custom_text = _parse_custom_text(d.pop("custom_text", UNSET))

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

        def _parse_include_custom_text(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_custom_text = _parse_include_custom_text(
            d.pop("include_custom_text", UNSET)
        )

        def _parse_include_date_time(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_date_time = _parse_include_date_time(d.pop("include_date_time", UNSET))

        def _parse_include_email(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_email = _parse_include_email(d.pop("include_email", UNSET))

        def _parse_include_ip_address(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_ip_address = _parse_include_ip_address(
            d.pop("include_ip_address", UNSET)
        )

        def _parse_shadow_opacity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        shadow_opacity = _parse_shadow_opacity(d.pop("shadow_opacity", UNSET))

        def _parse_show_for_groups(
            data: object,
        ) -> None | Unset | WatermarkOptionsTypeShowForGroupsType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                show_for_groups_type_1 = (
                    WatermarkOptionsTypeShowForGroupsType1.from_dict(data)
                )

                return show_for_groups_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WatermarkOptionsTypeShowForGroupsType1, data)

        show_for_groups = _parse_show_for_groups(d.pop("show_for_groups", UNSET))

        def _parse_show_in_context(
            data: object,
        ) -> None | Unset | WatermarkOptionsTypeShowInContextType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                show_in_context_type_1 = (
                    WatermarkOptionsTypeShowInContextType1.from_dict(data)
                )

                return show_in_context_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WatermarkOptionsTypeShowInContextType1, data)

        show_in_context = _parse_show_in_context(d.pop("show_in_context", UNSET))

        def _parse_show_watermark(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_watermark = _parse_show_watermark(d.pop("show_watermark", UNSET))

        def _parse_text_appearance(
            data: object,
        ) -> None | Unset | WatermarkOptionsTypeTextAppearanceType1:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                text_appearance_type_1 = (
                    WatermarkOptionsTypeTextAppearanceType1.from_dict(data)
                )

                return text_appearance_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WatermarkOptionsTypeTextAppearanceType1, data)

        text_appearance = _parse_text_appearance(d.pop("text_appearance", UNSET))

        def _parse_text_opacity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        text_opacity = _parse_text_opacity(d.pop("text_opacity", UNSET))

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
