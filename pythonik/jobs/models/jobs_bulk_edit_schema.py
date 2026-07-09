from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jobs_bulk_edit_schema_status import JobsBulkEditSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jobs_bulk_edit_schema_job_context_type_0 import (
        JobsBulkEditSchemaJobContextType0,
    )
    from ..models.jobs_bulk_edit_schema_metadata_type_0 import (
        JobsBulkEditSchemaMetadataType0,
    )


T = TypeVar("T", bound="JobsBulkEditSchema")


@_attrs_define
class JobsBulkEditSchema:
    """
    Attributes:
        error_message (None | str | Unset):
        job_context (JobsBulkEditSchemaJobContextType0 | None | Unset):
        message (None | str | Unset):
        metadata (JobsBulkEditSchemaMetadataType0 | None | Unset):
        status (JobsBulkEditSchemaStatus | None | Unset):
    """

    error_message: None | str | Unset = UNSET
    job_context: JobsBulkEditSchemaJobContextType0 | None | Unset = UNSET
    message: None | str | Unset = UNSET
    metadata: JobsBulkEditSchemaMetadataType0 | None | Unset = UNSET
    status: JobsBulkEditSchemaStatus | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.jobs_bulk_edit_schema_job_context_type_0 import (
            JobsBulkEditSchemaJobContextType0,
        )
        from ..models.jobs_bulk_edit_schema_metadata_type_0 import (
            JobsBulkEditSchemaMetadataType0,
        )

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        job_context: dict[str, Any] | None | Unset
        if isinstance(self.job_context, Unset):
            job_context = UNSET
        elif isinstance(self.job_context, JobsBulkEditSchemaJobContextType0):
            job_context = self.job_context.to_dict()
        else:
            job_context = self.job_context

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, JobsBulkEditSchemaMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, JobsBulkEditSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if job_context is not UNSET:
            field_dict["job_context"] = job_context
        if message is not UNSET:
            field_dict["message"] = message
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jobs_bulk_edit_schema_job_context_type_0 import (
            JobsBulkEditSchemaJobContextType0,
        )
        from ..models.jobs_bulk_edit_schema_metadata_type_0 import (
            JobsBulkEditSchemaMetadataType0,
        )

        d = dict(src_dict)

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_job_context(
            data: object,
        ) -> JobsBulkEditSchemaJobContextType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_context_type_0 = JobsBulkEditSchemaJobContextType0.from_dict(data)

                return job_context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobsBulkEditSchemaJobContextType0 | None | Unset, data)

        job_context = _parse_job_context(d.pop("job_context", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_metadata(
            data: object,
        ) -> JobsBulkEditSchemaMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = JobsBulkEditSchemaMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobsBulkEditSchemaMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_status(data: object) -> JobsBulkEditSchemaStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = JobsBulkEditSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JobsBulkEditSchemaStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        jobs_bulk_edit_schema = cls(
            error_message=error_message,
            job_context=job_context,
            message=message,
            metadata=metadata,
            status=status,
        )

        jobs_bulk_edit_schema.additional_properties = d
        return jobs_bulk_edit_schema

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
