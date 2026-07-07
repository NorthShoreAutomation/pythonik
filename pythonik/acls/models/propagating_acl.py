from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PropagatingACL")


@_attrs_define
class PropagatingACL:
    """
    Attributes:
        permissions (list[str]):
        object_key (str | Unset):
        object_type (str | Unset):
        user_id (UUID | Unset):
    """

    permissions: list[str]
    object_key: str | Unset = UNSET
    object_type: str | Unset = UNSET
    user_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permissions = self.permissions

        object_key = self.object_key

        object_type = self.object_type

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permissions": permissions,
            }
        )
        if object_key is not UNSET:
            field_dict["object_key"] = object_key
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        permissions = cast(list[str], d.pop("permissions"))

        object_key = d.pop("object_key", UNSET)

        object_type = d.pop("object_type", UNSET)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        propagating_acl = cls(
            permissions=permissions,
            object_key=object_key,
            object_type=object_type,
            user_id=user_id,
        )

        propagating_acl.additional_properties = d
        return propagating_acl

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
