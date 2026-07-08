from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostUsersByUserIdPhotoResponse201")


@_attrs_define
class PostUsersByUserIdPhotoResponse201:
    """
    Attributes:
        photo (None | str | Unset): Url for the user original photo
        photo_big (None | str | Unset): Url for the user re-sized big photo
        photo_small (None | str | Unset): Url for the user re-sized small photo
    """

    photo: None | str | Unset = UNSET
    photo_big: None | str | Unset = UNSET
    photo_small: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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

        post_users_by_user_id_photo_response_201 = cls(
            photo=photo,
            photo_big=photo_big,
            photo_small=photo_small,
        )

        post_users_by_user_id_photo_response_201.additional_properties = d
        return post_users_by_user_id_photo_response_201

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
