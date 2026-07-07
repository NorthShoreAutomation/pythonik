from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_bulk_ac_ls_schema_mode import CreateBulkACLsSchemaMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateBulkACLsSchema")


@_attrs_define
class CreateBulkACLsSchema:
    """
    Attributes:
        include_assets (bool):
        include_collections (bool):
        permissions (list[str]):
        group_ids (list[UUID] | Unset):
        mode (CreateBulkACLsSchemaMode | Unset):  Default: CreateBulkACLsSchemaMode.OVERWRITE.
        object_ids (list[UUID] | Unset): The number of object_ids in the list is limited to a minimum of 0 and a maximum
            of 500
        object_type (str | Unset):
        user_ids (list[UUID] | Unset):
    """

    include_assets: bool
    include_collections: bool
    permissions: list[str]
    group_ids: list[UUID] | Unset = UNSET
    mode: CreateBulkACLsSchemaMode | Unset = CreateBulkACLsSchemaMode.OVERWRITE
    object_ids: list[UUID] | Unset = UNSET
    object_type: str | Unset = UNSET
    user_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_assets = self.include_assets

        include_collections = self.include_collections

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

        object_ids: list[str] | Unset = UNSET
        if not isinstance(self.object_ids, Unset):
            object_ids = []
            for object_ids_item_data in self.object_ids:
                object_ids_item = str(object_ids_item_data)
                object_ids.append(object_ids_item)

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
                "include_assets": include_assets,
                "include_collections": include_collections,
                "permissions": permissions,
            }
        )
        if group_ids is not UNSET:
            field_dict["group_ids"] = group_ids
        if mode is not UNSET:
            field_dict["mode"] = mode
        if object_ids is not UNSET:
            field_dict["object_ids"] = object_ids
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_assets = d.pop("include_assets")

        include_collections = d.pop("include_collections")

        permissions = cast(list[str], d.pop("permissions"))

        _group_ids = d.pop("group_ids", UNSET)
        group_ids: list[UUID] | Unset = UNSET
        if _group_ids is not UNSET:
            group_ids = []
            for group_ids_item_data in _group_ids:
                group_ids_item = UUID(group_ids_item_data)

                group_ids.append(group_ids_item)

        _mode = d.pop("mode", UNSET)
        mode: CreateBulkACLsSchemaMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CreateBulkACLsSchemaMode(_mode)

        _object_ids = d.pop("object_ids", UNSET)
        object_ids: list[UUID] | Unset = UNSET
        if _object_ids is not UNSET:
            object_ids = []
            for object_ids_item_data in _object_ids:
                object_ids_item = UUID(object_ids_item_data)

                object_ids.append(object_ids_item)

        object_type = d.pop("object_type", UNSET)

        _user_ids = d.pop("user_ids", UNSET)
        user_ids: list[UUID] | Unset = UNSET
        if _user_ids is not UNSET:
            user_ids = []
            for user_ids_item_data in _user_ids:
                user_ids_item = UUID(user_ids_item_data)

                user_ids.append(user_ids_item)

        create_bulk_ac_ls_schema = cls(
            include_assets=include_assets,
            include_collections=include_collections,
            permissions=permissions,
            group_ids=group_ids,
            mode=mode,
            object_ids=object_ids,
            object_type=object_type,
            user_ids=user_ids,
        )

        create_bulk_ac_ls_schema.additional_properties = d
        return create_bulk_ac_ls_schema

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
