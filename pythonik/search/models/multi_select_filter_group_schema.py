from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multi_select_filter_group_schema_modifier_type_1 import (
        MultiSelectFilterGroupSchemaModifierType1,
    )


T = TypeVar("T", bound="MultiSelectFilterGroupSchema")


@_attrs_define
class MultiSelectFilterGroupSchema:
    """
    Attributes:
        items (list[str] | None | Unset):
        modifier (MultiSelectFilterGroupSchemaModifierType1 | None | Unset):
    """

    items: list[str] | None | Unset = UNSET
    modifier: MultiSelectFilterGroupSchemaModifierType1 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.multi_select_filter_group_schema_modifier_type_1 import (
            MultiSelectFilterGroupSchemaModifierType1,
        )

        items: list[str] | None | Unset
        if isinstance(self.items, Unset):
            items = UNSET
        elif isinstance(self.items, list):
            items = self.items

        else:
            items = self.items

        modifier: dict[str, Any] | None | Unset
        if isinstance(self.modifier, Unset):
            modifier = UNSET
        elif isinstance(self.modifier, MultiSelectFilterGroupSchemaModifierType1):
            modifier = self.modifier.to_dict()
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
        from ..models.multi_select_filter_group_schema_modifier_type_1 import (
            MultiSelectFilterGroupSchemaModifierType1,
        )

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
        ) -> MultiSelectFilterGroupSchemaModifierType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                modifier_type_1 = MultiSelectFilterGroupSchemaModifierType1.from_dict(
                    data
                )

                return modifier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MultiSelectFilterGroupSchemaModifierType1 | None | Unset, data)

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
