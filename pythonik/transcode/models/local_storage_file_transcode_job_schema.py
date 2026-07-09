from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalStorageFileTranscodeJobSchema")


@_attrs_define
class LocalStorageFileTranscodeJobSchema:
    """
    Attributes:
        asset_id (str):
        directory_path (str):
        file_id (str):
        file_set_id (str):
        filename (str):
        format_id (str):
        job_id (str):
        size (int):
        version_id (str):
        checksum (None | str | Unset):
        collection_id (None | str | Unset):
        component_ids (list[str] | None | Unset):
        id (None | str | Unset):
        metadata_update_only (bool | None | Unset):
        priority (int | None | Unset):
    """

    asset_id: str
    directory_path: str
    file_id: str
    file_set_id: str
    filename: str
    format_id: str
    job_id: str
    size: int
    version_id: str
    checksum: None | str | Unset = UNSET
    collection_id: None | str | Unset = UNSET
    component_ids: list[str] | None | Unset = UNSET
    id: None | str | Unset = UNSET
    metadata_update_only: bool | None | Unset = UNSET
    priority: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = self.asset_id

        directory_path = self.directory_path

        file_id = self.file_id

        file_set_id = self.file_set_id

        filename = self.filename

        format_id = self.format_id

        job_id = self.job_id

        size = self.size

        version_id = self.version_id

        checksum: None | str | Unset
        if isinstance(self.checksum, Unset):
            checksum = UNSET
        else:
            checksum = self.checksum

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = self.collection_id

        component_ids: list[str] | None | Unset
        if isinstance(self.component_ids, Unset):
            component_ids = UNSET
        elif isinstance(self.component_ids, list):
            component_ids = self.component_ids

        else:
            component_ids = self.component_ids

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        metadata_update_only: bool | None | Unset
        if isinstance(self.metadata_update_only, Unset):
            metadata_update_only = UNSET
        else:
            metadata_update_only = self.metadata_update_only

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "directory_path": directory_path,
                "file_id": file_id,
                "file_set_id": file_set_id,
                "filename": filename,
                "format_id": format_id,
                "job_id": job_id,
                "size": size,
                "version_id": version_id,
            }
        )
        if checksum is not UNSET:
            field_dict["checksum"] = checksum
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if component_ids is not UNSET:
            field_dict["component_ids"] = component_ids
        if id is not UNSET:
            field_dict["id"] = id
        if metadata_update_only is not UNSET:
            field_dict["metadata_update_only"] = metadata_update_only
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = d.pop("asset_id")

        directory_path = d.pop("directory_path")

        file_id = d.pop("file_id")

        file_set_id = d.pop("file_set_id")

        filename = d.pop("filename")

        format_id = d.pop("format_id")

        job_id = d.pop("job_id")

        size = d.pop("size")

        version_id = d.pop("version_id")

        def _parse_checksum(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        checksum = _parse_checksum(d.pop("checksum", UNSET))

        def _parse_collection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        def _parse_component_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                component_ids_type_0 = cast(list[str], data)

                return component_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        component_ids = _parse_component_ids(d.pop("component_ids", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_metadata_update_only(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        metadata_update_only = _parse_metadata_update_only(
            d.pop("metadata_update_only", UNSET)
        )

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        local_storage_file_transcode_job_schema = cls(
            asset_id=asset_id,
            directory_path=directory_path,
            file_id=file_id,
            file_set_id=file_set_id,
            filename=filename,
            format_id=format_id,
            job_id=job_id,
            size=size,
            version_id=version_id,
            checksum=checksum,
            collection_id=collection_id,
            component_ids=component_ids,
            id=id,
            metadata_update_only=metadata_update_only,
            priority=priority,
        )

        local_storage_file_transcode_job_schema.additional_properties = d
        return local_storage_file_transcode_job_schema

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
