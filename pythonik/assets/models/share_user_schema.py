from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareUserSchema")


@_attrs_define
class ShareUserSchema:
    """
    Attributes:
        email (str):
        access_count (int | None | Unset):
        first_name (None | str | Unset):
        id (None | str | Unset):
        internal_user_id (None | str | Unset):
        last_access_date (datetime.datetime | None | Unset):
        last_name (None | str | Unset):
        object_id (None | str | Unset):
        object_type (None | str | Unset):
        password (None | str | Unset):
        photo (None | str | Unset):
        photo_big (None | str | Unset):
        photo_small (None | str | Unset):
        share_id (None | str | Unset):
    """

    email: str
    access_count: int | None | Unset = UNSET
    first_name: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    internal_user_id: None | str | Unset = UNSET
    last_access_date: datetime.datetime | None | Unset = UNSET
    last_name: None | str | Unset = UNSET
    object_id: None | str | Unset = UNSET
    object_type: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    photo: None | str | Unset = UNSET
    photo_big: None | str | Unset = UNSET
    photo_small: None | str | Unset = UNSET
    share_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        access_count: int | None | Unset
        if isinstance(self.access_count, Unset):
            access_count = UNSET
        else:
            access_count = self.access_count

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        internal_user_id: None | str | Unset
        if isinstance(self.internal_user_id, Unset):
            internal_user_id = UNSET
        else:
            internal_user_id = self.internal_user_id

        last_access_date: None | str | Unset
        if isinstance(self.last_access_date, Unset):
            last_access_date = UNSET
        elif isinstance(self.last_access_date, datetime.datetime):
            last_access_date = self.last_access_date.isoformat()
        else:
            last_access_date = self.last_access_date

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        object_id: None | str | Unset
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        else:
            object_id = self.object_id

        object_type: None | str | Unset
        if isinstance(self.object_type, Unset):
            object_type = UNSET
        else:
            object_type = self.object_type

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        photo: None | str | Unset
        if isinstance(self.photo, Unset):
            photo = UNSET
        else:
            photo = self.photo

        photo_big: None | str | Unset
        if isinstance(self.photo_big, Unset):
            photo_big = UNSET
        else:
            photo_big = self.photo_big

        photo_small: None | str | Unset
        if isinstance(self.photo_small, Unset):
            photo_small = UNSET
        else:
            photo_small = self.photo_small

        share_id: None | str | Unset
        if isinstance(self.share_id, Unset):
            share_id = UNSET
        else:
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

        def _parse_access_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        access_count = _parse_access_count(d.pop("access_count", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_internal_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        internal_user_id = _parse_internal_user_id(d.pop("internal_user_id", UNSET))

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

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_object_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_id = _parse_object_id(d.pop("object_id", UNSET))

        def _parse_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        object_type = _parse_object_type(d.pop("object_type", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_photo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo = _parse_photo(d.pop("photo", UNSET))

        def _parse_photo_big(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_big = _parse_photo_big(d.pop("photo_big", UNSET))

        def _parse_photo_small(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        photo_small = _parse_photo_small(d.pop("photo_small", UNSET))

        def _parse_share_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        share_id = _parse_share_id(d.pop("share_id", UNSET))

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
