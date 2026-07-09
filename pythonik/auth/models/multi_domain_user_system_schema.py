from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.multi_domain_user_system_schema_mfa_methods_configured_type_0_item import (
    MultiDomainUserSystemSchemaMfaMethodsConfiguredType0Item,
)
from ..models.multi_domain_user_system_schema_mfa_methods_type_0_item import (
    MultiDomainUserSystemSchemaMfaMethodsType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiDomainUserSystemSchema")


@_attrs_define
class MultiDomainUserSystemSchema:
    """
    Attributes:
        system_domain_id (UUID):
        logo_url (None | str | Unset):
        mfa_methods (list[MultiDomainUserSystemSchemaMfaMethodsType0Item] | None | Unset):
        mfa_methods_configured (list[MultiDomainUserSystemSchemaMfaMethodsConfiguredType0Item] | None | Unset):
        mfa_required (bool | None | Unset):
        mfa_required_configured (bool | None | Unset):
        platform_url (None | str | Unset):
        system_domain_name (None | str | Unset):
        url (None | str | Unset):
    """

    system_domain_id: UUID
    logo_url: None | str | Unset = UNSET
    mfa_methods: list[MultiDomainUserSystemSchemaMfaMethodsType0Item] | None | Unset = (
        UNSET
    )
    mfa_methods_configured: (
        list[MultiDomainUserSystemSchemaMfaMethodsConfiguredType0Item] | None | Unset
    ) = UNSET
    mfa_required: bool | None | Unset = UNSET
    mfa_required_configured: bool | None | Unset = UNSET
    platform_url: None | str | Unset = UNSET
    system_domain_name: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system_domain_id = str(self.system_domain_id)

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        mfa_methods: list[str] | None | Unset
        if isinstance(self.mfa_methods, Unset):
            mfa_methods = UNSET
        elif isinstance(self.mfa_methods, list):
            mfa_methods = []
            for mfa_methods_type_0_item_data in self.mfa_methods:
                mfa_methods_type_0_item = mfa_methods_type_0_item_data.value
                mfa_methods.append(mfa_methods_type_0_item)

        else:
            mfa_methods = self.mfa_methods

        mfa_methods_configured: list[str] | None | Unset
        if isinstance(self.mfa_methods_configured, Unset):
            mfa_methods_configured = UNSET
        elif isinstance(self.mfa_methods_configured, list):
            mfa_methods_configured = []
            for mfa_methods_configured_type_0_item_data in self.mfa_methods_configured:
                mfa_methods_configured_type_0_item = (
                    mfa_methods_configured_type_0_item_data.value
                )
                mfa_methods_configured.append(mfa_methods_configured_type_0_item)

        else:
            mfa_methods_configured = self.mfa_methods_configured

        mfa_required: bool | None | Unset
        if isinstance(self.mfa_required, Unset):
            mfa_required = UNSET
        else:
            mfa_required = self.mfa_required

        mfa_required_configured: bool | None | Unset
        if isinstance(self.mfa_required_configured, Unset):
            mfa_required_configured = UNSET
        else:
            mfa_required_configured = self.mfa_required_configured

        platform_url: None | str | Unset
        if isinstance(self.platform_url, Unset):
            platform_url = UNSET
        else:
            platform_url = self.platform_url

        system_domain_name: None | str | Unset
        if isinstance(self.system_domain_name, Unset):
            system_domain_name = UNSET
        else:
            system_domain_name = self.system_domain_name

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "system_domain_id": system_domain_id,
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

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_mfa_methods(
            data: object,
        ) -> list[MultiDomainUserSystemSchemaMfaMethodsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mfa_methods_type_0 = []
                _mfa_methods_type_0 = data
                for mfa_methods_type_0_item_data in _mfa_methods_type_0:
                    mfa_methods_type_0_item = (
                        MultiDomainUserSystemSchemaMfaMethodsType0Item(
                            mfa_methods_type_0_item_data
                        )
                    )

                    mfa_methods_type_0.append(mfa_methods_type_0_item)

                return mfa_methods_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[MultiDomainUserSystemSchemaMfaMethodsType0Item] | None | Unset,
                data,
            )

        mfa_methods = _parse_mfa_methods(d.pop("mfa_methods", UNSET))

        def _parse_mfa_methods_configured(
            data: object,
        ) -> (
            list[MultiDomainUserSystemSchemaMfaMethodsConfiguredType0Item]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                mfa_methods_configured_type_0 = []
                _mfa_methods_configured_type_0 = data
                for (
                    mfa_methods_configured_type_0_item_data
                ) in _mfa_methods_configured_type_0:
                    mfa_methods_configured_type_0_item = (
                        MultiDomainUserSystemSchemaMfaMethodsConfiguredType0Item(
                            mfa_methods_configured_type_0_item_data
                        )
                    )

                    mfa_methods_configured_type_0.append(
                        mfa_methods_configured_type_0_item
                    )

                return mfa_methods_configured_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[MultiDomainUserSystemSchemaMfaMethodsConfiguredType0Item]
                | None
                | Unset,
                data,
            )

        mfa_methods_configured = _parse_mfa_methods_configured(
            d.pop("mfa_methods_configured", UNSET)
        )

        def _parse_mfa_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mfa_required = _parse_mfa_required(d.pop("mfa_required", UNSET))

        def _parse_mfa_required_configured(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        mfa_required_configured = _parse_mfa_required_configured(
            d.pop("mfa_required_configured", UNSET)
        )

        def _parse_platform_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform_url = _parse_platform_url(d.pop("platform_url", UNSET))

        def _parse_system_domain_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_domain_name = _parse_system_domain_name(
            d.pop("system_domain_name", UNSET)
        )

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        multi_domain_user_system_schema = cls(
            system_domain_id=system_domain_id,
            logo_url=logo_url,
            mfa_methods=mfa_methods,
            mfa_methods_configured=mfa_methods_configured,
            mfa_required=mfa_required,
            mfa_required_configured=mfa_required_configured,
            platform_url=platform_url,
            system_domain_name=system_domain_name,
            url=url,
        )

        multi_domain_user_system_schema.additional_properties = d
        return multi_domain_user_system_schema

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
