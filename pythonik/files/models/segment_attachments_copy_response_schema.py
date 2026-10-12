from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SegmentAttachmentsCopyResponseSchema")


@_attrs_define
class SegmentAttachmentsCopyResponseSchema:
    """
    Attributes:
        destination_segment_ids_with_attachments (list[UUID] | None | Unset):
    """

    destination_segment_ids_with_attachments: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_segment_ids_with_attachments: list[str] | None | Unset
        if isinstance(self.destination_segment_ids_with_attachments, Unset):
            destination_segment_ids_with_attachments = UNSET
        elif isinstance(self.destination_segment_ids_with_attachments, list):
            destination_segment_ids_with_attachments = []
            for (
                destination_segment_ids_with_attachments_type_0_item_data
            ) in self.destination_segment_ids_with_attachments:
                destination_segment_ids_with_attachments_type_0_item = str(
                    destination_segment_ids_with_attachments_type_0_item_data
                )
                destination_segment_ids_with_attachments.append(
                    destination_segment_ids_with_attachments_type_0_item
                )

        else:
            destination_segment_ids_with_attachments = (
                self.destination_segment_ids_with_attachments
            )

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if destination_segment_ids_with_attachments is not UNSET:
            field_dict["destination_segment_ids_with_attachments"] = (
                destination_segment_ids_with_attachments
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_destination_segment_ids_with_attachments(
            data: object,
        ) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                destination_segment_ids_with_attachments_type_0 = []
                _destination_segment_ids_with_attachments_type_0 = data
                for (
                    destination_segment_ids_with_attachments_type_0_item_data
                ) in _destination_segment_ids_with_attachments_type_0:
                    destination_segment_ids_with_attachments_type_0_item = UUID(
                        destination_segment_ids_with_attachments_type_0_item_data
                    )

                    destination_segment_ids_with_attachments_type_0.append(
                        destination_segment_ids_with_attachments_type_0_item
                    )

                return destination_segment_ids_with_attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        destination_segment_ids_with_attachments = (
            _parse_destination_segment_ids_with_attachments(
                d.pop("destination_segment_ids_with_attachments", UNSET)
            )
        )

        segment_attachments_copy_response_schema = cls(
            destination_segment_ids_with_attachments=destination_segment_ids_with_attachments,
        )

        segment_attachments_copy_response_schema.additional_properties = d
        return segment_attachments_copy_response_schema

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
