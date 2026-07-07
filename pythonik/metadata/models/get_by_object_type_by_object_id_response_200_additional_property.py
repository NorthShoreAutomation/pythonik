from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_by_object_type_by_object_id_response_200_additional_property_values_item import (
        GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesItem,
    )


T = TypeVar("T", bound="GetByObjectTypeByObjectIdResponse200AdditionalProperty")


@_attrs_define
class GetByObjectTypeByObjectIdResponse200AdditionalProperty:
    """
    Attributes:
        name (str | Unset):
        type_ (str | Unset):
        values (list[GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesItem] | Unset):
    """

    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    values: (
        list[GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesItem] | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_by_object_type_by_object_id_response_200_additional_property_values_item import (
            GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesItem,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        _values = d.pop("values", UNSET)
        values: (
            list[GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesItem]
            | Unset
        ) = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesItem.from_dict(
                    values_item_data
                )

                values.append(values_item)

        get_by_object_type_by_object_id_response_200_additional_property = cls(
            name=name,
            type_=type_,
            values=values,
        )

        get_by_object_type_by_object_id_response_200_additional_property.additional_properties = d
        return get_by_object_type_by_object_id_response_200_additional_property

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
