from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        include_assets (bool | None | Unset):
        include_collections (bool | None | Unset):
    """

    job_id: UUID
    search_ids: list[UUID]
    include_assets: bool | None | Unset = UNSET
    include_collections: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = str(self.job_id)

        search_ids = []
        for search_ids_item_data in self.search_ids:
            search_ids_item = str(search_ids_item_data)
            search_ids.append(search_ids_item)

        include_assets: bool | None | Unset
        if isinstance(self.include_assets, Unset):
            include_assets = UNSET
        else:
            include_assets = self.include_assets

        include_collections: bool | None | Unset
        if isinstance(self.include_collections, Unset):
            include_collections = UNSET
        else:
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

        def _parse_include_assets(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_assets = _parse_include_assets(d.pop("include_assets", UNSET))

        def _parse_include_collections(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_collections = _parse_include_collections(
            d.pop("include_collections", UNSET)
        )

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
