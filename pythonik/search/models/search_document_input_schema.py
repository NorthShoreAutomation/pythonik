from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.search_document_input_schema_fields_item import (
        SearchDocumentInputSchemaFieldsItem,
    )


T = TypeVar("T", bound="SearchDocumentInputSchema")


@_attrs_define
class SearchDocumentInputSchema:
    """
    Attributes:
        fields (list[SearchDocumentInputSchemaFieldsItem]):
    """

    fields: list[SearchDocumentInputSchemaFieldsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fields = []
        for fields_item_data in self.fields:
            fields_item = fields_item_data.to_dict()
            fields.append(fields_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fields": fields,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_document_input_schema_fields_item import (
            SearchDocumentInputSchemaFieldsItem,
        )

        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields")
        for fields_item_data in _fields:
            fields_item = SearchDocumentInputSchemaFieldsItem.from_dict(
                fields_item_data
            )

            fields.append(fields_item)

        search_document_input_schema = cls(
            fields=fields,
        )

        search_document_input_schema.additional_properties = d
        return search_document_input_schema

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
