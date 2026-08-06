from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nltf_displayed_filters_facets_type_0 import (
        NltfDisplayedFiltersFacetsType0,
    )
    from ..models.nltf_displayed_filters_filters_type_0 import (
        NltfDisplayedFiltersFiltersType0,
    )


T = TypeVar("T", bound="NltfDisplayedFilters")


@_attrs_define
class NltfDisplayedFilters:
    """
    Attributes:
        facets (NltfDisplayedFiltersFacetsType0 | None | Unset):
        filters (NltfDisplayedFiltersFiltersType0 | None | Unset):
    """

    facets: NltfDisplayedFiltersFacetsType0 | None | Unset = UNSET
    filters: NltfDisplayedFiltersFiltersType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nltf_displayed_filters_facets_type_0 import (
            NltfDisplayedFiltersFacetsType0,
        )
        from ..models.nltf_displayed_filters_filters_type_0 import (
            NltfDisplayedFiltersFiltersType0,
        )

        facets: dict[str, Any] | None | Unset
        if isinstance(self.facets, Unset):
            facets = UNSET
        elif isinstance(self.facets, NltfDisplayedFiltersFacetsType0):
            facets = self.facets.to_dict()
        else:
            facets = self.facets

        filters: dict[str, Any] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, NltfDisplayedFiltersFiltersType0):
            filters = self.filters.to_dict()
        else:
            filters = self.filters

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
        from ..models.nltf_displayed_filters_facets_type_0 import (
            NltfDisplayedFiltersFacetsType0,
        )
        from ..models.nltf_displayed_filters_filters_type_0 import (
            NltfDisplayedFiltersFiltersType0,
        )

        d = dict(src_dict)

        def _parse_facets(
            data: object,
        ) -> NltfDisplayedFiltersFacetsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                facets_type_0 = NltfDisplayedFiltersFacetsType0.from_dict(data)

                return facets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NltfDisplayedFiltersFacetsType0 | None | Unset, data)

        facets = _parse_facets(d.pop("facets", UNSET))

        def _parse_filters(
            data: object,
        ) -> NltfDisplayedFiltersFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filters_type_0 = NltfDisplayedFiltersFiltersType0.from_dict(data)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NltfDisplayedFiltersFiltersType0 | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

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
