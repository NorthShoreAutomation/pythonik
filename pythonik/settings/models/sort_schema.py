from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sort_schema_order import SortSchemaOrder
from ..types import UNSET, Unset

T = TypeVar("T", bound="SortSchema")


@_attrs_define
class SortSchema:
    """
    Attributes:
        name (str):
        order (SortSchemaOrder | Unset):
    """

    name: str
    order: SortSchemaOrder | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        order: str | Unset = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if order is not UNSET:
            field_dict["order"] = order

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _order = d.pop("order", UNSET)
        order: SortSchemaOrder | Unset
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = SortSchemaOrder(_order)

        sort_schema = cls(
            name=name,
            order=order,
        )

        sort_schema.additional_properties = d
        return sort_schema

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
