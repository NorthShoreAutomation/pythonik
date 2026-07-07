from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_suggest_schema_doc_types_item import (
    SearchSuggestSchemaDocTypesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchSuggestSchema")


@_attrs_define
class SearchSuggestSchema:
    """
    Attributes:
        field_name (str):
        query (str):
        doc_types (list[SearchSuggestSchemaDocTypesItem] | Unset):
        metadata_view_id (UUID | Unset):
    """

    field_name: str
    query: str
    doc_types: list[SearchSuggestSchemaDocTypesItem] | Unset = UNSET
    metadata_view_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_name = self.field_name

        query = self.query

        doc_types: list[str] | Unset = UNSET
        if not isinstance(self.doc_types, Unset):
            doc_types = []
            for doc_types_item_data in self.doc_types:
                doc_types_item = doc_types_item_data.value
                doc_types.append(doc_types_item)

        metadata_view_id: str | Unset = UNSET
        if not isinstance(self.metadata_view_id, Unset):
            metadata_view_id = str(self.metadata_view_id)

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

        _doc_types = d.pop("doc_types", UNSET)
        doc_types: list[SearchSuggestSchemaDocTypesItem] | Unset = UNSET
        if _doc_types is not UNSET:
            doc_types = []
            for doc_types_item_data in _doc_types:
                doc_types_item = SearchSuggestSchemaDocTypesItem(doc_types_item_data)

                doc_types.append(doc_types_item)

        _metadata_view_id = d.pop("metadata_view_id", UNSET)
        metadata_view_id: UUID | Unset
        if isinstance(_metadata_view_id, Unset):
            metadata_view_id = UNSET
        else:
            metadata_view_id = UUID(_metadata_view_id)

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
