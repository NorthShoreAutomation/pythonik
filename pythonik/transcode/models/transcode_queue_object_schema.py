from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscodeQueueObjectSchema")


@_attrs_define
class TranscodeQueueObjectSchema:
    """
    Attributes:
        date_created (datetime.datetime | Unset):
        date_updated (datetime.datetime | Unset):
        id (UUID | Unset):
        job_id (UUID | Unset):
        priority (int | Unset):
        retry_count (int | Unset):
        status (str | Unset):
        system_domain (str | Unset):
        system_domain_id (UUID | Unset):
        system_domain_timestamp (float | Unset):
        system_name (str | Unset):
        type_ (str | Unset):
        user_id (UUID | Unset):
    """

    date_created: datetime.datetime | Unset = UNSET
    date_updated: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    job_id: UUID | Unset = UNSET
    priority: int | Unset = UNSET
    retry_count: int | Unset = UNSET
    status: str | Unset = UNSET
    system_domain: str | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    system_domain_timestamp: float | Unset = UNSET
    system_name: str | Unset = UNSET
    type_: str | Unset = UNSET
    user_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_updated: str | Unset = UNSET
        if not isinstance(self.date_updated, Unset):
            date_updated = self.date_updated.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)

        priority = self.priority

        retry_count = self.retry_count

        status = self.status

        system_domain = self.system_domain

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        system_domain_timestamp = self.system_domain_timestamp

        system_name = self.system_name

        type_ = self.type_

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_updated is not UNSET:
            field_dict["date_updated"] = date_updated
        if id is not UNSET:
            field_dict["id"] = id
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if status is not UNSET:
            field_dict["status"] = status
        if system_domain is not UNSET:
            field_dict["system_domain"] = system_domain
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if system_domain_timestamp is not UNSET:
            field_dict["system_domain_timestamp"] = system_domain_timestamp
        if system_name is not UNSET:
            field_dict["system_name"] = system_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_updated = d.pop("date_updated", UNSET)
        date_updated: datetime.datetime | Unset
        if isinstance(_date_updated, Unset):
            date_updated = UNSET
        else:
            date_updated = datetime.datetime.fromisoformat(_date_updated)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _job_id = d.pop("job_id", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id, Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)

        priority = d.pop("priority", UNSET)

        retry_count = d.pop("retry_count", UNSET)

        status = d.pop("status", UNSET)

        system_domain = d.pop("system_domain", UNSET)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        system_domain_timestamp = d.pop("system_domain_timestamp", UNSET)

        system_name = d.pop("system_name", UNSET)

        type_ = d.pop("type", UNSET)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        transcode_queue_object_schema = cls(
            date_created=date_created,
            date_updated=date_updated,
            id=id,
            job_id=job_id,
            priority=priority,
            retry_count=retry_count,
            status=status,
            system_domain=system_domain,
            system_domain_id=system_domain_id,
            system_domain_timestamp=system_domain_timestamp,
            system_name=system_name,
            type_=type_,
            user_id=user_id,
        )

        transcode_queue_object_schema.additional_properties = d
        return transcode_queue_object_schema

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
