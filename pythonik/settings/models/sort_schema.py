from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sort_schema_order_type_1 import SortSchemaOrderType1


T = TypeVar("T", bound="SortSchema")


@_attrs_define
class SortSchema:
    """
    Attributes:
        name (str):
        order (None | SortSchemaOrderType1 | Unset):
    """

    name: str
    order: None | SortSchemaOrderType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sort_schema_order_type_1 import SortSchemaOrderType1

        name = self.name

        order: dict[str, Any] | None | Unset
        if isinstance(self.order, Unset):
            order = UNSET
        elif isinstance(self.order, SortSchemaOrderType1):
            order = self.order.to_dict()
        else:
            order = self.order

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
        from ..models.sort_schema_order_type_1 import SortSchemaOrderType1

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_order(data: object) -> None | SortSchemaOrderType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                order_type_1 = SortSchemaOrderType1.from_dict(data)

                return order_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SortSchemaOrderType1 | Unset, data)

        order = _parse_order(d.pop("order", UNSET))

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
