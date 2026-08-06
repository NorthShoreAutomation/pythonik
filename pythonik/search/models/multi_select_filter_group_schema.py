from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.multi_select_filter_group_schema_modifier import (
    MultiSelectFilterGroupSchemaModifier,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiSelectFilterGroupSchema")


@_attrs_define
class MultiSelectFilterGroupSchema:
    """
    Attributes:
        items (list[str] | None | Unset):
        modifier (MultiSelectFilterGroupSchemaModifier | None | Unset):
    """

    items: list[str] | None | Unset = UNSET
    modifier: MultiSelectFilterGroupSchemaModifier | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: list[str] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = self.items

        else:
            items = self.items

        modifier: None | str | Unset
        if isinstance(self.modifier, Unset):
            modifier = UNSET
        elif isinstance(self.modifier, MultiSelectFilterGroupSchemaModifier):
            modifier = self.modifier.value
        else:
            modifier = self.modifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if modifier is not UNSET:
            field_dict["modifier"] = modifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_items(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                items_type_0 = cast(list[str], data)

                return items_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        items = _parse_items(d.pop("items", UNSET))

        def _parse_modifier(
            data: object,
        ) -> MultiSelectFilterGroupSchemaModifier | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                modifier_type_1 = MultiSelectFilterGroupSchemaModifier(data)

                return modifier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MultiSelectFilterGroupSchemaModifier | None | Unset, data)

        modifier = _parse_modifier(d.pop("modifier", UNSET))

        multi_select_filter_group_schema = cls(
            items=items,
            modifier=modifier,
        )

        multi_select_filter_group_schema.additional_properties = d
        return multi_select_filter_group_schema

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
