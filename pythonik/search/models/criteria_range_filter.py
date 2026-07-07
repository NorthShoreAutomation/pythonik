from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CriteriaRangeFilter")


@_attrs_define
class CriteriaRangeFilter:
    """
    Attributes:
        max_ (str | Unset):
        min_ (str | Unset):
        timezone (str | Unset): Format: +02:00. Results returned in UTC by default
    """

    max_: str | Unset = UNSET
    min_: str | Unset = UNSET
    timezone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_ = self.max_

        min_ = self.min_

        timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        timezone = d.pop("timezone", UNSET)

        criteria_range_filter = cls(
            max_=max_,
            min_=min_,
            timezone=timezone,
        )

        criteria_range_filter.additional_properties = d
        return criteria_range_filter

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
