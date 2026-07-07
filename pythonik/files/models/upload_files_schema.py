from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upload_files_schema_format_metadata_item import (
        UploadFilesSchemaFormatMetadataItem,
    )


T = TypeVar("T", bound="UploadFilesSchema")


@_attrs_define
class UploadFilesSchema:
    """
    Attributes:
        file_name (str):
        storage_id (UUID):
        asset_id (UUID | Unset):
        asset_title (str | Unset):
        collection_id (UUID | Unset):
        create_keyframes (bool | Unset):
        format_metadata (list[UploadFilesSchemaFormatMetadataItem] | Unset): Sequence cannot have more than 10000.
            Excess values will be stripped
        format_name (str | Unset):
        version_id (UUID | Unset):
    """

    file_name: str
    storage_id: UUID
    asset_id: UUID | Unset = UNSET
    asset_title: str | Unset = UNSET
    collection_id: UUID | Unset = UNSET
    create_keyframes: bool | Unset = UNSET
    format_metadata: list[UploadFilesSchemaFormatMetadataItem] | Unset = UNSET
    format_name: str | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        storage_id = str(self.storage_id)

        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        asset_title = self.asset_title

        collection_id: str | Unset = UNSET
        if not isinstance(self.collection_id, Unset):
            collection_id = str(self.collection_id)

        create_keyframes = self.create_keyframes

        format_metadata: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.format_metadata, Unset):
            format_metadata = []
            for format_metadata_item_data in self.format_metadata:
                format_metadata_item = format_metadata_item_data.to_dict()
                format_metadata.append(format_metadata_item)

        format_name = self.format_name

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file_name": file_name,
                "storage_id": storage_id,
            }
        )
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if asset_title is not UNSET:
            field_dict["asset_title"] = asset_title
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if create_keyframes is not UNSET:
            field_dict["create_keyframes"] = create_keyframes
        if format_metadata is not UNSET:
            field_dict["format_metadata"] = format_metadata
        if format_name is not UNSET:
            field_dict["format_name"] = format_name
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file_name", (None, str(self.file_name).encode(), "text/plain")))

        files.append(("storage_id", (None, str(self.storage_id), "text/plain")))

        if not isinstance(self.asset_id, Unset):
            files.append(("asset_id", (None, str(self.asset_id), "text/plain")))

        if not isinstance(self.asset_title, Unset):
            files.append(
                ("asset_title", (None, str(self.asset_title).encode(), "text/plain"))
            )

        if not isinstance(self.collection_id, Unset):
            files.append(
                ("collection_id", (None, str(self.collection_id), "text/plain"))
            )

        if not isinstance(self.create_keyframes, Unset):
            files.append(
                (
                    "create_keyframes",
                    (None, str(self.create_keyframes).encode(), "text/plain"),
                )
            )

        if not isinstance(self.format_metadata, Unset):
            for format_metadata_item_element in self.format_metadata:
                files.append(
                    (
                        "format_metadata",
                        (
                            None,
                            json.dumps(format_metadata_item_element.to_dict()).encode(),
                            "application/json",
                        ),
                    )
                )

        if not isinstance(self.format_name, Unset):
            files.append(
                ("format_name", (None, str(self.format_name).encode(), "text/plain"))
            )

        if not isinstance(self.version_id, Unset):
            files.append(("version_id", (None, str(self.version_id), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_files_schema_format_metadata_item import (
            UploadFilesSchemaFormatMetadataItem,
        )

        d = dict(src_dict)
        file_name = d.pop("file_name")

        storage_id = UUID(d.pop("storage_id"))

        _asset_id = d.pop("asset_id", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        asset_title = d.pop("asset_title", UNSET)

        _collection_id = d.pop("collection_id", UNSET)
        collection_id: UUID | Unset
        if isinstance(_collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = UUID(_collection_id)

        create_keyframes = d.pop("create_keyframes", UNSET)

        _format_metadata = d.pop("format_metadata", UNSET)
        format_metadata: list[UploadFilesSchemaFormatMetadataItem] | Unset = UNSET
        if _format_metadata is not UNSET:
            format_metadata = []
            for format_metadata_item_data in _format_metadata:
                format_metadata_item = UploadFilesSchemaFormatMetadataItem.from_dict(
                    format_metadata_item_data
                )

                format_metadata.append(format_metadata_item)

        format_name = d.pop("format_name", UNSET)

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

        upload_files_schema = cls(
            file_name=file_name,
            storage_id=storage_id,
            asset_id=asset_id,
            asset_title=asset_title,
            collection_id=collection_id,
            create_keyframes=create_keyframes,
            format_metadata=format_metadata,
            format_name=format_name,
            version_id=version_id,
        )

        upload_files_schema.additional_properties = d
        return upload_files_schema

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
