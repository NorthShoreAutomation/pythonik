from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_criteria_base_schema_doc_types_type_0_item import (
    SearchCriteriaBaseSchemaDocTypesType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.criteria_filter_schema import CriteriaFilterSchema
    from ..models.criteria_sort_schema import CriteriaSortSchema
    from ..models.facet_filter_schema import FacetFilterSchema


T = TypeVar("T", bound="SearchCriteriaBaseSchema")


@_attrs_define
class SearchCriteriaBaseSchema:
    """
    Attributes:
        doc_types (list[SearchCriteriaBaseSchemaDocTypesType0Item] | None | Unset):
        exclude_fields (list[str] | None | Unset):
        facets (list[str] | None | Unset):
        facets_filters (list[FacetFilterSchema] | None | Unset):
        filter_ (CriteriaFilterSchema | None | Unset):
        include_fields (list[str] | None | Unset):
        metadata_view_id (None | Unset | UUID):
        query (None | str | Unset):
        search_fields (list[str] | None | Unset):
        sort (list[CriteriaSortSchema] | None | Unset):
    """

    doc_types: list[SearchCriteriaBaseSchemaDocTypesType0Item] | None | Unset = UNSET
    exclude_fields: list[str] | None | Unset = UNSET
    facets: list[str] | None | Unset = UNSET
    facets_filters: list[FacetFilterSchema] | None | Unset = UNSET
    filter_: CriteriaFilterSchema | None | Unset = UNSET
    include_fields: list[str] | None | Unset = UNSET
    metadata_view_id: None | Unset | UUID = UNSET
    query: None | str | Unset = UNSET
    search_fields: list[str] | None | Unset = UNSET
    sort: list[CriteriaSortSchema] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.criteria_filter_schema import CriteriaFilterSchema

        doc_types: list[str] | None | Unset
        if isinstance(self.doc_types, Unset):
            doc_types = UNSET
        elif isinstance(self.doc_types, list):
            doc_types = []
            for doc_types_type_0_item_data in self.doc_types:
                doc_types_type_0_item = doc_types_type_0_item_data.value
                doc_types.append(doc_types_type_0_item)

        else:
            doc_types = self.doc_types

        exclude_fields: list[str] | None | Unset
        if isinstance(self.exclude_fields, Unset):
            exclude_fields = UNSET
        elif isinstance(self.exclude_fields, list):
            exclude_fields = self.exclude_fields

        else:
            exclude_fields = self.exclude_fields

        facets: list[str] | None | Unset
        if isinstance(self.facets, Unset):
            facets = UNSET
        elif isinstance(self.facets, list):
            facets = self.facets

        else:
            facets = self.facets

        facets_filters: list[dict[str, Any]] | None | Unset
        if isinstance(self.facets_filters, Unset):
            facets_filters = UNSET
        elif isinstance(self.facets_filters, list):
            facets_filters = []
            for facets_filters_type_0_item_data in self.facets_filters:
                facets_filters_type_0_item = facets_filters_type_0_item_data.to_dict()
                facets_filters.append(facets_filters_type_0_item)

        else:
            facets_filters = self.facets_filters

        filter_: dict[str, Any] | None | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        elif isinstance(self.filter_, CriteriaFilterSchema):
            filter_ = self.filter_.to_dict()
        else:
            filter_ = self.filter_

        include_fields: list[str] | None | Unset
        if isinstance(self.include_fields, Unset):
            include_fields = UNSET
        elif isinstance(self.include_fields, list):
            include_fields = self.include_fields

        else:
            include_fields = self.include_fields

        metadata_view_id: None | str | Unset
        if isinstance(self.metadata_view_id, Unset):
            metadata_view_id = UNSET
        elif isinstance(self.metadata_view_id, UUID):
            metadata_view_id = str(self.metadata_view_id)
        else:
            metadata_view_id = self.metadata_view_id

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        search_fields: list[str] | None | Unset
        if isinstance(self.search_fields, Unset):
            search_fields = UNSET
        elif isinstance(self.search_fields, list):
            search_fields = self.search_fields

        else:
            search_fields = self.search_fields

        sort: list[dict[str, Any]] | None | Unset
        if isinstance(self.sort, Unset):
            sort = UNSET
        elif isinstance(self.sort, list):
            sort = []
            for sort_type_0_item_data in self.sort:
                sort_type_0_item = sort_type_0_item_data.to_dict()
                sort.append(sort_type_0_item)

        else:
            sort = self.sort

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

        def _parse_doc_types(
            data: object,
        ) -> list[SearchCriteriaBaseSchemaDocTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                doc_types_type_0 = []
                _doc_types_type_0 = data
                for doc_types_type_0_item_data in _doc_types_type_0:
                    doc_types_type_0_item = SearchCriteriaBaseSchemaDocTypesType0Item(
                        doc_types_type_0_item_data
                    )

                    doc_types_type_0.append(doc_types_type_0_item)

                return doc_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[SearchCriteriaBaseSchemaDocTypesType0Item] | None | Unset, data
            )

        doc_types = _parse_doc_types(d.pop("doc_types", UNSET))

        def _parse_exclude_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_fields_type_0 = cast(list[str], data)

                return exclude_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude_fields = _parse_exclude_fields(d.pop("exclude_fields", UNSET))

        def _parse_facets(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                facets_type_0 = cast(list[str], data)

                return facets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        facets = _parse_facets(d.pop("facets", UNSET))

        def _parse_facets_filters(
            data: object,
        ) -> list[FacetFilterSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                facets_filters_type_0 = []
                _facets_filters_type_0 = data
                for facets_filters_type_0_item_data in _facets_filters_type_0:
                    facets_filters_type_0_item = FacetFilterSchema.from_dict(
                        facets_filters_type_0_item_data
                    )

                    facets_filters_type_0.append(facets_filters_type_0_item)

                return facets_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[FacetFilterSchema] | None | Unset, data)

        facets_filters = _parse_facets_filters(d.pop("facets_filters", UNSET))

        def _parse_filter_(data: object) -> CriteriaFilterSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_type_1 = CriteriaFilterSchema.from_dict(data)

                return filter_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CriteriaFilterSchema | None | Unset, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        def _parse_include_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                include_fields_type_0 = cast(list[str], data)

                return include_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        include_fields = _parse_include_fields(d.pop("include_fields", UNSET))

        def _parse_metadata_view_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metadata_view_id_type_0 = UUID(data)

                return metadata_view_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        metadata_view_id = _parse_metadata_view_id(d.pop("metadata_view_id", UNSET))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_search_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                search_fields_type_0 = cast(list[str], data)

                return search_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        search_fields = _parse_search_fields(d.pop("search_fields", UNSET))

        def _parse_sort(data: object) -> list[CriteriaSortSchema] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sort_type_0 = []
                _sort_type_0 = data
                for sort_type_0_item_data in _sort_type_0:
                    sort_type_0_item = CriteriaSortSchema.from_dict(
                        sort_type_0_item_data
                    )

                    sort_type_0.append(sort_type_0_item)

                return sort_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CriteriaSortSchema] | None | Unset, data)

        sort = _parse_sort(d.pop("sort", UNSET))

        search_criteria_base_schema = cls(
            doc_types=doc_types,
            exclude_fields=exclude_fields,
            facets=facets,
            facets_filters=facets_filters,
            filter_=filter_,
            include_fields=include_fields,
            metadata_view_id=metadata_view_id,
            query=query,
            search_fields=search_fields,
            sort=sort,
        )

        search_criteria_base_schema.additional_properties = d
        return search_criteria_base_schema

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
