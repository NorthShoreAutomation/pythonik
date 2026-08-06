from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserBasicElasticSchema")


@_attrs_define
class UserBasicElasticSchema:
    """
    Attributes:
        email (None | str | Unset):
        first_name (None | str | Unset):
        id (None | Unset | UUID):
        last_name (None | str | Unset):
        photo (None | str | Unset):
        photo_big (None | str | Unset):
        photo_small (None | str | Unset):
        photo_storage_id (None | Unset | UUID):
    """

    email: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    last_name: None | str | Unset = UNSET
    photo: None | str | Unset = UNSET
    photo_big: None | str | Unset = UNSET
    photo_small: None | str | Unset = UNSET
    photo_storage_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

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

        photo_storage_id: None | str | Unset
        if isinstance(self.photo_storage_id, Unset):
            photo_storage_id = UNSET
        elif isinstance(self.photo_storage_id, UUID):
            photo_storage_id = str(self.photo_storage_id)
        else:
            photo_storage_id = self.photo_storage_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if photo is not UNSET:
            field_dict["photo"] = photo
        if photo_big is not UNSET:
            field_dict["photo_big"] = photo_big
        if photo_small is not UNSET:
            field_dict["photo_small"] = photo_small
        if photo_storage_id is not UNSET:
            field_dict["photo_storage_id"] = photo_storage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

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

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

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

        def _parse_photo_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                photo_storage_id_type_0 = UUID(data)

                return photo_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        photo_storage_id = _parse_photo_storage_id(d.pop("photo_storage_id", UNSET))

        user_basic_elastic_schema = cls(
            email=email,
            first_name=first_name,
            id=id,
            last_name=last_name,
            photo=photo,
            photo_big=photo_big,
            photo_small=photo_small,
            photo_storage_id=photo_storage_id,
        )

        user_basic_elastic_schema.additional_properties = d
        return user_basic_elastic_schema

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
