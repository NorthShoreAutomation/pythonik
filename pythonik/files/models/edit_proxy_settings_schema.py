from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditProxySettingsSchema")


@_attrs_define
class EditProxySettingsSchema:
    """
    Attributes:
        height (int):
        width (int):
        audio_bitrate (int | Unset):
        audio_codec (None | str | Unset):
        bitrate (int | Unset):
        codec (str | Unset):
        data (str | Unset):
        delete_after_upload (bool | Unset):
        destination_path (None | str | Unset):
        exclude_patterns (list[str] | Unset):
        include_patterns (list[str] | Unset):
        local (bool | Unset):
        local_destination_path (None | str | Unset):
        min_height (int | Unset):
        min_width (int | Unset):
        priority (int | None | Unset):
        storage_id (None | Unset | UUID):
    """

    height: int
    width: int
    audio_bitrate: int | Unset = UNSET
    audio_codec: None | str | Unset = UNSET
    bitrate: int | Unset = UNSET
    codec: str | Unset = UNSET
    data: str | Unset = UNSET
    delete_after_upload: bool | Unset = UNSET
    destination_path: None | str | Unset = UNSET
    exclude_patterns: list[str] | Unset = UNSET
    include_patterns: list[str] | Unset = UNSET
    local: bool | Unset = UNSET
    local_destination_path: None | str | Unset = UNSET
    min_height: int | Unset = UNSET
    min_width: int | Unset = UNSET
    priority: int | None | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        height = self.height

        width = self.width

        audio_bitrate = self.audio_bitrate

        audio_codec: None | str | Unset
        if isinstance(self.audio_codec, Unset):
            audio_codec = UNSET
        else:
            audio_codec = self.audio_codec

        bitrate = self.bitrate

        codec = self.codec

        data = self.data

        delete_after_upload = self.delete_after_upload

        destination_path: None | str | Unset
        if isinstance(self.destination_path, Unset):
            destination_path = UNSET
        else:
            destination_path = self.destination_path

        exclude_patterns: list[str] | Unset = UNSET
        if not isinstance(self.exclude_patterns, Unset):
            exclude_patterns = self.exclude_patterns

        include_patterns: list[str] | Unset = UNSET
        if not isinstance(self.include_patterns, Unset):
            include_patterns = self.include_patterns

        local = self.local

        local_destination_path: None | str | Unset
        if isinstance(self.local_destination_path, Unset):
            local_destination_path = UNSET
        else:
            local_destination_path = self.local_destination_path

        min_height = self.min_height

        min_width = self.min_width

        priority: int | None | Unset
        if isinstance(self.priority, Unset):
            priority = UNSET
        else:
            priority = self.priority

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "height": height,
                "width": width,
            }
        )
        if audio_bitrate is not UNSET:
            field_dict["audio_bitrate"] = audio_bitrate
        if audio_codec is not UNSET:
            field_dict["audio_codec"] = audio_codec
        if bitrate is not UNSET:
            field_dict["bitrate"] = bitrate
        if codec is not UNSET:
            field_dict["codec"] = codec
        if data is not UNSET:
            field_dict["data"] = data
        if delete_after_upload is not UNSET:
            field_dict["delete_after_upload"] = delete_after_upload
        if destination_path is not UNSET:
            field_dict["destination_path"] = destination_path
        if exclude_patterns is not UNSET:
            field_dict["exclude_patterns"] = exclude_patterns
        if include_patterns is not UNSET:
            field_dict["include_patterns"] = include_patterns
        if local is not UNSET:
            field_dict["local"] = local
        if local_destination_path is not UNSET:
            field_dict["local_destination_path"] = local_destination_path
        if min_height is not UNSET:
            field_dict["min_height"] = min_height
        if min_width is not UNSET:
            field_dict["min_width"] = min_width
        if priority is not UNSET:
            field_dict["priority"] = priority
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        height = d.pop("height")

        width = d.pop("width")

        audio_bitrate = d.pop("audio_bitrate", UNSET)

        def _parse_audio_codec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        audio_codec = _parse_audio_codec(d.pop("audio_codec", UNSET))

        bitrate = d.pop("bitrate", UNSET)

        codec = d.pop("codec", UNSET)

        data = d.pop("data", UNSET)

        delete_after_upload = d.pop("delete_after_upload", UNSET)

        def _parse_destination_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        destination_path = _parse_destination_path(d.pop("destination_path", UNSET))

        exclude_patterns = cast(list[str], d.pop("exclude_patterns", UNSET))

        include_patterns = cast(list[str], d.pop("include_patterns", UNSET))

        local = d.pop("local", UNSET)

        def _parse_local_destination_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        local_destination_path = _parse_local_destination_path(
            d.pop("local_destination_path", UNSET)
        )

        min_height = d.pop("min_height", UNSET)

        min_width = d.pop("min_width", UNSET)

        def _parse_priority(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        priority = _parse_priority(d.pop("priority", UNSET))

        def _parse_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_id_type_0 = UUID(data)

                return storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        storage_id = _parse_storage_id(d.pop("storage_id", UNSET))

        edit_proxy_settings_schema = cls(
            height=height,
            width=width,
            audio_bitrate=audio_bitrate,
            audio_codec=audio_codec,
            bitrate=bitrate,
            codec=codec,
            data=data,
            delete_after_upload=delete_after_upload,
            destination_path=destination_path,
            exclude_patterns=exclude_patterns,
            include_patterns=include_patterns,
            local=local,
            local_destination_path=local_destination_path,
            min_height=min_height,
            min_width=min_width,
            priority=priority,
            storage_id=storage_id,
        )

        edit_proxy_settings_schema.additional_properties = d
        return edit_proxy_settings_schema

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
