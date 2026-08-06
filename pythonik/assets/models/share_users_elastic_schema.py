from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareUsersElasticSchema")


@_attrs_define
class ShareUsersElasticSchema:
    """
    Attributes:
        access_count (int | None | Unset):
        email (None | str | Unset):
        id (None | Unset | UUID):
        last_access_date (datetime.datetime | None | Unset):
    """

    access_count: int | None | Unset = UNSET
    email: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    last_access_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        access_count: int | None | Unset
        if isinstance(self.access_count, Unset):
            access_count = UNSET
        else:
            access_count = self.access_count

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        last_access_date: None | str | Unset
        if isinstance(self.last_access_date, Unset):
            last_access_date = UNSET
        elif isinstance(self.last_access_date, datetime.datetime):
            last_access_date = self.last_access_date.isoformat()
        else:
            last_access_date = self.last_access_date

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

        def _parse_access_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        access_count = _parse_access_count(d.pop("access_count", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_last_access_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_access_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_access_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_access_date = _parse_last_access_date(d.pop("last_access_date", UNSET))

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
