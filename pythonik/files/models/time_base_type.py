from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeBaseType")


@_attrs_define
class TimeBaseType:
    """
    Attributes:
        denominator (int | Unset):
        numerator (int | Unset):
    """

    denominator: int | Unset = UNSET
    numerator: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        denominator = self.denominator

        numerator = self.numerator

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if denominator is not UNSET:
            field_dict["denominator"] = denominator
        if numerator is not UNSET:
            field_dict["numerator"] = numerator

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        denominator = d.pop("denominator", UNSET)

        numerator = d.pop("numerator", UNSET)

        time_base_type = cls(
            denominator=denominator,
            numerator=numerator,
        )

        time_base_type.additional_properties = d
        return time_base_type

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
