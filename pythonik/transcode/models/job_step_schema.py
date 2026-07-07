from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobStepSchema")


@_attrs_define
class JobStepSchema:
    """
    Attributes:
        date_created (datetime.datetime | Unset):
        date_updated (datetime.datetime | Unset):
        id (str | Unset):
        label (str | Unset):
        message (str | Unset):
        status (str | Unset):
    """

    date_created: datetime.datetime | Unset = UNSET
    date_updated: datetime.datetime | Unset = UNSET
    id: str | Unset = UNSET
    label: str | Unset = UNSET
    message: str | Unset = UNSET
    status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_updated: str | Unset = UNSET
        if not isinstance(self.date_updated, Unset):
            date_updated = self.date_updated.isoformat()

        id = self.id

        label = self.label

        message = self.message

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_updated is not UNSET:
            field_dict["date_updated"] = date_updated
        if id is not UNSET:
            field_dict["id"] = id
        if label is not UNSET:
            field_dict["label"] = label
        if message is not UNSET:
            field_dict["message"] = message
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_updated = d.pop("date_updated", UNSET)
        date_updated: datetime.datetime | Unset
        if isinstance(_date_updated, Unset):
            date_updated = UNSET
        else:
            date_updated = datetime.datetime.fromisoformat(_date_updated)

        id = d.pop("id", UNSET)

        label = d.pop("label", UNSET)

        message = d.pop("message", UNSET)

        status = d.pop("status", UNSET)

        job_step_schema = cls(
            date_created=date_created,
            date_updated=date_updated,
            id=id,
            label=label,
            message=message,
            status=status,
        )

        job_step_schema.additional_properties = d
        return job_step_schema

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
