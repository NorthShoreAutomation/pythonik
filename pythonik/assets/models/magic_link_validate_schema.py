from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

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
        app_id (None | str | Unset): App ID for session fallback authentication
        password (None | str | Unset): Password for password-protected shares
        token (None | str | Unset): Auth token for session fallback authentication
    """

    email: str
    hash_: str
    app_id: None | str | Unset = UNSET
    password: None | str | Unset = UNSET
    token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        hash_ = self.hash_

        app_id: None | str | Unset
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        else:
            app_id = self.app_id

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
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

        def _parse_app_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_id = _parse_app_id(d.pop("app_id", UNSET))

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))

        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))

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
