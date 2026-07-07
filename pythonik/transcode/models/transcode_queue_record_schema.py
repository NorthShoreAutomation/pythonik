from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscodeQueueRecordSchema")


@_attrs_define
class TranscodeQueueRecordSchema:
    """
    Attributes:
        bytes_params (Any | Unset):
        date_created (str | Unset):
        date_updated (str | Unset):
        id (UUID | Unset):
        job_id (None | Unset | UUID):
        media_info (None | str | Unset):
        object_id (None | Unset | UUID):
        object_type (None | str | Unset):
        params (None | str | Unset):
        priority (int | None | Unset):
        retry_count (int | None | Unset):
        spec (None | str | Unset):
        status (None | str | Unset):
        system_domain_id (None | Unset | UUID):
        system_name (str | Unset):
        transcoder_id (None | Unset | UUID):
        type_ (None | str | Unset):
        user_id (None | Unset | UUID):
        version_id (None | Unset | UUID):
    """

    bytes_params: Any | Unset = UNSET
    date_created: str | Unset = UNSET
    date_updated: str | Unset = UNSET
    id: UUID | Unset = UNSET
    job_id: None | Unset | UUID = UNSET
    media_info: None | str | Unset = UNSET
    object_id: None | Unset | UUID = UNSET
    object_type: None | str | Unset = UNSET
    params: None | str | Unset = UNSET
    priority: int | None | Unset = UNSET
    retry_count: int | None | Unset = UNSET
    spec: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    system_name: str | Unset = UNSET
    transcoder_id: None | Unset | UUID = UNSET
    type_: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bytes_params = self.bytes_params

        date_created = self.date_created

        date_updated = self.date_updated

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        elif isinstance(self.job_id, UUID):
            job_id = str(self.job_id)
        else:
            job_id = self.job_id

        media_info: None | str | Unset
        if isinstance(self.media_info, Unset):
            media_info = UNSET
        else:
            media_info = self.media_info

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

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        system_name = self.system_name

        transcoder_id: None | str | Unset
        if isinstance(self.transcoder_id, Unset):
            transcoder_id = UNSET
        elif isinstance(self.transcoder_id, UUID):
            transcoder_id = str(self.transcoder_id)
        else:
            transcoder_id = self.transcoder_id

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        elif isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bytes_params is not UNSET:
            field_dict["bytes_params"] = bytes_params
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_updated is not UNSET:
            field_dict["date_updated"] = date_updated
        if id is not UNSET:
            field_dict["id"] = id
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if media_info is not UNSET:
            field_dict["media_info"] = media_info
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if params is not UNSET:
            field_dict["params"] = params
        if priority is not UNSET:
            field_dict["priority"] = priority
        if retry_count is not UNSET:
            field_dict["retry_count"] = retry_count
        if spec is not UNSET:
            field_dict["spec"] = spec
        if status is not UNSET:
            field_dict["status"] = status
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if system_name is not UNSET:
            field_dict["system_name"] = system_name
        if transcoder_id is not UNSET:
            field_dict["transcoder_id"] = transcoder_id
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
        bytes_params = d.pop("bytes_params", UNSET)

        date_created = d.pop("date_created", UNSET)

        date_updated = d.pop("date_updated", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_id_type_0 = UUID(data)

                return job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

        def _parse_media_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_info = _parse_media_info(d.pop("media_info", UNSET))

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

        def _parse_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_id_type_0 = UUID(data)

                return system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

        system_name = d.pop("system_name", UNSET)

        def _parse_transcoder_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transcoder_id_type_0 = UUID(data)

                return transcoder_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        transcoder_id = _parse_transcoder_id(d.pop("transcoder_id", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

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

        transcode_queue_record_schema = cls(
            bytes_params=bytes_params,
            date_created=date_created,
            date_updated=date_updated,
            id=id,
            job_id=job_id,
            media_info=media_info,
            object_id=object_id,
            object_type=object_type,
            params=params,
            priority=priority,
            retry_count=retry_count,
            spec=spec,
            status=status,
            system_domain_id=system_domain_id,
            system_name=system_name,
            transcoder_id=transcoder_id,
            type_=type_,
            user_id=user_id,
            version_id=version_id,
        )

        transcode_queue_record_schema.additional_properties = d
        return transcode_queue_record_schema

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
