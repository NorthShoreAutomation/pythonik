from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubscriptionSchema")


@_attrs_define
class SubscriptionSchema:
    """
    Attributes:
        object_type (str):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        event_type (str | Unset):
        id (UUID | Unset):
        object_id (UUID | Unset):
        sub_object_id (UUID | Unset):
        sub_object_type (str | Unset):
        system_domain_id (UUID | Unset):
        user_id (UUID | Unset):
    """

    object_type: str
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    event_type: str | Unset = UNSET
    id: UUID | Unset = UNSET
    object_id: UUID | Unset = UNSET
    sub_object_id: UUID | Unset = UNSET
    sub_object_type: str | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    user_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_type = self.object_type

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        event_type = self.event_type

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        object_id: str | Unset = UNSET
        if not isinstance(self.object_id, Unset):
            object_id = str(self.object_id)

        sub_object_id: str | Unset = UNSET
        if not isinstance(self.sub_object_id, Unset):
            sub_object_id = str(self.sub_object_id)

        sub_object_type = self.sub_object_type

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_type": object_type,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if id is not UNSET:
            field_dict["id"] = id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if sub_object_id is not UNSET:
            field_dict["sub_object_id"] = sub_object_id
        if sub_object_type is not UNSET:
            field_dict["sub_object_type"] = sub_object_type
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_type = d.pop("object_type")

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

        event_type = d.pop("event_type", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _object_id = d.pop("object_id", UNSET)
        object_id: UUID | Unset
        if isinstance(_object_id, Unset):
            object_id = UNSET
        else:
            object_id = UUID(_object_id)

        _sub_object_id = d.pop("sub_object_id", UNSET)
        sub_object_id: UUID | Unset
        if isinstance(_sub_object_id, Unset):
            sub_object_id = UNSET
        else:
            sub_object_id = UUID(_sub_object_id)

        sub_object_type = d.pop("sub_object_type", UNSET)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        subscription_schema = cls(
            object_type=object_type,
            date_created=date_created,
            date_modified=date_modified,
            event_type=event_type,
            id=id,
            object_id=object_id,
            sub_object_id=sub_object_id,
            sub_object_type=sub_object_type,
            system_domain_id=system_domain_id,
            user_id=user_id,
        )

        subscription_schema.additional_properties = d
        return subscription_schema

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
