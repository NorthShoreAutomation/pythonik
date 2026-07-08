from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_asset_version_from_version_schema_include_segment_types_type_0_item import (
    CreateAssetVersionFromVersionSchemaIncludeSegmentTypesType0Item,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAssetVersionFromVersionSchema")


@_attrs_define
class CreateAssetVersionFromVersionSchema:
    """
    Attributes:
        copy_previous_version_persons (bool | None | Unset):
        copy_previous_version_segments (bool | None | Unset):
        exclude_format_ids (list[str] | None | Unset):
        include_segment_types (list[CreateAssetVersionFromVersionSchemaIncludeSegmentTypesType0Item] | None | Unset):
        source_metadata_asset_id (None | Unset | UUID):
        system_domain_id (None | Unset | UUID):
    """

    copy_previous_version_persons: bool | None | Unset = UNSET
    copy_previous_version_segments: bool | None | Unset = UNSET
    exclude_format_ids: list[str] | None | Unset = UNSET
    include_segment_types: (
        list[CreateAssetVersionFromVersionSchemaIncludeSegmentTypesType0Item]
        | None
        | Unset
    ) = UNSET
    source_metadata_asset_id: None | Unset | UUID = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        copy_previous_version_persons: bool | None | Unset
        if isinstance(self.copy_previous_version_persons, Unset):
            copy_previous_version_persons = UNSET
        else:
            copy_previous_version_persons = self.copy_previous_version_persons

        copy_previous_version_segments: bool | None | Unset
        if isinstance(self.copy_previous_version_segments, Unset):
            copy_previous_version_segments = UNSET
        else:
            copy_previous_version_segments = self.copy_previous_version_segments

        exclude_format_ids: list[str] | None | Unset
        if isinstance(self.exclude_format_ids, Unset):
            exclude_format_ids = UNSET
        elif isinstance(self.exclude_format_ids, list):
            exclude_format_ids = self.exclude_format_ids

        else:
            exclude_format_ids = self.exclude_format_ids

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

        source_metadata_asset_id: None | str | Unset
        if isinstance(self.source_metadata_asset_id, Unset):
            source_metadata_asset_id = UNSET
        elif isinstance(self.source_metadata_asset_id, UUID):
            source_metadata_asset_id = str(self.source_metadata_asset_id)
        else:
            source_metadata_asset_id = self.source_metadata_asset_id

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
        if copy_previous_version_persons is not UNSET:
            field_dict["copy_previous_version_persons"] = copy_previous_version_persons
        if copy_previous_version_segments is not UNSET:
            field_dict["copy_previous_version_segments"] = (
                copy_previous_version_segments
            )
        if exclude_format_ids is not UNSET:
            field_dict["exclude_format_ids"] = exclude_format_ids
        if include_segment_types is not UNSET:
            field_dict["include_segment_types"] = include_segment_types
        if source_metadata_asset_id is not UNSET:
            field_dict["source_metadata_asset_id"] = source_metadata_asset_id
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_copy_previous_version_persons(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        copy_previous_version_persons = _parse_copy_previous_version_persons(
            d.pop("copy_previous_version_persons", UNSET)
        )

        def _parse_copy_previous_version_segments(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        copy_previous_version_segments = _parse_copy_previous_version_segments(
            d.pop("copy_previous_version_segments", UNSET)
        )

        def _parse_exclude_format_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_format_ids_type_0 = cast(list[str], data)

                return exclude_format_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude_format_ids = _parse_exclude_format_ids(
            d.pop("exclude_format_ids", UNSET)
        )

        def _parse_include_segment_types(
            data: object,
        ) -> (
            list[CreateAssetVersionFromVersionSchemaIncludeSegmentTypesType0Item]
            | None
            | Unset
        ):
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
                        CreateAssetVersionFromVersionSchemaIncludeSegmentTypesType0Item(
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
                list[CreateAssetVersionFromVersionSchemaIncludeSegmentTypesType0Item]
                | None
                | Unset,
                data,
            )

        include_segment_types = _parse_include_segment_types(
            d.pop("include_segment_types", UNSET)
        )

        def _parse_source_metadata_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                source_metadata_asset_id_type_0 = UUID(data)

                return source_metadata_asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        source_metadata_asset_id = _parse_source_metadata_asset_id(
            d.pop("source_metadata_asset_id", UNSET)
        )

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

        create_asset_version_from_version_schema = cls(
            copy_previous_version_persons=copy_previous_version_persons,
            copy_previous_version_segments=copy_previous_version_segments,
            exclude_format_ids=exclude_format_ids,
            include_segment_types=include_segment_types,
            source_metadata_asset_id=source_metadata_asset_id,
            system_domain_id=system_domain_id,
        )

        create_asset_version_from_version_schema.additional_properties = d
        return create_asset_version_from_version_schema

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
