from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        date_executed (datetime.datetime | None | Unset):
        error_message (None | str | Unset):
        job_id (None | Unset | UUID):
    """

    automation_id: UUID
    object_id: UUID
    object_type: str
    status: AutomationHistorySchemaStatus
    system_domain_id: UUID
    version_id: UUID
    date_executed: datetime.datetime | None | Unset = UNSET
    error_message: None | str | Unset = UNSET
    job_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        automation_id = str(self.automation_id)

        object_id = str(self.object_id)

        object_type = self.object_type

        status = self.status.value

        system_domain_id = str(self.system_domain_id)

        version_id = str(self.version_id)

        date_executed: None | str | Unset
        if isinstance(self.date_executed, Unset):
            date_executed = UNSET
        elif isinstance(self.date_executed, datetime.datetime):
            date_executed = self.date_executed.isoformat()
        else:
            date_executed = self.date_executed

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        elif isinstance(self.job_id, UUID):
            job_id = str(self.job_id)
        else:
            job_id = self.job_id

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

        def _parse_date_executed(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_executed_type_0 = datetime.datetime.fromisoformat(data)

                return date_executed_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_executed = _parse_date_executed(d.pop("date_executed", UNSET))

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))

        def _parse_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_id_type_0 = UUID(data)

                return job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

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
