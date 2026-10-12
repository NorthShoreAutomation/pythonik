from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_segments_schema_segment_type import DeleteSegmentsSchemaSegmentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment_attribute_match import SegmentAttributeMatch


T = TypeVar("T", bound="DeleteSegmentsSchema")


@_attrs_define
class DeleteSegmentsSchema:
    """
    Attributes:
        attributes (list[SegmentAttributeMatch] | None | Unset): List of Segment attribute name/value pairs that must
            all match for a segment to be deleted. Can be combined with segment_ids or segment_type to further filter which
            segments are deleted.
        segment_ids (list[UUID] | None | Unset):
        segment_type (DeleteSegmentsSchemaSegmentType | None | Unset):
        version_id (None | Unset | UUID):
    """

    attributes: list[SegmentAttributeMatch] | None | Unset = UNSET
    segment_ids: list[UUID] | None | Unset = UNSET
    segment_type: DeleteSegmentsSchemaSegmentType | None | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attributes: list[dict[str, Any]] | None | Unset
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        elif isinstance(self.attributes, list):
            attributes = []
            for attributes_type_0_item_data in self.attributes:
                attributes_type_0_item = attributes_type_0_item_data.to_dict()
                attributes.append(attributes_type_0_item)

        else:
            attributes = self.attributes

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

        segment_type: None | str | Unset
        if isinstance(self.segment_type, Unset):
            segment_type = UNSET
        elif isinstance(self.segment_type, DeleteSegmentsSchemaSegmentType):
            segment_type = self.segment_type.value
        else:
            segment_type = self.segment_type

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
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if segment_ids is not UNSET:
            field_dict["segment_ids"] = segment_ids
        if segment_type is not UNSET:
            field_dict["segment_type"] = segment_type
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.segment_attribute_match import SegmentAttributeMatch

        d = dict(src_dict)

        def _parse_attributes(
            data: object,
        ) -> list[SegmentAttributeMatch] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attributes_type_0 = []
                _attributes_type_0 = data
                for attributes_type_0_item_data in _attributes_type_0:
                    attributes_type_0_item = SegmentAttributeMatch.from_dict(
                        attributes_type_0_item_data
                    )

                    attributes_type_0.append(attributes_type_0_item)

                return attributes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[SegmentAttributeMatch] | None | Unset, data)

        attributes = _parse_attributes(d.pop("attributes", UNSET))

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

        def _parse_segment_type(
            data: object,
        ) -> DeleteSegmentsSchemaSegmentType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                segment_type_type_1 = DeleteSegmentsSchemaSegmentType(data)

                return segment_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeleteSegmentsSchemaSegmentType | None | Unset, data)

        segment_type = _parse_segment_type(d.pop("segment_type", UNSET))

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
            attributes=attributes,
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
