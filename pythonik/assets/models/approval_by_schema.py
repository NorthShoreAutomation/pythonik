from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_by_schema_status import ApprovalBySchemaStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalBySchema")


@_attrs_define
class ApprovalBySchema:
    """
    Attributes:
        change_date (datetime.datetime | Unset):
        external (str | Unset):
        object_id (UUID | Unset):
        object_type (str | Unset):
        status (ApprovalBySchemaStatus | Unset):
        user (UUID | Unset):
        version_id (UUID | Unset):
    """

    change_date: datetime.datetime | Unset = UNSET
    external: str | Unset = UNSET
    object_id: UUID | Unset = UNSET
    object_type: str | Unset = UNSET
    status: ApprovalBySchemaStatus | Unset = UNSET
    user: UUID | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        change_date: str | Unset = UNSET
        if not isinstance(self.change_date, Unset):
            change_date = self.change_date.isoformat()

        external = self.external

        object_id: str | Unset = UNSET
        if not isinstance(self.object_id, Unset):
            object_id = str(self.object_id)

        object_type = self.object_type

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        user: str | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = str(self.user)

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if change_date is not UNSET:
            field_dict["change_date"] = change_date
        if external is not UNSET:
            field_dict["external"] = external
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if status is not UNSET:
            field_dict["status"] = status
        if user is not UNSET:
            field_dict["user"] = user
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _change_date = d.pop("change_date", UNSET)
        change_date: datetime.datetime | Unset
        if isinstance(_change_date, Unset):
            change_date = UNSET
        else:
            change_date = datetime.datetime.fromisoformat(_change_date)

        external = d.pop("external", UNSET)

        _object_id = d.pop("object_id", UNSET)
        object_id: UUID | Unset
        if isinstance(_object_id, Unset):
            object_id = UNSET
        else:
            object_id = UUID(_object_id)

        object_type = d.pop("object_type", UNSET)

        _status = d.pop("status", UNSET)
        status: ApprovalBySchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ApprovalBySchemaStatus(_status)

        _user = d.pop("user", UNSET)
        user: UUID | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = UUID(_user)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

        approval_by_schema = cls(
            change_date=change_date,
            external=external,
            object_id=object_id,
            object_type=object_type,
            status=status,
            user=user,
            version_id=version_id,
        )

        approval_by_schema.additional_properties = d
        return approval_by_schema

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
