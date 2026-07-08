from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_export_schema_metadata_format import AssetExportSchemaMetadataFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetExportSchema")


@_attrs_define
class AssetExportSchema:
    """
    Attributes:
        export_metadata (bool | None | Unset):
        export_to_asset_folder (bool | None | Unset):
        file_name (None | str | Unset):
        format_id (None | Unset | UUID):
        metadata_format (AssetExportSchemaMetadataFormat | None | Unset):
        metadata_view (None | Unset | UUID):
        overwrite (bool | None | Unset):
        preferred_original_storage_id (None | Unset | UUID):
        transcode_profile_ids (list[UUID] | None | Unset):
    """

    export_metadata: bool | None | Unset = UNSET
    export_to_asset_folder: bool | None | Unset = UNSET
    file_name: None | str | Unset = UNSET
    format_id: None | Unset | UUID = UNSET
    metadata_format: AssetExportSchemaMetadataFormat | None | Unset = UNSET
    metadata_view: None | Unset | UUID = UNSET
    overwrite: bool | None | Unset = UNSET
    preferred_original_storage_id: None | Unset | UUID = UNSET
    transcode_profile_ids: list[UUID] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        format_id: None | str | Unset
        if isinstance(self.format_id, Unset):
            format_id = UNSET
        elif isinstance(self.format_id, UUID):
            format_id = str(self.format_id)
        else:
            format_id = self.format_id

        metadata_format: None | str | Unset
        if isinstance(self.metadata_format, Unset):
            metadata_format = UNSET
        elif isinstance(self.metadata_format, AssetExportSchemaMetadataFormat):
            metadata_format = self.metadata_format.value
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

        transcode_profile_ids: list[str] | None | Unset
        if isinstance(self.transcode_profile_ids, Unset):
            transcode_profile_ids = UNSET
        elif isinstance(self.transcode_profile_ids, list):
            transcode_profile_ids = []
            for transcode_profile_ids_type_0_item_data in self.transcode_profile_ids:
                transcode_profile_ids_type_0_item = str(
                    transcode_profile_ids_type_0_item_data
                )
                transcode_profile_ids.append(transcode_profile_ids_type_0_item)

        else:
            transcode_profile_ids = self.transcode_profile_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if export_metadata is not UNSET:
            field_dict["export_metadata"] = export_metadata
        if export_to_asset_folder is not UNSET:
            field_dict["export_to_asset_folder"] = export_to_asset_folder
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if format_id is not UNSET:
            field_dict["format_id"] = format_id
        if metadata_format is not UNSET:
            field_dict["metadata_format"] = metadata_format
        if metadata_view is not UNSET:
            field_dict["metadata_view"] = metadata_view
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if preferred_original_storage_id is not UNSET:
            field_dict["preferred_original_storage_id"] = preferred_original_storage_id
        if transcode_profile_ids is not UNSET:
            field_dict["transcode_profile_ids"] = transcode_profile_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("file_name", UNSET))

        def _parse_format_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_id_type_0 = UUID(data)

                return format_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        format_id = _parse_format_id(d.pop("format_id", UNSET))

        def _parse_metadata_format(
            data: object,
        ) -> AssetExportSchemaMetadataFormat | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metadata_format_type_1 = AssetExportSchemaMetadataFormat(data)

                return metadata_format_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetExportSchemaMetadataFormat | None | Unset, data)

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

        def _parse_transcode_profile_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                transcode_profile_ids_type_0 = []
                _transcode_profile_ids_type_0 = data
                for (
                    transcode_profile_ids_type_0_item_data
                ) in _transcode_profile_ids_type_0:
                    transcode_profile_ids_type_0_item = UUID(
                        transcode_profile_ids_type_0_item_data
                    )

                    transcode_profile_ids_type_0.append(
                        transcode_profile_ids_type_0_item
                    )

                return transcode_profile_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        transcode_profile_ids = _parse_transcode_profile_ids(
            d.pop("transcode_profile_ids", UNSET)
        )

        asset_export_schema = cls(
            export_metadata=export_metadata,
            export_to_asset_folder=export_to_asset_folder,
            file_name=file_name,
            format_id=format_id,
            metadata_format=metadata_format,
            metadata_view=metadata_view,
            overwrite=overwrite,
            preferred_original_storage_id=preferred_original_storage_id,
            transcode_profile_ids=transcode_profile_ids,
        )

        asset_export_schema.additional_properties = d
        return asset_export_schema

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
