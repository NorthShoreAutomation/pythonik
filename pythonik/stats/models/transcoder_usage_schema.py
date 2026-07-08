from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transcoder_usage_schema_operation_type import (
    TranscoderUsageSchemaOperationType,
)
from ..models.transcoder_usage_schema_status import TranscoderUsageSchemaStatus
from ..models.transcoder_usage_schema_transcoder_type import (
    TranscoderUsageSchemaTranscoderType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="TranscoderUsageSchema")


@_attrs_define
class TranscoderUsageSchema:
    """
    Attributes:
        status (TranscoderUsageSchemaStatus):
        system_name (str):
        transcoder_type (TranscoderUsageSchemaTranscoderType):
        adjusted_duration_seconds (int | None | Unset):
        date (datetime.date | None | Unset):
        destination_bytes (int | None | Unset):
        duration_seconds (int | None | Unset):
        id (None | Unset | UUID):
        is_user_transcoder (bool | None | Unset):
        job_id (None | Unset | UUID):
        object_id (None | Unset | UUID):
        object_type (None | str | Unset):
        operation_type (None | TranscoderUsageSchemaOperationType | Unset):
        percent_done (int | None | Unset):
        source_bytes (int | None | Unset):
        system_domain_id (None | Unset | UUID):
        time (datetime.datetime | None | Unset):
    """

    status: TranscoderUsageSchemaStatus
    system_name: str
    transcoder_type: TranscoderUsageSchemaTranscoderType
    adjusted_duration_seconds: int | None | Unset = UNSET
    date: datetime.date | None | Unset = UNSET
    destination_bytes: int | None | Unset = UNSET
    duration_seconds: int | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    is_user_transcoder: bool | None | Unset = UNSET
    job_id: None | Unset | UUID = UNSET
    object_id: None | Unset | UUID = UNSET
    object_type: None | str | Unset = UNSET
    operation_type: None | TranscoderUsageSchemaOperationType | Unset = UNSET
    percent_done: int | None | Unset = UNSET
    source_bytes: int | None | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        system_name = self.system_name

        transcoder_type = self.transcoder_type.value

        adjusted_duration_seconds: int | None | Unset
        if isinstance(self.adjusted_duration_seconds, Unset):
            adjusted_duration_seconds = UNSET
        else:
            adjusted_duration_seconds = self.adjusted_duration_seconds

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        destination_bytes: int | None | Unset
        if isinstance(self.destination_bytes, Unset):
            destination_bytes = UNSET
        else:
            destination_bytes = self.destination_bytes

        duration_seconds: int | None | Unset
        if isinstance(self.duration_seconds, Unset):
            duration_seconds = UNSET
        else:
            duration_seconds = self.duration_seconds

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_user_transcoder: bool | None | Unset
        if isinstance(self.is_user_transcoder, Unset):
            is_user_transcoder = UNSET
        else:
            is_user_transcoder = self.is_user_transcoder

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        elif isinstance(self.job_id, UUID):
            job_id = str(self.job_id)
        else:
            job_id = self.job_id

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

        operation_type: None | str | Unset
        if isinstance(self.operation_type, Unset):
            operation_type = UNSET
        elif isinstance(self.operation_type, TranscoderUsageSchemaOperationType):
            operation_type = self.operation_type.value
        else:
            operation_type = self.operation_type

        percent_done: int | None | Unset
        if isinstance(self.percent_done, Unset):
            percent_done = UNSET
        else:
            percent_done = self.percent_done

        source_bytes: int | None | Unset
        if isinstance(self.source_bytes, Unset):
            source_bytes = UNSET
        else:
            source_bytes = self.source_bytes

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "system_name": system_name,
                "transcoder_type": transcoder_type,
            }
        )
        if adjusted_duration_seconds is not UNSET:
            field_dict["adjusted_duration_seconds"] = adjusted_duration_seconds
        if date is not UNSET:
            field_dict["date"] = date
        if destination_bytes is not UNSET:
            field_dict["destination_bytes"] = destination_bytes
        if duration_seconds is not UNSET:
            field_dict["duration_seconds"] = duration_seconds
        if id is not UNSET:
            field_dict["id"] = id
        if is_user_transcoder is not UNSET:
            field_dict["is_user_transcoder"] = is_user_transcoder
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if operation_type is not UNSET:
            field_dict["operation_type"] = operation_type
        if percent_done is not UNSET:
            field_dict["percent_done"] = percent_done
        if source_bytes is not UNSET:
            field_dict["source_bytes"] = source_bytes
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = TranscoderUsageSchemaStatus(d.pop("status"))

        system_name = d.pop("system_name")

        transcoder_type = TranscoderUsageSchemaTranscoderType(d.pop("transcoder_type"))

        def _parse_adjusted_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        adjusted_duration_seconds = _parse_adjusted_duration_seconds(
            d.pop("adjusted_duration_seconds", UNSET)
        )

        def _parse_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = datetime.date.fromisoformat(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_destination_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        destination_bytes = _parse_destination_bytes(d.pop("destination_bytes", UNSET))

        def _parse_duration_seconds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_is_user_transcoder(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_user_transcoder = _parse_is_user_transcoder(
            d.pop("is_user_transcoder", UNSET)
        )

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

        def _parse_operation_type(
            data: object,
        ) -> None | TranscoderUsageSchemaOperationType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operation_type_type_1 = TranscoderUsageSchemaOperationType(data)

                return operation_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TranscoderUsageSchemaOperationType | Unset, data)

        operation_type = _parse_operation_type(d.pop("operation_type", UNSET))

        def _parse_percent_done(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        percent_done = _parse_percent_done(d.pop("percent_done", UNSET))

        def _parse_source_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source_bytes = _parse_source_bytes(d.pop("source_bytes", UNSET))

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

        def _parse_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_type_0 = datetime.datetime.fromisoformat(data)

                return time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time = _parse_time(d.pop("time", UNSET))

        transcoder_usage_schema = cls(
            status=status,
            system_name=system_name,
            transcoder_type=transcoder_type,
            adjusted_duration_seconds=adjusted_duration_seconds,
            date=date,
            destination_bytes=destination_bytes,
            duration_seconds=duration_seconds,
            id=id,
            is_user_transcoder=is_user_transcoder,
            job_id=job_id,
            object_id=object_id,
            object_type=object_type,
            operation_type=operation_type,
            percent_done=percent_done,
            source_bytes=source_bytes,
            system_domain_id=system_domain_id,
            time=time,
        )

        transcoder_usage_schema.additional_properties = d
        return transcoder_usage_schema

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
