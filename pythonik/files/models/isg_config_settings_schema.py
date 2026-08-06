from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ISGConfigSettingsSchema")


@_attrs_define
class ISGConfigSettingsSchema:
    """
    Attributes:
        checksum_max_workers (int | None | Unset):
        file_download_parallel_downloads_num (int | None | Unset):
        file_upload_parallel_uploads_num (int | None | Unset):
        max_transcoding_jobs (int | None | Unset):
        scanner_concurrency_value (int | None | Unset):
    """

    checksum_max_workers: int | None | Unset = UNSET
    file_download_parallel_downloads_num: int | None | Unset = UNSET
    file_upload_parallel_uploads_num: int | None | Unset = UNSET
    max_transcoding_jobs: int | None | Unset = UNSET
    scanner_concurrency_value: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checksum_max_workers: int | None | Unset
        if isinstance(self.checksum_max_workers, Unset):
            checksum_max_workers = UNSET
        else:
            checksum_max_workers = self.checksum_max_workers

        file_download_parallel_downloads_num: int | None | Unset
        if isinstance(self.file_download_parallel_downloads_num, Unset):
            file_download_parallel_downloads_num = UNSET
        else:
            file_download_parallel_downloads_num = (
                self.file_download_parallel_downloads_num
            )

        file_upload_parallel_uploads_num: int | None | Unset
        if isinstance(self.file_upload_parallel_uploads_num, Unset):
            file_upload_parallel_uploads_num = UNSET
        else:
            file_upload_parallel_uploads_num = self.file_upload_parallel_uploads_num

        max_transcoding_jobs: int | None | Unset
        if isinstance(self.max_transcoding_jobs, Unset):
            max_transcoding_jobs = UNSET
        else:
            max_transcoding_jobs = self.max_transcoding_jobs

        scanner_concurrency_value: int | None | Unset
        if isinstance(self.scanner_concurrency_value, Unset):
            scanner_concurrency_value = UNSET
        else:
            scanner_concurrency_value = self.scanner_concurrency_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checksum_max_workers is not UNSET:
            field_dict["checksum_max_workers"] = checksum_max_workers
        if file_download_parallel_downloads_num is not UNSET:
            field_dict["file_download_parallel_downloads_num"] = (
                file_download_parallel_downloads_num
            )
        if file_upload_parallel_uploads_num is not UNSET:
            field_dict["file_upload_parallel_uploads_num"] = (
                file_upload_parallel_uploads_num
            )
        if max_transcoding_jobs is not UNSET:
            field_dict["max_transcoding_jobs"] = max_transcoding_jobs
        if scanner_concurrency_value is not UNSET:
            field_dict["scanner_concurrency_value"] = scanner_concurrency_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_checksum_max_workers(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        checksum_max_workers = _parse_checksum_max_workers(
            d.pop("checksum_max_workers", UNSET)
        )

        def _parse_file_download_parallel_downloads_num(
            data: object,
        ) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_download_parallel_downloads_num = (
            _parse_file_download_parallel_downloads_num(
                d.pop("file_download_parallel_downloads_num", UNSET)
            )
        )

        def _parse_file_upload_parallel_uploads_num(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        file_upload_parallel_uploads_num = _parse_file_upload_parallel_uploads_num(
            d.pop("file_upload_parallel_uploads_num", UNSET)
        )

        def _parse_max_transcoding_jobs(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_transcoding_jobs = _parse_max_transcoding_jobs(
            d.pop("max_transcoding_jobs", UNSET)
        )

        def _parse_scanner_concurrency_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        scanner_concurrency_value = _parse_scanner_concurrency_value(
            d.pop("scanner_concurrency_value", UNSET)
        )

        isg_config_settings_schema = cls(
            checksum_max_workers=checksum_max_workers,
            file_download_parallel_downloads_num=file_download_parallel_downloads_num,
            file_upload_parallel_uploads_num=file_upload_parallel_uploads_num,
            max_transcoding_jobs=max_transcoding_jobs,
            scanner_concurrency_value=scanner_concurrency_value,
        )

        isg_config_settings_schema.additional_properties = d
        return isg_config_settings_schema

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
