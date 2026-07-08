from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.transfer_cloud_schema_status import TransferCloudSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transfer_cloud_schema_job_steps_type_0 import (
        TransferCloudSchemaJobStepsType0,
    )


T = TypeVar("T", bound="TransferCloudSchema")


@_attrs_define
class TransferCloudSchema:
    """
    Attributes:
        asset_id (None | Unset | UUID):
        asset_paths (list[str] | None | Unset):
        celery_task_id (None | Unset | UUID):
        collection_storage_id (None | Unset | UUID):
        component_ids (list[UUID] | None | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        delete_only_from_source_folder (bool | None | Unset):
        delete_original (bool | None | Unset):
        destination_directory_path (None | str | Unset):
        destination_filename (None | str | Unset):
        destination_storage_id (None | Unset | UUID):
        id (None | Unset | UUID):
        job_id (None | Unset | UUID):
        job_steps (None | TransferCloudSchemaJobStepsType0 | Unset):
        original_file_set_id (None | Unset | UUID):
        original_storage_id (None | Unset | UUID):
        original_url (None | str | Unset):
        parent_job_id (None | Unset | UUID):
        priority (int | None | Unset):
        status (None | TransferCloudSchemaStatus | Unset):
        success (None | str | Unset):
        transfer_type (None | Unset | UUID):
        user_id (None | Unset | UUID):
    """

    asset_id: None | Unset | UUID = UNSET
    asset_paths: list[str] | None | Unset = UNSET
    celery_task_id: None | Unset | UUID = UNSET
    collection_storage_id: None | Unset | UUID = UNSET
    component_ids: list[UUID] | None | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    delete_only_from_source_folder: bool | None | Unset = UNSET
    delete_original: bool | None | Unset = UNSET
    destination_directory_path: None | str | Unset = UNSET
    destination_filename: None | str | Unset = UNSET
    destination_storage_id: None | Unset | UUID = UNSET
    id: None | Unset | UUID = UNSET
    job_id: None | Unset | UUID = UNSET
    job_steps: None | TransferCloudSchemaJobStepsType0 | Unset = UNSET
    original_file_set_id: None | Unset | UUID = UNSET
    original_storage_id: None | Unset | UUID = UNSET
    original_url: None | str | Unset = UNSET
    parent_job_id: None | Unset | UUID = UNSET
    priority: int | None | Unset = UNSET
    status: None | TransferCloudSchemaStatus | Unset = UNSET
    success: None | str | Unset = UNSET
    transfer_type: None | Unset | UUID = UNSET
    user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.transfer_cloud_schema_job_steps_type_0 import (
            TransferCloudSchemaJobStepsType0,
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

        celery_task_id: None | str | Unset
        if isinstance(self.celery_task_id, Unset):
            celery_task_id = UNSET
        elif isinstance(self.celery_task_id, UUID):
            celery_task_id = str(self.celery_task_id)
        else:
            celery_task_id = self.celery_task_id

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

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        delete_only_from_source_folder: bool | None | Unset
        if isinstance(self.delete_only_from_source_folder, Unset):
            delete_only_from_source_folder = UNSET
        else:
            delete_only_from_source_folder = self.delete_only_from_source_folder

        delete_original: bool | None | Unset
        if isinstance(self.delete_original, Unset):
            delete_original = UNSET
        else:
            delete_original = self.delete_original

        destination_directory_path: None | str | Unset
        if isinstance(self.destination_directory_path, Unset):
            destination_directory_path = UNSET
        else:
            destination_directory_path = self.destination_directory_path

        destination_filename: None | str | Unset
        if isinstance(self.destination_filename, Unset):
            destination_filename = UNSET
        else:
            destination_filename = self.destination_filename

        destination_storage_id: None | str | Unset
        if isinstance(self.destination_storage_id, Unset):
            destination_storage_id = UNSET
        elif isinstance(self.destination_storage_id, UUID):
            destination_storage_id = str(self.destination_storage_id)
        else:
            destination_storage_id = self.destination_storage_id

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
        elif isinstance(self.job_steps, TransferCloudSchemaJobStepsType0):
            job_steps = self.job_steps.to_dict()
        else:
            job_steps = self.job_steps

        original_file_set_id: None | str | Unset
        if isinstance(self.original_file_set_id, Unset):
            original_file_set_id = UNSET
        elif isinstance(self.original_file_set_id, UUID):
            original_file_set_id = str(self.original_file_set_id)
        else:
            original_file_set_id = self.original_file_set_id

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

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, TransferCloudSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        success: None | str | Unset
        if isinstance(self.success, Unset):
            success = UNSET
        else:
            success = self.success

        transfer_type: None | str | Unset
        if isinstance(self.transfer_type, Unset):
            transfer_type = UNSET
        elif isinstance(self.transfer_type, UUID):
            transfer_type = str(self.transfer_type)
        else:
            transfer_type = self.transfer_type

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if asset_paths is not UNSET:
            field_dict["asset_paths"] = asset_paths
        if celery_task_id is not UNSET:
            field_dict["celery_task_id"] = celery_task_id
        if collection_storage_id is not UNSET:
            field_dict["collection_storage_id"] = collection_storage_id
        if component_ids is not UNSET:
            field_dict["component_ids"] = component_ids
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if delete_only_from_source_folder is not UNSET:
            field_dict["delete_only_from_source_folder"] = (
                delete_only_from_source_folder
            )
        if delete_original is not UNSET:
            field_dict["delete_original"] = delete_original
        if destination_directory_path is not UNSET:
            field_dict["destination_directory_path"] = destination_directory_path
        if destination_filename is not UNSET:
            field_dict["destination_filename"] = destination_filename
        if destination_storage_id is not UNSET:
            field_dict["destination_storage_id"] = destination_storage_id
        if id is not UNSET:
            field_dict["id"] = id
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if job_steps is not UNSET:
            field_dict["job_steps"] = job_steps
        if original_file_set_id is not UNSET:
            field_dict["original_file_set_id"] = original_file_set_id
        if original_storage_id is not UNSET:
            field_dict["original_storage_id"] = original_storage_id
        if original_url is not UNSET:
            field_dict["original_url"] = original_url
        if parent_job_id is not UNSET:
            field_dict["parent_job_id"] = parent_job_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if status is not UNSET:
            field_dict["status"] = status
        if success is not UNSET:
            field_dict["success"] = success
        if transfer_type is not UNSET:
            field_dict["transfer_type"] = transfer_type
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transfer_cloud_schema_job_steps_type_0 import (
            TransferCloudSchemaJobStepsType0,
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

        def _parse_celery_task_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                celery_task_id_type_0 = UUID(data)

                return celery_task_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        celery_task_id = _parse_celery_task_id(d.pop("celery_task_id", UNSET))

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

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = datetime.datetime.fromisoformat(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_delete_only_from_source_folder(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_only_from_source_folder = _parse_delete_only_from_source_folder(
            d.pop("delete_only_from_source_folder", UNSET)
        )

        def _parse_delete_original(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_original = _parse_delete_original(d.pop("delete_original", UNSET))

        def _parse_destination_directory_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_directory_path = _parse_destination_directory_path(
            d.pop("destination_directory_path", UNSET)
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

        def _parse_destination_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                destination_storage_id_type_0 = UUID(data)

                return destination_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        destination_storage_id = _parse_destination_storage_id(
            d.pop("destination_storage_id", UNSET)
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
        ) -> None | TransferCloudSchemaJobStepsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                job_steps_type_0 = TransferCloudSchemaJobStepsType0.from_dict(data)

                return job_steps_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransferCloudSchemaJobStepsType0 | Unset, data)

        job_steps = _parse_job_steps(d.pop("job_steps", UNSET))

        def _parse_original_file_set_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_file_set_id_type_0 = UUID(data)

                return original_file_set_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        original_file_set_id = _parse_original_file_set_id(
            d.pop("original_file_set_id", UNSET)
        )

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

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_status(data: object) -> None | TransferCloudSchemaStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = TransferCloudSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TransferCloudSchemaStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_success(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        success = _parse_success(d.pop("success", UNSET))

        def _parse_transfer_type(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transfer_type_type_0 = UUID(data)

                return transfer_type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        transfer_type = _parse_transfer_type(d.pop("transfer_type", UNSET))

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        transfer_cloud_schema = cls(
            asset_id=asset_id,
            asset_paths=asset_paths,
            celery_task_id=celery_task_id,
            collection_storage_id=collection_storage_id,
            component_ids=component_ids,
            date_created=date_created,
            date_modified=date_modified,
            delete_only_from_source_folder=delete_only_from_source_folder,
            delete_original=delete_original,
            destination_directory_path=destination_directory_path,
            destination_filename=destination_filename,
            destination_storage_id=destination_storage_id,
            id=id,
            job_id=job_id,
            job_steps=job_steps,
            original_file_set_id=original_file_set_id,
            original_storage_id=original_storage_id,
            original_url=original_url,
            parent_job_id=parent_job_id,
            priority=priority,
            status=status,
            success=success,
            transfer_type=transfer_type,
            user_id=user_id,
        )

        transfer_cloud_schema.additional_properties = d
        return transfer_cloud_schema

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
