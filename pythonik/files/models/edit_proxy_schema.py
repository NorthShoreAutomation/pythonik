from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditProxySchema")


@_attrs_define
class EditProxySchema:
    """
    Attributes:
        directory_path (None | str):
        height (int):
        name (str):
        storage_id (UUID):
        version_id (UUID):
        width (int):
        allow_mxf (bool | None | Unset):
        file_suffix (None | str | Unset):
        force_storage_id (bool | None | Unset):
        ignore_transcoder_settings (bool | None | Unset):
        keep_extension (bool | None | Unset):
    """

    directory_path: None | str
    height: int
    name: str
    storage_id: UUID
    version_id: UUID
    width: int
    allow_mxf: bool | None | Unset = UNSET
    file_suffix: None | str | Unset = UNSET
    force_storage_id: bool | None | Unset = UNSET
    ignore_transcoder_settings: bool | None | Unset = UNSET
    keep_extension: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        directory_path: None | str
        directory_path = self.directory_path

        height = self.height

        name = self.name

        storage_id = str(self.storage_id)

        version_id = str(self.version_id)

        width = self.width

        allow_mxf: bool | None | Unset
        if isinstance(self.allow_mxf, Unset):
            allow_mxf = UNSET
        else:
            allow_mxf = self.allow_mxf

        file_suffix: None | str | Unset
        if isinstance(self.file_suffix, Unset):
            file_suffix = UNSET
        else:
            file_suffix = self.file_suffix

        force_storage_id: bool | None | Unset
        if isinstance(self.force_storage_id, Unset):
            force_storage_id = UNSET
        else:
            force_storage_id = self.force_storage_id

        ignore_transcoder_settings: bool | None | Unset
        if isinstance(self.ignore_transcoder_settings, Unset):
            ignore_transcoder_settings = UNSET
        else:
            ignore_transcoder_settings = self.ignore_transcoder_settings

        keep_extension: bool | None | Unset
        if isinstance(self.keep_extension, Unset):
            keep_extension = UNSET
        else:
            keep_extension = self.keep_extension

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "directory_path": directory_path,
                "height": height,
                "name": name,
                "storage_id": storage_id,
                "version_id": version_id,
                "width": width,
            }
        )
        if allow_mxf is not UNSET:
            field_dict["allow_mxf"] = allow_mxf
        if file_suffix is not UNSET:
            field_dict["file_suffix"] = file_suffix
        if force_storage_id is not UNSET:
            field_dict["force_storage_id"] = force_storage_id
        if ignore_transcoder_settings is not UNSET:
            field_dict["ignore_transcoder_settings"] = ignore_transcoder_settings
        if keep_extension is not UNSET:
            field_dict["keep_extension"] = keep_extension

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_directory_path(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        directory_path = _parse_directory_path(d.pop("directory_path"))

        height = d.pop("height")

        name = d.pop("name")

        storage_id = UUID(d.pop("storage_id"))

        version_id = UUID(d.pop("version_id"))

        width = d.pop("width")

        def _parse_allow_mxf(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allow_mxf = _parse_allow_mxf(d.pop("allow_mxf", UNSET))

        def _parse_file_suffix(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_suffix = _parse_file_suffix(d.pop("file_suffix", UNSET))

        def _parse_force_storage_id(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        force_storage_id = _parse_force_storage_id(d.pop("force_storage_id", UNSET))

        def _parse_ignore_transcoder_settings(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ignore_transcoder_settings = _parse_ignore_transcoder_settings(
            d.pop("ignore_transcoder_settings", UNSET)
        )

        def _parse_keep_extension(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        keep_extension = _parse_keep_extension(d.pop("keep_extension", UNSET))

        edit_proxy_schema = cls(
            directory_path=directory_path,
            height=height,
            name=name,
            storage_id=storage_id,
            version_id=version_id,
            width=width,
            allow_mxf=allow_mxf,
            file_suffix=file_suffix,
            force_storage_id=force_storage_id,
            ignore_transcoder_settings=ignore_transcoder_settings,
            keep_extension=keep_extension,
        )

        edit_proxy_schema.additional_properties = d
        return edit_proxy_schema

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
