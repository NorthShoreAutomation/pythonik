from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.otp_internal_schema_otp_type import OtpInternalSchemaOtpType

T = TypeVar("T", bound="OtpInternalSchema")


@_attrs_define
class OtpInternalSchema:
    """
    Attributes:
        email (str):
        otp (str):
        otp_type (OtpInternalSchemaOtpType):
    """

    email: str
    otp: str
    otp_type: OtpInternalSchemaOtpType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        otp = self.otp

        otp_type = self.otp_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "otp": otp,
                "otp_type": otp_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        otp = d.pop("otp")

        otp_type = OtpInternalSchemaOtpType(d.pop("otp_type"))

        otp_internal_schema = cls(
            email=email,
            otp=otp,
            otp_type=otp_type,
        )

        otp_internal_schema.additional_properties = d
        return otp_internal_schema

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
