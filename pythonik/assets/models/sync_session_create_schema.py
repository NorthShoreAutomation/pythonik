from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncSessionCreateSchema")


@_attrs_define
class SyncSessionCreateSchema:
    """
    Attributes:
        current_dc_url (str | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        dc_url (str | Unset):
        id (UUID | Unset):
        node (str | Unset):
    """

    current_dc_url: str | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    dc_url: str | Unset = UNSET
    id: UUID | Unset = UNSET
    node: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_dc_url = self.current_dc_url

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        dc_url = self.dc_url

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        node = self.node

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_dc_url is not UNSET:
            field_dict["current_dc_url"] = current_dc_url
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if dc_url is not UNSET:
            field_dict["dc_url"] = dc_url
        if id is not UNSET:
            field_dict["id"] = id
        if node is not UNSET:
            field_dict["node"] = node

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_dc_url = d.pop("current_dc_url", UNSET)

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

        dc_url = d.pop("dc_url", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        node = d.pop("node", UNSET)

        sync_session_create_schema = cls(
            current_dc_url=current_dc_url,
            date_created=date_created,
            date_modified=date_modified,
            dc_url=dc_url,
            id=id,
            node=node,
        )

        sync_session_create_schema.additional_properties = d
        return sync_session_create_schema

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
