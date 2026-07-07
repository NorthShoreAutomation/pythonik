from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, FileTypes, Unset

T = TypeVar("T", bound="PostUsersByUserIdPhotoBody")


@_attrs_define
class PostUsersByUserIdPhotoBody:
    """
    Attributes:
        photo (File | Unset):
    """

    photo: File | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        photo: FileTypes | Unset = UNSET
        if not isinstance(self.photo, Unset):
            photo = self.photo.to_tuple()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if photo is not UNSET:
            field_dict["photo"] = photo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _photo = d.pop("photo", UNSET)
        photo: File | Unset
        if isinstance(_photo, Unset):
            photo = UNSET
        else:
            photo = File(payload=BytesIO(_photo))

        post_users_by_user_id_photo_body = cls(
            photo=photo,
        )

        post_users_by_user_id_photo_body.additional_properties = d
        return post_users_by_user_id_photo_body

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
