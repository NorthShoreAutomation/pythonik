from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteACLsSchema")


@_attrs_define
class DeleteACLsSchema:
    """
    Attributes:
        group_ids (list[UUID] | Unset):
        object_keys (list[str] | Unset): The number of object_keys in the list is limitedto a minimum of 0 and a maximum
            of 500
        object_type (str | Unset):
        user_ids (list[UUID] | Unset):
    """

    group_ids: list[UUID] | Unset = UNSET
    object_keys: list[str] | Unset = UNSET
    object_type: str | Unset = UNSET
    user_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = []
            for group_ids_item_data in self.group_ids:
                group_ids_item = str(group_ids_item_data)
                group_ids.append(group_ids_item)

        object_keys: list[str] | Unset = UNSET
        if not isinstance(self.object_keys, Unset):
            object_keys = self.object_keys

        object_type = self.object_type

        user_ids: list[str] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = []
            for user_ids_item_data in self.user_ids:
                user_ids_item = str(user_ids_item_data)
                user_ids.append(user_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if object_keys is not UNSET:
            field_dict["object_keys"] = object_keys
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _group_ids = d.pop("group_ids", UNSET)
        group_ids: list[UUID] | Unset = UNSET
        if _group_ids is not UNSET:
            group_ids = []
            for group_ids_item_data in _group_ids:
                group_ids_item = UUID(group_ids_item_data)

                group_ids.append(group_ids_item)

        object_keys = cast(list[str], d.pop("object_keys", UNSET))

        object_type = d.pop("object_type", UNSET)

        _user_ids = d.pop("user_ids", UNSET)
        user_ids: list[UUID] | Unset = UNSET
        if _user_ids is not UNSET:
            user_ids = []
            for user_ids_item_data in _user_ids:
                user_ids_item = UUID(user_ids_item_data)

                user_ids.append(user_ids_item)

        delete_ac_ls_schema = cls(
            group_ids=group_ids,
            object_keys=object_keys,
            object_type=object_type,
            user_ids=user_ids,
        )

        delete_ac_ls_schema.additional_properties = d
        return delete_ac_ls_schema

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
