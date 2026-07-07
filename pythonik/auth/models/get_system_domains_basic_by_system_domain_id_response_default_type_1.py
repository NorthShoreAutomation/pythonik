from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_system_domains_basic_by_system_domain_id_response_default_type_1_errors import (
        GetSystemDomainsBasicBySystemDomainIdResponseDefaultType1Errors,
    )


T = TypeVar("T", bound="GetSystemDomainsBasicBySystemDomainIdResponseDefaultType1")


@_attrs_define
class GetSystemDomainsBasicBySystemDomainIdResponseDefaultType1:
    """
    Attributes:
        errors (GetSystemDomainsBasicBySystemDomainIdResponseDefaultType1Errors | Unset):
    """

    errors: GetSystemDomainsBasicBySystemDomainIdResponseDefaultType1Errors | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_system_domains_basic_by_system_domain_id_response_default_type_1_errors import (
            GetSystemDomainsBasicBySystemDomainIdResponseDefaultType1Errors,
        )

        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: GetSystemDomainsBasicBySystemDomainIdResponseDefaultType1Errors | Unset
        if isinstance(_errors, Unset):
            errors = UNSET
        else:
            errors = GetSystemDomainsBasicBySystemDomainIdResponseDefaultType1Errors.from_dict(
                _errors
            )

        get_system_domains_basic_by_system_domain_id_response_default_type_1 = cls(
            errors=errors,
        )

        get_system_domains_basic_by_system_domain_id_response_default_type_1.additional_properties = d
        return get_system_domains_basic_by_system_domain_id_response_default_type_1

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
