from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReindexAllCollectionsSchema")


@_attrs_define
class ReindexAllCollectionsSchema:
    """
    Attributes:
        collection_ids (list[UUID] | None):
        realms (list[str] | None | Unset):
    """

    collection_ids: list[UUID] | None
    realms: list[str] | None | Unset = UNSET
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

        realms: list[str] | None | Unset
        if isinstance(self.realms, Unset):
            realms = UNSET
        elif isinstance(self.realms, list):
            realms = self.realms

        else:
            realms = self.realms

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_ids": collection_ids,
            }
        )
        if realms is not UNSET:
            field_dict["realms"] = realms

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

        def _parse_realms(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                realms_type_0 = cast(list[str], data)

                return realms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        realms = _parse_realms(d.pop("realms", UNSET))

        reindex_all_collections_schema = cls(
            collection_ids=collection_ids,
            realms=realms,
        )

        reindex_all_collections_schema.additional_properties = d
        return reindex_all_collections_schema

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
