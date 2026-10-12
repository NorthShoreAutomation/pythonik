from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SegmentAttachmentsMoveRequestSchema")


@_attrs_define
class SegmentAttachmentsMoveRequestSchema:
    """
    Attributes:
        destination_asset_id (UUID):
        segment_ids (list[UUID]):
    """

    destination_asset_id: UUID
    segment_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_asset_id = str(self.destination_asset_id)

        segment_ids = []
        for segment_ids_item_data in self.segment_ids:
            segment_ids_item = str(segment_ids_item_data)
            segment_ids.append(segment_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination_asset_id": destination_asset_id,
                "segment_ids": segment_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        destination_asset_id = UUID(d.pop("destination_asset_id"))

        segment_ids = []
        _segment_ids = d.pop("segment_ids")
        for segment_ids_item_data in _segment_ids:
            segment_ids_item = UUID(segment_ids_item_data)

            segment_ids.append(segment_ids_item)

        segment_attachments_move_request_schema = cls(
            destination_asset_id=destination_asset_id,
            segment_ids=segment_ids,
        )

        segment_attachments_move_request_schema.additional_properties = d
        return segment_attachments_move_request_schema

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
