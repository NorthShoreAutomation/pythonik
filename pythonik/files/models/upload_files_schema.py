from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.upload_files_schema_format_metadata_type_0_item import (
        UploadFilesSchemaFormatMetadataType0Item,
    )


T = TypeVar("T", bound="UploadFilesSchema")


@_attrs_define
class UploadFilesSchema:
    """
    Attributes:
        file_name (str):
        storage_id (UUID):
        asset_id (None | Unset | UUID):
        asset_title (None | str | Unset):
        collection_id (None | Unset | UUID):
        create_keyframes (bool | None | Unset):
        format_metadata (list[UploadFilesSchemaFormatMetadataType0Item] | None | Unset): Sequence cannot have more than
            10000. Excess values will be stripped
        format_name (None | str | Unset):
        version_id (None | Unset | UUID):
    """

    file_name: str
    storage_id: UUID
    asset_id: None | Unset | UUID = UNSET
    asset_title: None | str | Unset = UNSET
    collection_id: None | Unset | UUID = UNSET
    create_keyframes: bool | None | Unset = UNSET
    format_metadata: list[UploadFilesSchemaFormatMetadataType0Item] | None | Unset = (
        UNSET
    )
    format_name: None | str | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        storage_id = str(self.storage_id)

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

        asset_title: None | str | Unset
        if isinstance(self.asset_title, Unset):
            asset_title = UNSET
        else:
            asset_title = self.asset_title

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        elif isinstance(self.collection_id, UUID):
            collection_id = str(self.collection_id)
        else:
            collection_id = self.collection_id

        create_keyframes: bool | None | Unset
        if isinstance(self.create_keyframes, Unset):
            create_keyframes = UNSET
        else:
            create_keyframes = self.create_keyframes

        format_metadata: list[dict[str, Any]] | None | Unset
        if isinstance(self.format_metadata, Unset):
            format_metadata = UNSET
        elif isinstance(self.format_metadata, list):
            format_metadata = []
            for format_metadata_type_0_item_data in self.format_metadata:
                format_metadata_type_0_item = format_metadata_type_0_item_data.to_dict()
                format_metadata.append(format_metadata_type_0_item)

        else:
            format_metadata = self.format_metadata

        format_name: None | str | Unset
        if isinstance(self.format_name, Unset):
            format_name = UNSET
        else:
            format_name = self.format_name

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        elif isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

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
            if isinstance(self.asset_id, UUID):
                files.append(("asset_id", (None, str(self.asset_id), "text/plain")))
            else:
                files.append(
                    ("asset_id", (None, str(self.asset_id).encode(), "text/plain"))
                )

        if not isinstance(self.asset_title, Unset):
            if isinstance(self.asset_title, str):
                files.append(
                    (
                        "asset_title",
                        (None, str(self.asset_title).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "asset_title",
                        (None, str(self.asset_title).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.collection_id, Unset):
            if isinstance(self.collection_id, UUID):
                files.append(
                    ("collection_id", (None, str(self.collection_id), "text/plain"))
                )
            else:
                files.append(
                    (
                        "collection_id",
                        (None, str(self.collection_id).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.create_keyframes, Unset):
            if isinstance(self.create_keyframes, bool):
                files.append(
                    (
                        "create_keyframes",
                        (None, str(self.create_keyframes).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "create_keyframes",
                        (None, str(self.create_keyframes).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.format_metadata, Unset):
            if isinstance(self.format_metadata, list):
                for format_metadata_type_0_item_element in self.format_metadata:
                    files.append(
                        (
                            "format_metadata",
                            (
                                None,
                                json.dumps(
                                    format_metadata_type_0_item_element.to_dict()
                                ).encode(),
                                "application/json",
                            ),
                        )
                    )
            else:
                files.append(
                    (
                        "format_metadata",
                        (None, str(self.format_metadata).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.format_name, Unset):
            if isinstance(self.format_name, str):
                files.append(
                    (
                        "format_name",
                        (None, str(self.format_name).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "format_name",
                        (None, str(self.format_name).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.version_id, Unset):
            if isinstance(self.version_id, UUID):
                files.append(("version_id", (None, str(self.version_id), "text/plain")))
            else:
                files.append(
                    ("version_id", (None, str(self.version_id).encode(), "text/plain"))
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.upload_files_schema_format_metadata_type_0_item import (
            UploadFilesSchemaFormatMetadataType0Item,
        )

        d = dict(src_dict)
        file_name = d.pop("file_name")

        storage_id = UUID(d.pop("storage_id"))

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

        def _parse_asset_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        asset_title = _parse_asset_title(d.pop("asset_title", UNSET))

        def _parse_collection_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                collection_id_type_0 = UUID(data)

                return collection_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

        def _parse_create_keyframes(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        create_keyframes = _parse_create_keyframes(d.pop("create_keyframes", UNSET))

        def _parse_format_metadata(
            data: object,
        ) -> list[UploadFilesSchemaFormatMetadataType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                format_metadata_type_0 = []
                _format_metadata_type_0 = data
                for format_metadata_type_0_item_data in _format_metadata_type_0:
                    format_metadata_type_0_item = (
                        UploadFilesSchemaFormatMetadataType0Item.from_dict(
                            format_metadata_type_0_item_data
                        )
                    )

                    format_metadata_type_0.append(format_metadata_type_0_item)

                return format_metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[UploadFilesSchemaFormatMetadataType0Item] | None | Unset, data
            )

        format_metadata = _parse_format_metadata(d.pop("format_metadata", UNSET))

        def _parse_format_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_name = _parse_format_name(d.pop("format_name", UNSET))

        def _parse_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                version_id_type_0 = UUID(data)

                return version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))

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
