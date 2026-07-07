from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.multi_platform_domain_user_system_schema_mfa_methods_configured_item import (
    MultiPlatformDomainUserSystemSchemaMfaMethodsConfiguredItem,
)
from ..models.multi_platform_domain_user_system_schema_mfa_methods_item import (
    MultiPlatformDomainUserSystemSchemaMfaMethodsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiPlatformDomainUserSystemSchema")


@_attrs_define
class MultiPlatformDomainUserSystemSchema:
    """
    Attributes:
        system_domain_id (UUID):
        token (str):
        logo_url (str | Unset):
        mfa_methods (list[MultiPlatformDomainUserSystemSchemaMfaMethodsItem] | Unset):
        mfa_methods_configured (list[MultiPlatformDomainUserSystemSchemaMfaMethodsConfiguredItem] | Unset):
        mfa_required (bool | Unset):
        mfa_required_configured (bool | Unset):
        platform_url (str | Unset):
        system_domain_name (str | Unset):
        url (str | Unset):
    """

    system_domain_id: UUID
    token: str
    logo_url: str | Unset = UNSET
    mfa_methods: list[MultiPlatformDomainUserSystemSchemaMfaMethodsItem] | Unset = UNSET
    mfa_methods_configured: (
        list[MultiPlatformDomainUserSystemSchemaMfaMethodsConfiguredItem] | Unset
    ) = UNSET
    mfa_required: bool | Unset = UNSET
    mfa_required_configured: bool | Unset = UNSET
    platform_url: str | Unset = UNSET
    system_domain_name: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system_domain_id = str(self.system_domain_id)

        token = self.token

        logo_url = self.logo_url

        mfa_methods: list[str] | Unset = UNSET
        if not isinstance(self.mfa_methods, Unset):
            mfa_methods = []
            for mfa_methods_item_data in self.mfa_methods:
                mfa_methods_item = mfa_methods_item_data.value
                mfa_methods.append(mfa_methods_item)

        mfa_methods_configured: list[str] | Unset = UNSET
        if not isinstance(self.mfa_methods_configured, Unset):
            mfa_methods_configured = []
            for mfa_methods_configured_item_data in self.mfa_methods_configured:
                mfa_methods_configured_item = mfa_methods_configured_item_data.value
                mfa_methods_configured.append(mfa_methods_configured_item)

        mfa_required = self.mfa_required

        mfa_required_configured = self.mfa_required_configured

        platform_url = self.platform_url

        system_domain_name = self.system_domain_name

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "system_domain_id": system_domain_id,
                "token": token,
            }
        )
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if mfa_methods is not UNSET:
            field_dict["mfa_methods"] = mfa_methods
        if mfa_methods_configured is not UNSET:
            field_dict["mfa_methods_configured"] = mfa_methods_configured
        if mfa_required is not UNSET:
            field_dict["mfa_required"] = mfa_required
        if mfa_required_configured is not UNSET:
            field_dict["mfa_required_configured"] = mfa_required_configured
        if platform_url is not UNSET:
            field_dict["platform_url"] = platform_url
        if system_domain_name is not UNSET:
            field_dict["system_domain_name"] = system_domain_name
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        system_domain_id = UUID(d.pop("system_domain_id"))

        token = d.pop("token")

        logo_url = d.pop("logo_url", UNSET)

        _mfa_methods = d.pop("mfa_methods", UNSET)
        mfa_methods: list[MultiPlatformDomainUserSystemSchemaMfaMethodsItem] | Unset = (
            UNSET
        )
        if _mfa_methods is not UNSET:
            mfa_methods = []
            for mfa_methods_item_data in _mfa_methods:
                mfa_methods_item = MultiPlatformDomainUserSystemSchemaMfaMethodsItem(
                    mfa_methods_item_data
                )

                mfa_methods.append(mfa_methods_item)

        _mfa_methods_configured = d.pop("mfa_methods_configured", UNSET)
        mfa_methods_configured: (
            list[MultiPlatformDomainUserSystemSchemaMfaMethodsConfiguredItem] | Unset
        ) = UNSET
        if _mfa_methods_configured is not UNSET:
            mfa_methods_configured = []
            for mfa_methods_configured_item_data in _mfa_methods_configured:
                mfa_methods_configured_item = (
                    MultiPlatformDomainUserSystemSchemaMfaMethodsConfiguredItem(
                        mfa_methods_configured_item_data
                    )
                )

                mfa_methods_configured.append(mfa_methods_configured_item)

        mfa_required = d.pop("mfa_required", UNSET)

        mfa_required_configured = d.pop("mfa_required_configured", UNSET)

        platform_url = d.pop("platform_url", UNSET)

        system_domain_name = d.pop("system_domain_name", UNSET)

        url = d.pop("url", UNSET)

        multi_platform_domain_user_system_schema = cls(
            system_domain_id=system_domain_id,
            token=token,
            logo_url=logo_url,
            mfa_methods=mfa_methods,
            mfa_methods_configured=mfa_methods_configured,
            mfa_required=mfa_required,
            mfa_required_configured=mfa_required_configured,
            platform_url=platform_url,
            system_domain_name=system_domain_name,
            url=url,
        )

        multi_platform_domain_user_system_schema.additional_properties = d
        return multi_platform_domain_user_system_schema

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
