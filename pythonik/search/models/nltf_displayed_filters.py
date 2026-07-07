from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nltf_displayed_filters_facets import NltfDisplayedFiltersFacets
    from ..models.nltf_displayed_filters_filters import NltfDisplayedFiltersFilters


T = TypeVar("T", bound="NltfDisplayedFilters")


@_attrs_define
class NltfDisplayedFilters:
    """
    Attributes:
        facets (NltfDisplayedFiltersFacets | Unset):
        filters (NltfDisplayedFiltersFilters | Unset):
    """

    facets: NltfDisplayedFiltersFacets | Unset = UNSET
    filters: NltfDisplayedFiltersFilters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.facets, Unset):
            facets = self.facets.to_dict()

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if facets is not UNSET:
            field_dict["facets"] = facets
        if filters is not UNSET:
            field_dict["filters"] = filters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nltf_displayed_filters_facets import NltfDisplayedFiltersFacets
        from ..models.nltf_displayed_filters_filters import NltfDisplayedFiltersFilters

        d = dict(src_dict)
        _facets = d.pop("facets", UNSET)
        facets: NltfDisplayedFiltersFacets | Unset
        if isinstance(_facets, Unset):
            facets = UNSET
        else:
            facets = NltfDisplayedFiltersFacets.from_dict(_facets)

        _filters = d.pop("filters", UNSET)
        filters: NltfDisplayedFiltersFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = NltfDisplayedFiltersFilters.from_dict(_filters)

        nltf_displayed_filters = cls(
            facets=facets,
            filters=filters,
        )

        nltf_displayed_filters.additional_properties = d
        return nltf_displayed_filters

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
