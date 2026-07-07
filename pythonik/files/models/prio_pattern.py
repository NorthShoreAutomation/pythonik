from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrioPattern")


@_attrs_define
class PrioPattern:
    """
    Attributes:
        pattern (str | Unset):
        priority (int | Unset):
    """

    pattern: str | Unset = UNSET
    priority: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pattern = self.pattern

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pattern = d.pop("pattern", UNSET)

        priority = d.pop("priority", UNSET)

        prio_pattern = cls(
            pattern=pattern,
            priority=priority,
        )

        prio_pattern.additional_properties = d
        return prio_pattern

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
