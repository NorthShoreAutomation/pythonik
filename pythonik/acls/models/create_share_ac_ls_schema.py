from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateShareACLsSchema")


@_attrs_define
class CreateShareACLsSchema:
    """
    Attributes:
        permissions (list[str]):
        object_keys (list[str] | Unset): The number of object_keys in the list is limited to a min of 0 and a maximum of
            500
        object_type (str | Unset):
        share_id (UUID | Unset):
    """

    permissions: list[str]
    object_keys: list[str] | Unset = UNSET
    object_type: str | Unset = UNSET
    share_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permissions = self.permissions

        object_keys: list[str] | Unset = UNSET
        if not isinstance(self.object_keys, Unset):
            object_keys = self.object_keys

        object_type = self.object_type

        share_id: str | Unset = UNSET
        if not isinstance(self.share_id, Unset):
            share_id = str(self.share_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permissions": permissions,
            }
        )
        if object_keys is not UNSET:
            field_dict["object_keys"] = object_keys
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if share_id is not UNSET:
            field_dict["share_id"] = share_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        permissions = cast(list[str], d.pop("permissions"))

        object_keys = cast(list[str], d.pop("object_keys", UNSET))

        object_type = d.pop("object_type", UNSET)

        _share_id = d.pop("share_id", UNSET)
        share_id: UUID | Unset
        if isinstance(_share_id, Unset):
            share_id = UNSET
        else:
            share_id = UUID(_share_id)

        create_share_ac_ls_schema = cls(
            permissions=permissions,
            object_keys=object_keys,
            object_type=object_type,
            share_id=share_id,
        )

        create_share_ac_ls_schema.additional_properties = d
        return create_share_ac_ls_schema

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
