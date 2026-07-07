from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_login_schema import AutoLoginSchema
    from ..models.system_domain_from_template_schema import (
        SystemDomainFromTemplateSchema,
    )


T = TypeVar("T", bound="VerificationResponseSchema")


@_attrs_define
class VerificationResponseSchema:
    """
    Attributes:
        auto_login (bool | Unset):
        domain_data (SystemDomainFromTemplateSchema | Unset):
        login_data (AutoLoginSchema | Unset):
    """

    auto_login: bool | Unset = UNSET
    domain_data: SystemDomainFromTemplateSchema | Unset = UNSET
    login_data: AutoLoginSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_login = self.auto_login

        domain_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.domain_data, Unset):
            domain_data = self.domain_data.to_dict()

        login_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.login_data, Unset):
            login_data = self.login_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_login is not UNSET:
            field_dict["auto_login"] = auto_login
        if domain_data is not UNSET:
            field_dict["domain_data"] = domain_data
        if login_data is not UNSET:
            field_dict["login_data"] = login_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_login_schema import AutoLoginSchema
        from ..models.system_domain_from_template_schema import (
            SystemDomainFromTemplateSchema,
        )

        d = dict(src_dict)
        auto_login = d.pop("auto_login", UNSET)

        _domain_data = d.pop("domain_data", UNSET)
        domain_data: SystemDomainFromTemplateSchema | Unset
        if isinstance(_domain_data, Unset):
            domain_data = UNSET
        else:
            domain_data = SystemDomainFromTemplateSchema.from_dict(_domain_data)

        _login_data = d.pop("login_data", UNSET)
        login_data: AutoLoginSchema | Unset
        if isinstance(_login_data, Unset):
            login_data = UNSET
        else:
            login_data = AutoLoginSchema.from_dict(_login_data)

        verification_response_schema = cls(
            auto_login=auto_login,
            domain_data=domain_data,
            login_data=login_data,
        )

        verification_response_schema.additional_properties = d
        return verification_response_schema

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
