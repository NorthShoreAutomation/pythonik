from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileDeletionFromLocalStorageSchema")


@_attrs_define
class FileDeletionFromLocalStorageSchema:
    """
    Attributes:
        file_id (UUID):
        filename (str):
        job_id (UUID):
        storage_id (UUID):
        asset_id (UUID | Unset):
        directory_path (str | Unset):
        file_type (str | Unset):
        format_id (UUID | Unset):
        id (UUID | Unset):
        keep_source (bool | Unset):
        template (str | Unset):
        template_engine (str | Unset):
        version_id (UUID | Unset):
    """

    file_id: UUID
    filename: str
    job_id: UUID
    storage_id: UUID
    asset_id: UUID | Unset = UNSET
    directory_path: str | Unset = UNSET
    file_type: str | Unset = UNSET
    format_id: UUID | Unset = UNSET
    id: UUID | Unset = UNSET
    keep_source: bool | Unset = UNSET
    template: str | Unset = UNSET
    template_engine: str | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = str(self.file_id)

        filename = self.filename

        job_id = str(self.job_id)

        storage_id = str(self.storage_id)

        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        directory_path = self.directory_path

        file_type = self.file_type

        format_id: str | Unset = UNSET
        if not isinstance(self.format_id, Unset):
            format_id = str(self.format_id)

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        keep_source = self.keep_source

        template = self.template

        template_engine = self.template_engine

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_id": file_id,
                "filename": filename,
                "job_id": job_id,
                "storage_id": storage_id,
            }
        )
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if directory_path is not UNSET:
            field_dict["directory_path"] = directory_path
        if file_type is not UNSET:
            field_dict["file_type"] = file_type
        if format_id is not UNSET:
            field_dict["format_id"] = format_id
        if id is not UNSET:
            field_dict["id"] = id
        if keep_source is not UNSET:
            field_dict["keep_source"] = keep_source
        if template is not UNSET:
            field_dict["template"] = template
        if template_engine is not UNSET:
            field_dict["template_engine"] = template_engine
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file_id = UUID(d.pop("file_id"))

        filename = d.pop("filename")

        job_id = UUID(d.pop("job_id"))

        storage_id = UUID(d.pop("storage_id"))

        _asset_id = d.pop("asset_id", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        directory_path = d.pop("directory_path", UNSET)

        file_type = d.pop("file_type", UNSET)

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

        keep_source = d.pop("keep_source", UNSET)

        template = d.pop("template", UNSET)

        template_engine = d.pop("template_engine", UNSET)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

        file_deletion_from_local_storage_schema = cls(
            file_id=file_id,
            filename=filename,
            job_id=job_id,
            storage_id=storage_id,
            asset_id=asset_id,
            directory_path=directory_path,
            file_type=file_type,
            format_id=format_id,
            id=id,
            keep_source=keep_source,
            template=template,
            template_engine=template_engine,
            version_id=version_id,
        )

        file_deletion_from_local_storage_schema.additional_properties = d
        return file_deletion_from_local_storage_schema

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
