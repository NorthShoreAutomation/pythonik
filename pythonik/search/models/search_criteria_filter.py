from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_criteria_filter_operator import SearchCriteriaFilterOperator
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_term import SearchTerm


T = TypeVar("T", bound="SearchCriteriaFilter")


@_attrs_define
class SearchCriteriaFilter:
    """
    Attributes:
        operator (SearchCriteriaFilterOperator):
        filters (list[SearchCriteriaFilter] | None | Unset):
        path (None | str | Unset): Nested field path. Required for the `NESTED` operator.
        terms (list[SearchTerm] | None | Unset):
    """

    operator: SearchCriteriaFilterOperator
    filters: list[SearchCriteriaFilter] | None | Unset = UNSET
    path: None | str | Unset = UNSET
    terms: list[SearchTerm] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator.value

        filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.filters, Unset):
            filters = UNSET
        elif isinstance(self.filters, list):
            filters = []
            for filters_type_0_item_data in self.filters:
                filters_type_0_item = filters_type_0_item_data.to_dict()
                filters.append(filters_type_0_item)

        else:
            filters = self.filters

        path: None | str | Unset
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        terms: list[dict[str, Any]] | None | Unset
        if isinstance(self.terms, Unset):
            terms = UNSET
        elif isinstance(self.terms, list):
            terms = []
            for terms_type_0_item_data in self.terms:
                terms_type_0_item = terms_type_0_item_data.to_dict()
                terms.append(terms_type_0_item)

        else:
            terms = self.terms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operator": operator,
            }
        )
        if filters is not UNSET:
            field_dict["filters"] = filters
        if path is not UNSET:
            field_dict["path"] = path
        if terms is not UNSET:
            field_dict["terms"] = terms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_term import SearchTerm

        d = dict(src_dict)
        operator = SearchCriteriaFilterOperator(d.pop("operator"))

        def _parse_filters(data: object) -> list[SearchCriteriaFilter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filters_type_0 = []
                _filters_type_0 = data
                for filters_type_0_item_data in _filters_type_0:
                    filters_type_0_item = SearchCriteriaFilter.from_dict(
                        filters_type_0_item_data
                    )

                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SearchCriteriaFilter] | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        path = _parse_path(d.pop("path", UNSET))

        def _parse_terms(data: object) -> list[SearchTerm] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                terms_type_0 = []
                _terms_type_0 = data
                for terms_type_0_item_data in _terms_type_0:
                    terms_type_0_item = SearchTerm.from_dict(terms_type_0_item_data)

                    terms_type_0.append(terms_type_0_item)

                return terms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SearchTerm] | None | Unset, data)

        terms = _parse_terms(d.pop("terms", UNSET))

        search_criteria_filter = cls(
            operator=operator,
            filters=filters,
            path=path,
            terms=terms,
        )

        search_criteria_filter.additional_properties = d
        return search_criteria_filter

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
