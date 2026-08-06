from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiDomainLoginSchema")


@_attrs_define
class MultiDomainLoginSchema:
    """
    Attributes:
        email (str):
        system_domain_id (UUID):
        app_name (None | str | Unset):
        marketplace_signup_nonce (None | str | Unset):
        otp (None | str | Unset):
        otp_type (None | str | Unset):
    """

    email: str
    system_domain_id: UUID
    app_name: None | str | Unset = UNSET
    marketplace_signup_nonce: None | str | Unset = UNSET
    otp: None | str | Unset = UNSET
    otp_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        system_domain_id = str(self.system_domain_id)

        app_name: None | str | Unset
        if isinstance(self.app_name, Unset):
            app_name = UNSET
        else:
            app_name = self.app_name

        marketplace_signup_nonce: None | str | Unset
        if isinstance(self.marketplace_signup_nonce, Unset):
            marketplace_signup_nonce = UNSET
        else:
            marketplace_signup_nonce = self.marketplace_signup_nonce

        otp: None | str | Unset
        if isinstance(self.otp, Unset):
            otp = UNSET
        else:
            otp = self.otp

        otp_type: None | str | Unset
        if isinstance(self.otp_type, Unset):
            otp_type = UNSET
        else:
            otp_type = self.otp_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "system_domain_id": system_domain_id,
            }
        )
        if app_name is not UNSET:
            field_dict["app_name"] = app_name
        if marketplace_signup_nonce is not UNSET:
            field_dict["marketplace_signup_nonce"] = marketplace_signup_nonce
        if otp is not UNSET:
            field_dict["otp"] = otp
        if otp_type is not UNSET:
            field_dict["otp_type"] = otp_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        system_domain_id = UUID(d.pop("system_domain_id"))

        def _parse_app_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_name = _parse_app_name(d.pop("app_name", UNSET))

        def _parse_marketplace_signup_nonce(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        marketplace_signup_nonce = _parse_marketplace_signup_nonce(
            d.pop("marketplace_signup_nonce", UNSET)
        )

        def _parse_otp(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        otp = _parse_otp(d.pop("otp", UNSET))

        def _parse_otp_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        otp_type = _parse_otp_type(d.pop("otp_type", UNSET))

        multi_domain_login_schema = cls(
            email=email,
            system_domain_id=system_domain_id,
            app_name=app_name,
            marketplace_signup_nonce=marketplace_signup_nonce,
            otp=otp,
            otp_type=otp_type,
        )

        multi_domain_login_schema.additional_properties = d
        return multi_domain_login_schema

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
