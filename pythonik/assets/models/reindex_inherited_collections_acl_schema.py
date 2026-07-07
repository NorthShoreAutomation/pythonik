from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReindexInheritedCollectionsACLSchema")


@_attrs_define
class ReindexInheritedCollectionsACLSchema:
    """
    Attributes:
        collection_ids (list[UUID] | None):
        content (bool | Unset):  Default: True.
        recursive (bool | Unset):  Default: True.
    """

    collection_ids: list[UUID] | None
    content: bool | Unset = True
    recursive: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_ids: list[str] | None
        if isinstance(self.collection_ids, list):
            collection_ids = []
            for collection_ids_type_0_item_data in self.collection_ids:
                collection_ids_type_0_item = str(collection_ids_type_0_item_data)
                collection_ids.append(collection_ids_type_0_item)

        else:
            collection_ids = self.collection_ids

        content = self.content

        recursive = self.recursive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_ids": collection_ids,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if recursive is not UNSET:
            field_dict["recursive"] = recursive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_collection_ids(data: object) -> list[UUID] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                collection_ids_type_0 = []
                _collection_ids_type_0 = data
                for collection_ids_type_0_item_data in _collection_ids_type_0:
                    collection_ids_type_0_item = UUID(collection_ids_type_0_item_data)

                    collection_ids_type_0.append(collection_ids_type_0_item)

                return collection_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None, data)

        collection_ids = _parse_collection_ids(d.pop("collection_ids"))

        content = d.pop("content", UNSET)

        recursive = d.pop("recursive", UNSET)

        reindex_inherited_collections_acl_schema = cls(
            collection_ids=collection_ids,
            content=content,
            recursive=recursive,
        )

        reindex_inherited_collections_acl_schema.additional_properties = d
        return reindex_inherited_collections_acl_schema

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
