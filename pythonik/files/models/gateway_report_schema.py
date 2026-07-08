from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_report_schema_start_status_type_1 import (
        GatewayReportSchemaStartStatusType1,
    )
    from ..models.gateway_report_schema_status_type_1 import (
        GatewayReportSchemaStatusType1,
    )


T = TypeVar("T", bound="GatewayReportSchema")


@_attrs_define
class GatewayReportSchema:
    """
    Attributes:
        await_checksum_files_number (int | None | Unset):
        date_reported (datetime.datetime | None | Unset):
        empty_files_number (int | None | Unset):
        error_log_lines (list[str] | None | Unset):
        exported_files_number (int | None | Unset):
        faulty_files_number (int | None | Unset):
        host_info (None | str | Unset):
        host_name (None | str | Unset):
        id (None | Unset | UUID):
        ingested_files_number (int | None | Unset):
        ingested_files_uploads_number (int | None | Unset):
        ingesting_files_number (int | None | Unset):
        last_scan_time (int | None | Unset):
        log_lines (list[str] | None | Unset):
        logs_url (None | str | Unset):
        missing_files_number (int | None | Unset):
        scanned_files_number (int | None | Unset):
        skipped_files_number (int | None | Unset):
        start_last_date (datetime.datetime | None | Unset):
        start_status (GatewayReportSchemaStartStatusType1 | None | Unset):
        start_status_message (None | str | Unset):
        status (GatewayReportSchemaStatusType1 | None | Unset):
        storage_id (None | Unset | UUID):
        total_files_number (int | None | Unset):
        total_folders_number (int | None | Unset):
        version (None | str | Unset):
        waiting_preview_transcode_jobs_number (int | None | Unset):
        waiting_transcode_jobs_number (int | None | Unset):
    """

    await_checksum_files_number: int | None | Unset = UNSET
    date_reported: datetime.datetime | None | Unset = UNSET
    empty_files_number: int | None | Unset = UNSET
    error_log_lines: list[str] | None | Unset = UNSET
    exported_files_number: int | None | Unset = UNSET
    faulty_files_number: int | None | Unset = UNSET
    host_info: None | str | Unset = UNSET
    host_name: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    ingested_files_number: int | None | Unset = UNSET
    ingested_files_uploads_number: int | None | Unset = UNSET
    ingesting_files_number: int | None | Unset = UNSET
    last_scan_time: int | None | Unset = UNSET
    log_lines: list[str] | None | Unset = UNSET
    logs_url: None | str | Unset = UNSET
    missing_files_number: int | None | Unset = UNSET
    scanned_files_number: int | None | Unset = UNSET
    skipped_files_number: int | None | Unset = UNSET
    start_last_date: datetime.datetime | None | Unset = UNSET
    start_status: GatewayReportSchemaStartStatusType1 | None | Unset = UNSET
    start_status_message: None | str | Unset = UNSET
    status: GatewayReportSchemaStatusType1 | None | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    total_files_number: int | None | Unset = UNSET
    total_folders_number: int | None | Unset = UNSET
    version: None | str | Unset = UNSET
    waiting_preview_transcode_jobs_number: int | None | Unset = UNSET
    waiting_transcode_jobs_number: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.gateway_report_schema_start_status_type_1 import (
            GatewayReportSchemaStartStatusType1,
        )
        from ..models.gateway_report_schema_status_type_1 import (
            GatewayReportSchemaStatusType1,
        )

        await_checksum_files_number: int | None | Unset
        if isinstance(self.await_checksum_files_number, Unset):
            await_checksum_files_number = UNSET
        else:
            await_checksum_files_number = self.await_checksum_files_number

        date_reported: None | str | Unset
        if isinstance(self.date_reported, Unset):
            date_reported = UNSET
        elif isinstance(self.date_reported, datetime.datetime):
            date_reported = self.date_reported.isoformat()
        else:
            date_reported = self.date_reported

        empty_files_number: int | None | Unset
        if isinstance(self.empty_files_number, Unset):
            empty_files_number = UNSET
        else:
            empty_files_number = self.empty_files_number

        error_log_lines: list[str] | None | Unset
        if isinstance(self.error_log_lines, Unset):
            error_log_lines = UNSET
        elif isinstance(self.error_log_lines, list):
            error_log_lines = self.error_log_lines

        else:
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

        host_info: None | str | Unset
        if isinstance(self.host_info, Unset):
            host_info = UNSET
        else:
            host_info = self.host_info

        host_name: None | str | Unset
        if isinstance(self.host_name, Unset):
            host_name = UNSET
        else:
            host_name = self.host_name

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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

        log_lines: list[str] | None | Unset
        if isinstance(self.log_lines, Unset):
            log_lines = UNSET
        elif isinstance(self.log_lines, list):
            log_lines = self.log_lines

        else:
            log_lines = self.log_lines

        logs_url: None | str | Unset
        if isinstance(self.logs_url, Unset):
            logs_url = UNSET
        else:
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
        elif isinstance(self.start_status, GatewayReportSchemaStartStatusType1):
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
        elif isinstance(self.status, GatewayReportSchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

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

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
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
        from ..models.gateway_report_schema_start_status_type_1 import (
            GatewayReportSchemaStartStatusType1,
        )
        from ..models.gateway_report_schema_status_type_1 import (
            GatewayReportSchemaStatusType1,
        )

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

        def _parse_date_reported(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_reported_type_0 = datetime.datetime.fromisoformat(data)

                return date_reported_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_reported = _parse_date_reported(d.pop("date_reported", UNSET))

        def _parse_empty_files_number(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        empty_files_number = _parse_empty_files_number(
            d.pop("empty_files_number", UNSET)
        )

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

        def _parse_host_info(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_info = _parse_host_info(d.pop("host_info", UNSET))

        def _parse_host_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_name = _parse_host_name(d.pop("host_name", UNSET))

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

        def _parse_logs_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logs_url = _parse_logs_url(d.pop("logs_url", UNSET))

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
        ) -> GatewayReportSchemaStartStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                start_status_type_1 = GatewayReportSchemaStartStatusType1.from_dict(
                    data
                )

                return start_status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GatewayReportSchemaStartStatusType1 | None | Unset, data)

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
        ) -> GatewayReportSchemaStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = GatewayReportSchemaStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GatewayReportSchemaStatusType1 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_id_type_0 = UUID(data)

                return storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        storage_id = _parse_storage_id(d.pop("storage_id", UNSET))

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

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

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
