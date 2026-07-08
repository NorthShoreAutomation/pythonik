from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.criteria_term import CriteriaTerm


T = TypeVar("T", bound="CriteriaFilterSchema")


@_attrs_define
class CriteriaFilterSchema:
    """
    Attributes:
        operator (str):
        filters (list[CriteriaFilterSchema] | None | Unset):
        terms (list[CriteriaTerm] | None | Unset):
    """

    operator: str
    filters: list[CriteriaFilterSchema] | None | Unset = UNSET
    terms: list[CriteriaTerm] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operator = self.operator

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
        if terms is not UNSET:
            field_dict["terms"] = terms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.criteria_term import CriteriaTerm

        d = dict(src_dict)
        operator = d.pop("operator")

        def _parse_filters(data: object) -> list[CriteriaFilterSchema] | None | Unset:
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
                    filters_type_0_item = CriteriaFilterSchema.from_dict(
                        filters_type_0_item_data
                    )

                    filters_type_0.append(filters_type_0_item)

                return filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CriteriaFilterSchema] | None | Unset, data)

        filters = _parse_filters(d.pop("filters", UNSET))

        def _parse_terms(data: object) -> list[CriteriaTerm] | None | Unset:
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
                    terms_type_0_item = CriteriaTerm.from_dict(terms_type_0_item_data)

                    terms_type_0.append(terms_type_0_item)

                return terms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CriteriaTerm] | None | Unset, data)

        terms = _parse_terms(d.pop("terms", UNSET))

        criteria_filter_schema = cls(
            operator=operator,
            filters=filters,
            terms=terms,
        )

        criteria_filter_schema.additional_properties = d
        return criteria_filter_schema

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
