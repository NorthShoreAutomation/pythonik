from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.otp_edit_schema_otp_type import OtpEditSchemaOtpType
from ..types import UNSET, Unset

T = TypeVar("T", bound="OtpEditSchema")


@_attrs_define
class OtpEditSchema:
    """
    Attributes:
        otp (str):
        otp_type (OtpEditSchemaOtpType):
        mfa_required (bool | Unset):
    """

    otp: str
    otp_type: OtpEditSchemaOtpType
    mfa_required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        otp = self.otp

        otp_type = self.otp_type.value

        mfa_required = self.mfa_required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "otp": otp,
                "otp_type": otp_type,
            }
        )
        if mfa_required is not UNSET:
            field_dict["mfa_required"] = mfa_required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        otp = d.pop("otp")

        otp_type = OtpEditSchemaOtpType(d.pop("otp_type"))

        mfa_required = d.pop("mfa_required", UNSET)

        otp_edit_schema = cls(
            otp=otp,
            otp_type=otp_type,
            mfa_required=mfa_required,
        )

        otp_edit_schema.additional_properties = d
        return otp_edit_schema

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
