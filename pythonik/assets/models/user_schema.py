from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSchema")


@_attrs_define
class UserSchema:
    """
    Attributes:
        email (str | Unset):
        first_name (str | Unset):
        id (UUID | Unset):
        last_name (str | Unset):
        photo (str | Unset):
        photo_big (str | Unset):
        photo_small (str | Unset):
    """

    email: str | Unset = UNSET
    first_name: str | Unset = UNSET
    id: UUID | Unset = UNSET
    last_name: str | Unset = UNSET
    photo: str | Unset = UNSET
    photo_big: str | Unset = UNSET
    photo_small: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        first_name = self.first_name

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        last_name = self.last_name

        photo = self.photo

        photo_big = self.photo_big

        photo_small = self.photo_small

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        first_name = d.pop("first_name", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        last_name = d.pop("last_name", UNSET)

        photo = d.pop("photo", UNSET)

        photo_big = d.pop("photo_big", UNSET)

        photo_small = d.pop("photo_small", UNSET)

        user_schema = cls(
            email=email,
            first_name=first_name,
            id=id,
            last_name=last_name,
            photo=photo,
            photo_big=photo_big,
            photo_small=photo_small,
        )

        user_schema.additional_properties = d
        return user_schema

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
