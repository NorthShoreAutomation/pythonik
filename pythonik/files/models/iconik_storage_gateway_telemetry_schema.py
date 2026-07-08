from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iconik_storage_gateway_telemetry_schema_start_status_type_1 import (
        IconikStorageGatewayTelemetrySchemaStartStatusType1,
    )
    from ..models.iconik_storage_gateway_telemetry_schema_status_type_1 import (
        IconikStorageGatewayTelemetrySchemaStatusType1,
    )


T = TypeVar("T", bound="IconikStorageGatewayTelemetrySchema")


@_attrs_define
class IconikStorageGatewayTelemetrySchema:
    """
    Attributes:
        worker_id (UUID):
        error_log_lines (list[str] | None | Unset):
        host_info (None | str | Unset):
        host_ip (None | str | Unset):
        host_name (None | str | Unset):
        is_leader (bool | None | Unset):
        log_lines (list[str] | None | Unset):
        start_last_date (datetime.datetime | None | Unset):
        start_status (IconikStorageGatewayTelemetrySchemaStartStatusType1 | None | Unset):
        start_status_message (None | str | Unset):
        status (IconikStorageGatewayTelemetrySchemaStatusType1 | None | Unset):
        storage_gateway_id (None | Unset | UUID):
        version (None | str | Unset):
    """

    worker_id: UUID
    error_log_lines: list[str] | None | Unset = UNSET
    host_info: None | str | Unset = UNSET
    host_ip: None | str | Unset = UNSET
    host_name: None | str | Unset = UNSET
    is_leader: bool | None | Unset = UNSET
    log_lines: list[str] | None | Unset = UNSET
    start_last_date: datetime.datetime | None | Unset = UNSET
    start_status: IconikStorageGatewayTelemetrySchemaStartStatusType1 | None | Unset = (
        UNSET
    )
    start_status_message: None | str | Unset = UNSET
    status: IconikStorageGatewayTelemetrySchemaStatusType1 | None | Unset = UNSET
    storage_gateway_id: None | Unset | UUID = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.iconik_storage_gateway_telemetry_schema_start_status_type_1 import (
            IconikStorageGatewayTelemetrySchemaStartStatusType1,
        )
        from ..models.iconik_storage_gateway_telemetry_schema_status_type_1 import (
            IconikStorageGatewayTelemetrySchemaStatusType1,
        )

        worker_id = str(self.worker_id)

        error_log_lines: list[str] | None | Unset
        if isinstance(self.error_log_lines, Unset):
            error_log_lines = UNSET
        elif isinstance(self.error_log_lines, list):
            error_log_lines = self.error_log_lines

        else:
            error_log_lines = self.error_log_lines

        host_info: None | str | Unset
        if isinstance(self.host_info, Unset):
            host_info = UNSET
        else:
            host_info = self.host_info

        host_ip: None | str | Unset
        if isinstance(self.host_ip, Unset):
            host_ip = UNSET
        else:
            host_ip = self.host_ip

        host_name: None | str | Unset
        if isinstance(self.host_name, Unset):
            host_name = UNSET
        else:
            host_name = self.host_name

        is_leader: bool | None | Unset
        if isinstance(self.is_leader, Unset):
            is_leader = UNSET
        else:
            is_leader = self.is_leader

        log_lines: list[str] | None | Unset
        if isinstance(self.log_lines, Unset):
            log_lines = UNSET
        elif isinstance(self.log_lines, list):
            log_lines = self.log_lines

        else:
            log_lines = self.log_lines

        start_last_date: None | str | Unset
        if isinstance(self.start_last_date, Unset):
            start_last_date = UNSET
        elif isinstance(self.start_last_date, datetime.datetime):
            start_last_date = self.start_last_date.isoformat()
        else:
            start_last_date = self.start_last_date

        start_status: dict[str, Any] | None | Unset
        if isinstance(self.start_status, Unset):
            start_status = UNSET
        elif isinstance(
            self.start_status, IconikStorageGatewayTelemetrySchemaStartStatusType1
        ):
            start_status = self.start_status.to_dict()
        else:
            start_status = self.start_status

        start_status_message: None | str | Unset
        if isinstance(self.start_status_message, Unset):
            start_status_message = UNSET
        else:
            start_status_message = self.start_status_message

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, IconikStorageGatewayTelemetrySchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

        storage_gateway_id: None | str | Unset
        if isinstance(self.storage_gateway_id, Unset):
            storage_gateway_id = UNSET
        elif isinstance(self.storage_gateway_id, UUID):
            storage_gateway_id = str(self.storage_gateway_id)
        else:
            storage_gateway_id = self.storage_gateway_id

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "worker_id": worker_id,
            }
        )
        if error_log_lines is not UNSET:
            field_dict["error_log_lines"] = error_log_lines
        if host_info is not UNSET:
            field_dict["host_info"] = host_info
        if host_ip is not UNSET:
            field_dict["host_ip"] = host_ip
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if is_leader is not UNSET:
            field_dict["is_leader"] = is_leader
        if log_lines is not UNSET:
            field_dict["log_lines"] = log_lines
        if start_last_date is not UNSET:
            field_dict["start_last_date"] = start_last_date
        if start_status is not UNSET:
            field_dict["start_status"] = start_status
        if start_status_message is not UNSET:
            field_dict["start_status_message"] = start_status_message
        if status is not UNSET:
            field_dict["status"] = status
        if storage_gateway_id is not UNSET:
            field_dict["storage_gateway_id"] = storage_gateway_id
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iconik_storage_gateway_telemetry_schema_start_status_type_1 import (
            IconikStorageGatewayTelemetrySchemaStartStatusType1,
        )
        from ..models.iconik_storage_gateway_telemetry_schema_status_type_1 import (
            IconikStorageGatewayTelemetrySchemaStatusType1,
        )

        d = dict(src_dict)
        worker_id = UUID(d.pop("worker_id"))

        def _parse_error_log_lines(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                error_log_lines_type_0 = cast(list[str], data)

                return error_log_lines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        error_log_lines = _parse_error_log_lines(d.pop("error_log_lines", UNSET))

        def _parse_host_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_info = _parse_host_info(d.pop("host_info", UNSET))

        def _parse_host_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_ip = _parse_host_ip(d.pop("host_ip", UNSET))

        def _parse_host_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_name = _parse_host_name(d.pop("host_name", UNSET))

        def _parse_is_leader(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_leader = _parse_is_leader(d.pop("is_leader", UNSET))

        def _parse_log_lines(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                log_lines_type_0 = cast(list[str], data)

                return log_lines_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        log_lines = _parse_log_lines(d.pop("log_lines", UNSET))

        def _parse_start_last_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_last_date_type_0 = datetime.datetime.fromisoformat(data)

                return start_last_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        start_last_date = _parse_start_last_date(d.pop("start_last_date", UNSET))

        def _parse_start_status(
            data: object,
        ) -> IconikStorageGatewayTelemetrySchemaStartStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                start_status_type_1 = (
                    IconikStorageGatewayTelemetrySchemaStartStatusType1.from_dict(data)
                )

                return start_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                IconikStorageGatewayTelemetrySchemaStartStatusType1 | None | Unset, data
            )

        start_status = _parse_start_status(d.pop("start_status", UNSET))

        def _parse_start_status_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_status_message = _parse_start_status_message(
            d.pop("start_status_message", UNSET)
        )

        def _parse_status(
            data: object,
        ) -> IconikStorageGatewayTelemetrySchemaStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = (
                    IconikStorageGatewayTelemetrySchemaStatusType1.from_dict(data)
                )

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                IconikStorageGatewayTelemetrySchemaStatusType1 | None | Unset, data
            )

        status = _parse_status(d.pop("status", UNSET))

        def _parse_storage_gateway_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_gateway_id_type_0 = UUID(data)

                return storage_gateway_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        storage_gateway_id = _parse_storage_gateway_id(
            d.pop("storage_gateway_id", UNSET)
        )

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        iconik_storage_gateway_telemetry_schema = cls(
            worker_id=worker_id,
            error_log_lines=error_log_lines,
            host_info=host_info,
            host_ip=host_ip,
            host_name=host_name,
            is_leader=is_leader,
            log_lines=log_lines,
            start_last_date=start_last_date,
            start_status=start_status,
            start_status_message=start_status_message,
            status=status,
            storage_gateway_id=storage_gateway_id,
            version=version,
        )

        iconik_storage_gateway_telemetry_schema.additional_properties = d
        return iconik_storage_gateway_telemetry_schema

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
