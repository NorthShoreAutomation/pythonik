from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OtpEditInternalSchema")


@_attrs_define
class OtpEditInternalSchema:
    """
    Attributes:
        email (str):
        mfa_required (bool | None | Unset):
    """

    email: str
    mfa_required: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        mfa_required: bool | None | Unset
        if isinstance(self.mfa_required, Unset):
            mfa_required = UNSET
        else:
            mfa_required = self.mfa_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if mfa_required is not UNSET:
            field_dict["mfa_required"] = mfa_required

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

        otp_edit_internal_schema = cls(
            email=email,
            mfa_required=mfa_required,
        )

        otp_edit_internal_schema.additional_properties = d
        return otp_edit_internal_schema

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
