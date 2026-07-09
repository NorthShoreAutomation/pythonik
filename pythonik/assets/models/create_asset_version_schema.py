from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_asset_version_schema_include_segment_types_type_0_item import (
    CreateAssetVersionSchemaIncludeSegmentTypesType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAssetVersionSchema")


@_attrs_define
class CreateAssetVersionSchema:
    """
    Attributes:
        copy_metadata (bool | None | Unset):
        copy_persons (bool | None | Unset):
        copy_segments (bool | None | Unset):
        include_segment_types (list[CreateAssetVersionSchemaIncludeSegmentTypesType0Item] | None | Unset):
        source_version_id (None | Unset | UUID):
        system_domain_id (None | Unset | UUID):
    """

    copy_metadata: bool | None | Unset = UNSET
    copy_persons: bool | None | Unset = UNSET
    copy_segments: bool | None | Unset = UNSET
    include_segment_types: (
        list[CreateAssetVersionSchemaIncludeSegmentTypesType0Item] | None | Unset
    ) = UNSET
    source_version_id: None | Unset | UUID = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        copy_metadata: bool | None | Unset
        if isinstance(self.copy_metadata, Unset):
            copy_metadata = UNSET
        else:
            copy_metadata = self.copy_metadata

        copy_persons: bool | None | Unset
        if isinstance(self.copy_persons, Unset):
            copy_persons = UNSET
        else:
            copy_persons = self.copy_persons

        copy_segments: bool | None | Unset
        if isinstance(self.copy_segments, Unset):
            copy_segments = UNSET
        else:
            copy_segments = self.copy_segments

        include_segment_types: list[str] | None | Unset
        if isinstance(self.include_segment_types, Unset):
            include_segment_types = UNSET
        elif isinstance(self.include_segment_types, list):
            include_segment_types = []
            for include_segment_types_type_0_item_data in self.include_segment_types:
                include_segment_types_type_0_item = (
                    include_segment_types_type_0_item_data.value
                )
                include_segment_types.append(include_segment_types_type_0_item)

        else:
            include_segment_types = self.include_segment_types

        source_version_id: None | str | Unset
        if isinstance(self.source_version_id, Unset):
            source_version_id = UNSET
        elif isinstance(self.source_version_id, UUID):
            source_version_id = str(self.source_version_id)
        else:
            source_version_id = self.source_version_id

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

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

        def _parse_copy_metadata(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        copy_metadata = _parse_copy_metadata(d.pop("copy_metadata", UNSET))

        def _parse_copy_persons(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        copy_persons = _parse_copy_persons(d.pop("copy_persons", UNSET))

        def _parse_copy_segments(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        copy_segments = _parse_copy_segments(d.pop("copy_segments", UNSET))

        def _parse_include_segment_types(
            data: object,
        ) -> list[CreateAssetVersionSchemaIncludeSegmentTypesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                include_segment_types_type_0 = []
                _include_segment_types_type_0 = data
                for (
                    include_segment_types_type_0_item_data
                ) in _include_segment_types_type_0:
                    include_segment_types_type_0_item = (
                        CreateAssetVersionSchemaIncludeSegmentTypesType0Item(
                            include_segment_types_type_0_item_data
                        )
                    )

                    include_segment_types_type_0.append(
                        include_segment_types_type_0_item
                    )

                return include_segment_types_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CreateAssetVersionSchemaIncludeSegmentTypesType0Item]
                | None
                | Unset,
                data,
            )

        include_segment_types = _parse_include_segment_types(
            d.pop("include_segment_types", UNSET)
        )

        def _parse_source_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_version_id_type_0 = UUID(data)

                return source_version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_version_id = _parse_source_version_id(d.pop("source_version_id", UNSET))

        def _parse_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_id_type_0 = UUID(data)

                return system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

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
