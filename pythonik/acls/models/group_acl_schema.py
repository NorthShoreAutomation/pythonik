from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupACLSchema")


@_attrs_define
class GroupACLSchema:
    """
    Attributes:
        permissions (list[str]):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        group_id (UUID | Unset):
        object_key (str | Unset):
        object_type (str | Unset):
    """

    permissions: list[str]
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    group_id: UUID | Unset = UNSET
    object_key: str | Unset = UNSET
    object_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        permissions = self.permissions

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        group_id: str | Unset = UNSET
        if not isinstance(self.group_id, Unset):
            group_id = str(self.group_id)

        object_key = self.object_key

        object_type = self.object_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permissions": permissions,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if object_key is not UNSET:
            field_dict["object_key"] = object_key
        if object_type is not UNSET:
            field_dict["object_type"] = object_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        permissions = cast(list[str], d.pop("permissions"))

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        _group_id = d.pop("group_id", UNSET)
        group_id: UUID | Unset
        if isinstance(_group_id, Unset):
            group_id = UNSET
        else:
            group_id = UUID(_group_id)

        object_key = d.pop("object_key", UNSET)

        object_type = d.pop("object_type", UNSET)

        group_acl_schema = cls(
            permissions=permissions,
            date_created=date_created,
            date_modified=date_modified,
            group_id=group_id,
            object_key=object_key,
            object_type=object_type,
        )

        group_acl_schema.additional_properties = d
        return group_acl_schema

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
