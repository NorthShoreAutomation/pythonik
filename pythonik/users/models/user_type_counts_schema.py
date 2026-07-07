from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserTypeCountsSchema")


@_attrs_define
class UserTypeCountsSchema:
    """
    Attributes:
        browse_api_only (int | Unset):
        browse_only (int | Unset):
        power (int | Unset):
        standard (int | Unset):
    """

    browse_api_only: int | Unset = UNSET
    browse_only: int | Unset = UNSET
    power: int | Unset = UNSET
    standard: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        browse_api_only = self.browse_api_only

        browse_only = self.browse_only

        power = self.power

        standard = self.standard

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if browse_api_only is not UNSET:
            field_dict["BROWSE_API_ONLY"] = browse_api_only
        if browse_only is not UNSET:
            field_dict["BROWSE_ONLY"] = browse_only
        if power is not UNSET:
            field_dict["POWER"] = power
        if standard is not UNSET:
            field_dict["STANDARD"] = standard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        browse_api_only = d.pop("BROWSE_API_ONLY", UNSET)

        browse_only = d.pop("BROWSE_ONLY", UNSET)

        power = d.pop("POWER", UNSET)

        standard = d.pop("STANDARD", UNSET)

        user_type_counts_schema = cls(
            browse_api_only=browse_api_only,
            browse_only=browse_only,
            power=power,
            standard=standard,
        )

        user_type_counts_schema.additional_properties = d
        return user_type_counts_schema

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
