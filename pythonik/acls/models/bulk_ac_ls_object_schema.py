from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_ac_ls_object_schema_permissions_item import (
    BulkACLsObjectSchemaPermissionsItem,
)

T = TypeVar("T", bound="BulkACLsObjectSchema")


@_attrs_define
class BulkACLsObjectSchema:
    """
    Attributes:
        object_keys (list[str]):
        object_type (str):
        permissions (list[BulkACLsObjectSchemaPermissionsItem]):
    """

    object_keys: list[str]
    object_type: str
    permissions: list[BulkACLsObjectSchemaPermissionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_keys = self.object_keys

        object_type = self.object_type

        permissions = []
        for permissions_item_data in self.permissions:
            permissions_item = permissions_item_data.value
            permissions.append(permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_keys": object_keys,
                "object_type": object_type,
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_keys = cast(list[str], d.pop("object_keys"))

        object_type = d.pop("object_type")

        permissions = []
        _permissions = d.pop("permissions")
        for permissions_item_data in _permissions:
            permissions_item = BulkACLsObjectSchemaPermissionsItem(
                permissions_item_data
            )

            permissions.append(permissions_item)

        bulk_ac_ls_object_schema = cls(
            object_keys=object_keys,
            object_type=object_type,
            permissions=permissions,
        )

        bulk_ac_ls_object_schema.additional_properties = d
        return bulk_ac_ls_object_schema

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
