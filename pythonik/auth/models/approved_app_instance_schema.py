from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovedAppInstanceSchema")


@_attrs_define
class ApprovedAppInstanceSchema:
    """
    Attributes:
        app_id (UUID):
        id (UUID):
        date_created (datetime.datetime | Unset):
    """

    app_id: UUID
    id: UUID
    date_created: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app_id = str(self.app_id)

        id = str(self.id)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_id": app_id,
                "id": id,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_id = UUID(d.pop("app_id"))

        id = UUID(d.pop("id"))

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        approved_app_instance_schema = cls(
            app_id=app_id,
            id=id,
            date_created=date_created,
        )

        approved_app_instance_schema.additional_properties = d
        return approved_app_instance_schema

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
