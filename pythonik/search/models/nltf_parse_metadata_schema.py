from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NltfParseMetadataSchema")


@_attrs_define
class NltfParseMetadataSchema:
    """
    Attributes:
        model (str | Unset):
        original_query (str | Unset):
        provider (str | Unset):
    """

    model: str | Unset = UNSET
    original_query: str | Unset = UNSET
    provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        original_query = self.original_query

        provider = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if original_query is not UNSET:
            field_dict["original_query"] = original_query
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model", UNSET)

        original_query = d.pop("original_query", UNSET)

        provider = d.pop("provider", UNSET)

        nltf_parse_metadata_schema = cls(
            model=model,
            original_query=original_query,
            provider=provider,
        )

        nltf_parse_metadata_schema.additional_properties = d
        return nltf_parse_metadata_schema

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
