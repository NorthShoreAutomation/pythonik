from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proxy_create_schema_status import ProxyCreateSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.proxy_create_schema_upload_credentials import (
        ProxyCreateSchemaUploadCredentials,
    )
    from ..models.resolution_type import ResolutionType


T = TypeVar("T", bound="ProxyCreateSchema")


@_attrs_define
class ProxyCreateSchema:
    """
    Attributes:
        asset_id (UUID | Unset):
        audio_bitrate (int | Unset):
        audio_channels (int | None | Unset):
        bit_rate (int | Unset):
        codec (str | Unset):
        content_type (str | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        filename (str | Unset):
        format_ (str | Unset):
        frame_rate (None | str | Unset):
        id (UUID | Unset):
        is_drop_frame (bool | None | Unset):
        is_multichannel (bool | None | Unset):
        is_public (bool | Unset):
        multipart_upload_url (str | Unset):
        name (str | Unset):
        proxy_container_id (None | Unset | UUID):
        resolution (ResolutionType | Unset):
        rotation (int | None | Unset):
        size (int | None | Unset):
        start_time_code (None | str | Unset):
        status (ProxyCreateSchemaStatus | Unset):
        storage_id (UUID | Unset):
        storage_method (str | Unset):
        upload_credentials (ProxyCreateSchemaUploadCredentials | Unset):
        upload_method (str | Unset):
        upload_url (str | Unset):
        url (str | Unset):
        version_id (None | Unset | UUID):
    """

    asset_id: UUID | Unset = UNSET
    audio_bitrate: int | Unset = UNSET
    audio_channels: int | None | Unset = UNSET
    bit_rate: int | Unset = UNSET
    codec: str | Unset = UNSET
    content_type: str | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    filename: str | Unset = UNSET
    format_: str | Unset = UNSET
    frame_rate: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    is_drop_frame: bool | None | Unset = UNSET
    is_multichannel: bool | None | Unset = UNSET
    is_public: bool | Unset = UNSET
    multipart_upload_url: str | Unset = UNSET
    name: str | Unset = UNSET
    proxy_container_id: None | Unset | UUID = UNSET
    resolution: ResolutionType | Unset = UNSET
    rotation: int | None | Unset = UNSET
    size: int | None | Unset = UNSET
    start_time_code: None | str | Unset = UNSET
    status: ProxyCreateSchemaStatus | Unset = UNSET
    storage_id: UUID | Unset = UNSET
    storage_method: str | Unset = UNSET
    upload_credentials: ProxyCreateSchemaUploadCredentials | Unset = UNSET
    upload_method: str | Unset = UNSET
    upload_url: str | Unset = UNSET
    url: str | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id: str | Unset = UNSET
        if not isinstance(self.asset_id, Unset):
            asset_id = str(self.asset_id)

        audio_bitrate = self.audio_bitrate

        audio_channels: int | None | Unset
        if isinstance(self.audio_channels, Unset):
            audio_channels = UNSET
        else:
            audio_channels = self.audio_channels

        bit_rate = self.bit_rate

        codec = self.codec

        content_type = self.content_type

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        filename = self.filename

        format_ = self.format_

        frame_rate: None | str | Unset
        if isinstance(self.frame_rate, Unset):
            frame_rate = UNSET
        else:
            frame_rate = self.frame_rate

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_drop_frame: bool | None | Unset
        if isinstance(self.is_drop_frame, Unset):
            is_drop_frame = UNSET
        else:
            is_drop_frame = self.is_drop_frame

        is_multichannel: bool | None | Unset
        if isinstance(self.is_multichannel, Unset):
            is_multichannel = UNSET
        else:
            is_multichannel = self.is_multichannel

        is_public = self.is_public

        multipart_upload_url = self.multipart_upload_url

        name = self.name

        proxy_container_id: None | str | Unset
        if isinstance(self.proxy_container_id, Unset):
            proxy_container_id = UNSET
        elif isinstance(self.proxy_container_id, UUID):
            proxy_container_id = str(self.proxy_container_id)
        else:
            proxy_container_id = self.proxy_container_id

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

        start_time_code: None | str | Unset
        if isinstance(self.start_time_code, Unset):
            start_time_code = UNSET
        else:
            start_time_code = self.start_time_code

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_id: str | Unset = UNSET
        if not isinstance(self.storage_id, Unset):
            storage_id = str(self.storage_id)

        storage_method = self.storage_method

        upload_credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upload_credentials, Unset):
            upload_credentials = self.upload_credentials.to_dict()

        upload_method = self.upload_method

        upload_url = self.upload_url

        url = self.url

        version_id: None | str | Unset
        if isinstance(self.version_id, Unset):
            version_id = UNSET
        elif isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if audio_bitrate is not UNSET:
            field_dict["audio_bitrate"] = audio_bitrate
        if audio_channels is not UNSET:
            field_dict["audio_channels"] = audio_channels
        if bit_rate is not UNSET:
            field_dict["bit_rate"] = bit_rate
        if codec is not UNSET:
            field_dict["codec"] = codec
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
        if frame_rate is not UNSET:
            field_dict["frame_rate"] = frame_rate
        if id is not UNSET:
            field_dict["id"] = id
        if is_drop_frame is not UNSET:
            field_dict["is_drop_frame"] = is_drop_frame
        if is_multichannel is not UNSET:
            field_dict["is_multichannel"] = is_multichannel
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if multipart_upload_url is not UNSET:
            field_dict["multipart_upload_url"] = multipart_upload_url
        if name is not UNSET:
            field_dict["name"] = name
        if proxy_container_id is not UNSET:
            field_dict["proxy_container_id"] = proxy_container_id
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if rotation is not UNSET:
            field_dict["rotation"] = rotation
        if size is not UNSET:
            field_dict["size"] = size
        if start_time_code is not UNSET:
            field_dict["start_time_code"] = start_time_code
        if status is not UNSET:
            field_dict["status"] = status
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if storage_method is not UNSET:
            field_dict["storage_method"] = storage_method
        if upload_credentials is not UNSET:
            field_dict["upload_credentials"] = upload_credentials
        if upload_method is not UNSET:
            field_dict["upload_method"] = upload_method
        if upload_url is not UNSET:
            field_dict["upload_url"] = upload_url
        if url is not UNSET:
            field_dict["url"] = url
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.proxy_create_schema_upload_credentials import (
            ProxyCreateSchemaUploadCredentials,
        )
        from ..models.resolution_type import ResolutionType

        d = dict(src_dict)
        _asset_id = d.pop("asset_id", UNSET)
        asset_id: UUID | Unset
        if isinstance(_asset_id, Unset):
            asset_id = UNSET
        else:
            asset_id = UUID(_asset_id)

        audio_bitrate = d.pop("audio_bitrate", UNSET)

        def _parse_audio_channels(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        audio_channels = _parse_audio_channels(d.pop("audio_channels", UNSET))

        bit_rate = d.pop("bit_rate", UNSET)

        codec = d.pop("codec", UNSET)

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

        format_ = d.pop("format", UNSET)

        def _parse_frame_rate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        frame_rate = _parse_frame_rate(d.pop("frame_rate", UNSET))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_is_drop_frame(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_drop_frame = _parse_is_drop_frame(d.pop("is_drop_frame", UNSET))

        def _parse_is_multichannel(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_multichannel = _parse_is_multichannel(d.pop("is_multichannel", UNSET))

        is_public = d.pop("is_public", UNSET)

        multipart_upload_url = d.pop("multipart_upload_url", UNSET)

        name = d.pop("name", UNSET)

        def _parse_proxy_container_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                proxy_container_id_type_0 = UUID(data)

                return proxy_container_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        proxy_container_id = _parse_proxy_container_id(
            d.pop("proxy_container_id", UNSET)
        )

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

        def _parse_start_time_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_time_code = _parse_start_time_code(d.pop("start_time_code", UNSET))

        _status = d.pop("status", UNSET)
        status: ProxyCreateSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProxyCreateSchemaStatus(_status)

        _storage_id = d.pop("storage_id", UNSET)
        storage_id: UUID | Unset
        if isinstance(_storage_id, Unset):
            storage_id = UNSET
        else:
            storage_id = UUID(_storage_id)

        storage_method = d.pop("storage_method", UNSET)

        _upload_credentials = d.pop("upload_credentials", UNSET)
        upload_credentials: ProxyCreateSchemaUploadCredentials | Unset
        if isinstance(_upload_credentials, Unset):
            upload_credentials = UNSET
        else:
            upload_credentials = ProxyCreateSchemaUploadCredentials.from_dict(
                _upload_credentials
            )

        upload_method = d.pop("upload_method", UNSET)

        upload_url = d.pop("upload_url", UNSET)

        url = d.pop("url", UNSET)

        def _parse_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                version_id_type_0 = UUID(data)

                return version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        version_id = _parse_version_id(d.pop("version_id", UNSET))

        proxy_create_schema = cls(
            asset_id=asset_id,
            audio_bitrate=audio_bitrate,
            audio_channels=audio_channels,
            bit_rate=bit_rate,
            codec=codec,
            content_type=content_type,
            date_created=date_created,
            date_modified=date_modified,
            filename=filename,
            format_=format_,
            frame_rate=frame_rate,
            id=id,
            is_drop_frame=is_drop_frame,
            is_multichannel=is_multichannel,
            is_public=is_public,
            multipart_upload_url=multipart_upload_url,
            name=name,
            proxy_container_id=proxy_container_id,
            resolution=resolution,
            rotation=rotation,
            size=size,
            start_time_code=start_time_code,
            status=status,
            storage_id=storage_id,
            storage_method=storage_method,
            upload_credentials=upload_credentials,
            upload_method=upload_method,
            upload_url=upload_url,
            url=url,
            version_id=version_id,
        )

        proxy_create_schema.additional_properties = d
        return proxy_create_schema

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
