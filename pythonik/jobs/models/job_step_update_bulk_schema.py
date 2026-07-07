from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.job_step_update_bulk_schema_status import JobStepUpdateBulkSchemaStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobStepUpdateBulkSchema")


@_attrs_define
class JobStepUpdateBulkSchema:
    """
    Attributes:
        id (UUID):
        label (str):
        status (JobStepUpdateBulkSchemaStatus):
        date_updated (datetime.datetime | Unset):
        error_message (None | str | Unset):
        message (None | str | Unset):
    """

    id: UUID
    label: str
    status: JobStepUpdateBulkSchemaStatus
    date_updated: datetime.datetime | Unset = UNSET
    error_message: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        label = self.label

        status = self.status.value

        date_updated: str | Unset = UNSET
        if not isinstance(self.date_updated, Unset):
            date_updated = self.date_updated.isoformat()

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "label": label,
                "status": status,
            }
        )
        if date_updated is not UNSET:
            field_dict["date_updated"] = date_updated
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        label = d.pop("label")

        status = JobStepUpdateBulkSchemaStatus(d.pop("status"))

        _date_updated = d.pop("date_updated", UNSET)
        date_updated: datetime.datetime | Unset
        if isinstance(_date_updated, Unset):
            date_updated = UNSET
        else:
            date_updated = datetime.datetime.fromisoformat(_date_updated)

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        job_step_update_bulk_schema = cls(
            id=id,
            label=label,
            status=status,
            date_updated=date_updated,
            error_message=error_message,
            message=message,
        )

        job_step_update_bulk_schema.additional_properties = d
        return job_step_update_bulk_schema

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
