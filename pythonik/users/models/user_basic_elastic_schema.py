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
        email (str | Unset):
        first_name (None | str | Unset):
        id (UUID | Unset):
        last_name (None | str | Unset):
        photo (str | Unset):
        photo_big (str | Unset):
        photo_small (str | Unset):
        photo_storage_id (UUID | Unset):
    """

    email: str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    last_name: None | str | Unset = UNSET
    photo: str | Unset = UNSET
    photo_big: str | Unset = UNSET
    photo_small: str | Unset = UNSET
    photo_storage_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        photo = self.photo

        photo_big = self.photo_big

        photo_small = self.photo_small

        photo_storage_id: str | Unset = UNSET
        if not isinstance(self.photo_storage_id, Unset):
            photo_storage_id = str(self.photo_storage_id)

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
        email = d.pop("email", UNSET)

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        photo = d.pop("photo", UNSET)

        photo_big = d.pop("photo_big", UNSET)

        photo_small = d.pop("photo_small", UNSET)

        _photo_storage_id = d.pop("photo_storage_id", UNSET)
        photo_storage_id: UUID | Unset
        if isinstance(_photo_storage_id, Unset):
            photo_storage_id = UNSET
        else:
            photo_storage_id = UUID(_photo_storage_id)

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
