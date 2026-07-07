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
    from ..models.transfer_cloud_schema_job_steps import TransferCloudSchemaJobSteps


T = TypeVar("T", bound="TransferCloudSchema")


@_attrs_define
class TransferCloudSchema:
    """
    Attributes:
        asset_id (UUID | Unset):
        asset_paths (list[str] | Unset):
        celery_task_id (UUID | Unset):
        collection_storage_id (UUID | Unset):
        component_ids (list[UUID] | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        delete_only_from_source_folder (bool | Unset):
        delete_original (bool | Unset):
        destination_directory_path (str | Unset):
        destination_filename (str | Unset):
        destination_storage_id (UUID | Unset):
        id (UUID | Unset):
        job_id (UUID | Unset):
        job_steps (TransferCloudSchemaJobSteps | Unset):
        original_file_set_id (UUID | Unset):
        original_storage_id (UUID | Unset):
        original_url (str | Unset):
        parent_job_id (UUID | Unset):
        priority (int | Unset):
        status (TransferCloudSchemaStatus | Unset):
        success (str | Unset):
        transfer_type (UUID | Unset):
        user_id (UUID | Unset):
    """

    asset_id: UUID | Unset = UNSET
    asset_paths: list[str] | Unset = UNSET
    celery_task_id: UUID | Unset = UNSET
    collection_storage_id: UUID | Unset = UNSET
    component_ids: list[UUID] | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    delete_only_from_source_folder: bool | Unset = UNSET
    delete_original: bool | Unset = UNSET
    destination_directory_path: str | Unset = UNSET
    destination_filename: str | Unset = UNSET
    destination_storage_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    job_id: UUID | Unset = UNSET
    job_steps: TransferCloudSchemaJobSteps | Unset = UNSET
    original_file_set_id: UUID | Unset = UNSET
    original_storage_id: UUID | Unset = UNSET
    original_url: str | Unset = UNSET
    parent_job_id: UUID | Unset = UNSET
    priority: int | Unset = UNSET
    status: TransferCloudSchemaStatus | Unset = UNSET
    success: str | Unset = UNSET
    transfer_type: UUID | Unset = UNSET
    user_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        asset_paths: list[str] | Unset = UNSET
        if not isinstance(self.asset_paths, Unset):
            asset_paths = self.asset_paths

        celery_task_id: str | Unset = UNSET
        if not isinstance(self.celery_task_id, Unset):
            celery_task_id = str(self.celery_task_id)

        collection_storage_id: str | Unset = UNSET
        if not isinstance(self.collection_storage_id, Unset):
            collection_storage_id = str(self.collection_storage_id)

        component_ids: list[str] | Unset = UNSET
        if not isinstance(self.component_ids, Unset):
            component_ids = []
            for component_ids_item_data in self.component_ids:
                component_ids_item = str(component_ids_item_data)
                component_ids.append(component_ids_item)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        delete_only_from_source_folder = self.delete_only_from_source_folder

        delete_original = self.delete_original

        destination_directory_path = self.destination_directory_path

        destination_filename = self.destination_filename

        destination_storage_id: str | Unset = UNSET
        if not isinstance(self.destination_storage_id, Unset):
            destination_storage_id = str(self.destination_storage_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        job_id: str | Unset = UNSET
        if not isinstance(self.job_id, Unset):
            job_id = str(self.job_id)

        job_steps: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_steps, Unset):
            job_steps = self.job_steps.to_dict()

        original_file_set_id: str | Unset = UNSET
        if not isinstance(self.original_file_set_id, Unset):
            original_file_set_id = str(self.original_file_set_id)

        original_storage_id: str | Unset = UNSET
        if not isinstance(self.original_storage_id, Unset):
            original_storage_id = str(self.original_storage_id)

        original_url = self.original_url

        parent_job_id: str | Unset = UNSET
        if not isinstance(self.parent_job_id, Unset):
            parent_job_id = str(self.parent_job_id)

        priority = self.priority

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        success = self.success

        transfer_type: str | Unset = UNSET
        if not isinstance(self.transfer_type, Unset):
            transfer_type = str(self.transfer_type)

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

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
        from ..models.transfer_cloud_schema_job_steps import TransferCloudSchemaJobSteps

        d = dict(src_dict)
        _asset_id = d.pop("asset_id", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        asset_paths = cast(list[str], d.pop("asset_paths", UNSET))

        _celery_task_id = d.pop("celery_task_id", UNSET)
        celery_task_id: UUID | Unset
        if isinstance(_celery_task_id, Unset):
            celery_task_id = UNSET
        else:
            celery_task_id = UUID(_celery_task_id)

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

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        delete_only_from_source_folder = d.pop("delete_only_from_source_folder", UNSET)

        delete_original = d.pop("delete_original", UNSET)

        destination_directory_path = d.pop("destination_directory_path", UNSET)

        destination_filename = d.pop("destination_filename", UNSET)

        _destination_storage_id = d.pop("destination_storage_id", UNSET)
        destination_storage_id: UUID | Unset
        if isinstance(_destination_storage_id, Unset):
            destination_storage_id = UNSET
        else:
            destination_storage_id = UUID(_destination_storage_id)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _job_id = d.pop("job_id", UNSET)
        job_id: UUID | Unset
        if isinstance(_job_id, Unset):
            job_id = UNSET
        else:
            job_id = UUID(_job_id)

        _job_steps = d.pop("job_steps", UNSET)
        job_steps: TransferCloudSchemaJobSteps | Unset
        if isinstance(_job_steps, Unset):
            job_steps = UNSET
        else:
            job_steps = TransferCloudSchemaJobSteps.from_dict(_job_steps)

        _original_file_set_id = d.pop("original_file_set_id", UNSET)
        original_file_set_id: UUID | Unset
        if isinstance(_original_file_set_id, Unset):
            original_file_set_id = UNSET
        else:
            original_file_set_id = UUID(_original_file_set_id)

        _original_storage_id = d.pop("original_storage_id", UNSET)
        original_storage_id: UUID | Unset
        if isinstance(_original_storage_id, Unset):
            original_storage_id = UNSET
        else:
            original_storage_id = UUID(_original_storage_id)

        original_url = d.pop("original_url", UNSET)

        _parent_job_id = d.pop("parent_job_id", UNSET)
        parent_job_id: UUID | Unset
        if isinstance(_parent_job_id, Unset):
            parent_job_id = UNSET
        else:
            parent_job_id = UUID(_parent_job_id)

        priority = d.pop("priority", UNSET)

        _status = d.pop("status", UNSET)
        status: TransferCloudSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TransferCloudSchemaStatus(_status)

        success = d.pop("success", UNSET)

        _transfer_type = d.pop("transfer_type", UNSET)
        transfer_type: UUID | Unset
        if isinstance(_transfer_type, Unset):
            transfer_type = UNSET
        else:
            transfer_type = UUID(_transfer_type)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

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
