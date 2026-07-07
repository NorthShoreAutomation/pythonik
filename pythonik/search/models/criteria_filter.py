from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.criteria_term import CriteriaTerm


T = TypeVar("T", bound="CriteriaFilter")


@_attrs_define
class CriteriaFilter:
    """
    Attributes:
        operator (str):
        filters (list[CriteriaFilter] | Unset):
        terms (list[CriteriaTerm] | Unset):
    """

    operator: str
    filters: list[CriteriaFilter] | Unset = UNSET
    terms: list[CriteriaTerm] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator

        filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = []
            for filters_item_data in self.filters:
                filters_item = filters_item_data.to_dict()
                filters.append(filters_item)

        terms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.terms, Unset):
            terms = []
            for terms_item_data in self.terms:
                terms_item = terms_item_data.to_dict()
                terms.append(terms_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operator": operator,
            }
        )
        if filters is not UNSET:
            field_dict["filters"] = filters
        if terms is not UNSET:
            field_dict["terms"] = terms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.criteria_term import CriteriaTerm

        d = dict(src_dict)
        operator = d.pop("operator")

        _filters = d.pop("filters", UNSET)
        filters: list[CriteriaFilter] | Unset = UNSET
        if _filters is not UNSET:
            filters = []
            for filters_item_data in _filters:
                filters_item = CriteriaFilter.from_dict(filters_item_data)

                filters.append(filters_item)

        _terms = d.pop("terms", UNSET)
        terms: list[CriteriaTerm] | Unset = UNSET
        if _terms is not UNSET:
            terms = []
            for terms_item_data in _terms:
                terms_item = CriteriaTerm.from_dict(terms_item_data)

                terms.append(terms_item)

        criteria_filter = cls(
            operator=operator,
            filters=filters,
            terms=terms,
        )

        criteria_filter.additional_properties = d
        return criteria_filter

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
