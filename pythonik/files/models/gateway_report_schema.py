from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.gateway_report_schema_start_status import GatewayReportSchemaStartStatus
from ..models.gateway_report_schema_status import GatewayReportSchemaStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayReportSchema")


@_attrs_define
class GatewayReportSchema:
    """
    Attributes:
        await_checksum_files_number (int | None | Unset):
        date_reported (datetime.datetime | Unset):
        empty_files_number (int | None | Unset):
        error_log_lines (list[str] | Unset):
        exported_files_number (int | None | Unset):
        faulty_files_number (int | None | Unset):
        host_info (str | Unset):
        host_name (str | Unset):
        id (UUID | Unset):
        ingested_files_number (int | None | Unset):
        ingested_files_uploads_number (int | None | Unset):
        ingesting_files_number (int | None | Unset):
        last_scan_time (int | None | Unset):
        log_lines (list[str] | Unset):
        logs_url (str | Unset):
        missing_files_number (int | None | Unset):
        scanned_files_number (int | None | Unset):
        skipped_files_number (int | None | Unset):
        start_last_date (datetime.datetime | Unset):
        start_status (GatewayReportSchemaStartStatus | Unset):
        start_status_message (str | Unset):
        status (GatewayReportSchemaStatus | Unset):
        storage_id (UUID | Unset):
        total_files_number (int | None | Unset):
        total_folders_number (int | None | Unset):
        version (str | Unset):
        waiting_preview_transcode_jobs_number (int | None | Unset):
        waiting_transcode_jobs_number (int | None | Unset):
    """

    await_checksum_files_number: int | None | Unset = UNSET
    date_reported: datetime.datetime | Unset = UNSET
    empty_files_number: int | None | Unset = UNSET
    error_log_lines: list[str] | Unset = UNSET
    exported_files_number: int | None | Unset = UNSET
    faulty_files_number: int | None | Unset = UNSET
    host_info: str | Unset = UNSET
    host_name: str | Unset = UNSET
    id: UUID | Unset = UNSET
    ingested_files_number: int | None | Unset = UNSET
    ingested_files_uploads_number: int | None | Unset = UNSET
    ingesting_files_number: int | None | Unset = UNSET
    last_scan_time: int | None | Unset = UNSET
    log_lines: list[str] | Unset = UNSET
    logs_url: str | Unset = UNSET
    missing_files_number: int | None | Unset = UNSET
    scanned_files_number: int | None | Unset = UNSET
    skipped_files_number: int | None | Unset = UNSET
    start_last_date: datetime.datetime | Unset = UNSET
    start_status: GatewayReportSchemaStartStatus | Unset = UNSET
    start_status_message: str | Unset = UNSET
    status: GatewayReportSchemaStatus | Unset = UNSET
    storage_id: UUID | Unset = UNSET
    total_files_number: int | None | Unset = UNSET
    total_folders_number: int | None | Unset = UNSET
    version: str | Unset = UNSET
    waiting_preview_transcode_jobs_number: int | None | Unset = UNSET
    waiting_transcode_jobs_number: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        await_checksum_files_number: int | None | Unset
        if isinstance(self.await_checksum_files_number, Unset):
            await_checksum_files_number = UNSET
        else:
            await_checksum_files_number = self.await_checksum_files_number

        date_reported: str | Unset = UNSET
        if not isinstance(self.date_reported, Unset):
            date_reported = self.date_reported.isoformat()

        empty_files_number: int | None | Unset
        if isinstance(self.empty_files_number, Unset):
            empty_files_number = UNSET
        else:
            empty_files_number = self.empty_files_number

        error_log_lines: list[str] | Unset = UNSET
        if not isinstance(self.error_log_lines, Unset):
            error_log_lines = self.error_log_lines

        exported_files_number: int | None | Unset
        if isinstance(self.exported_files_number, Unset):
            exported_files_number = UNSET
        else:
            exported_files_number = self.exported_files_number

        faulty_files_number: int | None | Unset
        if isinstance(self.faulty_files_number, Unset):
            faulty_files_number = UNSET
        else:
            faulty_files_number = self.faulty_files_number

        host_info = self.host_info

        host_name = self.host_name

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        ingested_files_number: int | None | Unset
        if isinstance(self.ingested_files_number, Unset):
            ingested_files_number = UNSET
        else:
            ingested_files_number = self.ingested_files_number

        ingested_files_uploads_number: int | None | Unset
        if isinstance(self.ingested_files_uploads_number, Unset):
            ingested_files_uploads_number = UNSET
        else:
            ingested_files_uploads_number = self.ingested_files_uploads_number

        ingesting_files_number: int | None | Unset
        if isinstance(self.ingesting_files_number, Unset):
            ingesting_files_number = UNSET
        else:
            ingesting_files_number = self.ingesting_files_number

        last_scan_time: int | None | Unset
        if isinstance(self.last_scan_time, Unset):
            last_scan_time = UNSET
        else:
            last_scan_time = self.last_scan_time

        log_lines: list[str] | Unset = UNSET
        if not isinstance(self.log_lines, Unset):
            log_lines = self.log_lines

        logs_url = self.logs_url

        missing_files_number: int | None | Unset
        if isinstance(self.missing_files_number, Unset):
            missing_files_number = UNSET
        else:
            missing_files_number = self.missing_files_number

        scanned_files_number: int | None | Unset
        if isinstance(self.scanned_files_number, Unset):
            scanned_files_number = UNSET
        else:
            scanned_files_number = self.scanned_files_number

        skipped_files_number: int | None | Unset
        if isinstance(self.skipped_files_number, Unset):
            skipped_files_number = UNSET
        else:
            skipped_files_number = self.skipped_files_number

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

        storage_id: str | Unset = UNSET
        if not isinstance(self.storage_id, Unset):
            storage_id = str(self.storage_id)

        total_files_number: int | None | Unset
        if isinstance(self.total_files_number, Unset):
            total_files_number = UNSET
        else:
            total_files_number = self.total_files_number

        total_folders_number: int | None | Unset
        if isinstance(self.total_folders_number, Unset):
            total_folders_number = UNSET
        else:
            total_folders_number = self.total_folders_number

        version = self.version

        waiting_preview_transcode_jobs_number: int | None | Unset
        if isinstance(self.waiting_preview_transcode_jobs_number, Unset):
            waiting_preview_transcode_jobs_number = UNSET
        else:
            waiting_preview_transcode_jobs_number = (
                self.waiting_preview_transcode_jobs_number
            )

        waiting_transcode_jobs_number: int | None | Unset
        if isinstance(self.waiting_transcode_jobs_number, Unset):
            waiting_transcode_jobs_number = UNSET
        else:
            waiting_transcode_jobs_number = self.waiting_transcode_jobs_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if await_checksum_files_number is not UNSET:
            field_dict["await_checksum_files_number"] = await_checksum_files_number
        if date_reported is not UNSET:
            field_dict["date_reported"] = date_reported
        if empty_files_number is not UNSET:
            field_dict["empty_files_number"] = empty_files_number
        if error_log_lines is not UNSET:
            field_dict["error_log_lines"] = error_log_lines
        if exported_files_number is not UNSET:
            field_dict["exported_files_number"] = exported_files_number
        if faulty_files_number is not UNSET:
            field_dict["faulty_files_number"] = faulty_files_number
        if host_info is not UNSET:
            field_dict["host_info"] = host_info
        if host_name is not UNSET:
            field_dict["host_name"] = host_name
        if id is not UNSET:
            field_dict["id"] = id
        if ingested_files_number is not UNSET:
            field_dict["ingested_files_number"] = ingested_files_number
        if ingested_files_uploads_number is not UNSET:
            field_dict["ingested_files_uploads_number"] = ingested_files_uploads_number
        if ingesting_files_number is not UNSET:
            field_dict["ingesting_files_number"] = ingesting_files_number
        if last_scan_time is not UNSET:
            field_dict["last_scan_time"] = last_scan_time
        if log_lines is not UNSET:
            field_dict["log_lines"] = log_lines
        if logs_url is not UNSET:
            field_dict["logs_url"] = logs_url
        if missing_files_number is not UNSET:
            field_dict["missing_files_number"] = missing_files_number
        if scanned_files_number is not UNSET:
            field_dict["scanned_files_number"] = scanned_files_number
        if skipped_files_number is not UNSET:
            field_dict["skipped_files_number"] = skipped_files_number
        if start_last_date is not UNSET:
            field_dict["start_last_date"] = start_last_date
        if start_status is not UNSET:
            field_dict["start_status"] = start_status
        if start_status_message is not UNSET:
            field_dict["start_status_message"] = start_status_message
        if status is not UNSET:
            field_dict["status"] = status
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if total_files_number is not UNSET:
            field_dict["total_files_number"] = total_files_number
        if total_folders_number is not UNSET:
            field_dict["total_folders_number"] = total_folders_number
        if version is not UNSET:
            field_dict["version"] = version
        if waiting_preview_transcode_jobs_number is not UNSET:
            field_dict["waiting_preview_transcode_jobs_number"] = (
                waiting_preview_transcode_jobs_number
            )
        if waiting_transcode_jobs_number is not UNSET:
            field_dict["waiting_transcode_jobs_number"] = waiting_transcode_jobs_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_await_checksum_files_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        await_checksum_files_number = _parse_await_checksum_files_number(
            d.pop("await_checksum_files_number", UNSET)
        )

        _date_reported = d.pop("date_reported", UNSET)
        date_reported: datetime.datetime | Unset
        if isinstance(_date_reported, Unset):
            date_reported = UNSET
        else:
            date_reported = datetime.datetime.fromisoformat(_date_reported)

        def _parse_empty_files_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        empty_files_number = _parse_empty_files_number(
            d.pop("empty_files_number", UNSET)
        )

        error_log_lines = cast(list[str], d.pop("error_log_lines", UNSET))

        def _parse_exported_files_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        exported_files_number = _parse_exported_files_number(
            d.pop("exported_files_number", UNSET)
        )

        def _parse_faulty_files_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        faulty_files_number = _parse_faulty_files_number(
            d.pop("faulty_files_number", UNSET)
        )

        host_info = d.pop("host_info", UNSET)

        host_name = d.pop("host_name", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_ingested_files_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ingested_files_number = _parse_ingested_files_number(
            d.pop("ingested_files_number", UNSET)
        )

        def _parse_ingested_files_uploads_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ingested_files_uploads_number = _parse_ingested_files_uploads_number(
            d.pop("ingested_files_uploads_number", UNSET)
        )

        def _parse_ingesting_files_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        ingesting_files_number = _parse_ingesting_files_number(
            d.pop("ingesting_files_number", UNSET)
        )

        def _parse_last_scan_time(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_scan_time = _parse_last_scan_time(d.pop("last_scan_time", UNSET))

        log_lines = cast(list[str], d.pop("log_lines", UNSET))

        logs_url = d.pop("logs_url", UNSET)

        def _parse_missing_files_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        missing_files_number = _parse_missing_files_number(
            d.pop("missing_files_number", UNSET)
        )

        def _parse_scanned_files_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scanned_files_number = _parse_scanned_files_number(
            d.pop("scanned_files_number", UNSET)
        )

        def _parse_skipped_files_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        skipped_files_number = _parse_skipped_files_number(
            d.pop("skipped_files_number", UNSET)
        )

        _start_last_date = d.pop("start_last_date", UNSET)
        start_last_date: datetime.datetime | Unset
        if isinstance(_start_last_date, Unset):
            start_last_date = UNSET
        else:
            start_last_date = datetime.datetime.fromisoformat(_start_last_date)

        _start_status = d.pop("start_status", UNSET)
        start_status: GatewayReportSchemaStartStatus | Unset
        if isinstance(_start_status, Unset):
            start_status = UNSET
        else:
            start_status = GatewayReportSchemaStartStatus(_start_status)

        start_status_message = d.pop("start_status_message", UNSET)

        _status = d.pop("status", UNSET)
        status: GatewayReportSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GatewayReportSchemaStatus(_status)

        _storage_id = d.pop("storage_id", UNSET)
        storage_id: UUID | Unset
        if isinstance(_storage_id, Unset):
            storage_id = UNSET
        else:
            storage_id = UUID(_storage_id)

        def _parse_total_files_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_files_number = _parse_total_files_number(
            d.pop("total_files_number", UNSET)
        )

        def _parse_total_folders_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_folders_number = _parse_total_folders_number(
            d.pop("total_folders_number", UNSET)
        )

        version = d.pop("version", UNSET)

        def _parse_waiting_preview_transcode_jobs_number(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        waiting_preview_transcode_jobs_number = (
            _parse_waiting_preview_transcode_jobs_number(
                d.pop("waiting_preview_transcode_jobs_number", UNSET)
            )
        )

        def _parse_waiting_transcode_jobs_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        waiting_transcode_jobs_number = _parse_waiting_transcode_jobs_number(
            d.pop("waiting_transcode_jobs_number", UNSET)
        )

        gateway_report_schema = cls(
            await_checksum_files_number=await_checksum_files_number,
            date_reported=date_reported,
            empty_files_number=empty_files_number,
            error_log_lines=error_log_lines,
            exported_files_number=exported_files_number,
            faulty_files_number=faulty_files_number,
            host_info=host_info,
            host_name=host_name,
            id=id,
            ingested_files_number=ingested_files_number,
            ingested_files_uploads_number=ingested_files_uploads_number,
            ingesting_files_number=ingesting_files_number,
            last_scan_time=last_scan_time,
            log_lines=log_lines,
            logs_url=logs_url,
            missing_files_number=missing_files_number,
            scanned_files_number=scanned_files_number,
            skipped_files_number=skipped_files_number,
            start_last_date=start_last_date,
            start_status=start_status,
            start_status_message=start_status_message,
            status=status,
            storage_id=storage_id,
            total_files_number=total_files_number,
            total_folders_number=total_folders_number,
            version=version,
            waiting_preview_transcode_jobs_number=waiting_preview_transcode_jobs_number,
            waiting_transcode_jobs_number=waiting_transcode_jobs_number,
        )

        gateway_report_schema.additional_properties = d
        return gateway_report_schema

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
