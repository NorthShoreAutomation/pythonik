from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_ac_ls_schema_multiple_mode import CreateACLsSchemaMultipleMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateACLsSchemaMultiple")


@_attrs_define
class CreateACLsSchemaMultiple:
    """
    Attributes:
        object_keys (list[str]): The number of object_keys in the list is limited to a minimum of 1 and a maximum of 1
        permissions (list[str]):
        group_ids (list[UUID] | Unset):
        mode (CreateACLsSchemaMultipleMode | Unset):  Default: CreateACLsSchemaMultipleMode.OVERWRITE.
        object_type (str | Unset):
        user_ids (list[UUID] | Unset):
    """

    object_keys: list[str]
    permissions: list[str]
    group_ids: list[UUID] | Unset = UNSET
    mode: CreateACLsSchemaMultipleMode | Unset = CreateACLsSchemaMultipleMode.OVERWRITE
    object_type: str | Unset = UNSET
    user_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_keys = self.object_keys

        permissions = self.permissions

        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = []
            for group_ids_item_data in self.group_ids:
                group_ids_item = str(group_ids_item_data)
                group_ids.append(group_ids_item)

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        object_type = self.object_type

        user_ids: list[str] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = []
            for user_ids_item_data in self.user_ids:
                user_ids_item = str(user_ids_item_data)
                user_ids.append(user_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_keys": object_keys,
                "permissions": permissions,
            }
        )
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if mode is not UNSET:
            field_dict["mode"] = mode
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_keys = cast(list[str], d.pop("object_keys"))

        permissions = cast(list[str], d.pop("permissions"))

        _group_ids = d.pop("group_ids", UNSET)
        group_ids: list[UUID] | Unset = UNSET
        if _group_ids is not UNSET:
            group_ids = []
            for group_ids_item_data in _group_ids:
                group_ids_item = UUID(group_ids_item_data)

                group_ids.append(group_ids_item)

        _mode = d.pop("mode", UNSET)
        mode: CreateACLsSchemaMultipleMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CreateACLsSchemaMultipleMode(_mode)

        object_type = d.pop("object_type", UNSET)

        _user_ids = d.pop("user_ids", UNSET)
        user_ids: list[UUID] | Unset = UNSET
        if _user_ids is not UNSET:
            user_ids = []
            for user_ids_item_data in _user_ids:
                user_ids_item = UUID(user_ids_item_data)

                user_ids.append(user_ids_item)

        create_ac_ls_schema_multiple = cls(
            object_keys=object_keys,
            permissions=permissions,
            group_ids=group_ids,
            mode=mode,
            object_type=object_type,
            user_ids=user_ids,
        )

        create_ac_ls_schema_multiple.additional_properties = d
        return create_ac_ls_schema_multiple

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
