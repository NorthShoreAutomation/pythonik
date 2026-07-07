from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nltf_parse_result_facets_filters import NltfParseResultFacetsFilters
    from ..models.nltf_parse_result_field_types import NltfParseResultFieldTypes
    from ..models.nltf_parse_result_filter import NltfParseResultFilter
    from ..models.nltf_parse_result_filter_options import NltfParseResultFilterOptions
    from ..models.nltf_parse_result_query_mapping import NltfParseResultQueryMapping


T = TypeVar("T", bound="NltfParseResult")


@_attrs_define
class NltfParseResult:
    """
    Attributes:
        facets_filters (NltfParseResultFacetsFilters | Unset):
        field_types (NltfParseResultFieldTypes | Unset):
        filter_ (NltfParseResultFilter | Unset):
        filter_options (NltfParseResultFilterOptions | Unset):
        query (str | Unset):
        query_mapping (NltfParseResultQueryMapping | Unset):
    """

    facets_filters: NltfParseResultFacetsFilters | Unset = UNSET
    field_types: NltfParseResultFieldTypes | Unset = UNSET
    filter_: NltfParseResultFilter | Unset = UNSET
    filter_options: NltfParseResultFilterOptions | Unset = UNSET
    query: str | Unset = UNSET
    query_mapping: NltfParseResultQueryMapping | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facets_filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.facets_filters, Unset):
            facets_filters = self.facets_filters.to_dict()

        field_types: dict[str, Any] | Unset = UNSET
        if not isinstance(self.field_types, Unset):
            field_types = self.field_types.to_dict()

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        filter_options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_options, Unset):
            filter_options = self.filter_options.to_dict()

        query = self.query

        query_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.query_mapping, Unset):
            query_mapping = self.query_mapping.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if facets_filters is not UNSET:
            field_dict["facets_filters"] = facets_filters
        if field_types is not UNSET:
            field_dict["field_types"] = field_types
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if filter_options is not UNSET:
            field_dict["filter_options"] = filter_options
        if query is not UNSET:
            field_dict["query"] = query
        if query_mapping is not UNSET:
            field_dict["query_mapping"] = query_mapping

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.nltf_parse_result_facets_filters import (
            NltfParseResultFacetsFilters,
        )
        from ..models.nltf_parse_result_field_types import NltfParseResultFieldTypes
        from ..models.nltf_parse_result_filter import NltfParseResultFilter
        from ..models.nltf_parse_result_filter_options import (
            NltfParseResultFilterOptions,
        )
        from ..models.nltf_parse_result_query_mapping import NltfParseResultQueryMapping

        d = dict(src_dict)
        _facets_filters = d.pop("facets_filters", UNSET)
        facets_filters: NltfParseResultFacetsFilters | Unset
        if isinstance(_facets_filters, Unset):
            facets_filters = UNSET
        else:
            facets_filters = NltfParseResultFacetsFilters.from_dict(_facets_filters)

        _field_types = d.pop("field_types", UNSET)
        field_types: NltfParseResultFieldTypes | Unset
        if isinstance(_field_types, Unset):
            field_types = UNSET
        else:
            field_types = NltfParseResultFieldTypes.from_dict(_field_types)

        _filter_ = d.pop("filter", UNSET)
        filter_: NltfParseResultFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = NltfParseResultFilter.from_dict(_filter_)

        _filter_options = d.pop("filter_options", UNSET)
        filter_options: NltfParseResultFilterOptions | Unset
        if isinstance(_filter_options, Unset):
            filter_options = UNSET
        else:
            filter_options = NltfParseResultFilterOptions.from_dict(_filter_options)

        query = d.pop("query", UNSET)

        _query_mapping = d.pop("query_mapping", UNSET)
        query_mapping: NltfParseResultQueryMapping | Unset
        if isinstance(_query_mapping, Unset):
            query_mapping = UNSET
        else:
            query_mapping = NltfParseResultQueryMapping.from_dict(_query_mapping)

        nltf_parse_result = cls(
            facets_filters=facets_filters,
            field_types=field_types,
            filter_=filter_,
            filter_options=filter_options,
            query=query,
            query_mapping=query_mapping,
        )

        nltf_parse_result.additional_properties = d
        return nltf_parse_result

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
