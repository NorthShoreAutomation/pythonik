from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.playlist_keyframe_update_schema_type import (
    PlaylistKeyframeUpdateSchemaType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.playlist_keyframe_update_schema_status_type_1 import (
        PlaylistKeyframeUpdateSchemaStatusType1,
    )
    from ..models.resolution_type import ResolutionType
    from ..models.time_code_type import TimeCodeType


T = TypeVar("T", bound="PlaylistKeyframeUpdateSchema")


@_attrs_define
class PlaylistKeyframeUpdateSchema:
    """
    Attributes:
        type_ (PlaylistKeyframeUpdateSchemaType):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        filename (None | str | Unset):
        format_ (None | str | Unset):
        is_custom_keyframe (bool | None | Unset):
        is_public (bool | None | Unset):
        name (None | str | Unset):
        resolution (None | ResolutionType | Unset):
        rotation (int | None | Unset):
        size (int | None | Unset):
        status (None | PlaylistKeyframeUpdateSchemaStatusType1 | Unset):
        time_code (None | TimeCodeType | Unset):
        url (None | str | Unset):
    """

    type_: PlaylistKeyframeUpdateSchemaType
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    filename: None | str | Unset = UNSET
    format_: None | str | Unset = UNSET
    is_custom_keyframe: bool | None | Unset = UNSET
    is_public: bool | None | Unset = UNSET
    name: None | str | Unset = UNSET
    resolution: None | ResolutionType | Unset = UNSET
    rotation: int | None | Unset = UNSET
    size: int | None | Unset = UNSET
    status: None | PlaylistKeyframeUpdateSchemaStatusType1 | Unset = UNSET
    time_code: None | TimeCodeType | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.playlist_keyframe_update_schema_status_type_1 import (
            PlaylistKeyframeUpdateSchemaStatusType1,
        )
        from ..models.resolution_type import ResolutionType
        from ..models.time_code_type import TimeCodeType

        type_ = self.type_.value

        date_created: None | str | Unset
        if isinstance(self.date_created, Unset):
            date_created = UNSET
        elif isinstance(self.date_created, datetime.datetime):
            date_created = self.date_created.isoformat()
        else:
            date_created = self.date_created

        date_modified: None | str | Unset
        if isinstance(self.date_modified, Unset):
            date_modified = UNSET
        elif isinstance(self.date_modified, datetime.datetime):
            date_modified = self.date_modified.isoformat()
        else:
            date_modified = self.date_modified

        filename: None | str | Unset
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        is_custom_keyframe: bool | None | Unset
        if isinstance(self.is_custom_keyframe, Unset):
            is_custom_keyframe = UNSET
        else:
            is_custom_keyframe = self.is_custom_keyframe

        is_public: bool | None | Unset
        if isinstance(self.is_public, Unset):
            is_public = UNSET
        else:
            is_public = self.is_public

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        resolution: dict[str, Any] | None | Unset
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        elif isinstance(self.resolution, ResolutionType):
            resolution = self.resolution.to_dict()
        else:
            resolution = self.resolution

        rotation: int | None | Unset
        if isinstance(self.rotation, Unset):
            rotation = UNSET
        else:
            rotation = self.rotation

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, PlaylistKeyframeUpdateSchemaStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

        time_code: dict[str, Any] | None | Unset
        if isinstance(self.time_code, Unset):
            time_code = UNSET
        elif isinstance(self.time_code, TimeCodeType):
            time_code = self.time_code.to_dict()
        else:
            time_code = self.time_code

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if filename is not UNSET:
            field_dict["filename"] = filename
        if format_ is not UNSET:
            field_dict["format"] = format_
        if is_custom_keyframe is not UNSET:
            field_dict["is_custom_keyframe"] = is_custom_keyframe
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if name is not UNSET:
            field_dict["name"] = name
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if rotation is not UNSET:
            field_dict["rotation"] = rotation
        if size is not UNSET:
            field_dict["size"] = size
        if status is not UNSET:
            field_dict["status"] = status
        if time_code is not UNSET:
            field_dict["time_code"] = time_code
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.playlist_keyframe_update_schema_status_type_1 import (
            PlaylistKeyframeUpdateSchemaStatusType1,
        )
        from ..models.resolution_type import ResolutionType
        from ..models.time_code_type import TimeCodeType

        d = dict(src_dict)
        type_ = PlaylistKeyframeUpdateSchemaType(d.pop("type"))

        def _parse_date_created(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_created_type_0 = datetime.datetime.fromisoformat(data)

                return date_created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_created = _parse_date_created(d.pop("date_created", UNSET))

        def _parse_date_modified(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_modified_type_0 = datetime.datetime.fromisoformat(data)

                return date_modified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_modified = _parse_date_modified(d.pop("date_modified", UNSET))

        def _parse_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filename = _parse_filename(d.pop("filename", UNSET))

        def _parse_format_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))

        def _parse_is_custom_keyframe(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_custom_keyframe = _parse_is_custom_keyframe(
            d.pop("is_custom_keyframe", UNSET)
        )

        def _parse_is_public(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_public = _parse_is_public(d.pop("is_public", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_resolution(data: object) -> None | ResolutionType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                resolution_type_1 = ResolutionType.from_dict(data)

                return resolution_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResolutionType | Unset, data)

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        def _parse_rotation(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        rotation = _parse_rotation(d.pop("rotation", UNSET))

        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_status(
            data: object,
        ) -> None | PlaylistKeyframeUpdateSchemaStatusType1 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = PlaylistKeyframeUpdateSchemaStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PlaylistKeyframeUpdateSchemaStatusType1 | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_time_code(data: object) -> None | TimeCodeType | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                time_code_type_1 = TimeCodeType.from_dict(data)

                return time_code_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TimeCodeType | Unset, data)

        time_code = _parse_time_code(d.pop("time_code", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        playlist_keyframe_update_schema = cls(
            type_=type_,
            date_created=date_created,
            date_modified=date_modified,
            filename=filename,
            format_=format_,
            is_custom_keyframe=is_custom_keyframe,
            is_public=is_public,
            name=name,
            resolution=resolution,
            rotation=rotation,
            size=size,
            status=status,
            time_code=time_code,
            url=url,
        )

        playlist_keyframe_update_schema.additional_properties = d
        return playlist_keyframe_update_schema

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
