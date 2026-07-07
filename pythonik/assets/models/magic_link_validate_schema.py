from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MagicLinkValidateSchema")


@_attrs_define
class MagicLinkValidateSchema:
    """
    Attributes:
        email (str): The recipient email address
        hash_ (str): The JWT magic link token
        app_id (str | Unset): App ID for session fallback authentication
        password (str | Unset): Password for password-protected shares
        token (str | Unset): Auth token for session fallback authentication
    """

    email: str
    hash_: str
    app_id: str | Unset = UNSET
    password: str | Unset = UNSET
    token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        hash_ = self.hash_

        app_id = self.app_id

        password = self.password

        token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "hash": hash_,
            }
        )
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if password is not UNSET:
            field_dict["password"] = password
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        hash_ = d.pop("hash")

        app_id = d.pop("app_id", UNSET)

        password = d.pop("password", UNSET)

        token = d.pop("token", UNSET)

        magic_link_validate_schema = cls(
            email=email,
            hash_=hash_,
            app_id=app_id,
            password=password,
            token=token,
        )

        magic_link_validate_schema.additional_properties = d
        return magic_link_validate_schema

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
