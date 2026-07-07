from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.collection_keyframe_create_schema_status import (
    CollectionKeyframeCreateSchemaStatus,
)
from ..models.collection_keyframe_create_schema_type import (
    CollectionKeyframeCreateSchemaType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.collection_keyframe_create_schema_upload_credentials import (
        CollectionKeyframeCreateSchemaUploadCredentials,
    )
    from ..models.resolution_type import ResolutionType
    from ..models.time_code_type import TimeCodeType


T = TypeVar("T", bound="CollectionKeyframeCreateSchema")


@_attrs_define
class CollectionKeyframeCreateSchema:
    """
    Attributes:
        type_ (CollectionKeyframeCreateSchemaType):
        collection_id (UUID | Unset):
        content_type (str | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        filename (str | Unset):
        format_ (None | str | Unset):
        id (UUID | Unset):
        is_custom_keyframe (bool | Unset):
        is_public (bool | Unset):
        name (str | Unset):
        resolution (ResolutionType | Unset):
        rotation (int | None | Unset):
        size (int | None | Unset):
        status (CollectionKeyframeCreateSchemaStatus | Unset):
        storage_id (UUID | Unset):
        time_code (TimeCodeType | Unset):
        upload_credentials (CollectionKeyframeCreateSchemaUploadCredentials | Unset):
        upload_method (str | Unset):
        upload_url (str | Unset):
        url (str | Unset):
    """

    type_: CollectionKeyframeCreateSchemaType
    collection_id: UUID | Unset = UNSET
    content_type: str | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    filename: str | Unset = UNSET
    format_: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_custom_keyframe: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    name: str | Unset = UNSET
    resolution: ResolutionType | Unset = UNSET
    rotation: int | None | Unset = UNSET
    size: int | None | Unset = UNSET
    status: CollectionKeyframeCreateSchemaStatus | Unset = UNSET
    storage_id: UUID | Unset = UNSET
    time_code: TimeCodeType | Unset = UNSET
    upload_credentials: CollectionKeyframeCreateSchemaUploadCredentials | Unset = UNSET
    upload_method: str | Unset = UNSET
    upload_url: str | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        collection_id: str | Unset = UNSET
        if not isinstance(self.collection_id, Unset):
            collection_id = str(self.collection_id)

        content_type = self.content_type

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

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        storage_id: str | Unset = UNSET
        if not isinstance(self.storage_id, Unset):
            storage_id = str(self.storage_id)

        time_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_code, Unset):
            time_code = self.time_code.to_dict()

        upload_credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upload_credentials, Unset):
            upload_credentials = self.upload_credentials.to_dict()

        upload_method = self.upload_method

        upload_url = self.upload_url

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if filename is not UNSET:
            field_dict["filename"] = filename
        if format_ is not UNSET:
            field_dict["format"] = format_
        if id is not UNSET:
            field_dict["id"] = id
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
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if time_code is not UNSET:
            field_dict["time_code"] = time_code
        if upload_credentials is not UNSET:
            field_dict["upload_credentials"] = upload_credentials
        if upload_method is not UNSET:
            field_dict["upload_method"] = upload_method
        if upload_url is not UNSET:
            field_dict["upload_url"] = upload_url
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.collection_keyframe_create_schema_upload_credentials import (
            CollectionKeyframeCreateSchemaUploadCredentials,
        )
        from ..models.resolution_type import ResolutionType
        from ..models.time_code_type import TimeCodeType

        d = dict(src_dict)
        type_ = CollectionKeyframeCreateSchemaType(d.pop("type"))

        _collection_id = d.pop("collection_id", UNSET)
        collection_id: UUID | Unset
        if isinstance(_collection_id, Unset):
            collection_id = UNSET
        else:
            collection_id = UUID(_collection_id)

        content_type = d.pop("content_type", UNSET)

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

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

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
        status: CollectionKeyframeCreateSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CollectionKeyframeCreateSchemaStatus(_status)

        _storage_id = d.pop("storage_id", UNSET)
        storage_id: UUID | Unset
        if isinstance(_storage_id, Unset):
            storage_id = UNSET
        else:
            storage_id = UUID(_storage_id)

        _time_code = d.pop("time_code", UNSET)
        time_code: TimeCodeType | Unset
        if isinstance(_time_code, Unset):
            time_code = UNSET
        else:
            time_code = TimeCodeType.from_dict(_time_code)

        _upload_credentials = d.pop("upload_credentials", UNSET)
        upload_credentials: CollectionKeyframeCreateSchemaUploadCredentials | Unset
        if isinstance(_upload_credentials, Unset):
            upload_credentials = UNSET
        else:
            upload_credentials = (
                CollectionKeyframeCreateSchemaUploadCredentials.from_dict(
                    _upload_credentials
                )
            )

        upload_method = d.pop("upload_method", UNSET)

        upload_url = d.pop("upload_url", UNSET)

        url = d.pop("url", UNSET)

        collection_keyframe_create_schema = cls(
            type_=type_,
            collection_id=collection_id,
            content_type=content_type,
            date_created=date_created,
            date_modified=date_modified,
            filename=filename,
            format_=format_,
            id=id,
            is_custom_keyframe=is_custom_keyframe,
            is_public=is_public,
            name=name,
            resolution=resolution,
            rotation=rotation,
            size=size,
            status=status,
            storage_id=storage_id,
            time_code=time_code,
            upload_credentials=upload_credentials,
            upload_method=upload_method,
            upload_url=upload_url,
            url=url,
        )

        collection_keyframe_create_schema.additional_properties = d
        return collection_keyframe_create_schema

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
