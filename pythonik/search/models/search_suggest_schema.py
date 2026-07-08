from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_suggest_schema_doc_types_type_0_item import (
    SearchSuggestSchemaDocTypesType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchSuggestSchema")


@_attrs_define
class SearchSuggestSchema:
    """
    Attributes:
        field_name (str):
        query (str):
        doc_types (list[SearchSuggestSchemaDocTypesType0Item] | None | Unset):
        metadata_view_id (None | Unset | UUID):
    """

    field_name: str
    query: str
    doc_types: list[SearchSuggestSchemaDocTypesType0Item] | None | Unset = UNSET
    metadata_view_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        query = self.query

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

        metadata_view_id: None | str | Unset
        if isinstance(self.metadata_view_id, Unset):
            metadata_view_id = UNSET
        elif isinstance(self.metadata_view_id, UUID):
            metadata_view_id = str(self.metadata_view_id)
        else:
            metadata_view_id = self.metadata_view_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "query": query,
            }
        )
        if doc_types is not UNSET:
            field_dict["doc_types"] = doc_types
        if metadata_view_id is not UNSET:
            field_dict["metadata_view_id"] = metadata_view_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_name = d.pop("field_name")

        query = d.pop("query")

        def _parse_doc_types(
            data: object,
        ) -> list[SearchSuggestSchemaDocTypesType0Item] | None | Unset:
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
                    doc_types_type_0_item = SearchSuggestSchemaDocTypesType0Item(
                        doc_types_type_0_item_data
                    )

                    doc_types_type_0.append(doc_types_type_0_item)

                return doc_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SearchSuggestSchemaDocTypesType0Item] | None | Unset, data)

        doc_types = _parse_doc_types(d.pop("doc_types", UNSET))

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

        search_suggest_schema = cls(
            field_name=field_name,
            query=query,
            doc_types=doc_types,
            metadata_view_id=metadata_view_id,
        )

        search_suggest_schema.additional_properties = d
        return search_suggest_schema

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
