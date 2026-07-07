from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareUsersElasticSchema")


@_attrs_define
class ShareUsersElasticSchema:
    """
    Attributes:
        access_count (int | Unset):
        email (str | Unset):
        id (UUID | Unset):
        last_access_date (datetime.datetime | Unset):
    """

    access_count: int | Unset = UNSET
    email: str | Unset = UNSET
    id: UUID | Unset = UNSET
    last_access_date: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_count = self.access_count

        email = self.email

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        last_access_date: str | Unset = UNSET
        if not isinstance(self.last_access_date, Unset):
            last_access_date = self.last_access_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_count is not UNSET:
            field_dict["access_count"] = access_count
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if last_access_date is not UNSET:
            field_dict["last_access_date"] = last_access_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_count = d.pop("access_count", UNSET)

        email = d.pop("email", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _last_access_date = d.pop("last_access_date", UNSET)
        last_access_date: datetime.datetime | Unset
        if isinstance(_last_access_date, Unset):
            last_access_date = UNSET
        else:
            last_access_date = datetime.datetime.fromisoformat(_last_access_date)

        share_users_elastic_schema = cls(
            access_count=access_count,
            email=email,
            id=id,
            last_access_date=last_access_date,
        )

        share_users_elastic_schema.additional_properties = d
        return share_users_elastic_schema

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
