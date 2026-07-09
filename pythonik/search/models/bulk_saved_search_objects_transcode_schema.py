from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BulkSavedSearchObjectsTranscodeSchema")


@_attrs_define
class BulkSavedSearchObjectsTranscodeSchema:
    """
    Attributes:
        job_id (UUID):
        search_ids (list[UUID]):
    """

    job_id: UUID
    search_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        job_id = str(self.job_id)

        search_ids = []
        for search_ids_item_data in self.search_ids:
            search_ids_item = str(search_ids_item_data)
            search_ids.append(search_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_id": job_id,
                "search_ids": search_ids,
            }
        )

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

        bulk_saved_search_objects_transcode_schema = cls(
            job_id=job_id,
            search_ids=search_ids,
        )

        bulk_saved_search_objects_transcode_schema.additional_properties = d
        return bulk_saved_search_objects_transcode_schema

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
