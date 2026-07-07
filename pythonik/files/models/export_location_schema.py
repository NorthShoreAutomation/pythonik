from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.export_location_schema_metadata_format import (
    ExportLocationSchemaMetadataFormat,
)
from ..models.export_location_schema_transcription_format import (
    ExportLocationSchemaTranscriptionFormat,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExportLocationSchema")


@_attrs_define
class ExportLocationSchema:
    """
    Attributes:
        name (str):
        path (str):
        storage_id (UUID):
        description (str | Unset):
        export_metadata (bool | Unset):
        export_original (bool | Unset):
        export_posters (bool | Unset):
        export_proxy (bool | Unset):
        export_to_asset_folder (bool | Unset):
        export_transcriptions (bool | Unset):
        id (UUID | Unset):
        include_original_extension (bool | Unset):
        metadata_format (ExportLocationSchemaMetadataFormat | Unset):
        metadata_view (UUID | Unset):
        system_domain_id (UUID | Unset):
        transcode_profile_ids (list[UUID] | Unset):
        transcription_format (ExportLocationSchemaTranscriptionFormat | Unset):
    """

    name: str
    path: str
    storage_id: UUID
    description: str | Unset = UNSET
    export_metadata: bool | Unset = UNSET
    export_original: bool | Unset = UNSET
    export_posters: bool | Unset = UNSET
    export_proxy: bool | Unset = UNSET
    export_to_asset_folder: bool | Unset = UNSET
    export_transcriptions: bool | Unset = UNSET
    id: UUID | Unset = UNSET
    include_original_extension: bool | Unset = UNSET
    metadata_format: ExportLocationSchemaMetadataFormat | Unset = UNSET
    metadata_view: UUID | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    transcode_profile_ids: list[UUID] | Unset = UNSET
    transcription_format: ExportLocationSchemaTranscriptionFormat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        path = self.path

        storage_id = str(self.storage_id)

        description = self.description

        export_metadata = self.export_metadata

        export_original = self.export_original

        export_posters = self.export_posters

        export_proxy = self.export_proxy

        export_to_asset_folder = self.export_to_asset_folder

        export_transcriptions = self.export_transcriptions

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        include_original_extension = self.include_original_extension

        metadata_format: str | Unset = UNSET
        if not isinstance(self.metadata_format, Unset):
            metadata_format = self.metadata_format.value

        metadata_view: str | Unset = UNSET
        if not isinstance(self.metadata_view, Unset):
            metadata_view = str(self.metadata_view)

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        transcode_profile_ids: list[str] | Unset = UNSET
        if not isinstance(self.transcode_profile_ids, Unset):
            transcode_profile_ids = []
            for transcode_profile_ids_item_data in self.transcode_profile_ids:
                transcode_profile_ids_item = str(transcode_profile_ids_item_data)
                transcode_profile_ids.append(transcode_profile_ids_item)

        transcription_format: str | Unset = UNSET
        if not isinstance(self.transcription_format, Unset):
            transcription_format = self.transcription_format.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "path": path,
                "storage_id": storage_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if export_metadata is not UNSET:
            field_dict["export_metadata"] = export_metadata
        if export_original is not UNSET:
            field_dict["export_original"] = export_original
        if export_posters is not UNSET:
            field_dict["export_posters"] = export_posters
        if export_proxy is not UNSET:
            field_dict["export_proxy"] = export_proxy
        if export_to_asset_folder is not UNSET:
            field_dict["export_to_asset_folder"] = export_to_asset_folder
        if export_transcriptions is not UNSET:
            field_dict["export_transcriptions"] = export_transcriptions
        if id is not UNSET:
            field_dict["id"] = id
        if include_original_extension is not UNSET:
            field_dict["include_original_extension"] = include_original_extension
        if metadata_format is not UNSET:
            field_dict["metadata_format"] = metadata_format
        if metadata_view is not UNSET:
            field_dict["metadata_view"] = metadata_view
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if transcode_profile_ids is not UNSET:
            field_dict["transcode_profile_ids"] = transcode_profile_ids
        if transcription_format is not UNSET:
            field_dict["transcription_format"] = transcription_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        path = d.pop("path")

        storage_id = UUID(d.pop("storage_id"))

        description = d.pop("description", UNSET)

        export_metadata = d.pop("export_metadata", UNSET)

        export_original = d.pop("export_original", UNSET)

        export_posters = d.pop("export_posters", UNSET)

        export_proxy = d.pop("export_proxy", UNSET)

        export_to_asset_folder = d.pop("export_to_asset_folder", UNSET)

        export_transcriptions = d.pop("export_transcriptions", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        include_original_extension = d.pop("include_original_extension", UNSET)

        _metadata_format = d.pop("metadata_format", UNSET)
        metadata_format: ExportLocationSchemaMetadataFormat | Unset
        if isinstance(_metadata_format, Unset):
            metadata_format = UNSET
        else:
            metadata_format = ExportLocationSchemaMetadataFormat(_metadata_format)

        _metadata_view = d.pop("metadata_view", UNSET)
        metadata_view: UUID | Unset
        if isinstance(_metadata_view, Unset):
            metadata_view = UNSET
        else:
            metadata_view = UUID(_metadata_view)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        _transcode_profile_ids = d.pop("transcode_profile_ids", UNSET)
        transcode_profile_ids: list[UUID] | Unset = UNSET
        if _transcode_profile_ids is not UNSET:
            transcode_profile_ids = []
            for transcode_profile_ids_item_data in _transcode_profile_ids:
                transcode_profile_ids_item = UUID(transcode_profile_ids_item_data)

                transcode_profile_ids.append(transcode_profile_ids_item)

        _transcription_format = d.pop("transcription_format", UNSET)
        transcription_format: ExportLocationSchemaTranscriptionFormat | Unset
        if isinstance(_transcription_format, Unset):
            transcription_format = UNSET
        else:
            transcription_format = ExportLocationSchemaTranscriptionFormat(
                _transcription_format
            )

        export_location_schema = cls(
            name=name,
            path=path,
            storage_id=storage_id,
            description=description,
            export_metadata=export_metadata,
            export_original=export_original,
            export_posters=export_posters,
            export_proxy=export_proxy,
            export_to_asset_folder=export_to_asset_folder,
            export_transcriptions=export_transcriptions,
            id=id,
            include_original_extension=include_original_extension,
            metadata_format=metadata_format,
            metadata_view=metadata_view,
            system_domain_id=system_domain_id,
            transcode_profile_ids=transcode_profile_ids,
            transcription_format=transcription_format,
        )

        export_location_schema.additional_properties = d
        return export_location_schema

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
