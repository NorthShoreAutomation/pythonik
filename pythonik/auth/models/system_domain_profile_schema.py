from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_domain_profile_schema_industry import (
    SystemDomainProfileSchemaIndustry,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemDomainProfileSchema")


@_attrs_define
class SystemDomainProfileSchema:
    """
    Attributes:
        industry (SystemDomainProfileSchemaIndustry | Unset):
    """

    industry: SystemDomainProfileSchemaIndustry | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        industry: str | Unset = UNSET
        if not isinstance(self.industry, Unset):
            industry = self.industry.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if industry is not UNSET:
            field_dict["industry"] = industry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _industry = d.pop("industry", UNSET)
        industry: SystemDomainProfileSchemaIndustry | Unset
        if isinstance(_industry, Unset):
            industry = UNSET
        else:
            industry = SystemDomainProfileSchemaIndustry(_industry)

        system_domain_profile_schema = cls(
            industry=industry,
        )

        system_domain_profile_schema.additional_properties = d
        return system_domain_profile_schema

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
