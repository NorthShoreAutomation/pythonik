from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.redline_schema_format_type_1 import RedlineSchemaFormatType1
    from ..models.redline_schema_prcodec_type_1 import RedlineSchemaPrcodecType1
    from ..models.redline_schema_qt_codec_type_1 import RedlineSchemaQtCodecType1


T = TypeVar("T", bound="RedlineSchema")


@_attrs_define
class RedlineSchema:
    """
    Attributes:
        default_lut3d_file (None | str | Unset):
        edit_proxy_local_storage_path (None | str | Unset):
        edit_proxy_upload_storage_id (None | str | Unset):
        edit_proxy_upload_storage_path (None | str | Unset):
        exclude_patterns (list[str] | None | Unset):
        format_ (None | RedlineSchemaFormatType1 | Unset):
        include_patterns (list[str] | None | Unset):
        keep_redline_proxy (bool | None | Unset):
        local (bool | None | Unset):
        opencl_device_indexes (list[str] | None | Unset):
        prcodec (None | RedlineSchemaPrcodecType1 | Unset):
        priority (int | None | Unset):
        qt_codec (None | RedlineSchemaQtCodecType1 | Unset):
        render_resolution (int | None | Unset):
        use_metadata_cube_file_in_proxy (bool | None | Unset):
        use_rmd (int | None | Unset):
    """

    default_lut3d_file: None | str | Unset = UNSET
    edit_proxy_local_storage_path: None | str | Unset = UNSET
    edit_proxy_upload_storage_id: None | str | Unset = UNSET
    edit_proxy_upload_storage_path: None | str | Unset = UNSET
    exclude_patterns: list[str] | None | Unset = UNSET
    format_: None | RedlineSchemaFormatType1 | Unset = UNSET
    include_patterns: list[str] | None | Unset = UNSET
    keep_redline_proxy: bool | None | Unset = UNSET
    local: bool | None | Unset = UNSET
    opencl_device_indexes: list[str] | None | Unset = UNSET
    prcodec: None | RedlineSchemaPrcodecType1 | Unset = UNSET
    priority: int | None | Unset = UNSET
    qt_codec: None | RedlineSchemaQtCodecType1 | Unset = UNSET
    render_resolution: int | None | Unset = UNSET
    use_metadata_cube_file_in_proxy: bool | None | Unset = UNSET
    use_rmd: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.redline_schema_format_type_1 import RedlineSchemaFormatType1
        from ..models.redline_schema_prcodec_type_1 import RedlineSchemaPrcodecType1
        from ..models.redline_schema_qt_codec_type_1 import RedlineSchemaQtCodecType1

        default_lut3d_file: None | str | Unset
        if isinstance(self.default_lut3d_file, Unset):
            default_lut3d_file = UNSET
        else:
            default_lut3d_file = self.default_lut3d_file

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

        exclude_patterns: list[str] | None | Unset
        if isinstance(self.exclude_patterns, Unset):
            exclude_patterns = UNSET
        elif isinstance(self.exclude_patterns, list):
            exclude_patterns = self.exclude_patterns

        else:
            exclude_patterns = self.exclude_patterns

        format_: dict[str, Any] | None | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        elif isinstance(self.format_, RedlineSchemaFormatType1):
            format_ = self.format_.to_dict()
        else:
            format_ = self.format_

        include_patterns: list[str] | None | Unset
        if isinstance(self.include_patterns, Unset):
            include_patterns = UNSET
        elif isinstance(self.include_patterns, list):
            include_patterns = self.include_patterns

        else:
            include_patterns = self.include_patterns

        keep_redline_proxy: bool | None | Unset
        if isinstance(self.keep_redline_proxy, Unset):
            keep_redline_proxy = UNSET
        else:
            keep_redline_proxy = self.keep_redline_proxy

        local: bool | None | Unset
        if isinstance(self.local, Unset):
            local = UNSET
        else:
            local = self.local

        opencl_device_indexes: list[str] | None | Unset
        if isinstance(self.opencl_device_indexes, Unset):
            opencl_device_indexes = UNSET
        elif isinstance(self.opencl_device_indexes, list):
            opencl_device_indexes = self.opencl_device_indexes

        else:
            opencl_device_indexes = self.opencl_device_indexes

        prcodec: dict[str, Any] | None | Unset
        if isinstance(self.prcodec, Unset):
            prcodec = UNSET
        elif isinstance(self.prcodec, RedlineSchemaPrcodecType1):
            prcodec = self.prcodec.to_dict()
        else:
            prcodec = self.prcodec

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        qt_codec: dict[str, Any] | None | Unset
        if isinstance(self.qt_codec, Unset):
            qt_codec = UNSET
        elif isinstance(self.qt_codec, RedlineSchemaQtCodecType1):
            qt_codec = self.qt_codec.to_dict()
        else:
            qt_codec = self.qt_codec

        render_resolution: int | None | Unset
        if isinstance(self.render_resolution, Unset):
            render_resolution = UNSET
        else:
            render_resolution = self.render_resolution

        use_metadata_cube_file_in_proxy: bool | None | Unset
        if isinstance(self.use_metadata_cube_file_in_proxy, Unset):
            use_metadata_cube_file_in_proxy = UNSET
        else:
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
        from ..models.redline_schema_format_type_1 import RedlineSchemaFormatType1
        from ..models.redline_schema_prcodec_type_1 import RedlineSchemaPrcodecType1
        from ..models.redline_schema_qt_codec_type_1 import RedlineSchemaQtCodecType1

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

        def _parse_format_(data: object) -> None | RedlineSchemaFormatType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                format_type_1 = RedlineSchemaFormatType1.from_dict(data)

                return format_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RedlineSchemaFormatType1 | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))

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

        def _parse_keep_redline_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        keep_redline_proxy = _parse_keep_redline_proxy(
            d.pop("keep_redline_proxy", UNSET)
        )

        def _parse_local(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        local = _parse_local(d.pop("local", UNSET))

        def _parse_opencl_device_indexes(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                opencl_device_indexes_type_0 = cast(list[str], data)

                return opencl_device_indexes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        opencl_device_indexes = _parse_opencl_device_indexes(
            d.pop("opencl_device_indexes", UNSET)
        )

        def _parse_prcodec(data: object) -> None | RedlineSchemaPrcodecType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prcodec_type_1 = RedlineSchemaPrcodecType1.from_dict(data)

                return prcodec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RedlineSchemaPrcodecType1 | Unset, data)

        prcodec = _parse_prcodec(d.pop("prcodec", UNSET))

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_qt_codec(data: object) -> None | RedlineSchemaQtCodecType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                qt_codec_type_1 = RedlineSchemaQtCodecType1.from_dict(data)

                return qt_codec_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RedlineSchemaQtCodecType1 | Unset, data)

        qt_codec = _parse_qt_codec(d.pop("qt_codec", UNSET))

        def _parse_render_resolution(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        render_resolution = _parse_render_resolution(d.pop("render_resolution", UNSET))

        def _parse_use_metadata_cube_file_in_proxy(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_metadata_cube_file_in_proxy = _parse_use_metadata_cube_file_in_proxy(
            d.pop("use_metadata_cube_file_in_proxy", UNSET)
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
