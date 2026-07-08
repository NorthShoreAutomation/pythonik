from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserTypeCountsSchema")


@_attrs_define
class UserTypeCountsSchema:
    """
    Attributes:
        browse_api_only (int | None | Unset):
        browse_only (int | None | Unset):
        power (int | None | Unset):
        standard (int | None | Unset):
    """

    browse_api_only: int | None | Unset = UNSET
    browse_only: int | None | Unset = UNSET
    power: int | None | Unset = UNSET
    standard: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        browse_api_only: int | None | Unset
        if isinstance(self.browse_api_only, Unset):
            browse_api_only = UNSET
        else:
            browse_api_only = self.browse_api_only

        browse_only: int | None | Unset
        if isinstance(self.browse_only, Unset):
            browse_only = UNSET
        else:
            browse_only = self.browse_only

        power: int | None | Unset
        if isinstance(self.power, Unset):
            power = UNSET
        else:
            power = self.power

        standard: int | None | Unset
        if isinstance(self.standard, Unset):
            standard = UNSET
        else:
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

        def _parse_browse_api_only(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        browse_api_only = _parse_browse_api_only(d.pop("BROWSE_API_ONLY", UNSET))

        def _parse_browse_only(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        browse_only = _parse_browse_only(d.pop("BROWSE_ONLY", UNSET))

        def _parse_power(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        power = _parse_power(d.pop("POWER", UNSET))

        def _parse_standard(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        standard = _parse_standard(d.pop("STANDARD", UNSET))

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
