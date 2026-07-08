from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_domain_profile_schema_industry_type_1 import (
        SystemDomainProfileSchemaIndustryType1,
    )


T = TypeVar("T", bound="SystemDomainProfileSchema")


@_attrs_define
class SystemDomainProfileSchema:
    """
    Attributes:
        industry (None | SystemDomainProfileSchemaIndustryType1 | Unset):
    """

    industry: None | SystemDomainProfileSchemaIndustryType1 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.system_domain_profile_schema_industry_type_1 import (
            SystemDomainProfileSchemaIndustryType1,
        )

        industry: dict[str, Any] | None | Unset
        if isinstance(self.industry, Unset):
            industry = UNSET
        elif isinstance(self.industry, SystemDomainProfileSchemaIndustryType1):
            industry = self.industry.to_dict()
        else:
            industry = self.industry

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if industry is not UNSET:
            field_dict["industry"] = industry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_domain_profile_schema_industry_type_1 import (
            SystemDomainProfileSchemaIndustryType1,
        )

        d = dict(src_dict)

        def _parse_industry(
            data: object,
        ) -> None | SystemDomainProfileSchemaIndustryType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                industry_type_1 = SystemDomainProfileSchemaIndustryType1.from_dict(data)

                return industry_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemDomainProfileSchemaIndustryType1 | Unset, data)

        industry = _parse_industry(d.pop("industry", UNSET))

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
