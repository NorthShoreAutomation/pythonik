from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fileset_transfer_base_schema_job_steps_type_0 import (
        FilesetTransferBaseSchemaJobStepsType0,
    )


T = TypeVar("T", bound="FilesetTransferBaseSchema")


@_attrs_define
class FilesetTransferBaseSchema:
    """
    Attributes:
        asset_id (None | Unset | UUID):
        asset_paths (list[str] | None | Unset):
        collection_storage_id (None | Unset | UUID):
        component_ids (list[UUID] | None | Unset):
        delete_only_from_source_folder (bool | None | Unset):
        destination_filename (None | str | Unset):
        id (None | Unset | UUID):
        job_id (None | Unset | UUID):
        job_steps (FilesetTransferBaseSchemaJobStepsType0 | None | Unset):
        original_storage_id (None | Unset | UUID):
        original_url (None | str | Unset):
        parent_job_id (None | Unset | UUID):
        transfer_type (None | str | Unset):
    """

    asset_id: None | Unset | UUID = UNSET
    asset_paths: list[str] | None | Unset = UNSET
    collection_storage_id: None | Unset | UUID = UNSET
    component_ids: list[UUID] | None | Unset = UNSET
    delete_only_from_source_folder: bool | None | Unset = UNSET
    destination_filename: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    job_id: None | Unset | UUID = UNSET
    job_steps: FilesetTransferBaseSchemaJobStepsType0 | None | Unset = UNSET
    original_storage_id: None | Unset | UUID = UNSET
    original_url: None | str | Unset = UNSET
    parent_job_id: None | Unset | UUID = UNSET
    transfer_type: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.fileset_transfer_base_schema_job_steps_type_0 import (
            FilesetTransferBaseSchemaJobStepsType0,
        )

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

        destination_filename: None | str | Unset
        if isinstance(self.destination_filename, Unset):
            destination_filename = UNSET
        else:
            destination_filename = self.destination_filename

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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
        elif isinstance(self.job_steps, FilesetTransferBaseSchemaJobStepsType0):
            job_steps = self.job_steps.to_dict()
        else:
            job_steps = self.job_steps

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

        parent_job_id: None | str | Unset
        if isinstance(self.parent_job_id, Unset):
            parent_job_id = UNSET
        elif isinstance(self.parent_job_id, UUID):
            parent_job_id = str(self.parent_job_id)
        else:
            parent_job_id = self.parent_job_id

        transfer_type: None | str | Unset
        if isinstance(self.transfer_type, Unset):
            transfer_type = UNSET
        else:
            transfer_type = self.transfer_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if destination_filename is not UNSET:
            field_dict["destination_filename"] = destination_filename
        if id is not UNSET:
            field_dict["id"] = id
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if job_steps is not UNSET:
            field_dict["job_steps"] = job_steps
        if original_storage_id is not UNSET:
            field_dict["original_storage_id"] = original_storage_id
        if original_url is not UNSET:
            field_dict["original_url"] = original_url
        if parent_job_id is not UNSET:
            field_dict["parent_job_id"] = parent_job_id
        if transfer_type is not UNSET:
            field_dict["transfer_type"] = transfer_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fileset_transfer_base_schema_job_steps_type_0 import (
            FilesetTransferBaseSchemaJobStepsType0,
        )

        d = dict(src_dict)

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

        def _parse_destination_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_filename = _parse_destination_filename(
            d.pop("destination_filename", UNSET)
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
        ) -> FilesetTransferBaseSchemaJobStepsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_steps_type_0 = FilesetTransferBaseSchemaJobStepsType0.from_dict(
                    data
                )

                return job_steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FilesetTransferBaseSchemaJobStepsType0 | None | Unset, data)

        job_steps = _parse_job_steps(d.pop("job_steps", UNSET))

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

        def _parse_transfer_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        transfer_type = _parse_transfer_type(d.pop("transfer_type", UNSET))

        fileset_transfer_base_schema = cls(
            asset_id=asset_id,
            asset_paths=asset_paths,
            collection_storage_id=collection_storage_id,
            component_ids=component_ids,
            delete_only_from_source_folder=delete_only_from_source_folder,
            destination_filename=destination_filename,
            id=id,
            job_id=job_id,
            job_steps=job_steps,
            original_storage_id=original_storage_id,
            original_url=original_url,
            parent_job_id=parent_job_id,
            transfer_type=transfer_type,
        )

        fileset_transfer_base_schema.additional_properties = d
        return fileset_transfer_base_schema

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
