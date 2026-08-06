from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateCollectionFromSavedSearchSchema")


@_attrs_define
class CreateCollectionFromSavedSearchSchema:
    """
    Attributes:
        collection_id (UUID):
        job_id (UUID):
        saved_search_id (UUID):
    """

    collection_id: UUID
    job_id: UUID
    saved_search_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        collection_id = str(self.collection_id)

        job_id = str(self.job_id)

        saved_search_id = str(self.saved_search_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "collection_id": collection_id,
                "job_id": job_id,
                "saved_search_id": saved_search_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection_id = UUID(d.pop("collection_id"))

        job_id = UUID(d.pop("job_id"))

        saved_search_id = UUID(d.pop("saved_search_id"))

        create_collection_from_saved_search_schema = cls(
            collection_id=collection_id,
            job_id=job_id,
            saved_search_id=saved_search_id,
        )

        create_collection_from_saved_search_schema.additional_properties = d
        return create_collection_from_saved_search_schema

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
