from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jobs_bulk_edit_schema_status import JobsBulkEditSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.jobs_bulk_edit_schema_job_context import JobsBulkEditSchemaJobContext
    from ..models.jobs_bulk_edit_schema_metadata import JobsBulkEditSchemaMetadata


T = TypeVar("T", bound="JobsBulkEditSchema")


@_attrs_define
class JobsBulkEditSchema:
    """
    Attributes:
        error_message (str | Unset):
        job_context (JobsBulkEditSchemaJobContext | Unset):
        message (str | Unset):
        metadata (JobsBulkEditSchemaMetadata | Unset):
        status (JobsBulkEditSchemaStatus | Unset):
    """

    error_message: str | Unset = UNSET
    job_context: JobsBulkEditSchemaJobContext | Unset = UNSET
    message: str | Unset = UNSET
    metadata: JobsBulkEditSchemaMetadata | Unset = UNSET
    status: JobsBulkEditSchemaStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error_message = self.error_message

        job_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_context, Unset):
            job_context = self.job_context.to_dict()

        message = self.message

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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
        from ..models.jobs_bulk_edit_schema_job_context import (
            JobsBulkEditSchemaJobContext,
        )
        from ..models.jobs_bulk_edit_schema_metadata import JobsBulkEditSchemaMetadata

        d = dict(src_dict)
        error_message = d.pop("error_message", UNSET)

        _job_context = d.pop("job_context", UNSET)
        job_context: JobsBulkEditSchemaJobContext | Unset
        if isinstance(_job_context, Unset):
            job_context = UNSET
        else:
            job_context = JobsBulkEditSchemaJobContext.from_dict(_job_context)

        message = d.pop("message", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: JobsBulkEditSchemaMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = JobsBulkEditSchemaMetadata.from_dict(_metadata)

        _status = d.pop("status", UNSET)
        status: JobsBulkEditSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = JobsBulkEditSchemaStatus(_status)

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
