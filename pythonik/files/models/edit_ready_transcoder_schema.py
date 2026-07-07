from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_ready_transcoder_schema_videocodec import (
    EditReadyTranscoderSchemaVideocodec,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="EditReadyTranscoderSchema")


@_attrs_define
class EditReadyTranscoderSchema:
    """
    Attributes:
        width (int):
        apply_color_conversion (bool | Unset):
        bitrate (int | Unset):
        create_edit_proxy (bool | Unset):
        delete_after_upload (bool | Unset):
        edit_proxy_height (int | Unset):
        edit_proxy_local_storage_path (str | Unset):
        edit_proxy_upload_storage_id (str | Unset):
        edit_proxy_upload_storage_path (str | Unset):
        edit_proxy_width (int | Unset):
        editready_preset (str | Unset):
        exclude_patterns (list[str] | Unset):
        include_patterns (list[str] | Unset):
        local (bool | Unset):
        min_height (int | Unset):
        min_width (int | Unset):
        overwrite_edit_proxy (bool | Unset):
        videocodec (EditReadyTranscoderSchemaVideocodec | Unset):
    """

    width: int
    apply_color_conversion: bool | Unset = UNSET
    bitrate: int | Unset = UNSET
    create_edit_proxy: bool | Unset = UNSET
    delete_after_upload: bool | Unset = UNSET
    edit_proxy_height: int | Unset = UNSET
    edit_proxy_local_storage_path: str | Unset = UNSET
    edit_proxy_upload_storage_id: str | Unset = UNSET
    edit_proxy_upload_storage_path: str | Unset = UNSET
    edit_proxy_width: int | Unset = UNSET
    editready_preset: str | Unset = UNSET
    exclude_patterns: list[str] | Unset = UNSET
    include_patterns: list[str] | Unset = UNSET
    local: bool | Unset = UNSET
    min_height: int | Unset = UNSET
    min_width: int | Unset = UNSET
    overwrite_edit_proxy: bool | Unset = UNSET
    videocodec: EditReadyTranscoderSchemaVideocodec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        apply_color_conversion = self.apply_color_conversion

        bitrate = self.bitrate

        create_edit_proxy = self.create_edit_proxy

        delete_after_upload = self.delete_after_upload

        edit_proxy_height = self.edit_proxy_height

        edit_proxy_local_storage_path = self.edit_proxy_local_storage_path

        edit_proxy_upload_storage_id = self.edit_proxy_upload_storage_id

        edit_proxy_upload_storage_path = self.edit_proxy_upload_storage_path

        edit_proxy_width = self.edit_proxy_width

        editready_preset = self.editready_preset

        exclude_patterns: list[str] | Unset = UNSET
        if not isinstance(self.exclude_patterns, Unset):
            exclude_patterns = self.exclude_patterns

        include_patterns: list[str] | Unset = UNSET
        if not isinstance(self.include_patterns, Unset):
            include_patterns = self.include_patterns

        local = self.local

        min_height = self.min_height

        min_width = self.min_width

        overwrite_edit_proxy = self.overwrite_edit_proxy

        videocodec: str | Unset = UNSET
        if not isinstance(self.videocodec, Unset):
            videocodec = self.videocodec.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "width": width,
            }
        )
        if apply_color_conversion is not UNSET:
            field_dict["apply_color_conversion"] = apply_color_conversion
        if bitrate is not UNSET:
            field_dict["bitrate"] = bitrate
        if create_edit_proxy is not UNSET:
            field_dict["create_edit_proxy"] = create_edit_proxy
        if delete_after_upload is not UNSET:
            field_dict["delete_after_upload"] = delete_after_upload
        if edit_proxy_height is not UNSET:
            field_dict["edit_proxy_height"] = edit_proxy_height
        if edit_proxy_local_storage_path is not UNSET:
            field_dict["edit_proxy_local_storage_path"] = edit_proxy_local_storage_path
        if edit_proxy_upload_storage_id is not UNSET:
            field_dict["edit_proxy_upload_storage_id"] = edit_proxy_upload_storage_id
        if edit_proxy_upload_storage_path is not UNSET:
            field_dict["edit_proxy_upload_storage_path"] = (
                edit_proxy_upload_storage_path
            )
        if edit_proxy_width is not UNSET:
            field_dict["edit_proxy_width"] = edit_proxy_width
        if editready_preset is not UNSET:
            field_dict["editready_preset"] = editready_preset
        if exclude_patterns is not UNSET:
            field_dict["exclude_patterns"] = exclude_patterns
        if include_patterns is not UNSET:
            field_dict["include_patterns"] = include_patterns
        if local is not UNSET:
            field_dict["local"] = local
        if min_height is not UNSET:
            field_dict["min_height"] = min_height
        if min_width is not UNSET:
            field_dict["min_width"] = min_width
        if overwrite_edit_proxy is not UNSET:
            field_dict["overwrite_edit_proxy"] = overwrite_edit_proxy
        if videocodec is not UNSET:
            field_dict["videocodec"] = videocodec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        width = d.pop("width")

        apply_color_conversion = d.pop("apply_color_conversion", UNSET)

        bitrate = d.pop("bitrate", UNSET)

        create_edit_proxy = d.pop("create_edit_proxy", UNSET)

        delete_after_upload = d.pop("delete_after_upload", UNSET)

        edit_proxy_height = d.pop("edit_proxy_height", UNSET)

        edit_proxy_local_storage_path = d.pop("edit_proxy_local_storage_path", UNSET)

        edit_proxy_upload_storage_id = d.pop("edit_proxy_upload_storage_id", UNSET)

        edit_proxy_upload_storage_path = d.pop("edit_proxy_upload_storage_path", UNSET)

        edit_proxy_width = d.pop("edit_proxy_width", UNSET)

        editready_preset = d.pop("editready_preset", UNSET)

        exclude_patterns = cast(list[str], d.pop("exclude_patterns", UNSET))

        include_patterns = cast(list[str], d.pop("include_patterns", UNSET))

        local = d.pop("local", UNSET)

        min_height = d.pop("min_height", UNSET)

        min_width = d.pop("min_width", UNSET)

        overwrite_edit_proxy = d.pop("overwrite_edit_proxy", UNSET)

        _videocodec = d.pop("videocodec", UNSET)
        videocodec: EditReadyTranscoderSchemaVideocodec | Unset
        if isinstance(_videocodec, Unset):
            videocodec = UNSET
        else:
            videocodec = EditReadyTranscoderSchemaVideocodec(_videocodec)

        edit_ready_transcoder_schema = cls(
            width=width,
            apply_color_conversion=apply_color_conversion,
            bitrate=bitrate,
            create_edit_proxy=create_edit_proxy,
            delete_after_upload=delete_after_upload,
            edit_proxy_height=edit_proxy_height,
            edit_proxy_local_storage_path=edit_proxy_local_storage_path,
            edit_proxy_upload_storage_id=edit_proxy_upload_storage_id,
            edit_proxy_upload_storage_path=edit_proxy_upload_storage_path,
            edit_proxy_width=edit_proxy_width,
            editready_preset=editready_preset,
            exclude_patterns=exclude_patterns,
            include_patterns=include_patterns,
            local=local,
            min_height=min_height,
            min_width=min_width,
            overwrite_edit_proxy=overwrite_edit_proxy,
            videocodec=videocodec,
        )

        edit_ready_transcoder_schema.additional_properties = d
        return edit_ready_transcoder_schema

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
