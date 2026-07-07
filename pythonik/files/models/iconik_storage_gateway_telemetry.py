from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.iconik_storage_gateway_telemetry_start_status import (
    IconikStorageGatewayTelemetryStartStatus,
)
from ..models.iconik_storage_gateway_telemetry_status import (
    IconikStorageGatewayTelemetryStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="IconikStorageGatewayTelemetry")


@_attrs_define
class IconikStorageGatewayTelemetry:
    """
    Attributes:
        worker_id (UUID):
        error_log_lines (list[str] | Unset):
        host_info (str | Unset):
        host_ip (str | Unset):
        host_name (str | Unset):
        is_leader (bool | Unset):
        log_lines (list[str] | Unset):
        start_last_date (datetime.datetime | Unset):
        start_status (IconikStorageGatewayTelemetryStartStatus | Unset):
        start_status_message (str | Unset):
        status (IconikStorageGatewayTelemetryStatus | Unset):
        storage_gateway_id (UUID | Unset):
        version (str | Unset):
    """

    worker_id: UUID
    error_log_lines: list[str] | Unset = UNSET
    host_info: str | Unset = UNSET
    host_ip: str | Unset = UNSET
    host_name: str | Unset = UNSET
    is_leader: bool | Unset = UNSET
    log_lines: list[str] | Unset = UNSET
    start_last_date: datetime.datetime | Unset = UNSET
    start_status: IconikStorageGatewayTelemetryStartStatus | Unset = UNSET
    start_status_message: str | Unset = UNSET
    status: IconikStorageGatewayTelemetryStatus | Unset = UNSET
    storage_gateway_id: UUID | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        worker_id = str(self.worker_id)

        error_log_lines: list[str] | Unset = UNSET
        if not isinstance(self.error_log_lines, Unset):
            error_log_lines = self.error_log_lines

        host_info = self.host_info

        host_ip = self.host_ip

        host_name = self.host_name

        is_leader = self.is_leader

        log_lines: list[str] | Unset = UNSET
        if not isinstance(self.log_lines, Unset):
            log_lines = self.log_lines

        start_last_date: str | Unset = UNSET
        if not isinstance(self.start_last_date, Unset):
            start_last_date = self.start_last_date.isoformat()

        start_status: str | Unset = UNSET
        if not isinstance(self.start_status, Unset):
            start_status = self.start_status.value

        start_status_message = self.start_status_message

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_gateway_id: str | Unset = UNSET
        if not isinstance(self.storage_gateway_id, Unset):
            storage_gateway_id = str(self.storage_gateway_id)

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
        d = dict(src_dict)
        worker_id = UUID(d.pop("worker_id"))

        error_log_lines = cast(list[str], d.pop("error_log_lines", UNSET))

        host_info = d.pop("host_info", UNSET)

        host_ip = d.pop("host_ip", UNSET)

        host_name = d.pop("host_name", UNSET)

        is_leader = d.pop("is_leader", UNSET)

        log_lines = cast(list[str], d.pop("log_lines", UNSET))

        _start_last_date = d.pop("start_last_date", UNSET)
        start_last_date: datetime.datetime | Unset
        if isinstance(_start_last_date, Unset):
            start_last_date = UNSET
        else:
            start_last_date = datetime.datetime.fromisoformat(_start_last_date)

        _start_status = d.pop("start_status", UNSET)
        start_status: IconikStorageGatewayTelemetryStartStatus | Unset
        if isinstance(_start_status, Unset):
            start_status = UNSET
        else:
            start_status = IconikStorageGatewayTelemetryStartStatus(_start_status)

        start_status_message = d.pop("start_status_message", UNSET)

        _status = d.pop("status", UNSET)
        status: IconikStorageGatewayTelemetryStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IconikStorageGatewayTelemetryStatus(_status)

        _storage_gateway_id = d.pop("storage_gateway_id", UNSET)
        storage_gateway_id: UUID | Unset
        if isinstance(_storage_gateway_id, Unset):
            storage_gateway_id = UNSET
        else:
            storage_gateway_id = UUID(_storage_gateway_id)

        version = d.pop("version", UNSET)

        iconik_storage_gateway_telemetry = cls(
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

        iconik_storage_gateway_telemetry.additional_properties = d
        return iconik_storage_gateway_telemetry

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
