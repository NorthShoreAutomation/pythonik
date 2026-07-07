from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_criteria_schema_doc_types_item import (
    SearchCriteriaSchemaDocTypesItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.criteria_filter_schema import CriteriaFilterSchema
    from ..models.criteria_sort_schema import CriteriaSortSchema
    from ..models.facet_filter_schema import FacetFilterSchema


T = TypeVar("T", bound="SearchCriteriaSchema")


@_attrs_define
class SearchCriteriaSchema:
    """
    Attributes:
        doc_types (list[SearchCriteriaSchemaDocTypesItem] | Unset):
        exclude_fields (list[str] | Unset):
        facets (list[str] | Unset):
        facets_filters (list[FacetFilterSchema] | Unset):
        filter_ (CriteriaFilterSchema | Unset):
        include_fields (list[str] | Unset):
        metadata_view_id (UUID | Unset):
        query (str | Unset):
        search_after (list[Any] | Unset): This parameter is used for infinite scroll pagination instead of
            deprecatedscroll API. It accepts a list of sort keys that will be used for getting a next page and it can be
            obtained from `_sort` key of the last object of the previous response
        search_fields (list[str] | Unset):
        sort (list[CriteriaSortSchema] | Unset):
    """

    doc_types: list[SearchCriteriaSchemaDocTypesItem] | Unset = UNSET
    exclude_fields: list[str] | Unset = UNSET
    facets: list[str] | Unset = UNSET
    facets_filters: list[FacetFilterSchema] | Unset = UNSET
    filter_: CriteriaFilterSchema | Unset = UNSET
    include_fields: list[str] | Unset = UNSET
    metadata_view_id: UUID | Unset = UNSET
    query: str | Unset = UNSET
    search_after: list[Any] | Unset = UNSET
    search_fields: list[str] | Unset = UNSET
    sort: list[CriteriaSortSchema] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        doc_types: list[str] | Unset = UNSET
        if not isinstance(self.doc_types, Unset):
            doc_types = []
            for doc_types_item_data in self.doc_types:
                doc_types_item = doc_types_item_data.value
                doc_types.append(doc_types_item)

        exclude_fields: list[str] | Unset = UNSET
        if not isinstance(self.exclude_fields, Unset):
            exclude_fields = self.exclude_fields

        facets: list[str] | Unset = UNSET
        if not isinstance(self.facets, Unset):
            facets = self.facets

        facets_filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.facets_filters, Unset):
            facets_filters = []
            for facets_filters_item_data in self.facets_filters:
                facets_filters_item = facets_filters_item_data.to_dict()
                facets_filters.append(facets_filters_item)

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        include_fields: list[str] | Unset = UNSET
        if not isinstance(self.include_fields, Unset):
            include_fields = self.include_fields

        metadata_view_id: str | Unset = UNSET
        if not isinstance(self.metadata_view_id, Unset):
            metadata_view_id = str(self.metadata_view_id)

        query = self.query

        search_after: list[Any] | Unset = UNSET
        if not isinstance(self.search_after, Unset):
            search_after = self.search_after

        search_fields: list[str] | Unset = UNSET
        if not isinstance(self.search_fields, Unset):
            search_fields = self.search_fields

        sort: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sort, Unset):
            sort = []
            for sort_item_data in self.sort:
                sort_item = sort_item_data.to_dict()
                sort.append(sort_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_types is not UNSET:
            field_dict["doc_types"] = doc_types
        if exclude_fields is not UNSET:
            field_dict["exclude_fields"] = exclude_fields
        if facets is not UNSET:
            field_dict["facets"] = facets
        if facets_filters is not UNSET:
            field_dict["facets_filters"] = facets_filters
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if include_fields is not UNSET:
            field_dict["include_fields"] = include_fields
        if metadata_view_id is not UNSET:
            field_dict["metadata_view_id"] = metadata_view_id
        if query is not UNSET:
            field_dict["query"] = query
        if search_after is not UNSET:
            field_dict["search_after"] = search_after
        if search_fields is not UNSET:
            field_dict["search_fields"] = search_fields
        if sort is not UNSET:
            field_dict["sort"] = sort

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.criteria_filter_schema import CriteriaFilterSchema
        from ..models.criteria_sort_schema import CriteriaSortSchema
        from ..models.facet_filter_schema import FacetFilterSchema

        d = dict(src_dict)
        _doc_types = d.pop("doc_types", UNSET)
        doc_types: list[SearchCriteriaSchemaDocTypesItem] | Unset = UNSET
        if _doc_types is not UNSET:
            doc_types = []
            for doc_types_item_data in _doc_types:
                doc_types_item = SearchCriteriaSchemaDocTypesItem(doc_types_item_data)

                doc_types.append(doc_types_item)

        exclude_fields = cast(list[str], d.pop("exclude_fields", UNSET))

        facets = cast(list[str], d.pop("facets", UNSET))

        _facets_filters = d.pop("facets_filters", UNSET)
        facets_filters: list[FacetFilterSchema] | Unset = UNSET
        if _facets_filters is not UNSET:
            facets_filters = []
            for facets_filters_item_data in _facets_filters:
                facets_filters_item = FacetFilterSchema.from_dict(
                    facets_filters_item_data
                )

                facets_filters.append(facets_filters_item)

        _filter_ = d.pop("filter", UNSET)
        filter_: CriteriaFilterSchema | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = CriteriaFilterSchema.from_dict(_filter_)

        include_fields = cast(list[str], d.pop("include_fields", UNSET))

        _metadata_view_id = d.pop("metadata_view_id", UNSET)
        metadata_view_id: UUID | Unset
        if isinstance(_metadata_view_id, Unset):
            metadata_view_id = UNSET
        else:
            metadata_view_id = UUID(_metadata_view_id)

        query = d.pop("query", UNSET)

        search_after = cast(list[Any], d.pop("search_after", UNSET))

        search_fields = cast(list[str], d.pop("search_fields", UNSET))

        _sort = d.pop("sort", UNSET)
        sort: list[CriteriaSortSchema] | Unset = UNSET
        if _sort is not UNSET:
            sort = []
            for sort_item_data in _sort:
                sort_item = CriteriaSortSchema.from_dict(sort_item_data)

                sort.append(sort_item)

        search_criteria_schema = cls(
            doc_types=doc_types,
            exclude_fields=exclude_fields,
            facets=facets,
            facets_filters=facets_filters,
            filter_=filter_,
            include_fields=include_fields,
            metadata_view_id=metadata_view_id,
            query=query,
            search_after=search_after,
            search_fields=search_fields,
            sort=sort,
        )

        search_criteria_schema.additional_properties = d
        return search_criteria_schema

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
