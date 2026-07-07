from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MLDetectionQueueRecordSchema")


@_attrs_define
class MLDetectionQueueRecordSchema:
    """
    Attributes:
        job_id (UUID):
        system_domain_id (UUID):
        user_id (UUID):
        bytes_params (Any | Unset):
        date_created (datetime.datetime | Unset):
        date_updated (datetime.datetime | Unset):
        id (UUID | Unset):
        object_id (None | Unset | UUID):
        object_type (None | str | Unset):
        params (None | str | Unset):
        parent_job_id (None | Unset | UUID):
        priority (int | None | Unset):
        retry_count (int | None | Unset):
        spec (None | str | Unset):
        status (None | str | Unset):
        system_name (str | Unset):
        type_ (None | str | Unset):
        version_id (None | Unset | UUID):
    """

    job_id: UUID
    system_domain_id: UUID
    user_id: UUID
    bytes_params: Any | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_updated: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    object_id: None | Unset | UUID = UNSET
    object_type: None | str | Unset = UNSET
    params: None | str | Unset = UNSET
    parent_job_id: None | Unset | UUID = UNSET
    priority: int | None | Unset = UNSET
    retry_count: int | None | Unset = UNSET
    spec: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    system_name: str | Unset = UNSET
    type_: None | str | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = str(self.job_id)

        system_domain_id = str(self.system_domain_id)

        user_id = str(self.user_id)

        bytes_params = self.bytes_params

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_updated: str | Unset = UNSET
        if not isinstance(self.date_updated, Unset):
            date_updated = self.date_updated.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        object_id: None | str | Unset
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        elif isinstance(self.object_id, UUID):
            object_id = str(self.object_id)
        else:
            object_id = self.object_id

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        params: None | str | Unset
        if isinstance(self.params, Unset):
            params = UNSET
        else:
            params = self.params

        parent_job_id: None | str | Unset
        if isinstance(self.parent_job_id, Unset):
            parent_job_id = UNSET
        elif isinstance(self.parent_job_id, UUID):
            parent_job_id = str(self.parent_job_id)
        else:
            parent_job_id = self.parent_job_id

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        retry_count: int | None | Unset
        if isinstance(self.retry_count, Unset):
            retry_count = UNSET
        else:
            retry_count = self.retry_count

        spec: None | str | Unset
        if isinstance(self.spec, Unset):
            spec = UNSET
        else:
            spec = self.spec

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        system_name = self.system_name

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        elif isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "system_domain_id": system_domain_id,
                "user_id": user_id,
            }
        )
        if bytes_params is not UNSET:
            field_dict["bytes_params"] = bytes_params
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_updated is not UNSET:
            field_dict["date_updated"] = date_updated
        if id is not UNSET:
            field_dict["id"] = id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if params is not UNSET:
            field_dict["params"] = params
        if parent_job_id is not UNSET:
            field_dict["parent_job_id"] = parent_job_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if spec is not UNSET:
            field_dict["spec"] = spec
        if status is not UNSET:
            field_dict["status"] = status
        if system_name is not UNSET:
            field_dict["system_name"] = system_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = UUID(d.pop("job_id"))

        system_domain_id = UUID(d.pop("system_domain_id"))

        user_id = UUID(d.pop("user_id"))

        bytes_params = d.pop("bytes_params", UNSET)

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

        def _parse_object_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_id_type_0 = UUID(data)

                return object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        object_id = _parse_object_id(d.pop("object_id", UNSET))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_params(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        params = _parse_params(d.pop("params", UNSET))

        def _parse_parent_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_job_id_type_0 = UUID(data)

                return parent_job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_job_id = _parse_parent_job_id(d.pop("parent_job_id", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_retry_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        retry_count = _parse_retry_count(d.pop("retry_count", UNSET))

        def _parse_spec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spec = _parse_spec(d.pop("spec", UNSET))

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        system_name = d.pop("system_name", UNSET)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                version_id_type_0 = UUID(data)

                return version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))

        ml_detection_queue_record_schema = cls(
            job_id=job_id,
            system_domain_id=system_domain_id,
            user_id=user_id,
            bytes_params=bytes_params,
            date_created=date_created,
            date_updated=date_updated,
            id=id,
            object_id=object_id,
            object_type=object_type,
            params=params,
            parent_job_id=parent_job_id,
            priority=priority,
            retry_count=retry_count,
            spec=spec,
            status=status,
            system_name=system_name,
            type_=type_,
            version_id=version_id,
        )

        ml_detection_queue_record_schema.additional_properties = d
        return ml_detection_queue_record_schema

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
