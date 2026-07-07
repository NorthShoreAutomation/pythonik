from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_keyframe_update_schema_status import (
    CollectionKeyframeUpdateSchemaStatus,
)
from ..models.collection_keyframe_update_schema_type import (
    CollectionKeyframeUpdateSchemaType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resolution_type import ResolutionType
    from ..models.time_code_type import TimeCodeType


T = TypeVar("T", bound="CollectionKeyframeUpdateSchema")


@_attrs_define
class CollectionKeyframeUpdateSchema:
    """
    Attributes:
        type_ (CollectionKeyframeUpdateSchemaType):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        filename (str | Unset):
        format_ (None | str | Unset):
        is_custom_keyframe (bool | Unset):
        is_public (bool | Unset):
        name (str | Unset):
        resolution (ResolutionType | Unset):
        rotation (int | None | Unset):
        size (int | None | Unset):
        status (CollectionKeyframeUpdateSchemaStatus | Unset):
        time_code (TimeCodeType | Unset):
        url (str | Unset):
    """

    type_: CollectionKeyframeUpdateSchemaType
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    filename: str | Unset = UNSET
    format_: None | str | Unset = UNSET
    is_custom_keyframe: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    name: str | Unset = UNSET
    resolution: ResolutionType | Unset = UNSET
    rotation: int | None | Unset = UNSET
    size: int | None | Unset = UNSET
    status: CollectionKeyframeUpdateSchemaStatus | Unset = UNSET
    time_code: TimeCodeType | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        filename = self.filename

        format_: None | str | Unset
        if isinstance(self.format_, Unset):
            format_ = UNSET
        else:
            format_ = self.format_

        is_custom_keyframe = self.is_custom_keyframe

        is_public = self.is_public

        name = self.name

        resolution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.to_dict()

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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        time_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_code, Unset):
            time_code = self.time_code.to_dict()

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
        from ..models.resolution_type import ResolutionType
        from ..models.time_code_type import TimeCodeType

        d = dict(src_dict)
        type_ = CollectionKeyframeUpdateSchemaType(d.pop("type"))

        _date_created = d.pop("date_created", UNSET)
        date_created: datetime.datetime | Unset
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = datetime.datetime.fromisoformat(_date_created)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = datetime.datetime.fromisoformat(_date_modified)

        filename = d.pop("filename", UNSET)

        def _parse_format_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        format_ = _parse_format_(d.pop("format", UNSET))

        is_custom_keyframe = d.pop("is_custom_keyframe", UNSET)

        is_public = d.pop("is_public", UNSET)

        name = d.pop("name", UNSET)

        _resolution = d.pop("resolution", UNSET)
        resolution: ResolutionType | Unset
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = ResolutionType.from_dict(_resolution)

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

        _status = d.pop("status", UNSET)
        status: CollectionKeyframeUpdateSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CollectionKeyframeUpdateSchemaStatus(_status)

        _time_code = d.pop("time_code", UNSET)
        time_code: TimeCodeType | Unset
        if isinstance(_time_code, Unset):
            time_code = UNSET
        else:
            time_code = TimeCodeType.from_dict(_time_code)

        url = d.pop("url", UNSET)

        collection_keyframe_update_schema = cls(
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

        collection_keyframe_update_schema.additional_properties = d
        return collection_keyframe_update_schema

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
