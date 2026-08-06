from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        asset_id (None | Unset | UUID):
        directory_path (None | str | Unset):
        file_type (None | str | Unset):
        format_id (None | Unset | UUID):
        id (None | Unset | UUID):
        keep_source (bool | None | Unset):
        template (None | str | Unset):
        template_engine (None | str | Unset):
        version_id (None | Unset | UUID):
    """

    file_id: UUID
    filename: str
    job_id: UUID
    storage_id: UUID
    asset_id: None | Unset | UUID = UNSET
    directory_path: None | str | Unset = UNSET
    file_type: None | str | Unset = UNSET
    format_id: None | Unset | UUID = UNSET
    id: None | Unset | UUID = UNSET
    keep_source: bool | None | Unset = UNSET
    template: None | str | Unset = UNSET
    template_engine: None | str | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id = str(self.file_id)

        filename = self.filename

        job_id = str(self.job_id)

        storage_id = str(self.storage_id)

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

        directory_path: None | str | Unset
        if isinstance(self.directory_path, Unset):
            directory_path = UNSET
        else:
            directory_path = self.directory_path

        file_type: None | str | Unset
        if isinstance(self.file_type, Unset):
            file_type = UNSET
        else:
            file_type = self.file_type

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

        keep_source: bool | None | Unset
        if isinstance(self.keep_source, Unset):
            keep_source = UNSET
        else:
            keep_source = self.keep_source

        template: None | str | Unset
        if isinstance(self.template, Unset):
            template = UNSET
        else:
            template = self.template

        template_engine: None | str | Unset
        if isinstance(self.template_engine, Unset):
            template_engine = UNSET
        else:
            template_engine = self.template_engine

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

        def _parse_directory_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directory_path = _parse_directory_path(d.pop("directory_path", UNSET))

        def _parse_file_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_type = _parse_file_type(d.pop("file_type", UNSET))

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

        def _parse_keep_source(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        keep_source = _parse_keep_source(d.pop("keep_source", UNSET))

        def _parse_template(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template = _parse_template(d.pop("template", UNSET))

        def _parse_template_engine(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        template_engine = _parse_template_engine(d.pop("template_engine", UNSET))

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
