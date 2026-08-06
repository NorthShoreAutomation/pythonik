from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.complete_export_to_local_storage_schema_job_steps_type_0 import (
        CompleteExportToLocalStorageSchemaJobStepsType0,
    )


T = TypeVar("T", bound="CompleteExportToLocalStorageSchema")


@_attrs_define
class CompleteExportToLocalStorageSchema:
    """
    Attributes:
        destination_directory_path (str):
        destination_file_set_name (str):
        add_file_set (bool | None | Unset):
        asset_id (None | Unset | UUID):
        asset_paths (list[str] | None | Unset):
        collection_storage_id (None | Unset | UUID):
        component_ids (list[UUID] | None | Unset):
        delete_only_from_source_folder (bool | None | Unset):
        delete_remote_file_set_after_download (bool | None | Unset):
        delete_source_file_set_after_download (bool | None | Unset):
        destination_base_directory (None | str | Unset):
        destination_filename (None | str | Unset):
        export_metadata_format (None | str | Unset):
        export_metadata_view (None | Unset | UUID):
        export_original (bool | None | Unset):
        export_posters (bool | None | Unset):
        export_proxy (bool | None | Unset):
        export_transcription_format (None | str | Unset):
        file_set_id (None | Unset | UUID):
        format_id (None | Unset | UUID):
        id (None | Unset | UUID):
        include_original_extension (bool | None | Unset):
        job_id (None | Unset | UUID):
        job_steps (CompleteExportToLocalStorageSchemaJobStepsType0 | None | Unset):
        local_storage_id (None | Unset | UUID):
        original_storage_id (None | Unset | UUID):
        original_url (None | str | Unset):
        overwrite (bool | None | Unset):
        parent_job_id (None | Unset | UUID):
        temporary_file_set_source (bool | None | Unset):
        transfer_type (None | str | Unset):
    """

    destination_directory_path: str
    destination_file_set_name: str
    add_file_set: bool | None | Unset = UNSET
    asset_id: None | Unset | UUID = UNSET
    asset_paths: list[str] | None | Unset = UNSET
    collection_storage_id: None | Unset | UUID = UNSET
    component_ids: list[UUID] | None | Unset = UNSET
    delete_only_from_source_folder: bool | None | Unset = UNSET
    delete_remote_file_set_after_download: bool | None | Unset = UNSET
    delete_source_file_set_after_download: bool | None | Unset = UNSET
    destination_base_directory: None | str | Unset = UNSET
    destination_filename: None | str | Unset = UNSET
    export_metadata_format: None | str | Unset = UNSET
    export_metadata_view: None | Unset | UUID = UNSET
    export_original: bool | None | Unset = UNSET
    export_posters: bool | None | Unset = UNSET
    export_proxy: bool | None | Unset = UNSET
    export_transcription_format: None | str | Unset = UNSET
    file_set_id: None | Unset | UUID = UNSET
    format_id: None | Unset | UUID = UNSET
    id: None | Unset | UUID = UNSET
    include_original_extension: bool | None | Unset = UNSET
    job_id: None | Unset | UUID = UNSET
    job_steps: CompleteExportToLocalStorageSchemaJobStepsType0 | None | Unset = UNSET
    local_storage_id: None | Unset | UUID = UNSET
    original_storage_id: None | Unset | UUID = UNSET
    original_url: None | str | Unset = UNSET
    overwrite: bool | None | Unset = UNSET
    parent_job_id: None | Unset | UUID = UNSET
    temporary_file_set_source: bool | None | Unset = UNSET
    transfer_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.complete_export_to_local_storage_schema_job_steps_type_0 import (
            CompleteExportToLocalStorageSchemaJobStepsType0,
        )

        destination_directory_path = self.destination_directory_path

        destination_file_set_name = self.destination_file_set_name

        add_file_set: bool | None | Unset
        if isinstance(self.add_file_set, Unset):
            add_file_set = UNSET
        else:
            add_file_set = self.add_file_set

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

        asset_paths: list[str] | None | Unset
        if isinstance(self.asset_paths, Unset):
            asset_paths = UNSET
        elif isinstance(self.asset_paths, list):
            asset_paths = self.asset_paths

        else:
            asset_paths = self.asset_paths

        collection_storage_id: None | str | Unset
        if isinstance(self.collection_storage_id, Unset):
            collection_storage_id = UNSET
        elif isinstance(self.collection_storage_id, UUID):
            collection_storage_id = str(self.collection_storage_id)
        else:
            collection_storage_id = self.collection_storage_id

        component_ids: list[str] | None | Unset
        if isinstance(self.component_ids, Unset):
            component_ids = UNSET
        elif isinstance(self.component_ids, list):
            component_ids = []
            for component_ids_type_0_item_data in self.component_ids:
                component_ids_type_0_item = str(component_ids_type_0_item_data)
                component_ids.append(component_ids_type_0_item)

        else:
            component_ids = self.component_ids

        delete_only_from_source_folder: bool | None | Unset
        if isinstance(self.delete_only_from_source_folder, Unset):
            delete_only_from_source_folder = UNSET
        else:
            delete_only_from_source_folder = self.delete_only_from_source_folder

        delete_remote_file_set_after_download: bool | None | Unset
        if isinstance(self.delete_remote_file_set_after_download, Unset):
            delete_remote_file_set_after_download = UNSET
        else:
            delete_remote_file_set_after_download = (
                self.delete_remote_file_set_after_download
            )

        delete_source_file_set_after_download: bool | None | Unset
        if isinstance(self.delete_source_file_set_after_download, Unset):
            delete_source_file_set_after_download = UNSET
        else:
            delete_source_file_set_after_download = (
                self.delete_source_file_set_after_download
            )

        destination_base_directory: None | str | Unset
        if isinstance(self.destination_base_directory, Unset):
            destination_base_directory = UNSET
        else:
            destination_base_directory = self.destination_base_directory

        destination_filename: None | str | Unset
        if isinstance(self.destination_filename, Unset):
            destination_filename = UNSET
        else:
            destination_filename = self.destination_filename

        export_metadata_format: None | str | Unset
        if isinstance(self.export_metadata_format, Unset):
            export_metadata_format = UNSET
        else:
            export_metadata_format = self.export_metadata_format

        export_metadata_view: None | str | Unset
        if isinstance(self.export_metadata_view, Unset):
            export_metadata_view = UNSET
        elif isinstance(self.export_metadata_view, UUID):
            export_metadata_view = str(self.export_metadata_view)
        else:
            export_metadata_view = self.export_metadata_view

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

        export_transcription_format: None | str | Unset
        if isinstance(self.export_transcription_format, Unset):
            export_transcription_format = UNSET
        else:
            export_transcription_format = self.export_transcription_format

        file_set_id: None | str | Unset
        if isinstance(self.file_set_id, Unset):
            file_set_id = UNSET
        elif isinstance(self.file_set_id, UUID):
            file_set_id = str(self.file_set_id)
        else:
            file_set_id = self.file_set_id

        format_id: None | str | Unset
        if isinstance(self.format_id, Unset):
            format_id = UNSET
        elif isinstance(self.format_id, UUID):
            format_id = str(self.format_id)
        else:
            format_id = self.format_id

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

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        elif isinstance(self.job_id, UUID):
            job_id = str(self.job_id)
        else:
            job_id = self.job_id

        job_steps: dict[str, Any] | None | Unset
        if isinstance(self.job_steps, Unset):
            job_steps = UNSET
        elif isinstance(
            self.job_steps, CompleteExportToLocalStorageSchemaJobStepsType0
        ):
            job_steps = self.job_steps.to_dict()
        else:
            job_steps = self.job_steps

        local_storage_id: None | str | Unset
        if isinstance(self.local_storage_id, Unset):
            local_storage_id = UNSET
        elif isinstance(self.local_storage_id, UUID):
            local_storage_id = str(self.local_storage_id)
        else:
            local_storage_id = self.local_storage_id

        original_storage_id: None | str | Unset
        if isinstance(self.original_storage_id, Unset):
            original_storage_id = UNSET
        elif isinstance(self.original_storage_id, UUID):
            original_storage_id = str(self.original_storage_id)
        else:
            original_storage_id = self.original_storage_id

        original_url: None | str | Unset
        if isinstance(self.original_url, Unset):
            original_url = UNSET
        else:
            original_url = self.original_url

        overwrite: bool | None | Unset
        if isinstance(self.overwrite, Unset):
            overwrite = UNSET
        else:
            overwrite = self.overwrite

        parent_job_id: None | str | Unset
        if isinstance(self.parent_job_id, Unset):
            parent_job_id = UNSET
        elif isinstance(self.parent_job_id, UUID):
            parent_job_id = str(self.parent_job_id)
        else:
            parent_job_id = self.parent_job_id

        temporary_file_set_source: bool | None | Unset
        if isinstance(self.temporary_file_set_source, Unset):
            temporary_file_set_source = UNSET
        else:
            temporary_file_set_source = self.temporary_file_set_source

        transfer_type: None | str | Unset
        if isinstance(self.transfer_type, Unset):
            transfer_type = UNSET
        else:
            transfer_type = self.transfer_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destination_directory_path": destination_directory_path,
                "destination_file_set_name": destination_file_set_name,
            }
        )
        if add_file_set is not UNSET:
            field_dict["add_file_set"] = add_file_set
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if asset_paths is not UNSET:
            field_dict["asset_paths"] = asset_paths
        if collection_storage_id is not UNSET:
            field_dict["collection_storage_id"] = collection_storage_id
        if component_ids is not UNSET:
            field_dict["component_ids"] = component_ids
        if delete_only_from_source_folder is not UNSET:
            field_dict["delete_only_from_source_folder"] = (
                delete_only_from_source_folder
            )
        if delete_remote_file_set_after_download is not UNSET:
            field_dict["delete_remote_file_set_after_download"] = (
                delete_remote_file_set_after_download
            )
        if delete_source_file_set_after_download is not UNSET:
            field_dict["delete_source_file_set_after_download"] = (
                delete_source_file_set_after_download
            )
        if destination_base_directory is not UNSET:
            field_dict["destination_base_directory"] = destination_base_directory
        if destination_filename is not UNSET:
            field_dict["destination_filename"] = destination_filename
        if export_metadata_format is not UNSET:
            field_dict["export_metadata_format"] = export_metadata_format
        if export_metadata_view is not UNSET:
            field_dict["export_metadata_view"] = export_metadata_view
        if export_original is not UNSET:
            field_dict["export_original"] = export_original
        if export_posters is not UNSET:
            field_dict["export_posters"] = export_posters
        if export_proxy is not UNSET:
            field_dict["export_proxy"] = export_proxy
        if export_transcription_format is not UNSET:
            field_dict["export_transcription_format"] = export_transcription_format
        if file_set_id is not UNSET:
            field_dict["file_set_id"] = file_set_id
        if format_id is not UNSET:
            field_dict["format_id"] = format_id
        if id is not UNSET:
            field_dict["id"] = id
        if include_original_extension is not UNSET:
            field_dict["include_original_extension"] = include_original_extension
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if job_steps is not UNSET:
            field_dict["job_steps"] = job_steps
        if local_storage_id is not UNSET:
            field_dict["local_storage_id"] = local_storage_id
        if original_storage_id is not UNSET:
            field_dict["original_storage_id"] = original_storage_id
        if original_url is not UNSET:
            field_dict["original_url"] = original_url
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite
        if parent_job_id is not UNSET:
            field_dict["parent_job_id"] = parent_job_id
        if temporary_file_set_source is not UNSET:
            field_dict["temporary_file_set_source"] = temporary_file_set_source
        if transfer_type is not UNSET:
            field_dict["transfer_type"] = transfer_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.complete_export_to_local_storage_schema_job_steps_type_0 import (
            CompleteExportToLocalStorageSchemaJobStepsType0,
        )

        d = dict(src_dict)
        destination_directory_path = d.pop("destination_directory_path")

        destination_file_set_name = d.pop("destination_file_set_name")

        def _parse_add_file_set(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        add_file_set = _parse_add_file_set(d.pop("add_file_set", UNSET))

        def _parse_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                asset_id_type_0 = UUID(data)

                return asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        asset_id = _parse_asset_id(d.pop("asset_id", UNSET))

        def _parse_asset_paths(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                asset_paths_type_0 = cast(list[str], data)

                return asset_paths_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        asset_paths = _parse_asset_paths(d.pop("asset_paths", UNSET))

        def _parse_collection_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                collection_storage_id_type_0 = UUID(data)

                return collection_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        collection_storage_id = _parse_collection_storage_id(
            d.pop("collection_storage_id", UNSET)
        )

        def _parse_component_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                component_ids_type_0 = []
                _component_ids_type_0 = data
                for component_ids_type_0_item_data in _component_ids_type_0:
                    component_ids_type_0_item = UUID(component_ids_type_0_item_data)

                    component_ids_type_0.append(component_ids_type_0_item)

                return component_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        component_ids = _parse_component_ids(d.pop("component_ids", UNSET))

        def _parse_delete_only_from_source_folder(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_only_from_source_folder = _parse_delete_only_from_source_folder(
            d.pop("delete_only_from_source_folder", UNSET)
        )

        def _parse_delete_remote_file_set_after_download(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_remote_file_set_after_download = (
            _parse_delete_remote_file_set_after_download(
                d.pop("delete_remote_file_set_after_download", UNSET)
            )
        )

        def _parse_delete_source_file_set_after_download(
            data: object,
        ) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_source_file_set_after_download = (
            _parse_delete_source_file_set_after_download(
                d.pop("delete_source_file_set_after_download", UNSET)
            )
        )

        def _parse_destination_base_directory(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_base_directory = _parse_destination_base_directory(
            d.pop("destination_base_directory", UNSET)
        )

        def _parse_destination_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_filename = _parse_destination_filename(
            d.pop("destination_filename", UNSET)
        )

        def _parse_export_metadata_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        export_metadata_format = _parse_export_metadata_format(
            d.pop("export_metadata_format", UNSET)
        )

        def _parse_export_metadata_view(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                export_metadata_view_type_0 = UUID(data)

                return export_metadata_view_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        export_metadata_view = _parse_export_metadata_view(
            d.pop("export_metadata_view", UNSET)
        )

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

        def _parse_export_transcription_format(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        export_transcription_format = _parse_export_transcription_format(
            d.pop("export_transcription_format", UNSET)
        )

        def _parse_file_set_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_set_id_type_0 = UUID(data)

                return file_set_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        file_set_id = _parse_file_set_id(d.pop("file_set_id", UNSET))

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

        def _parse_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_id_type_0 = UUID(data)

                return job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

        def _parse_job_steps(
            data: object,
        ) -> CompleteExportToLocalStorageSchemaJobStepsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_steps_type_0 = (
                    CompleteExportToLocalStorageSchemaJobStepsType0.from_dict(data)
                )

                return job_steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                CompleteExportToLocalStorageSchemaJobStepsType0 | None | Unset, data
            )

        job_steps = _parse_job_steps(d.pop("job_steps", UNSET))

        def _parse_local_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                local_storage_id_type_0 = UUID(data)

                return local_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        local_storage_id = _parse_local_storage_id(d.pop("local_storage_id", UNSET))

        def _parse_original_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_storage_id_type_0 = UUID(data)

                return original_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        original_storage_id = _parse_original_storage_id(
            d.pop("original_storage_id", UNSET)
        )

        def _parse_original_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_url = _parse_original_url(d.pop("original_url", UNSET))

        def _parse_overwrite(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        overwrite = _parse_overwrite(d.pop("overwrite", UNSET))

        def _parse_parent_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_job_id_type_0 = UUID(data)

                return parent_job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_job_id = _parse_parent_job_id(d.pop("parent_job_id", UNSET))

        def _parse_temporary_file_set_source(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        temporary_file_set_source = _parse_temporary_file_set_source(
            d.pop("temporary_file_set_source", UNSET)
        )

        def _parse_transfer_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transfer_type = _parse_transfer_type(d.pop("transfer_type", UNSET))

        complete_export_to_local_storage_schema = cls(
            destination_directory_path=destination_directory_path,
            destination_file_set_name=destination_file_set_name,
            add_file_set=add_file_set,
            asset_id=asset_id,
            asset_paths=asset_paths,
            collection_storage_id=collection_storage_id,
            component_ids=component_ids,
            delete_only_from_source_folder=delete_only_from_source_folder,
            delete_remote_file_set_after_download=delete_remote_file_set_after_download,
            delete_source_file_set_after_download=delete_source_file_set_after_download,
            destination_base_directory=destination_base_directory,
            destination_filename=destination_filename,
            export_metadata_format=export_metadata_format,
            export_metadata_view=export_metadata_view,
            export_original=export_original,
            export_posters=export_posters,
            export_proxy=export_proxy,
            export_transcription_format=export_transcription_format,
            file_set_id=file_set_id,
            format_id=format_id,
            id=id,
            include_original_extension=include_original_extension,
            job_id=job_id,
            job_steps=job_steps,
            local_storage_id=local_storage_id,
            original_storage_id=original_storage_id,
            original_url=original_url,
            overwrite=overwrite,
            parent_job_id=parent_job_id,
            temporary_file_set_source=temporary_file_set_source,
            transfer_type=transfer_type,
        )

        complete_export_to_local_storage_schema.additional_properties = d
        return complete_export_to_local_storage_schema

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
