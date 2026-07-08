from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_location_schema_metadata_format_type_1 import (
        ExportLocationSchemaMetadataFormatType1,
    )
    from ..models.export_location_schema_transcription_format_type_1 import (
        ExportLocationSchemaTranscriptionFormatType1,
    )


T = TypeVar("T", bound="ExportLocationSchema")


@_attrs_define
class ExportLocationSchema:
    """
    Attributes:
        name (str):
        path (str):
        storage_id (UUID):
        description (None | str | Unset):
        export_metadata (bool | None | Unset):
        export_original (bool | None | Unset):
        export_posters (bool | None | Unset):
        export_proxy (bool | None | Unset):
        export_to_asset_folder (bool | None | Unset):
        export_transcriptions (bool | None | Unset):
        id (None | Unset | UUID):
        include_original_extension (bool | None | Unset):
        metadata_format (ExportLocationSchemaMetadataFormatType1 | None | Unset):
        metadata_view (None | Unset | UUID):
        system_domain_id (None | Unset | UUID):
        transcode_profile_ids (list[UUID] | None | Unset):
        transcription_format (ExportLocationSchemaTranscriptionFormatType1 | None | Unset):
    """

    name: str
    path: str
    storage_id: UUID
    description: None | str | Unset = UNSET
    export_metadata: bool | None | Unset = UNSET
    export_original: bool | None | Unset = UNSET
    export_posters: bool | None | Unset = UNSET
    export_proxy: bool | None | Unset = UNSET
    export_to_asset_folder: bool | None | Unset = UNSET
    export_transcriptions: bool | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    include_original_extension: bool | None | Unset = UNSET
    metadata_format: ExportLocationSchemaMetadataFormatType1 | None | Unset = UNSET
    metadata_view: None | Unset | UUID = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    transcode_profile_ids: list[UUID] | None | Unset = UNSET
    transcription_format: (
        ExportLocationSchemaTranscriptionFormatType1 | None | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.export_location_schema_metadata_format_type_1 import (
            ExportLocationSchemaMetadataFormatType1,
        )
        from ..models.export_location_schema_transcription_format_type_1 import (
            ExportLocationSchemaTranscriptionFormatType1,
        )

        name = self.name

        path = self.path

        storage_id = str(self.storage_id)

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        export_metadata: bool | None | Unset
        if isinstance(self.export_metadata, Unset):
            export_metadata = UNSET
        else:
            export_metadata = self.export_metadata

        export_original: bool | None | Unset
        if isinstance(self.export_original, Unset):
            export_original = UNSET
        else:
            export_original = self.export_original

        export_posters: bool | None | Unset
        if isinstance(self.export_posters, Unset):
            export_posters = UNSET
        else:
            export_posters = self.export_posters

        export_proxy: bool | None | Unset
        if isinstance(self.export_proxy, Unset):
            export_proxy = UNSET
        else:
            export_proxy = self.export_proxy

        export_to_asset_folder: bool | None | Unset
        if isinstance(self.export_to_asset_folder, Unset):
            export_to_asset_folder = UNSET
        else:
            export_to_asset_folder = self.export_to_asset_folder

        export_transcriptions: bool | None | Unset
        if isinstance(self.export_transcriptions, Unset):
            export_transcriptions = UNSET
        else:
            export_transcriptions = self.export_transcriptions

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        include_original_extension: bool | None | Unset
        if isinstance(self.include_original_extension, Unset):
            include_original_extension = UNSET
        else:
            include_original_extension = self.include_original_extension

        metadata_format: dict[str, Any] | None | Unset
        if isinstance(self.metadata_format, Unset):
            metadata_format = UNSET
        elif isinstance(self.metadata_format, ExportLocationSchemaMetadataFormatType1):
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

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

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

        transcription_format: dict[str, Any] | None | Unset
        if isinstance(self.transcription_format, Unset):
            transcription_format = UNSET
        elif isinstance(
            self.transcription_format, ExportLocationSchemaTranscriptionFormatType1
        ):
            transcription_format = self.transcription_format.to_dict()
        else:
            transcription_format = self.transcription_format

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
        from ..models.export_location_schema_metadata_format_type_1 import (
            ExportLocationSchemaMetadataFormatType1,
        )
        from ..models.export_location_schema_transcription_format_type_1 import (
            ExportLocationSchemaTranscriptionFormatType1,
        )

        d = dict(src_dict)
        name = d.pop("name")

        path = d.pop("path")

        storage_id = UUID(d.pop("storage_id"))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_export_metadata(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        export_metadata = _parse_export_metadata(d.pop("export_metadata", UNSET))

        def _parse_export_original(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        export_original = _parse_export_original(d.pop("export_original", UNSET))

        def _parse_export_posters(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        export_posters = _parse_export_posters(d.pop("export_posters", UNSET))

        def _parse_export_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        export_proxy = _parse_export_proxy(d.pop("export_proxy", UNSET))

        def _parse_export_to_asset_folder(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        export_to_asset_folder = _parse_export_to_asset_folder(
            d.pop("export_to_asset_folder", UNSET)
        )

        def _parse_export_transcriptions(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        export_transcriptions = _parse_export_transcriptions(
            d.pop("export_transcriptions", UNSET)
        )

        def _parse_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                id_type_0 = UUID(data)

                return id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_include_original_extension(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        include_original_extension = _parse_include_original_extension(
            d.pop("include_original_extension", UNSET)
        )

        def _parse_metadata_format(
            data: object,
        ) -> ExportLocationSchemaMetadataFormatType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_format_type_1 = (
                    ExportLocationSchemaMetadataFormatType1.from_dict(data)
                )

                return metadata_format_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportLocationSchemaMetadataFormatType1 | None | Unset, data)

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

        def _parse_transcription_format(
            data: object,
        ) -> ExportLocationSchemaTranscriptionFormatType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                transcription_format_type_1 = (
                    ExportLocationSchemaTranscriptionFormatType1.from_dict(data)
                )

                return transcription_format_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                ExportLocationSchemaTranscriptionFormatType1 | None | Unset, data
            )

        transcription_format = _parse_transcription_format(
            d.pop("transcription_format", UNSET)
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
