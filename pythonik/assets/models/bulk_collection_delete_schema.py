from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkCollectionDeleteSchema")


@_attrs_define
class BulkCollectionDeleteSchema:
    """
    Attributes:
        collection_ids (list[UUID]):
        job_id (UUID):
        storage_id (UUID):
    """

    collection_ids: list[UUID]
    job_id: UUID
    storage_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_ids = []
        for collection_ids_item_data in self.collection_ids:
            collection_ids_item = str(collection_ids_item_data)
            collection_ids.append(collection_ids_item)

        job_id = str(self.job_id)

        storage_id = str(self.storage_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_ids": collection_ids,
                "job_id": job_id,
                "storage_id": storage_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_ids = []
        _collection_ids = d.pop("collection_ids")
        for collection_ids_item_data in _collection_ids:
            collection_ids_item = UUID(collection_ids_item_data)

            collection_ids.append(collection_ids_item)

        job_id = UUID(d.pop("job_id"))

        storage_id = UUID(d.pop("storage_id"))

        bulk_collection_delete_schema = cls(
            collection_ids=collection_ids,
            job_id=job_id,
            storage_id=storage_id,
        )

        bulk_collection_delete_schema.additional_properties = d
        return bulk_collection_delete_schema

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
