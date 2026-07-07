from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.automation_history_schema_status import AutomationHistorySchemaStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AutomationHistorySchema")


@_attrs_define
class AutomationHistorySchema:
    """
    Attributes:
        automation_id (UUID):
        object_id (UUID):
        object_type (str):
        status (AutomationHistorySchemaStatus):
        system_domain_id (UUID):
        version_id (UUID):
        date_executed (datetime.datetime | Unset):
        error_message (str | Unset):
        job_id (UUID | Unset):
    """

    automation_id: UUID
    object_id: UUID
    object_type: str
    status: AutomationHistorySchemaStatus
    system_domain_id: UUID
    version_id: UUID
    date_executed: datetime.datetime | Unset = UNSET
    error_message: str | Unset = UNSET
    job_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automation_id = str(self.automation_id)

        object_id = str(self.object_id)

        object_type = self.object_type

        status = self.status.value

        system_domain_id = str(self.system_domain_id)

        version_id = str(self.version_id)

        date_executed: str | Unset = UNSET
        if not isinstance(self.date_executed, Unset):
            date_executed = self.date_executed.isoformat()

        error_message = self.error_message

        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "automation_id": automation_id,
                "object_id": object_id,
                "object_type": object_type,
                "status": status,
                "system_domain_id": system_domain_id,
                "version_id": version_id,
            }
        )
        if date_executed is not UNSET:
            field_dict["date_executed"] = date_executed
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if job_id is not UNSET:
            field_dict["job_id"] = job_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        automation_id = UUID(d.pop("automation_id"))

        object_id = UUID(d.pop("object_id"))

        object_type = d.pop("object_type")

        status = AutomationHistorySchemaStatus(d.pop("status"))

        system_domain_id = UUID(d.pop("system_domain_id"))

        version_id = UUID(d.pop("version_id"))

        _date_executed = d.pop("date_executed", UNSET)
        date_executed: datetime.datetime | Unset
        if isinstance(_date_executed, Unset):
            date_executed = UNSET
        else:
            date_executed = datetime.datetime.fromisoformat(_date_executed)

        error_message = d.pop("error_message", UNSET)

        _job_id = d.pop("job_id", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id, Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)

        automation_history_schema = cls(
            automation_id=automation_id,
            object_id=object_id,
            object_type=object_type,
            status=status,
            system_domain_id=system_domain_id,
            version_id=version_id,
            date_executed=date_executed,
            error_message=error_message,
            job_id=job_id,
        )

        automation_history_schema.additional_properties = d
        return automation_history_schema

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
