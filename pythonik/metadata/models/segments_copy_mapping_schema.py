from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SegmentsCopyMappingSchema")


@_attrs_define
class SegmentsCopyMappingSchema:
    """
    Attributes:
        destination_object_id (UUID):
        destination_version_id (UUID):
        source_object_id (UUID):
        source_version_id (UUID):
    """

    destination_object_id: UUID
    destination_version_id: UUID
    source_object_id: UUID
    source_version_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_object_id = str(self.destination_object_id)

        destination_version_id = str(self.destination_version_id)

        source_object_id = str(self.source_object_id)

        source_version_id = str(self.source_version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination_object_id": destination_object_id,
                "destination_version_id": destination_version_id,
                "source_object_id": source_object_id,
                "source_version_id": source_version_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination_object_id = UUID(d.pop("destination_object_id"))

        destination_version_id = UUID(d.pop("destination_version_id"))

        source_object_id = UUID(d.pop("source_object_id"))

        source_version_id = UUID(d.pop("source_version_id"))

        segments_copy_mapping_schema = cls(
            destination_object_id=destination_object_id,
            destination_version_id=destination_version_id,
            source_object_id=source_object_id,
            source_version_id=source_version_id,
        )

        segments_copy_mapping_schema.additional_properties = d
        return segments_copy_mapping_schema

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
