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
        apply_color_conversion (bool | None | Unset):
        bitrate (int | None | Unset):
        create_edit_proxy (bool | None | Unset):
        delete_after_upload (bool | None | Unset):
        edit_proxy_height (int | None | Unset):
        edit_proxy_local_storage_path (None | str | Unset):
        edit_proxy_upload_storage_id (None | str | Unset):
        edit_proxy_upload_storage_path (None | str | Unset):
        edit_proxy_width (int | None | Unset):
        editready_preset (None | str | Unset):
        exclude_patterns (list[str] | None | Unset):
        include_patterns (list[str] | None | Unset):
        local (bool | None | Unset):
        min_height (int | None | Unset):
        min_width (int | None | Unset):
        overwrite_edit_proxy (bool | None | Unset):
        videocodec (EditReadyTranscoderSchemaVideocodec | None | Unset):
    """

    width: int
    apply_color_conversion: bool | None | Unset = UNSET
    bitrate: int | None | Unset = UNSET
    create_edit_proxy: bool | None | Unset = UNSET
    delete_after_upload: bool | None | Unset = UNSET
    edit_proxy_height: int | None | Unset = UNSET
    edit_proxy_local_storage_path: None | str | Unset = UNSET
    edit_proxy_upload_storage_id: None | str | Unset = UNSET
    edit_proxy_upload_storage_path: None | str | Unset = UNSET
    edit_proxy_width: int | None | Unset = UNSET
    editready_preset: None | str | Unset = UNSET
    exclude_patterns: list[str] | None | Unset = UNSET
    include_patterns: list[str] | None | Unset = UNSET
    local: bool | None | Unset = UNSET
    min_height: int | None | Unset = UNSET
    min_width: int | None | Unset = UNSET
    overwrite_edit_proxy: bool | None | Unset = UNSET
    videocodec: EditReadyTranscoderSchemaVideocodec | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        apply_color_conversion: bool | None | Unset
        if isinstance(self.apply_color_conversion, Unset):
            apply_color_conversion = UNSET
        else:
            apply_color_conversion = self.apply_color_conversion

        bitrate: int | None | Unset
        if isinstance(self.bitrate, Unset):
            bitrate = UNSET
        else:
            bitrate = self.bitrate

        create_edit_proxy: bool | None | Unset
        if isinstance(self.create_edit_proxy, Unset):
            create_edit_proxy = UNSET
        else:
            create_edit_proxy = self.create_edit_proxy

        delete_after_upload: bool | None | Unset
        if isinstance(self.delete_after_upload, Unset):
            delete_after_upload = UNSET
        else:
            delete_after_upload = self.delete_after_upload

        edit_proxy_height: int | None | Unset
        if isinstance(self.edit_proxy_height, Unset):
            edit_proxy_height = UNSET
        else:
            edit_proxy_height = self.edit_proxy_height

        edit_proxy_local_storage_path: None | str | Unset
        if isinstance(self.edit_proxy_local_storage_path, Unset):
            edit_proxy_local_storage_path = UNSET
        else:
            edit_proxy_local_storage_path = self.edit_proxy_local_storage_path

        edit_proxy_upload_storage_id: None | str | Unset
        if isinstance(self.edit_proxy_upload_storage_id, Unset):
            edit_proxy_upload_storage_id = UNSET
        else:
            edit_proxy_upload_storage_id = self.edit_proxy_upload_storage_id

        edit_proxy_upload_storage_path: None | str | Unset
        if isinstance(self.edit_proxy_upload_storage_path, Unset):
            edit_proxy_upload_storage_path = UNSET
        else:
            edit_proxy_upload_storage_path = self.edit_proxy_upload_storage_path

        edit_proxy_width: int | None | Unset
        if isinstance(self.edit_proxy_width, Unset):
            edit_proxy_width = UNSET
        else:
            edit_proxy_width = self.edit_proxy_width

        editready_preset: None | str | Unset
        if isinstance(self.editready_preset, Unset):
            editready_preset = UNSET
        else:
            editready_preset = self.editready_preset

        exclude_patterns: list[str] | None | Unset
        if isinstance(self.exclude_patterns, Unset):
            exclude_patterns = UNSET
        elif isinstance(self.exclude_patterns, list):
            exclude_patterns = self.exclude_patterns

        else:
            exclude_patterns = self.exclude_patterns

        include_patterns: list[str] | None | Unset
        if isinstance(self.include_patterns, Unset):
            include_patterns = UNSET
        elif isinstance(self.include_patterns, list):
            include_patterns = self.include_patterns

        else:
            include_patterns = self.include_patterns

        local: bool | None | Unset
        if isinstance(self.local, Unset):
            local = UNSET
        else:
            local = self.local

        min_height: int | None | Unset
        if isinstance(self.min_height, Unset):
            min_height = UNSET
        else:
            min_height = self.min_height

        min_width: int | None | Unset
        if isinstance(self.min_width, Unset):
            min_width = UNSET
        else:
            min_width = self.min_width

        overwrite_edit_proxy: bool | None | Unset
        if isinstance(self.overwrite_edit_proxy, Unset):
            overwrite_edit_proxy = UNSET
        else:
            overwrite_edit_proxy = self.overwrite_edit_proxy

        videocodec: None | str | Unset
        if isinstance(self.videocodec, Unset):
            videocodec = UNSET
        elif isinstance(self.videocodec, EditReadyTranscoderSchemaVideocodec):
            videocodec = self.videocodec.value
        else:
            videocodec = self.videocodec

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

        def _parse_apply_color_conversion(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        apply_color_conversion = _parse_apply_color_conversion(
            d.pop("apply_color_conversion", UNSET)
        )

        def _parse_bitrate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bitrate = _parse_bitrate(d.pop("bitrate", UNSET))

        def _parse_create_edit_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        create_edit_proxy = _parse_create_edit_proxy(d.pop("create_edit_proxy", UNSET))

        def _parse_delete_after_upload(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        delete_after_upload = _parse_delete_after_upload(
            d.pop("delete_after_upload", UNSET)
        )

        def _parse_edit_proxy_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edit_proxy_height = _parse_edit_proxy_height(d.pop("edit_proxy_height", UNSET))

        def _parse_edit_proxy_local_storage_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edit_proxy_local_storage_path = _parse_edit_proxy_local_storage_path(
            d.pop("edit_proxy_local_storage_path", UNSET)
        )

        def _parse_edit_proxy_upload_storage_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edit_proxy_upload_storage_id = _parse_edit_proxy_upload_storage_id(
            d.pop("edit_proxy_upload_storage_id", UNSET)
        )

        def _parse_edit_proxy_upload_storage_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        edit_proxy_upload_storage_path = _parse_edit_proxy_upload_storage_path(
            d.pop("edit_proxy_upload_storage_path", UNSET)
        )

        def _parse_edit_proxy_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        edit_proxy_width = _parse_edit_proxy_width(d.pop("edit_proxy_width", UNSET))

        def _parse_editready_preset(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        editready_preset = _parse_editready_preset(d.pop("editready_preset", UNSET))

        def _parse_exclude_patterns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_patterns_type_0 = cast(list[str], data)

                return exclude_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        exclude_patterns = _parse_exclude_patterns(d.pop("exclude_patterns", UNSET))

        def _parse_include_patterns(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                include_patterns_type_0 = cast(list[str], data)

                return include_patterns_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        include_patterns = _parse_include_patterns(d.pop("include_patterns", UNSET))

        def _parse_local(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        local = _parse_local(d.pop("local", UNSET))

        def _parse_min_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_height = _parse_min_height(d.pop("min_height", UNSET))

        def _parse_min_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_width = _parse_min_width(d.pop("min_width", UNSET))

        def _parse_overwrite_edit_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        overwrite_edit_proxy = _parse_overwrite_edit_proxy(
            d.pop("overwrite_edit_proxy", UNSET)
        )

        def _parse_videocodec(
            data: object,
        ) -> EditReadyTranscoderSchemaVideocodec | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                videocodec_type_1 = EditReadyTranscoderSchemaVideocodec(data)

                return videocodec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EditReadyTranscoderSchemaVideocodec | None | Unset, data)

        videocodec = _parse_videocodec(d.pop("videocodec", UNSET))

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
