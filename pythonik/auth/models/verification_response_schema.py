from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

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
        auto_login (bool | None | Unset):
        domain_data (None | SystemDomainFromTemplateSchema | Unset):
        login_data (AutoLoginSchema | None | Unset):
    """

    auto_login: bool | None | Unset = UNSET
    domain_data: None | SystemDomainFromTemplateSchema | Unset = UNSET
    login_data: AutoLoginSchema | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.auto_login_schema import AutoLoginSchema
        from ..models.system_domain_from_template_schema import (
            SystemDomainFromTemplateSchema,
        )

        auto_login: bool | None | Unset
        if isinstance(self.auto_login, Unset):
            auto_login = UNSET
        else:
            auto_login = self.auto_login

        domain_data: dict[str, Any] | None | Unset
        if isinstance(self.domain_data, Unset):
            domain_data = UNSET
        elif isinstance(self.domain_data, SystemDomainFromTemplateSchema):
            domain_data = self.domain_data.to_dict()
        else:
            domain_data = self.domain_data

        login_data: dict[str, Any] | None | Unset
        if isinstance(self.login_data, Unset):
            login_data = UNSET
        elif isinstance(self.login_data, AutoLoginSchema):
            login_data = self.login_data.to_dict()
        else:
            login_data = self.login_data

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

        def _parse_auto_login(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        auto_login = _parse_auto_login(d.pop("auto_login", UNSET))

        def _parse_domain_data(
            data: object,
        ) -> None | SystemDomainFromTemplateSchema | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                domain_data_type_1 = SystemDomainFromTemplateSchema.from_dict(data)

                return domain_data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemDomainFromTemplateSchema | Unset, data)

        domain_data = _parse_domain_data(d.pop("domain_data", UNSET))

        def _parse_login_data(data: object) -> AutoLoginSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                login_data_type_1 = AutoLoginSchema.from_dict(data)

                return login_data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutoLoginSchema | None | Unset, data)

        login_data = _parse_login_data(d.pop("login_data", UNSET))

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
