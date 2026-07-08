from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automation_run_estimate_schema_facets_type_0 import (
        AutomationRunEstimateSchemaFacetsType0,
    )


T = TypeVar("T", bound="AutomationRunEstimateSchema")


@_attrs_define
class AutomationRunEstimateSchema:
    """
    Attributes:
        errors (list[str] | None | Unset):
        facets (AutomationRunEstimateSchemaFacetsType0 | None | Unset):
        total (int | None | Unset):
    """

    errors: list[str] | None | Unset = UNSET
    facets: AutomationRunEstimateSchemaFacetsType0 | None | Unset = UNSET
    total: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.automation_run_estimate_schema_facets_type_0 import (
            AutomationRunEstimateSchemaFacetsType0,
        )

        errors: list[str] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = self.errors

        else:
            errors = self.errors

        facets: dict[str, Any] | None | Unset
        if isinstance(self.facets, Unset):
            facets = UNSET
        elif isinstance(self.facets, AutomationRunEstimateSchemaFacetsType0):
            facets = self.facets.to_dict()
        else:
            facets = self.facets

        total: int | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
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
        from ..models.automation_run_estimate_schema_facets_type_0 import (
            AutomationRunEstimateSchemaFacetsType0,
        )

        d = dict(src_dict)

        def _parse_errors(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = cast(list[str], data)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        def _parse_facets(
            data: object,
        ) -> AutomationRunEstimateSchemaFacetsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                facets_type_0 = AutomationRunEstimateSchemaFacetsType0.from_dict(data)

                return facets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AutomationRunEstimateSchemaFacetsType0 | None | Unset, data)

        facets = _parse_facets(d.pop("facets", UNSET))

        def _parse_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))

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
