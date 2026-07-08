from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_export_schema_metadata_format_type_1 import (
        CollectionExportSchemaMetadataFormatType1,
    )


T = TypeVar("T", bound="CollectionExportSchema")


@_attrs_define
class CollectionExportSchema:
    """
    Attributes:
        delete_original (bool | None | Unset):
        export_metadata (bool | None | Unset):
        export_to_asset_folder (bool | None | Unset):
        keep_collection_structure (bool | None | Unset):
        metadata_format (CollectionExportSchemaMetadataFormatType1 | None | Unset):
        metadata_view (None | Unset | UUID):
        overwrite (bool | None | Unset):
        preferred_original_storage_id (None | Unset | UUID):
    """

    delete_original: bool | None | Unset = UNSET
    export_metadata: bool | None | Unset = UNSET
    export_to_asset_folder: bool | None | Unset = UNSET
    keep_collection_structure: bool | None | Unset = UNSET
    metadata_format: CollectionExportSchemaMetadataFormatType1 | None | Unset = UNSET
    metadata_view: None | Unset | UUID = UNSET
    overwrite: bool | None | Unset = UNSET
    preferred_original_storage_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.collection_export_schema_metadata_format_type_1 import (
            CollectionExportSchemaMetadataFormatType1,
        )

        delete_original: bool | None | Unset
        if isinstance(self.delete_original, Unset):
            delete_original = UNSET
        else:
            delete_original = self.delete_original

        export_metadata: bool | None | Unset
        if isinstance(self.export_metadata, Unset):
            export_metadata = UNSET
        else:
            export_metadata = self.export_metadata

        export_to_asset_folder: bool | None | Unset
        if isinstance(self.export_to_asset_folder, Unset):
            export_to_asset_folder = UNSET
        else:
            export_to_asset_folder = self.export_to_asset_folder

        keep_collection_structure: bool | None | Unset
        if isinstance(self.keep_collection_structure, Unset):
            keep_collection_structure = UNSET
        else:
            keep_collection_structure = self.keep_collection_structure

        metadata_format: dict[str, Any] | None | Unset
        if isinstance(self.metadata_format, Unset):
            metadata_format = UNSET
        elif isinstance(
            self.metadata_format, CollectionExportSchemaMetadataFormatType1
        ):
            metadata_format = self.metadata_format.to_dict()
        else:
            metadata_format = self.metadata_format

        metadata_view: None | str | Unset
        if isinstance(self.metadata_view, Unset):
            metadata_view = UNSET
        elif isinstance(self.metadata_view, UUID):
            metadata_view = str(self.metadata_view)
        else:
            metadata_view = self.metadata_view

        overwrite: bool | None | Unset
        if isinstance(self.overwrite, Unset):
            overwrite = UNSET
        else:
            overwrite = self.overwrite

        preferred_original_storage_id: None | str | Unset
        if isinstance(self.preferred_original_storage_id, Unset):
            preferred_original_storage_id = UNSET
        elif isinstance(self.preferred_original_storage_id, UUID):
            preferred_original_storage_id = str(self.preferred_original_storage_id)
        else:
            preferred_original_storage_id = self.preferred_original_storage_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete_original is not UNSET:
            field_dict["delete_original"] = delete_original
        if export_metadata is not UNSET:
            field_dict["export_metadata"] = export_metadata
        if export_to_asset_folder is not UNSET:
            field_dict["export_to_asset_folder"] = export_to_asset_folder
        if keep_collection_structure is not UNSET:
            field_dict["keep_collection_structure"] = keep_collection_structure
        if metadata_format is not UNSET:
            field_dict["metadata_format"] = metadata_format
        if metadata_view is not UNSET:
            field_dict["metadata_view"] = metadata_view
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if preferred_original_storage_id is not UNSET:
            field_dict["preferred_original_storage_id"] = preferred_original_storage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_export_schema_metadata_format_type_1 import (
            CollectionExportSchemaMetadataFormatType1,
        )

        d = dict(src_dict)

        def _parse_delete_original(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_original = _parse_delete_original(d.pop("delete_original", UNSET))

        def _parse_export_metadata(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        export_metadata = _parse_export_metadata(d.pop("export_metadata", UNSET))

        def _parse_export_to_asset_folder(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        export_to_asset_folder = _parse_export_to_asset_folder(
            d.pop("export_to_asset_folder", UNSET)
        )

        def _parse_keep_collection_structure(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        keep_collection_structure = _parse_keep_collection_structure(
            d.pop("keep_collection_structure", UNSET)
        )

        def _parse_metadata_format(
            data: object,
        ) -> CollectionExportSchemaMetadataFormatType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_format_type_1 = (
                    CollectionExportSchemaMetadataFormatType1.from_dict(data)
                )

                return metadata_format_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CollectionExportSchemaMetadataFormatType1 | None | Unset, data)

        metadata_format = _parse_metadata_format(d.pop("metadata_format", UNSET))

        def _parse_metadata_view(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metadata_view_type_0 = UUID(data)

                return metadata_view_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        metadata_view = _parse_metadata_view(d.pop("metadata_view", UNSET))

        def _parse_overwrite(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        overwrite = _parse_overwrite(d.pop("overwrite", UNSET))

        def _parse_preferred_original_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preferred_original_storage_id_type_0 = UUID(data)

                return preferred_original_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        preferred_original_storage_id = _parse_preferred_original_storage_id(
            d.pop("preferred_original_storage_id", UNSET)
        )

        collection_export_schema = cls(
            delete_original=delete_original,
            export_metadata=export_metadata,
            export_to_asset_folder=export_to_asset_folder,
            keep_collection_structure=keep_collection_structure,
            metadata_format=metadata_format,
            metadata_view=metadata_view,
            overwrite=overwrite,
            preferred_original_storage_id=preferred_original_storage_id,
        )

        collection_export_schema.additional_properties = d
        return collection_export_schema

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
