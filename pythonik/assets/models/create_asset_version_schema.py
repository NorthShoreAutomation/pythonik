from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_asset_version_schema_include_segment_types_item import (
    CreateAssetVersionSchemaIncludeSegmentTypesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAssetVersionSchema")


@_attrs_define
class CreateAssetVersionSchema:
    """
    Attributes:
        copy_metadata (bool | Unset):
        copy_persons (bool | Unset):
        copy_segments (bool | Unset):
        include_segment_types (list[CreateAssetVersionSchemaIncludeSegmentTypesItem] | Unset):
        source_version_id (UUID | Unset):
        system_domain_id (UUID | Unset):
    """

    copy_metadata: bool | Unset = UNSET
    copy_persons: bool | Unset = UNSET
    copy_segments: bool | Unset = UNSET
    include_segment_types: (
        list[CreateAssetVersionSchemaIncludeSegmentTypesItem] | Unset
    ) = UNSET
    source_version_id: UUID | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        copy_metadata = self.copy_metadata

        copy_persons = self.copy_persons

        copy_segments = self.copy_segments

        include_segment_types: list[str] | Unset = UNSET
        if not isinstance(self.include_segment_types, Unset):
            include_segment_types = []
            for include_segment_types_item_data in self.include_segment_types:
                include_segment_types_item = include_segment_types_item_data.value
                include_segment_types.append(include_segment_types_item)

        source_version_id: str | Unset = UNSET
        if not isinstance(self.source_version_id, Unset):
            source_version_id = str(self.source_version_id)

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if copy_metadata is not UNSET:
            field_dict["copy_metadata"] = copy_metadata
        if copy_persons is not UNSET:
            field_dict["copy_persons"] = copy_persons
        if copy_segments is not UNSET:
            field_dict["copy_segments"] = copy_segments
        if include_segment_types is not UNSET:
            field_dict["include_segment_types"] = include_segment_types
        if source_version_id is not UNSET:
            field_dict["source_version_id"] = source_version_id
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        copy_metadata = d.pop("copy_metadata", UNSET)

        copy_persons = d.pop("copy_persons", UNSET)

        copy_segments = d.pop("copy_segments", UNSET)

        _include_segment_types = d.pop("include_segment_types", UNSET)
        include_segment_types: (
            list[CreateAssetVersionSchemaIncludeSegmentTypesItem] | Unset
        ) = UNSET
        if _include_segment_types is not UNSET:
            include_segment_types = []
            for include_segment_types_item_data in _include_segment_types:
                include_segment_types_item = (
                    CreateAssetVersionSchemaIncludeSegmentTypesItem(
                        include_segment_types_item_data
                    )
                )

                include_segment_types.append(include_segment_types_item)

        _source_version_id = d.pop("source_version_id", UNSET)
        source_version_id: UUID | Unset
        if isinstance(_source_version_id, Unset):
            source_version_id = UNSET
        else:
            source_version_id = UUID(_source_version_id)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        create_asset_version_schema = cls(
            copy_metadata=copy_metadata,
            copy_persons=copy_persons,
            copy_segments=copy_segments,
            include_segment_types=include_segment_types,
            source_version_id=source_version_id,
            system_domain_id=system_domain_id,
        )

        create_asset_version_schema.additional_properties = d
        return create_asset_version_schema

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
