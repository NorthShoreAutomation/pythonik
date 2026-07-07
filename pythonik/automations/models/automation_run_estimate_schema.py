from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automation_run_estimate_schema_facets import (
        AutomationRunEstimateSchemaFacets,
    )


T = TypeVar("T", bound="AutomationRunEstimateSchema")


@_attrs_define
class AutomationRunEstimateSchema:
    """
    Attributes:
        errors (list[str] | Unset):
        facets (AutomationRunEstimateSchemaFacets | Unset):
        total (int | Unset):
    """

    errors: list[str] | Unset = UNSET
    facets: AutomationRunEstimateSchemaFacets | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        errors: list[str] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        facets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.facets, Unset):
            facets = self.facets.to_dict()

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if facets is not UNSET:
            field_dict["facets"] = facets
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automation_run_estimate_schema_facets import (
            AutomationRunEstimateSchemaFacets,
        )

        d = dict(src_dict)
        errors = cast(list[str], d.pop("errors", UNSET))

        _facets = d.pop("facets", UNSET)
        facets: AutomationRunEstimateSchemaFacets | Unset
        if isinstance(_facets, Unset):
            facets = UNSET
        else:
            facets = AutomationRunEstimateSchemaFacets.from_dict(_facets)

        total = d.pop("total", UNSET)

        automation_run_estimate_schema = cls(
            errors=errors,
            facets=facets,
            total=total,
        )

        automation_run_estimate_schema.additional_properties = d
        return automation_run_estimate_schema

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
