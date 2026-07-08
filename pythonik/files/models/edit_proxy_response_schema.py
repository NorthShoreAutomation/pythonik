from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditProxyResponseSchema")


@_attrs_define
class EditProxyResponseSchema:
    """
    Attributes:
        audio_bitrate (int | None | Unset):
        audio_codec (None | str | Unset):
        bitrate (int | None | Unset):
        codec (None | str | Unset):
        directory_path (None | str | Unset):
        file_set_id (None | Unset | UUID):
        format_id (None | Unset | UUID):
        height (int | None | Unset):
        id (None | Unset | UUID):
        name (None | str | Unset):
        transcoder_id (None | Unset | UUID):
        type_ (None | str | Unset):
        width (int | None | Unset):
    """

    audio_bitrate: int | None | Unset = UNSET
    audio_codec: None | str | Unset = UNSET
    bitrate: int | None | Unset = UNSET
    codec: None | str | Unset = UNSET
    directory_path: None | str | Unset = UNSET
    file_set_id: None | Unset | UUID = UNSET
    format_id: None | Unset | UUID = UNSET
    height: int | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    transcoder_id: None | Unset | UUID = UNSET
    type_: None | str | Unset = UNSET
    width: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio_bitrate: int | None | Unset
        if isinstance(self.audio_bitrate, Unset):
            audio_bitrate = UNSET
        else:
            audio_bitrate = self.audio_bitrate

        audio_codec: None | str | Unset
        if isinstance(self.audio_codec, Unset):
            audio_codec = UNSET
        else:
            audio_codec = self.audio_codec

        bitrate: int | None | Unset
        if isinstance(self.bitrate, Unset):
            bitrate = UNSET
        else:
            bitrate = self.bitrate

        codec: None | str | Unset
        if isinstance(self.codec, Unset):
            codec = UNSET
        else:
            codec = self.codec

        directory_path: None | str | Unset
        if isinstance(self.directory_path, Unset):
            directory_path = UNSET
        else:
            directory_path = self.directory_path

        file_set_id: None | str | Unset
        if isinstance(self.file_set_id, Unset):
            file_set_id = UNSET
        elif isinstance(self.file_set_id, UUID):
            file_set_id = str(self.file_set_id)
        else:
            file_set_id = self.file_set_id

        format_id: None | str | Unset
        if isinstance(self.format_id, Unset):
            format_id = UNSET
        elif isinstance(self.format_id, UUID):
            format_id = str(self.format_id)
        else:
            format_id = self.format_id

        height: int | None | Unset
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        transcoder_id: None | str | Unset
        if isinstance(self.transcoder_id, Unset):
            transcoder_id = UNSET
        elif isinstance(self.transcoder_id, UUID):
            transcoder_id = str(self.transcoder_id)
        else:
            transcoder_id = self.transcoder_id

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        width: int | None | Unset
        if isinstance(self.width, Unset):
            width = UNSET
        else:
            width = self.width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audio_bitrate is not UNSET:
            field_dict["audio_bitrate"] = audio_bitrate
        if audio_codec is not UNSET:
            field_dict["audio_codec"] = audio_codec
        if bitrate is not UNSET:
            field_dict["bitrate"] = bitrate
        if codec is not UNSET:
            field_dict["codec"] = codec
        if directory_path is not UNSET:
            field_dict["directory_path"] = directory_path
        if file_set_id is not UNSET:
            field_dict["file_set_id"] = file_set_id
        if format_id is not UNSET:
            field_dict["format_id"] = format_id
        if height is not UNSET:
            field_dict["height"] = height
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if transcoder_id is not UNSET:
            field_dict["transcoder_id"] = transcoder_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_audio_bitrate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        audio_bitrate = _parse_audio_bitrate(d.pop("audio_bitrate", UNSET))

        def _parse_audio_codec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        audio_codec = _parse_audio_codec(d.pop("audio_codec", UNSET))

        def _parse_bitrate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bitrate = _parse_bitrate(d.pop("bitrate", UNSET))

        def _parse_codec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codec = _parse_codec(d.pop("codec", UNSET))

        def _parse_directory_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directory_path = _parse_directory_path(d.pop("directory_path", UNSET))

        def _parse_file_set_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                file_set_id_type_0 = UUID(data)

                return file_set_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        file_set_id = _parse_file_set_id(d.pop("file_set_id", UNSET))

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

        def _parse_height(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        height = _parse_height(d.pop("height", UNSET))

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_transcoder_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                transcoder_id_type_0 = UUID(data)

                return transcoder_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        transcoder_id = _parse_transcoder_id(d.pop("transcoder_id", UNSET))

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_width(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        width = _parse_width(d.pop("width", UNSET))

        edit_proxy_response_schema = cls(
            audio_bitrate=audio_bitrate,
            audio_codec=audio_codec,
            bitrate=bitrate,
            codec=codec,
            directory_path=directory_path,
            file_set_id=file_set_id,
            format_id=format_id,
            height=height,
            id=id,
            name=name,
            transcoder_id=transcoder_id,
            type_=type_,
            width=width,
        )

        edit_proxy_response_schema.additional_properties = d
        return edit_proxy_response_schema

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
