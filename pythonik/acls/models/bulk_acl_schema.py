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
        access_denied (list[str] | None | Unset):
        access_granted (list[str] | None | Unset):
    """

    access_denied: list[str] | None | Unset = UNSET
    access_granted: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_denied: list[str] | None | Unset
        if isinstance(self.access_denied, Unset):
            access_denied = UNSET
        elif isinstance(self.access_denied, list):
            access_denied = self.access_denied

        else:
            access_denied = self.access_denied

        access_granted: list[str] | None | Unset
        if isinstance(self.access_granted, Unset):
            access_granted = UNSET
        elif isinstance(self.access_granted, list):
            access_granted = self.access_granted

        else:
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

        def _parse_access_denied(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_denied_type_0 = cast(list[str], data)

                return access_denied_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        access_denied = _parse_access_denied(d.pop("access_denied", UNSET))

        def _parse_access_granted(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                access_granted_type_0 = cast(list[str], data)

                return access_granted_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        access_granted = _parse_access_granted(d.pop("access_granted", UNSET))

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
