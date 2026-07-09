from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscodeElasticQueueRecordSchema")


@_attrs_define
class TranscodeElasticQueueRecordSchema:
    """
    Attributes:
        date_created (None | str | Unset):
        date_updated (None | str | Unset):
        id (None | str | Unset):
        job_id (None | str | Unset):
        object_id (None | str | Unset):
        object_type (None | str | Unset):
        priority (None | str | Unset):
        queue (None | str | Unset):
        retry_count (None | str | Unset):
        status (None | str | Unset):
        storage_id (None | str | Unset):
        system_domain_id (None | str | Unset):
        system_domain_timestamp (None | str | Unset):
        system_name (None | str | Unset):
        type_ (None | str | Unset):
        user_id (None | str | Unset):
        version_id (None | str | Unset):
    """

    date_created: None | str | Unset = UNSET
    date_updated: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    job_id: None | str | Unset = UNSET
    object_id: None | str | Unset = UNSET
    object_type: None | str | Unset = UNSET
    priority: None | str | Unset = UNSET
    queue: None | str | Unset = UNSET
    retry_count: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    storage_id: None | str | Unset = UNSET
    system_domain_id: None | str | Unset = UNSET
    system_domain_timestamp: None | str | Unset = UNSET
    system_name: None | str | Unset = UNSET
    type_: None | str | Unset = UNSET
    user_id: None | str | Unset = UNSET
    version_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        else:
            date_created = self.date_created

        date_updated: None | str | Unset
        if isinstance(self.date_updated, Unset):
            date_updated = UNSET
        else:
            date_updated = self.date_updated

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        else:
            job_id = self.job_id

        object_id: None | str | Unset
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        else:
            object_id = self.object_id

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        priority: None | str | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        queue: None | str | Unset
        if isinstance(self.queue, Unset):
            queue = UNSET
        else:
            queue = self.queue

        retry_count: None | str | Unset
        if isinstance(self.retry_count, Unset):
            retry_count = UNSET
        else:
            retry_count = self.retry_count

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        else:
            storage_id = self.storage_id

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = self.system_domain_id

        system_domain_timestamp: None | str | Unset
        if isinstance(self.system_domain_timestamp, Unset):
            system_domain_timestamp = UNSET
        else:
            system_domain_timestamp = self.system_domain_timestamp

        system_name: None | str | Unset
        if isinstance(self.system_name, Unset):
            system_name = UNSET
        else:
            system_name = self.system_name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        else:
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

        def _parse_date_created(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_updated(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_updated = _parse_date_updated(d.pop("date_updated", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_job_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

        def _parse_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_id = _parse_object_id(d.pop("object_id", UNSET))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_priority(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_queue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        queue = _parse_queue(d.pop("queue", UNSET))

        def _parse_retry_count(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        retry_count = _parse_retry_count(d.pop("retry_count", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_storage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_id = _parse_storage_id(d.pop("storage_id", UNSET))

        def _parse_system_domain_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

        def _parse_system_domain_timestamp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_domain_timestamp = _parse_system_domain_timestamp(
            d.pop("system_domain_timestamp", UNSET)
        )

        def _parse_system_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_name = _parse_system_name(d.pop("system_name", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        def _parse_version_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))

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
