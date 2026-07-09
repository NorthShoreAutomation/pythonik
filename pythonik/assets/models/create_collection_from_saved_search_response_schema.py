from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCollectionFromSavedSearchResponseSchema")


@_attrs_define
class CreateCollectionFromSavedSearchResponseSchema:
    """
    Attributes:
        collection_title (None | str | Unset):
    """

    collection_title: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_title: None | str | Unset
        if isinstance(self.collection_title, Unset):
            collection_title = UNSET
        else:
            collection_title = self.collection_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if collection_title is not UNSET:
            field_dict["collection_title"] = collection_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_collection_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_title = _parse_collection_title(d.pop("collection_title", UNSET))

        create_collection_from_saved_search_response_schema = cls(
            collection_title=collection_title,
        )

        create_collection_from_saved_search_response_schema.additional_properties = d
        return create_collection_from_saved_search_response_schema

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
