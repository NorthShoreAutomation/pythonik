from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_segments_schema_segment_type import DeleteSegmentsSchemaSegmentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteSegmentsSchema")


@_attrs_define
class DeleteSegmentsSchema:
    """
    Attributes:
        segment_ids (list[UUID] | Unset):
        segment_type (DeleteSegmentsSchemaSegmentType | Unset):
        version_id (None | Unset | UUID):
    """

    segment_ids: list[UUID] | Unset = UNSET
    segment_type: DeleteSegmentsSchemaSegmentType | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segment_ids: list[str] | Unset = UNSET
        if not isinstance(self.segment_ids, Unset):
            segment_ids = []
            for segment_ids_item_data in self.segment_ids:
                segment_ids_item = str(segment_ids_item_data)
                segment_ids.append(segment_ids_item)

        segment_type: str | Unset = UNSET
        if not isinstance(self.segment_type, Unset):
            segment_type = self.segment_type.value

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        elif isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if segment_ids is not UNSET:
            field_dict["segment_ids"] = segment_ids
        if segment_type is not UNSET:
            field_dict["segment_type"] = segment_type
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _segment_ids = d.pop("segment_ids", UNSET)
        segment_ids: list[UUID] | Unset = UNSET
        if _segment_ids is not UNSET:
            segment_ids = []
            for segment_ids_item_data in _segment_ids:
                segment_ids_item = UUID(segment_ids_item_data)

                segment_ids.append(segment_ids_item)

        _segment_type = d.pop("segment_type", UNSET)
        segment_type: DeleteSegmentsSchemaSegmentType | Unset
        if isinstance(_segment_type, Unset):
            segment_type = UNSET
        else:
            segment_type = DeleteSegmentsSchemaSegmentType(_segment_type)

        def _parse_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                version_id_type_0 = UUID(data)

                return version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))

        delete_segments_schema = cls(
            segment_ids=segment_ids,
            segment_type=segment_type,
            version_id=version_id,
        )

        delete_segments_schema.additional_properties = d
        return delete_segments_schema

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
