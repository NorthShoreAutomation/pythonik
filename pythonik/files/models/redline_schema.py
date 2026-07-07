from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.redline_schema_format import RedlineSchemaFormat
from ..models.redline_schema_prcodec import RedlineSchemaPrcodec
from ..models.redline_schema_qt_codec import RedlineSchemaQtCodec
from ..types import UNSET, Unset

T = TypeVar("T", bound="RedlineSchema")


@_attrs_define
class RedlineSchema:
    """
    Attributes:
        default_lut3d_file (None | str | Unset):
        edit_proxy_local_storage_path (str | Unset):
        edit_proxy_upload_storage_id (str | Unset):
        edit_proxy_upload_storage_path (str | Unset):
        exclude_patterns (list[str] | Unset):
        format_ (RedlineSchemaFormat | Unset):
        include_patterns (list[str] | Unset):
        keep_redline_proxy (bool | Unset):
        local (bool | Unset):
        opencl_device_indexes (list[str] | Unset):
        prcodec (RedlineSchemaPrcodec | Unset):
        priority (int | None | Unset):
        qt_codec (RedlineSchemaQtCodec | Unset):
        render_resolution (int | None | Unset):
        use_metadata_cube_file_in_proxy (bool | Unset):
        use_rmd (int | None | Unset):
    """

    default_lut3d_file: None | str | Unset = UNSET
    edit_proxy_local_storage_path: str | Unset = UNSET
    edit_proxy_upload_storage_id: str | Unset = UNSET
    edit_proxy_upload_storage_path: str | Unset = UNSET
    exclude_patterns: list[str] | Unset = UNSET
    format_: RedlineSchemaFormat | Unset = UNSET
    include_patterns: list[str] | Unset = UNSET
    keep_redline_proxy: bool | Unset = UNSET
    local: bool | Unset = UNSET
    opencl_device_indexes: list[str] | Unset = UNSET
    prcodec: RedlineSchemaPrcodec | Unset = UNSET
    priority: int | None | Unset = UNSET
    qt_codec: RedlineSchemaQtCodec | Unset = UNSET
    render_resolution: int | None | Unset = UNSET
    use_metadata_cube_file_in_proxy: bool | Unset = UNSET
    use_rmd: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_lut3d_file: None | str | Unset
        if isinstance(self.default_lut3d_file, Unset):
            default_lut3d_file = UNSET
        else:
            default_lut3d_file = self.default_lut3d_file

        edit_proxy_local_storage_path = self.edit_proxy_local_storage_path

        edit_proxy_upload_storage_id = self.edit_proxy_upload_storage_id

        edit_proxy_upload_storage_path = self.edit_proxy_upload_storage_path

        exclude_patterns: list[str] | Unset = UNSET
        if not isinstance(self.exclude_patterns, Unset):
            exclude_patterns = self.exclude_patterns

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        include_patterns: list[str] | Unset = UNSET
        if not isinstance(self.include_patterns, Unset):
            include_patterns = self.include_patterns

        keep_redline_proxy = self.keep_redline_proxy

        local = self.local

        opencl_device_indexes: list[str] | Unset = UNSET
        if not isinstance(self.opencl_device_indexes, Unset):
            opencl_device_indexes = self.opencl_device_indexes

        prcodec: str | Unset = UNSET
        if not isinstance(self.prcodec, Unset):
            prcodec = self.prcodec.value

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        qt_codec: str | Unset = UNSET
        if not isinstance(self.qt_codec, Unset):
            qt_codec = self.qt_codec.value

        render_resolution: int | None | Unset
        if isinstance(self.render_resolution, Unset):
            render_resolution = UNSET
        else:
            render_resolution = self.render_resolution

        use_metadata_cube_file_in_proxy = self.use_metadata_cube_file_in_proxy

        use_rmd: int | None | Unset
        if isinstance(self.use_rmd, Unset):
            use_rmd = UNSET
        else:
            use_rmd = self.use_rmd

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_lut3d_file is not UNSET:
            field_dict["default_lut3d_file"] = default_lut3d_file
        if edit_proxy_local_storage_path is not UNSET:
            field_dict["edit_proxy_local_storage_path"] = edit_proxy_local_storage_path
        if edit_proxy_upload_storage_id is not UNSET:
            field_dict["edit_proxy_upload_storage_id"] = edit_proxy_upload_storage_id
        if edit_proxy_upload_storage_path is not UNSET:
            field_dict["edit_proxy_upload_storage_path"] = (
                edit_proxy_upload_storage_path
            )
        if exclude_patterns is not UNSET:
            field_dict["exclude_patterns"] = exclude_patterns
        if format_ is not UNSET:
            field_dict["format"] = format_
        if include_patterns is not UNSET:
            field_dict["include_patterns"] = include_patterns
        if keep_redline_proxy is not UNSET:
            field_dict["keep_redline_proxy"] = keep_redline_proxy
        if local is not UNSET:
            field_dict["local"] = local
        if opencl_device_indexes is not UNSET:
            field_dict["opencl_device_indexes"] = opencl_device_indexes
        if prcodec is not UNSET:
            field_dict["prcodec"] = prcodec
        if priority is not UNSET:
            field_dict["priority"] = priority
        if qt_codec is not UNSET:
            field_dict["qt_codec"] = qt_codec
        if render_resolution is not UNSET:
            field_dict["render_resolution"] = render_resolution
        if use_metadata_cube_file_in_proxy is not UNSET:
            field_dict["use_metadata_cube_file_in_proxy"] = (
                use_metadata_cube_file_in_proxy
            )
        if use_rmd is not UNSET:
            field_dict["use_rmd"] = use_rmd

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_default_lut3d_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        default_lut3d_file = _parse_default_lut3d_file(
            d.pop("default_lut3d_file", UNSET)
        )

        edit_proxy_local_storage_path = d.pop("edit_proxy_local_storage_path", UNSET)

        edit_proxy_upload_storage_id = d.pop("edit_proxy_upload_storage_id", UNSET)

        edit_proxy_upload_storage_path = d.pop("edit_proxy_upload_storage_path", UNSET)

        exclude_patterns = cast(list[str], d.pop("exclude_patterns", UNSET))

        _format_ = d.pop("format", UNSET)
        format_: RedlineSchemaFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = RedlineSchemaFormat(_format_)

        include_patterns = cast(list[str], d.pop("include_patterns", UNSET))

        keep_redline_proxy = d.pop("keep_redline_proxy", UNSET)

        local = d.pop("local", UNSET)

        opencl_device_indexes = cast(list[str], d.pop("opencl_device_indexes", UNSET))

        _prcodec = d.pop("prcodec", UNSET)
        prcodec: RedlineSchemaPrcodec | Unset
        if isinstance(_prcodec, Unset):
            prcodec = UNSET
        else:
            prcodec = RedlineSchemaPrcodec(_prcodec)

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        _qt_codec = d.pop("qt_codec", UNSET)
        qt_codec: RedlineSchemaQtCodec | Unset
        if isinstance(_qt_codec, Unset):
            qt_codec = UNSET
        else:
            qt_codec = RedlineSchemaQtCodec(_qt_codec)

        def _parse_render_resolution(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        render_resolution = _parse_render_resolution(d.pop("render_resolution", UNSET))

        use_metadata_cube_file_in_proxy = d.pop(
            "use_metadata_cube_file_in_proxy", UNSET
        )

        def _parse_use_rmd(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        use_rmd = _parse_use_rmd(d.pop("use_rmd", UNSET))

        redline_schema = cls(
            default_lut3d_file=default_lut3d_file,
            edit_proxy_local_storage_path=edit_proxy_local_storage_path,
            edit_proxy_upload_storage_id=edit_proxy_upload_storage_id,
            edit_proxy_upload_storage_path=edit_proxy_upload_storage_path,
            exclude_patterns=exclude_patterns,
            format_=format_,
            include_patterns=include_patterns,
            keep_redline_proxy=keep_redline_proxy,
            local=local,
            opencl_device_indexes=opencl_device_indexes,
            prcodec=prcodec,
            priority=priority,
            qt_codec=qt_codec,
            render_resolution=render_resolution,
            use_metadata_cube_file_in_proxy=use_metadata_cube_file_in_proxy,
            use_rmd=use_rmd,
        )

        redline_schema.additional_properties = d
        return redline_schema

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
