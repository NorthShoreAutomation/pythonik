from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserOTPEditMultiPlatformSchema")


@_attrs_define
class UserOTPEditMultiPlatformSchema:
    """
    Attributes:
        email (str):
        mfa_required (bool | None | Unset):
        otp_secret (None | str | Unset):
        totp_last_counter (int | None | Unset):
        totp_verified (bool | None | Unset):
    """

    email: str
    mfa_required: bool | None | Unset = UNSET
    otp_secret: None | str | Unset = UNSET
    totp_last_counter: int | None | Unset = UNSET
    totp_verified: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        mfa_required: bool | None | Unset
        if isinstance(self.mfa_required, Unset):
            mfa_required = UNSET
        else:
            mfa_required = self.mfa_required

        otp_secret: None | str | Unset
        if isinstance(self.otp_secret, Unset):
            otp_secret = UNSET
        else:
            otp_secret = self.otp_secret

        totp_last_counter: int | None | Unset
        if isinstance(self.totp_last_counter, Unset):
            totp_last_counter = UNSET
        else:
            totp_last_counter = self.totp_last_counter

        totp_verified: bool | None | Unset
        if isinstance(self.totp_verified, Unset):
            totp_verified = UNSET
        else:
            totp_verified = self.totp_verified

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if mfa_required is not UNSET:
            field_dict["mfa_required"] = mfa_required
        if otp_secret is not UNSET:
            field_dict["otp_secret"] = otp_secret
        if totp_last_counter is not UNSET:
            field_dict["totp_last_counter"] = totp_last_counter
        if totp_verified is not UNSET:
            field_dict["totp_verified"] = totp_verified

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        def _parse_mfa_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mfa_required = _parse_mfa_required(d.pop("mfa_required", UNSET))

        def _parse_otp_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        otp_secret = _parse_otp_secret(d.pop("otp_secret", UNSET))

        def _parse_totp_last_counter(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        totp_last_counter = _parse_totp_last_counter(d.pop("totp_last_counter", UNSET))

        def _parse_totp_verified(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        totp_verified = _parse_totp_verified(d.pop("totp_verified", UNSET))

        user_otp_edit_multi_platform_schema = cls(
            email=email,
            mfa_required=mfa_required,
            otp_secret=otp_secret,
            totp_last_counter=totp_last_counter,
            totp_verified=totp_verified,
        )

        user_otp_edit_multi_platform_schema.additional_properties = d
        return user_otp_edit_multi_platform_schema

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
