from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareUserSchema")


@_attrs_define
class ShareUserSchema:
    """
    Attributes:
        email (str):
        access_count (int | Unset):
        first_name (str | Unset):
        id (str | Unset):
        internal_user_id (str | Unset):
        last_access_date (datetime.datetime | Unset):
        last_name (str | Unset):
        object_id (str | Unset):
        object_type (str | Unset):
        password (str | Unset):
        photo (str | Unset):
        photo_big (str | Unset):
        photo_small (str | Unset):
        share_id (str | Unset):
    """

    email: str
    access_count: int | Unset = UNSET
    first_name: str | Unset = UNSET
    id: str | Unset = UNSET
    internal_user_id: str | Unset = UNSET
    last_access_date: datetime.datetime | Unset = UNSET
    last_name: str | Unset = UNSET
    object_id: str | Unset = UNSET
    object_type: str | Unset = UNSET
    password: str | Unset = UNSET
    photo: str | Unset = UNSET
    photo_big: str | Unset = UNSET
    photo_small: str | Unset = UNSET
    share_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        access_count = self.access_count

        first_name = self.first_name

        id = self.id

        internal_user_id = self.internal_user_id

        last_access_date: str | Unset = UNSET
        if not isinstance(self.last_access_date, Unset):
            last_access_date = self.last_access_date.isoformat()

        last_name = self.last_name

        object_id = self.object_id

        object_type = self.object_type

        password = self.password

        photo = self.photo

        photo_big = self.photo_big

        photo_small = self.photo_small

        share_id = self.share_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if access_count is not UNSET:
            field_dict["access_count"] = access_count
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if internal_user_id is not UNSET:
            field_dict["internal_user_id"] = internal_user_id
        if last_access_date is not UNSET:
            field_dict["last_access_date"] = last_access_date
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if password is not UNSET:
            field_dict["password"] = password
        if photo is not UNSET:
            field_dict["photo"] = photo
        if photo_big is not UNSET:
            field_dict["photo_big"] = photo_big
        if photo_small is not UNSET:
            field_dict["photo_small"] = photo_small
        if share_id is not UNSET:
            field_dict["share_id"] = share_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        access_count = d.pop("access_count", UNSET)

        first_name = d.pop("first_name", UNSET)

        id = d.pop("id", UNSET)

        internal_user_id = d.pop("internal_user_id", UNSET)

        _last_access_date = d.pop("last_access_date", UNSET)
        last_access_date: datetime.datetime | Unset
        if isinstance(_last_access_date, Unset):
            last_access_date = UNSET
        else:
            last_access_date = datetime.datetime.fromisoformat(_last_access_date)

        last_name = d.pop("last_name", UNSET)

        object_id = d.pop("object_id", UNSET)

        object_type = d.pop("object_type", UNSET)

        password = d.pop("password", UNSET)

        photo = d.pop("photo", UNSET)

        photo_big = d.pop("photo_big", UNSET)

        photo_small = d.pop("photo_small", UNSET)

        share_id = d.pop("share_id", UNSET)

        share_user_schema = cls(
            email=email,
            access_count=access_count,
            first_name=first_name,
            id=id,
            internal_user_id=internal_user_id,
            last_access_date=last_access_date,
            last_name=last_name,
            object_id=object_id,
            object_type=object_type,
            password=password,
            photo=photo,
            photo_big=photo_big,
            photo_small=photo_small,
            share_id=share_id,
        )

        share_user_schema.additional_properties = d
        return share_user_schema

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
