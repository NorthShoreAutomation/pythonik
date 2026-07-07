from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyframe_status import KeyframeStatus
from ..models.keyframe_type import KeyframeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyframe_upload_credentials import KeyframeUploadCredentials
    from ..models.resolution_type import ResolutionType
    from ..models.time_code_type import TimeCodeType


T = TypeVar("T", bound="Keyframe")


@_attrs_define
class Keyframe:
    """
    Attributes:
        type_ (KeyframeType):
        asset_id (None | Unset | UUID):
        collection_id (None | Unset | UUID):
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
        status (KeyframeStatus | Unset):
        storage_id (UUID | Unset):
        storage_method (str | Unset):
        time_code (TimeCodeType | Unset):
        upload_credentials (KeyframeUploadCredentials | Unset):
        upload_method (str | Unset):
        upload_url (str | Unset):
        url (str | Unset):
        version_id (None | Unset | UUID):
    """

    type_: KeyframeType
    asset_id: None | Unset | UUID = UNSET
    collection_id: None | Unset | UUID = UNSET
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
    status: KeyframeStatus | Unset = UNSET
    storage_id: UUID | Unset = UNSET
    storage_method: str | Unset = UNSET
    time_code: TimeCodeType | Unset = UNSET
    upload_credentials: KeyframeUploadCredentials | Unset = UNSET
    upload_method: str | Unset = UNSET
    upload_url: str | Unset = UNSET
    url: str | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

        collection_id: None | str | Unset
        if isinstance(self.collection_id, Unset):
            collection_id = UNSET
        elif isinstance(self.collection_id, UUID):
            collection_id = str(self.collection_id)
        else:
            collection_id = self.collection_id

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

        storage_method = self.storage_method

        time_code: dict[str, Any] | Unset = UNSET
        if not isinstance(self.time_code, Unset):
            time_code = self.time_code.to_dict()

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
        field_dict.update(
            {
                "type": type_,
            }
        )
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
        if collection_id is not UNSET:
            field_dict["collection_id"] = collection_id
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
        if storage_method is not UNSET:
            field_dict["storage_method"] = storage_method
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
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.keyframe_upload_credentials import KeyframeUploadCredentials
        from ..models.resolution_type import ResolutionType
        from ..models.time_code_type import TimeCodeType

        d = dict(src_dict)
        type_ = KeyframeType(d.pop("type"))

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

        def _parse_collection_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                collection_id_type_0 = UUID(data)

                return collection_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        collection_id = _parse_collection_id(d.pop("collection_id", UNSET))

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
        status: KeyframeStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = KeyframeStatus(_status)

        _storage_id = d.pop("storage_id", UNSET)
        storage_id: UUID | Unset
        if isinstance(_storage_id, Unset):
            storage_id = UNSET
        else:
            storage_id = UUID(_storage_id)

        storage_method = d.pop("storage_method", UNSET)

        _time_code = d.pop("time_code", UNSET)
        time_code: TimeCodeType | Unset
        if isinstance(_time_code, Unset):
            time_code = UNSET
        else:
            time_code = TimeCodeType.from_dict(_time_code)

        _upload_credentials = d.pop("upload_credentials", UNSET)
        upload_credentials: KeyframeUploadCredentials | Unset
        if isinstance(_upload_credentials, Unset):
            upload_credentials = UNSET
        else:
            upload_credentials = KeyframeUploadCredentials.from_dict(
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

        keyframe = cls(
            type_=type_,
            asset_id=asset_id,
            collection_id=collection_id,
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
            storage_method=storage_method,
            time_code=time_code,
            upload_credentials=upload_credentials,
            upload_method=upload_method,
            upload_url=upload_url,
            url=url,
            version_id=version_id,
        )

        keyframe.additional_properties = d
        return keyframe

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
