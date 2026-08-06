from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nltf_parse_result_schema_facets_filters_type_0 import (
        NltfParseResultSchemaFacetsFiltersType0,
    )
    from ..models.nltf_parse_result_schema_field_types_type_0 import (
        NltfParseResultSchemaFieldTypesType0,
    )
    from ..models.nltf_parse_result_schema_filter_options_type_0 import (
        NltfParseResultSchemaFilterOptionsType0,
    )
    from ..models.nltf_parse_result_schema_filter_type_0 import (
        NltfParseResultSchemaFilterType0,
    )
    from ..models.nltf_parse_result_schema_query_mapping_type_0 import (
        NltfParseResultSchemaQueryMappingType0,
    )


T = TypeVar("T", bound="NltfParseResultSchema")


@_attrs_define
class NltfParseResultSchema:
    """
    Attributes:
        facets_filters (NltfParseResultSchemaFacetsFiltersType0 | None | Unset):
        field_types (NltfParseResultSchemaFieldTypesType0 | None | Unset):
        filter_ (NltfParseResultSchemaFilterType0 | None | Unset):
        filter_options (NltfParseResultSchemaFilterOptionsType0 | None | Unset):
        query (None | str | Unset):
        query_mapping (NltfParseResultSchemaQueryMappingType0 | None | Unset):
    """

    facets_filters: NltfParseResultSchemaFacetsFiltersType0 | None | Unset = UNSET
    field_types: NltfParseResultSchemaFieldTypesType0 | None | Unset = UNSET
    filter_: NltfParseResultSchemaFilterType0 | None | Unset = UNSET
    filter_options: NltfParseResultSchemaFilterOptionsType0 | None | Unset = UNSET
    query: None | str | Unset = UNSET
    query_mapping: NltfParseResultSchemaQueryMappingType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.nltf_parse_result_schema_facets_filters_type_0 import (
            NltfParseResultSchemaFacetsFiltersType0,
        )
        from ..models.nltf_parse_result_schema_field_types_type_0 import (
            NltfParseResultSchemaFieldTypesType0,
        )
        from ..models.nltf_parse_result_schema_filter_options_type_0 import (
            NltfParseResultSchemaFilterOptionsType0,
        )
        from ..models.nltf_parse_result_schema_filter_type_0 import (
            NltfParseResultSchemaFilterType0,
        )
        from ..models.nltf_parse_result_schema_query_mapping_type_0 import (
            NltfParseResultSchemaQueryMappingType0,
        )

        facets_filters: dict[str, Any] | None | Unset
        if isinstance(self.facets_filters, Unset):
            facets_filters = UNSET
        elif isinstance(self.facets_filters, NltfParseResultSchemaFacetsFiltersType0):
            facets_filters = self.facets_filters.to_dict()
        else:
            facets_filters = self.facets_filters

        field_types: dict[str, Any] | None | Unset
        if isinstance(self.field_types, Unset):
            field_types = UNSET
        elif isinstance(self.field_types, NltfParseResultSchemaFieldTypesType0):
            field_types = self.field_types.to_dict()
        else:
            field_types = self.field_types

        filter_: dict[str, Any] | None | Unset
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        elif isinstance(self.filter_, NltfParseResultSchemaFilterType0):
            filter_ = self.filter_.to_dict()
        else:
            filter_ = self.filter_

        filter_options: dict[str, Any] | None | Unset
        if isinstance(self.filter_options, Unset):
            filter_options = UNSET
        elif isinstance(self.filter_options, NltfParseResultSchemaFilterOptionsType0):
            filter_options = self.filter_options.to_dict()
        else:
            filter_options = self.filter_options

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        query_mapping: dict[str, Any] | None | Unset
        if isinstance(self.query_mapping, Unset):
            query_mapping = UNSET
        elif isinstance(self.query_mapping, NltfParseResultSchemaQueryMappingType0):
            query_mapping = self.query_mapping.to_dict()
        else:
            query_mapping = self.query_mapping

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
        from ..models.nltf_parse_result_schema_facets_filters_type_0 import (
            NltfParseResultSchemaFacetsFiltersType0,
        )
        from ..models.nltf_parse_result_schema_field_types_type_0 import (
            NltfParseResultSchemaFieldTypesType0,
        )
        from ..models.nltf_parse_result_schema_filter_options_type_0 import (
            NltfParseResultSchemaFilterOptionsType0,
        )
        from ..models.nltf_parse_result_schema_filter_type_0 import (
            NltfParseResultSchemaFilterType0,
        )
        from ..models.nltf_parse_result_schema_query_mapping_type_0 import (
            NltfParseResultSchemaQueryMappingType0,
        )

        d = dict(src_dict)

        def _parse_facets_filters(
            data: object,
        ) -> NltfParseResultSchemaFacetsFiltersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                facets_filters_type_0 = (
                    NltfParseResultSchemaFacetsFiltersType0.from_dict(data)
                )

                return facets_filters_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NltfParseResultSchemaFacetsFiltersType0 | None | Unset, data)

        facets_filters = _parse_facets_filters(d.pop("facets_filters", UNSET))

        def _parse_field_types(
            data: object,
        ) -> NltfParseResultSchemaFieldTypesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                field_types_type_0 = NltfParseResultSchemaFieldTypesType0.from_dict(
                    data
                )

                return field_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NltfParseResultSchemaFieldTypesType0 | None | Unset, data)

        field_types = _parse_field_types(d.pop("field_types", UNSET))

        def _parse_filter_(
            data: object,
        ) -> NltfParseResultSchemaFilterType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_type_0 = NltfParseResultSchemaFilterType0.from_dict(data)

                return filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NltfParseResultSchemaFilterType0 | None | Unset, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        def _parse_filter_options(
            data: object,
        ) -> NltfParseResultSchemaFilterOptionsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_options_type_0 = (
                    NltfParseResultSchemaFilterOptionsType0.from_dict(data)
                )

                return filter_options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NltfParseResultSchemaFilterOptionsType0 | None | Unset, data)

        filter_options = _parse_filter_options(d.pop("filter_options", UNSET))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_query_mapping(
            data: object,
        ) -> NltfParseResultSchemaQueryMappingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                query_mapping_type_0 = NltfParseResultSchemaQueryMappingType0.from_dict(
                    data
                )

                return query_mapping_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NltfParseResultSchemaQueryMappingType0 | None | Unset, data)

        query_mapping = _parse_query_mapping(d.pop("query_mapping", UNSET))

        nltf_parse_result_schema = cls(
            facets_filters=facets_filters,
            field_types=field_types,
            filter_=filter_,
            filter_options=filter_options,
            query=query,
            query_mapping=query_mapping,
        )

        nltf_parse_result_schema.additional_properties = d
        return nltf_parse_result_schema

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
