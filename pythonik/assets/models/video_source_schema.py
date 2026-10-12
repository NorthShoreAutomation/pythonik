from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.video_source_schema_mode import VideoSourceSchemaMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoSourceSchema")


@_attrs_define
class VideoSourceSchema:
    """
    Attributes:
        file_id (None | str | Unset): The iconik file ID to use as the video source for the import.
        mode (None | Unset | VideoSourceSchemaMode):
    """

    file_id: None | str | Unset = UNSET
    mode: None | Unset | VideoSourceSchemaMode = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_id: None | str | Unset
        if isinstance(self.file_id, Unset):
            file_id = UNSET
        else:
            file_id = self.file_id

        mode: None | str | Unset
        if isinstance(self.mode, Unset):
            mode = UNSET
        elif isinstance(self.mode, VideoSourceSchemaMode):
            mode = self.mode.value
        else:
            mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_id is not UNSET:
            field_dict["file_id"] = file_id
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_file_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_id = _parse_file_id(d.pop("file_id", UNSET))

        def _parse_mode(data: object) -> None | Unset | VideoSourceSchemaMode:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mode_type_1 = VideoSourceSchemaMode(data)

                return mode_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VideoSourceSchemaMode, data)

        mode = _parse_mode(d.pop("mode", UNSET))

        video_source_schema = cls(
            file_id=file_id,
            mode=mode,
        )

        video_source_schema.additional_properties = d
        return video_source_schema

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
