from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transfer_to_storage_read_schema_job_steps import (
        TransferToStorageReadSchemaJobSteps,
    )


T = TypeVar("T", bound="TransferToStorageReadSchema")


@_attrs_define
class TransferToStorageReadSchema:
    """
    Attributes:
        destination_directory_path (str):
        destination_file_set_name (str):
        add_file_set (bool | Unset):
        asset_id (UUID | Unset):
        asset_paths (list[str] | Unset):
        collection_storage_id (UUID | Unset):
        component_ids (list[UUID] | Unset):
        delete_only_from_source_folder (bool | Unset):
        delete_remote_file_set_after_download (bool | Unset):
        delete_source_file_set_after_download (bool | Unset):
        destination_base_directory (str | Unset):
        destination_filename (str | Unset):
        export_metadata_format (str | Unset):
        export_metadata_view (UUID | Unset):
        export_original (bool | Unset):
        export_posters (bool | Unset):
        export_proxy (bool | Unset):
        export_transcription_format (str | Unset):
        file_set_id (UUID | Unset):
        format_id (UUID | Unset):
        id (UUID | Unset):
        include_original_extension (bool | Unset):
        job_id (UUID | Unset):
        job_steps (TransferToStorageReadSchemaJobSteps | Unset):
        local_storage_id (UUID | Unset):
        original_storage_id (UUID | Unset):
        original_url (str | Unset):
        overwrite (bool | Unset):
        parent_job_id (UUID | Unset):
        temporary_file_set_source (bool | Unset):
        transfer_type (str | Unset):
    """

    destination_directory_path: str
    destination_file_set_name: str
    add_file_set: bool | Unset = UNSET
    asset_id: UUID | Unset = UNSET
    asset_paths: list[str] | Unset = UNSET
    collection_storage_id: UUID | Unset = UNSET
    component_ids: list[UUID] | Unset = UNSET
    delete_only_from_source_folder: bool | Unset = UNSET
    delete_remote_file_set_after_download: bool | Unset = UNSET
    delete_source_file_set_after_download: bool | Unset = UNSET
    destination_base_directory: str | Unset = UNSET
    destination_filename: str | Unset = UNSET
    export_metadata_format: str | Unset = UNSET
    export_metadata_view: UUID | Unset = UNSET
    export_original: bool | Unset = UNSET
    export_posters: bool | Unset = UNSET
    export_proxy: bool | Unset = UNSET
    export_transcription_format: str | Unset = UNSET
    file_set_id: UUID | Unset = UNSET
    format_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    include_original_extension: bool | Unset = UNSET
    job_id: UUID | Unset = UNSET
    job_steps: TransferToStorageReadSchemaJobSteps | Unset = UNSET
    local_storage_id: UUID | Unset = UNSET
    original_storage_id: UUID | Unset = UNSET
    original_url: str | Unset = UNSET
    overwrite: bool | Unset = UNSET
    parent_job_id: UUID | Unset = UNSET
    temporary_file_set_source: bool | Unset = UNSET
    transfer_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_directory_path = self.destination_directory_path

        destination_file_set_name = self.destination_file_set_name

        add_file_set = self.add_file_set

        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        asset_paths: list[str] | Unset = UNSET
        if not isinstance(self.asset_paths, Unset):
            asset_paths = self.asset_paths

        collection_storage_id: str | Unset = UNSET
        if not isinstance(self.collection_storage_id, Unset):
            collection_storage_id = str(self.collection_storage_id)

        component_ids: list[str] | Unset = UNSET
        if not isinstance(self.component_ids, Unset):
            component_ids = []
            for component_ids_item_data in self.component_ids:
                component_ids_item = str(component_ids_item_data)
                component_ids.append(component_ids_item)

        delete_only_from_source_folder = self.delete_only_from_source_folder

        delete_remote_file_set_after_download = (
            self.delete_remote_file_set_after_download
        )

        delete_source_file_set_after_download = (
            self.delete_source_file_set_after_download
        )

        destination_base_directory = self.destination_base_directory

        destination_filename = self.destination_filename

        export_metadata_format = self.export_metadata_format

        export_metadata_view: str | Unset = UNSET
        if not isinstance(self.export_metadata_view, Unset):
            export_metadata_view = str(self.export_metadata_view)

        export_original = self.export_original

        export_posters = self.export_posters

        export_proxy = self.export_proxy

        export_transcription_format = self.export_transcription_format

        file_set_id: str | Unset = UNSET
        if not isinstance(self.file_set_id, Unset):
            file_set_id = str(self.file_set_id)

        format_id: str | Unset = UNSET
        if not isinstance(self.format_id, Unset):
            format_id = str(self.format_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        include_original_extension = self.include_original_extension

        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)

        job_steps: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_steps, Unset):
            job_steps = self.job_steps.to_dict()

        local_storage_id: str | Unset = UNSET
        if not isinstance(self.local_storage_id, Unset):
            local_storage_id = str(self.local_storage_id)

        original_storage_id: str | Unset = UNSET
        if not isinstance(self.original_storage_id, Unset):
            original_storage_id = str(self.original_storage_id)

        original_url = self.original_url

        overwrite = self.overwrite

        parent_job_id: str | Unset = UNSET
        if not isinstance(self.parent_job_id, Unset):
            parent_job_id = str(self.parent_job_id)

        temporary_file_set_source = self.temporary_file_set_source

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
        from ..models.transfer_to_storage_read_schema_job_steps import (
            TransferToStorageReadSchemaJobSteps,
        )

        d = dict(src_dict)
        destination_directory_path = d.pop("destination_directory_path")

        destination_file_set_name = d.pop("destination_file_set_name")

        add_file_set = d.pop("add_file_set", UNSET)

        _asset_id = d.pop("asset_id", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        asset_paths = cast(list[str], d.pop("asset_paths", UNSET))

        _collection_storage_id = d.pop("collection_storage_id", UNSET)
        collection_storage_id: UUID | Unset
        if isinstance(_collection_storage_id, Unset):
            collection_storage_id = UNSET
        else:
            collection_storage_id = UUID(_collection_storage_id)

        _component_ids = d.pop("component_ids", UNSET)
        component_ids: list[UUID] | Unset = UNSET
        if _component_ids is not UNSET:
            component_ids = []
            for component_ids_item_data in _component_ids:
                component_ids_item = UUID(component_ids_item_data)

                component_ids.append(component_ids_item)

        delete_only_from_source_folder = d.pop("delete_only_from_source_folder", UNSET)

        delete_remote_file_set_after_download = d.pop(
            "delete_remote_file_set_after_download", UNSET
        )

        delete_source_file_set_after_download = d.pop(
            "delete_source_file_set_after_download", UNSET
        )

        destination_base_directory = d.pop("destination_base_directory", UNSET)

        destination_filename = d.pop("destination_filename", UNSET)

        export_metadata_format = d.pop("export_metadata_format", UNSET)

        _export_metadata_view = d.pop("export_metadata_view", UNSET)
        export_metadata_view: UUID | Unset
        if isinstance(_export_metadata_view, Unset):
            export_metadata_view = UNSET
        else:
            export_metadata_view = UUID(_export_metadata_view)

        export_original = d.pop("export_original", UNSET)

        export_posters = d.pop("export_posters", UNSET)

        export_proxy = d.pop("export_proxy", UNSET)

        export_transcription_format = d.pop("export_transcription_format", UNSET)

        _file_set_id = d.pop("file_set_id", UNSET)
        file_set_id: UUID | Unset
        if isinstance(_file_set_id, Unset):
            file_set_id = UNSET
        else:
            file_set_id = UUID(_file_set_id)

        _format_id = d.pop("format_id", UNSET)
        format_id: UUID | Unset
        if isinstance(_format_id, Unset):
            format_id = UNSET
        else:
            format_id = UUID(_format_id)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        include_original_extension = d.pop("include_original_extension", UNSET)

        _job_id = d.pop("job_id", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id, Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)

        _job_steps = d.pop("job_steps", UNSET)
        job_steps: TransferToStorageReadSchemaJobSteps | Unset
        if isinstance(_job_steps, Unset):
            job_steps = UNSET
        else:
            job_steps = TransferToStorageReadSchemaJobSteps.from_dict(_job_steps)

        _local_storage_id = d.pop("local_storage_id", UNSET)
        local_storage_id: UUID | Unset
        if isinstance(_local_storage_id, Unset):
            local_storage_id = UNSET
        else:
            local_storage_id = UUID(_local_storage_id)

        _original_storage_id = d.pop("original_storage_id", UNSET)
        original_storage_id: UUID | Unset
        if isinstance(_original_storage_id, Unset):
            original_storage_id = UNSET
        else:
            original_storage_id = UUID(_original_storage_id)

        original_url = d.pop("original_url", UNSET)

        overwrite = d.pop("overwrite", UNSET)

        _parent_job_id = d.pop("parent_job_id", UNSET)
        parent_job_id: UUID | Unset
        if isinstance(_parent_job_id, Unset):
            parent_job_id = UNSET
        else:
            parent_job_id = UUID(_parent_job_id)

        temporary_file_set_source = d.pop("temporary_file_set_source", UNSET)

        transfer_type = d.pop("transfer_type", UNSET)

        transfer_to_storage_read_schema = cls(
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

        transfer_to_storage_read_schema.additional_properties = d
        return transfer_to_storage_read_schema

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
