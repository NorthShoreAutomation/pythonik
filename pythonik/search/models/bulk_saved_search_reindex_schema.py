from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkSavedSearchReindexSchema")


@_attrs_define
class BulkSavedSearchReindexSchema:
    """
    Attributes:
        job_id (UUID):
        search_ids (list[UUID]):
        include_assets (bool | Unset):
        include_collections (bool | Unset):
    """

    job_id: UUID
    search_ids: list[UUID]
    include_assets: bool | Unset = UNSET
    include_collections: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = str(self.job_id)

        search_ids = []
        for search_ids_item_data in self.search_ids:
            search_ids_item = str(search_ids_item_data)
            search_ids.append(search_ids_item)

        include_assets = self.include_assets

        include_collections = self.include_collections

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "search_ids": search_ids,
            }
        )
        if include_assets is not UNSET:
            field_dict["include_assets"] = include_assets
        if include_collections is not UNSET:
            field_dict["include_collections"] = include_collections

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = UUID(d.pop("job_id"))

        search_ids = []
        _search_ids = d.pop("search_ids")
        for search_ids_item_data in _search_ids:
            search_ids_item = UUID(search_ids_item_data)

            search_ids.append(search_ids_item)

        include_assets = d.pop("include_assets", UNSET)

        include_collections = d.pop("include_collections", UNSET)

        bulk_saved_search_reindex_schema = cls(
            job_id=job_id,
            search_ids=search_ids,
            include_assets=include_assets,
            include_collections=include_collections,
        )

        bulk_saved_search_reindex_schema.additional_properties = d
        return bulk_saved_search_reindex_schema

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
