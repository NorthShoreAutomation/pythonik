from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_by_object_type_by_object_id_response_200_additional_property_values_type_0_item import (
        GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesType0Item,
    )


T = TypeVar("T", bound="GetByObjectTypeByObjectIdResponse200AdditionalProperty")


@_attrs_define
class GetByObjectTypeByObjectIdResponse200AdditionalProperty:
    """
    Attributes:
        name (None | str | Unset):
        type_ (None | str | Unset):
        values (list[GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesType0Item] | None | Unset):
    """

    name: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    values: (
        list[GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesType0Item]
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        values: list[dict[str, Any]] | None | Unset
        if isinstance(self.values, Unset):
            values = UNSET
        elif isinstance(self.values, list):
            values = []
            for values_type_0_item_data in self.values:
                values_type_0_item = values_type_0_item_data.to_dict()
                values.append(values_type_0_item)

        else:
            values = self.values

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
        from ..models.get_by_object_type_by_object_id_response_200_additional_property_values_type_0_item import (
            GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesType0Item,
        )

        d = dict(src_dict)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_values(
            data: object,
        ) -> (
            list[GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesType0Item]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                values_type_0 = []
                _values_type_0 = data
                for values_type_0_item_data in _values_type_0:
                    values_type_0_item = GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesType0Item.from_dict(
                        values_type_0_item_data
                    )

                    values_type_0.append(values_type_0_item)

                return values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    GetByObjectTypeByObjectIdResponse200AdditionalPropertyValuesType0Item
                ]
                | None
                | Unset,
                data,
            )

        values = _parse_values(d.pop("values", UNSET))

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
