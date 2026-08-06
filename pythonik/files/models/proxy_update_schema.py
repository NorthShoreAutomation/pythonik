from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proxy_update_schema_status import ProxyUpdateSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resolution_type import ResolutionType


T = TypeVar("T", bound="ProxyUpdateSchema")


@_attrs_define
class ProxyUpdateSchema:
    """
    Attributes:
        asset_id (None | Unset | UUID):
        audio_bitrate (int | None | Unset):
        audio_channels (int | None | Unset):
        bit_rate (int | None | Unset):
        codec (None | str | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        filename (None | str | Unset):
        format_ (None | str | Unset):
        frame_rate (None | str | Unset):
        id (None | Unset | UUID):
        is_drop_frame (bool | None | Unset):
        is_multichannel (bool | None | Unset):
        is_public (bool | None | Unset):
        name (None | str | Unset):
        resolution (None | ResolutionType | Unset):
        rotation (int | None | Unset):
        size (int | None | Unset):
        start_time_code (None | str | Unset):
        status (None | ProxyUpdateSchemaStatus | Unset):
        storage_id (None | Unset | UUID):
        url (None | str | Unset):
        version_id (None | Unset | UUID):
    """

    asset_id: None | Unset | UUID = UNSET
    audio_bitrate: int | None | Unset = UNSET
    audio_channels: int | None | Unset = UNSET
    bit_rate: int | None | Unset = UNSET
    codec: None | str | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    filename: None | str | Unset = UNSET
    format_: None | str | Unset = UNSET
    frame_rate: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    is_drop_frame: bool | None | Unset = UNSET
    is_multichannel: bool | None | Unset = UNSET
    is_public: bool | None | Unset = UNSET
    name: None | str | Unset = UNSET
    resolution: None | ResolutionType | Unset = UNSET
    rotation: int | None | Unset = UNSET
    size: int | None | Unset = UNSET
    start_time_code: None | str | Unset = UNSET
    status: None | ProxyUpdateSchemaStatus | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    url: None | str | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resolution_type import ResolutionType

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

        audio_bitrate: int | None | Unset
        if isinstance(self.audio_bitrate, Unset):
            audio_bitrate = UNSET
        else:
            audio_bitrate = self.audio_bitrate

        audio_channels: int | None | Unset
        if isinstance(self.audio_channels, Unset):
            audio_channels = UNSET
        else:
            audio_channels = self.audio_channels

        bit_rate: int | None | Unset
        if isinstance(self.bit_rate, Unset):
            bit_rate = UNSET
        else:
            bit_rate = self.bit_rate

        codec: None | str | Unset
        if isinstance(self.codec, Unset):
            codec = UNSET
        else:
            codec = self.codec

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

        frame_rate: None | str | Unset
        if isinstance(self.frame_rate, Unset):
            frame_rate = UNSET
        else:
            frame_rate = self.frame_rate

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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

        start_time_code: None | str | Unset
        if isinstance(self.start_time_code, Unset):
            start_time_code = UNSET
        else:
            start_time_code = self.start_time_code

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ProxyUpdateSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
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
        if name is not UNSET:
            field_dict["name"] = name
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
        if url is not UNSET:
            field_dict["url"] = url
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resolution_type import ResolutionType

        d = dict(src_dict)

        def _parse_asset_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                asset_id_type_0 = UUID(data)

                return asset_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        asset_id = _parse_asset_id(d.pop("asset_id", UNSET))

        def _parse_audio_bitrate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        audio_bitrate = _parse_audio_bitrate(d.pop("audio_bitrate", UNSET))

        def _parse_audio_channels(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        audio_channels = _parse_audio_channels(d.pop("audio_channels", UNSET))

        def _parse_bit_rate(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bit_rate = _parse_bit_rate(d.pop("bit_rate", UNSET))

        def _parse_codec(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        codec = _parse_codec(d.pop("codec", UNSET))

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

        def _parse_frame_rate(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        frame_rate = _parse_frame_rate(d.pop("frame_rate", UNSET))

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

        def _parse_start_time_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_time_code = _parse_start_time_code(d.pop("start_time_code", UNSET))

        def _parse_status(data: object) -> None | ProxyUpdateSchemaStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = ProxyUpdateSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProxyUpdateSchemaStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

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

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

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

        proxy_update_schema = cls(
            asset_id=asset_id,
            audio_bitrate=audio_bitrate,
            audio_channels=audio_channels,
            bit_rate=bit_rate,
            codec=codec,
            date_created=date_created,
            date_modified=date_modified,
            filename=filename,
            format_=format_,
            frame_rate=frame_rate,
            id=id,
            is_drop_frame=is_drop_frame,
            is_multichannel=is_multichannel,
            is_public=is_public,
            name=name,
            resolution=resolution,
            rotation=rotation,
            size=size,
            start_time_code=start_time_code,
            status=status,
            storage_id=storage_id,
            url=url,
            version_id=version_id,
        )

        proxy_update_schema.additional_properties = d
        return proxy_update_schema

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
