from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscodeElasticQueueRecordSchema")


@_attrs_define
class TranscodeElasticQueueRecordSchema:
    """
    Attributes:
        date_created (str | Unset):
        date_updated (str | Unset):
        id (str | Unset):
        job_id (str | Unset):
        object_id (str | Unset):
        object_type (str | Unset):
        priority (str | Unset):
        queue (str | Unset):
        retry_count (str | Unset):
        status (str | Unset):
        storage_id (str | Unset):
        system_domain_id (str | Unset):
        system_domain_timestamp (str | Unset):
        system_name (str | Unset):
        type_ (str | Unset):
        user_id (str | Unset):
        version_id (str | Unset):
    """

    date_created: str | Unset = UNSET
    date_updated: str | Unset = UNSET
    id: str | Unset = UNSET
    job_id: str | Unset = UNSET
    object_id: str | Unset = UNSET
    object_type: str | Unset = UNSET
    priority: str | Unset = UNSET
    queue: str | Unset = UNSET
    retry_count: str | Unset = UNSET
    status: str | Unset = UNSET
    storage_id: str | Unset = UNSET
    system_domain_id: str | Unset = UNSET
    system_domain_timestamp: str | Unset = UNSET
    system_name: str | Unset = UNSET
    type_: str | Unset = UNSET
    user_id: str | Unset = UNSET
    version_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created = self.date_created

        date_updated = self.date_updated

        id = self.id

        job_id = self.job_id

        object_id = self.object_id

        object_type = self.object_type

        priority = self.priority

        queue = self.queue

        retry_count = self.retry_count

        status = self.status

        storage_id = self.storage_id

        system_domain_id = self.system_domain_id

        system_domain_timestamp = self.system_domain_timestamp

        system_name = self.system_name

        type_ = self.type_

        user_id = self.user_id

        version_id = self.version_id

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
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if priority is not UNSET:
            field_dict["priority"] = priority
        if queue is not UNSET:
            field_dict["queue"] = queue
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if status is not UNSET:
            field_dict["status"] = status
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
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
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date_created = d.pop("date_created", UNSET)

        date_updated = d.pop("date_updated", UNSET)

        id = d.pop("id", UNSET)

        job_id = d.pop("job_id", UNSET)

        object_id = d.pop("object_id", UNSET)

        object_type = d.pop("object_type", UNSET)

        priority = d.pop("priority", UNSET)

        queue = d.pop("queue", UNSET)

        retry_count = d.pop("retry_count", UNSET)

        status = d.pop("status", UNSET)

        storage_id = d.pop("storage_id", UNSET)

        system_domain_id = d.pop("system_domain_id", UNSET)

        system_domain_timestamp = d.pop("system_domain_timestamp", UNSET)

        system_name = d.pop("system_name", UNSET)

        type_ = d.pop("type", UNSET)

        user_id = d.pop("user_id", UNSET)

        version_id = d.pop("version_id", UNSET)

        transcode_elastic_queue_record_schema = cls(
            date_created=date_created,
            date_updated=date_updated,
            id=id,
            job_id=job_id,
            object_id=object_id,
            object_type=object_type,
            priority=priority,
            queue=queue,
            retry_count=retry_count,
            status=status,
            storage_id=storage_id,
            system_domain_id=system_domain_id,
            system_domain_timestamp=system_domain_timestamp,
            system_name=system_name,
            type_=type_,
            user_id=user_id,
            version_id=version_id,
        )

        transcode_elastic_queue_record_schema.additional_properties = d
        return transcode_elastic_queue_record_schema

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
