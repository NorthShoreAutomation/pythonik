from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareLoginSchema")


@_attrs_define
class ShareLoginSchema:
    """
    Attributes:
        hash_ (str):
        app_id (str | Unset):
        object_id (str | Unset):
        object_type (str | Unset):
        password (str | Unset):
        token (str | Unset):
    """

    hash_: str
    app_id: str | Unset = UNSET
    object_id: str | Unset = UNSET
    object_type: str | Unset = UNSET
    password: str | Unset = UNSET
    token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hash_ = self.hash_

        app_id = self.app_id

        object_id = self.object_id

        object_type = self.object_type

        password = self.password

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hash": hash_,
            }
        )
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if object_type is not UNSET:
            field_dict["object_type"] = object_type
        if password is not UNSET:
            field_dict["password"] = password
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hash_ = d.pop("hash")

        app_id = d.pop("app_id", UNSET)

        object_id = d.pop("object_id", UNSET)

        object_type = d.pop("object_type", UNSET)

        password = d.pop("password", UNSET)

        token = d.pop("token", UNSET)

        share_login_schema = cls(
            hash_=hash_,
            app_id=app_id,
            object_id=object_id,
            object_type=object_type,
            password=password,
            token=token,
        )

        share_login_schema.additional_properties = d
        return share_login_schema

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
