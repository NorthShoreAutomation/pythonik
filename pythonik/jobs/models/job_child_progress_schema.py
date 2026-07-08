from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_child_progress_schema_status import JobChildProgressSchemaStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobChildProgressSchema")


@_attrs_define
class JobChildProgressSchema:
    """
    Attributes:
        progress_processed (int | None | Unset):
        progress_total (int | None | Unset):
        status (JobChildProgressSchemaStatus | None | Unset):
    """

    progress_processed: int | None | Unset = UNSET
    progress_total: int | None | Unset = UNSET
    status: JobChildProgressSchemaStatus | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        progress_processed: int | None | Unset
        if isinstance(self.progress_processed, Unset):
            progress_processed = UNSET
        else:
            progress_processed = self.progress_processed

        progress_total: int | None | Unset
        if isinstance(self.progress_total, Unset):
            progress_total = UNSET
        else:
            progress_total = self.progress_total

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, JobChildProgressSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if progress_processed is not UNSET:
            field_dict["progress_processed"] = progress_processed
        if progress_total is not UNSET:
            field_dict["progress_total"] = progress_total
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_progress_processed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        progress_processed = _parse_progress_processed(
            d.pop("progress_processed", UNSET)
        )

        def _parse_progress_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        progress_total = _parse_progress_total(d.pop("progress_total", UNSET))

        def _parse_status(data: object) -> JobChildProgressSchemaStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = JobChildProgressSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobChildProgressSchemaStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        job_child_progress_schema = cls(
            progress_processed=progress_processed,
            progress_total=progress_total,
            status=status,
        )

        job_child_progress_schema.additional_properties = d
        return job_child_progress_schema

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
