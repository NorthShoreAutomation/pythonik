from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SegmentAttachmentsMoveResponseSchema")


@_attrs_define
class SegmentAttachmentsMoveResponseSchema:
    """
    Attributes:
        segment_ids (list[UUID] | None | Unset):
    """

    segment_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segment_ids: list[str] | None | Unset
        if isinstance(self.segment_ids, Unset):
            segment_ids = UNSET
        elif isinstance(self.segment_ids, list):
            segment_ids = []
            for segment_ids_type_0_item_data in self.segment_ids:
                segment_ids_type_0_item = str(segment_ids_type_0_item_data)
                segment_ids.append(segment_ids_type_0_item)

        else:
            segment_ids = self.segment_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if segment_ids is not UNSET:
            field_dict["segment_ids"] = segment_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_segment_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                segment_ids_type_0 = []
                _segment_ids_type_0 = data
                for segment_ids_type_0_item_data in _segment_ids_type_0:
                    segment_ids_type_0_item = UUID(segment_ids_type_0_item_data)

                    segment_ids_type_0.append(segment_ids_type_0_item)

                return segment_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        segment_ids = _parse_segment_ids(d.pop("segment_ids", UNSET))

        segment_attachments_move_response_schema = cls(
            segment_ids=segment_ids,
        )

        segment_attachments_move_response_schema.additional_properties = d
        return segment_attachments_move_response_schema

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
