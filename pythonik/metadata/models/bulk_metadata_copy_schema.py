from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.segments_copy_mapping import SegmentsCopyMapping


T = TypeVar("T", bound="BulkMetadataCopySchema")


@_attrs_define
class BulkMetadataCopySchema:
    """
    Attributes:
        object_ids_mapping (list[SegmentsCopyMapping]):
    """

    object_ids_mapping: list[SegmentsCopyMapping]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ids_mapping = []
        for object_ids_mapping_item_data in self.object_ids_mapping:
            object_ids_mapping_item = object_ids_mapping_item_data.to_dict()
            object_ids_mapping.append(object_ids_mapping_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object_ids_mapping": object_ids_mapping,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segments_copy_mapping import SegmentsCopyMapping

        d = dict(src_dict)
        object_ids_mapping = []
        _object_ids_mapping = d.pop("object_ids_mapping")
        for object_ids_mapping_item_data in _object_ids_mapping:
            object_ids_mapping_item = SegmentsCopyMapping.from_dict(
                object_ids_mapping_item_data
            )

            object_ids_mapping.append(object_ids_mapping_item)

        bulk_metadata_copy_schema = cls(
            object_ids_mapping=object_ids_mapping,
        )

        bulk_metadata_copy_schema.additional_properties = d
        return bulk_metadata_copy_schema

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
