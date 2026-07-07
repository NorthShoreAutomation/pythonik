from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditProxyResponseSchema")


@_attrs_define
class EditProxyResponseSchema:
    """
    Attributes:
        audio_bitrate (int | Unset):
        audio_codec (str | Unset):
        bitrate (int | Unset):
        codec (str | Unset):
        directory_path (str | Unset):
        file_set_id (UUID | Unset):
        format_id (UUID | Unset):
        height (int | Unset):
        id (UUID | Unset):
        name (str | Unset):
        transcoder_id (UUID | Unset):
        type_ (str | Unset):
        width (int | Unset):
    """

    audio_bitrate: int | Unset = UNSET
    audio_codec: str | Unset = UNSET
    bitrate: int | Unset = UNSET
    codec: str | Unset = UNSET
    directory_path: str | Unset = UNSET
    file_set_id: UUID | Unset = UNSET
    format_id: UUID | Unset = UNSET
    height: int | Unset = UNSET
    id: UUID | Unset = UNSET
    name: str | Unset = UNSET
    transcoder_id: UUID | Unset = UNSET
    type_: str | Unset = UNSET
    width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio_bitrate = self.audio_bitrate

        audio_codec = self.audio_codec

        bitrate = self.bitrate

        codec = self.codec

        directory_path = self.directory_path

        file_set_id: str | Unset = UNSET
        if not isinstance(self.file_set_id, Unset):
            file_set_id = str(self.file_set_id)

        format_id: str | Unset = UNSET
        if not isinstance(self.format_id, Unset):
            format_id = str(self.format_id)

        height = self.height

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        name = self.name

        transcoder_id: str | Unset = UNSET
        if not isinstance(self.transcoder_id, Unset):
            transcoder_id = str(self.transcoder_id)

        type_ = self.type_

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
        audio_bitrate = d.pop("audio_bitrate", UNSET)

        audio_codec = d.pop("audio_codec", UNSET)

        bitrate = d.pop("bitrate", UNSET)

        codec = d.pop("codec", UNSET)

        directory_path = d.pop("directory_path", UNSET)

        _file_set_id = d.pop("file_set_id", UNSET)
        file_set_id: UUID | Unset
        if isinstance(_file_set_id, Unset):
            file_set_id = UNSET
        else:
            file_set_id = UUID(_file_set_id)

        _format_id = d.pop("format_id", UNSET)
        format_id: UUID | Unset
        if isinstance(_format_id, Unset):
            format_id = UNSET
        else:
            format_id = UUID(_format_id)

        height = d.pop("height", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        name = d.pop("name", UNSET)

        _transcoder_id = d.pop("transcoder_id", UNSET)
        transcoder_id: UUID | Unset
        if isinstance(_transcoder_id, Unset):
            transcoder_id = UNSET
        else:
            transcoder_id = UUID(_transcoder_id)

        type_ = d.pop("type", UNSET)

        width = d.pop("width", UNSET)

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
