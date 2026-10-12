from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SegmentAttachmentsCopyPairSchema")


@_attrs_define
class SegmentAttachmentsCopyPairSchema:
    """
    Attributes:
        destination_segment_id (UUID):
        source_segment_id (UUID):
    """

    destination_segment_id: UUID
    source_segment_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_segment_id = str(self.destination_segment_id)

        source_segment_id = str(self.source_segment_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination_segment_id": destination_segment_id,
                "source_segment_id": source_segment_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination_segment_id = UUID(d.pop("destination_segment_id"))

        source_segment_id = UUID(d.pop("source_segment_id"))

        segment_attachments_copy_pair_schema = cls(
            destination_segment_id=destination_segment_id,
            source_segment_id=source_segment_id,
        )

        segment_attachments_copy_pair_schema.additional_properties = d
        return segment_attachments_copy_pair_schema

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
