from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetUsersCurrentOtpConfigureResponse200")


@_attrs_define
class GetUsersCurrentOtpConfigureResponse200:
    """
    Attributes:
        mfa_methods (Any | Unset): mfa methods
        mfa_required (bool | Unset): is mfa required for the user
    """

    mfa_methods: Any | Unset = UNSET
    mfa_required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mfa_methods = self.mfa_methods

        mfa_required = self.mfa_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mfa_methods is not UNSET:
            field_dict["mfa_methods"] = mfa_methods
        if mfa_required is not UNSET:
            field_dict["mfa_required"] = mfa_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mfa_methods = d.pop("mfa_methods", UNSET)

        mfa_required = d.pop("mfa_required", UNSET)

        get_users_current_otp_configure_response_200 = cls(
            mfa_methods=mfa_methods,
            mfa_required=mfa_required,
        )

        get_users_current_otp_configure_response_200.additional_properties = d
        return get_users_current_otp_configure_response_200

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
