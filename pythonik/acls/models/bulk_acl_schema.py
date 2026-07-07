from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkACLSchema")


@_attrs_define
class BulkACLSchema:
    """
    Attributes:
        access_denied (list[str] | Unset):
        access_granted (list[str] | Unset):
    """

    access_denied: list[str] | Unset = UNSET
    access_granted: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_denied: list[str] | Unset = UNSET
        if not isinstance(self.access_denied, Unset):
            access_denied = self.access_denied

        access_granted: list[str] | Unset = UNSET
        if not isinstance(self.access_granted, Unset):
            access_granted = self.access_granted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_denied is not UNSET:
            field_dict["access_denied"] = access_denied
        if access_granted is not UNSET:
            field_dict["access_granted"] = access_granted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_denied = cast(list[str], d.pop("access_denied", UNSET))

        access_granted = cast(list[str], d.pop("access_granted", UNSET))

        bulk_acl_schema = cls(
            access_denied=access_denied,
            access_granted=access_granted,
        )

        bulk_acl_schema.additional_properties = d
        return bulk_acl_schema

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
