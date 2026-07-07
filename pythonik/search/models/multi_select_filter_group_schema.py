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
        items (list[str] | Unset):
        modifier (MultiSelectFilterGroupSchemaModifier | Unset):
    """

    items: list[str] | Unset = UNSET
    modifier: MultiSelectFilterGroupSchemaModifier | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: list[str] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items

        modifier: str | Unset = UNSET
        if not isinstance(self.modifier, Unset):
            modifier = self.modifier.value

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
        items = cast(list[str], d.pop("items", UNSET))

        _modifier = d.pop("modifier", UNSET)
        modifier: MultiSelectFilterGroupSchemaModifier | Unset
        if isinstance(_modifier, Unset):
            modifier = UNSET
        else:
            modifier = MultiSelectFilterGroupSchemaModifier(_modifier)

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
