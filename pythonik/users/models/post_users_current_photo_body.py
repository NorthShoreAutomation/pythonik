from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PostUsersCurrentPhotoBody")


@_attrs_define
class PostUsersCurrentPhotoBody:
    """
    Attributes:
        photo (File | None | Unset):
    """

    photo: File | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        photo: FileTypes | None | Unset
        if isinstance(self.photo, Unset):
            photo = UNSET
        elif isinstance(self.photo, File):
            photo = self.photo.to_tuple()

        else:
            photo = self.photo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if photo is not UNSET:
            field_dict["photo"] = photo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_photo(data: object) -> File | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, bytes):
                    raise TypeError()
                photo_type_0 = File(payload=BytesIO(data))

                return photo_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(File | None | Unset, data)

        photo = _parse_photo(d.pop("photo", UNSET))

        post_users_current_photo_body = cls(
            photo=photo,
        )

        post_users_current_photo_body.additional_properties = d
        return post_users_current_photo_body

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
