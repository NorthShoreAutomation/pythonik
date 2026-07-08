from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.keyframe_type import KeyframeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.keyframe_status_type_1 import KeyframeStatusType1
    from ..models.keyframe_upload_credentials_type_0 import (
        KeyframeUploadCredentialsType0,
    )
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
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        filename (None | str | Unset):
        format_ (None | str | Unset):
        id (None | Unset | UUID):
        is_custom_keyframe (bool | None | Unset):
        is_public (bool | None | Unset):
        name (None | str | Unset):
        resolution (None | ResolutionType | Unset):
        rotation (int | None | Unset):
        size (int | None | Unset):
        status (KeyframeStatusType1 | None | Unset):
        storage_id (None | Unset | UUID):
        storage_method (None | str | Unset):
        time_code (None | TimeCodeType | Unset):
        upload_credentials (KeyframeUploadCredentialsType0 | None | Unset):
        upload_method (None | str | Unset):
        upload_url (None | str | Unset):
        url (None | str | Unset):
        version_id (None | Unset | UUID):
    """

    type_: KeyframeType
    asset_id: None | Unset | UUID = UNSET
    collection_id: None | Unset | UUID = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    filename: None | str | Unset = UNSET
    format_: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    is_custom_keyframe: bool | None | Unset = UNSET
    is_public: bool | None | Unset = UNSET
    name: None | str | Unset = UNSET
    resolution: None | ResolutionType | Unset = UNSET
    rotation: int | None | Unset = UNSET
    size: int | None | Unset = UNSET
    status: KeyframeStatusType1 | None | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    storage_method: None | str | Unset = UNSET
    time_code: None | TimeCodeType | Unset = UNSET
    upload_credentials: KeyframeUploadCredentialsType0 | None | Unset = UNSET
    upload_method: None | str | Unset = UNSET
    upload_url: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.keyframe_status_type_1 import KeyframeStatusType1
        from ..models.keyframe_upload_credentials_type_0 import (
            KeyframeUploadCredentialsType0,
        )
        from ..models.resolution_type import ResolutionType
        from ..models.time_code_type import TimeCodeType

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

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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
        elif isinstance(self.status, KeyframeStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

        storage_id: None | str | Unset
        if isinstance(self.storage_id, Unset):
            storage_id = UNSET
        elif isinstance(self.storage_id, UUID):
            storage_id = str(self.storage_id)
        else:
            storage_id = self.storage_id

        storage_method: None | str | Unset
        if isinstance(self.storage_method, Unset):
            storage_method = UNSET
        else:
            storage_method = self.storage_method

        time_code: dict[str, Any] | None | Unset
        if isinstance(self.time_code, Unset):
            time_code = UNSET
        elif isinstance(self.time_code, TimeCodeType):
            time_code = self.time_code.to_dict()
        else:
            time_code = self.time_code

        upload_credentials: dict[str, Any] | None | Unset
        if isinstance(self.upload_credentials, Unset):
            upload_credentials = UNSET
        elif isinstance(self.upload_credentials, KeyframeUploadCredentialsType0):
            upload_credentials = self.upload_credentials.to_dict()
        else:
            upload_credentials = self.upload_credentials

        upload_method: None | str | Unset
        if isinstance(self.upload_method, Unset):
            upload_method = UNSET
        else:
            upload_method = self.upload_method

        upload_url: None | str | Unset
        if isinstance(self.upload_url, Unset):
            upload_url = UNSET
        else:
            upload_url = self.upload_url

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
        from ..models.keyframe_status_type_1 import KeyframeStatusType1
        from ..models.keyframe_upload_credentials_type_0 import (
            KeyframeUploadCredentialsType0,
        )
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

        def _parse_status(data: object) -> KeyframeStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = KeyframeStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeyframeStatusType1 | None | Unset, data)

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

        def _parse_storage_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_method = _parse_storage_method(d.pop("storage_method", UNSET))

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

        def _parse_upload_credentials(
            data: object,
        ) -> KeyframeUploadCredentialsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upload_credentials_type_0 = KeyframeUploadCredentialsType0.from_dict(
                    data
                )

                return upload_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(KeyframeUploadCredentialsType0 | None | Unset, data)

        upload_credentials = _parse_upload_credentials(
            d.pop("upload_credentials", UNSET)
        )

        def _parse_upload_method(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_method = _parse_upload_method(d.pop("upload_method", UNSET))

        def _parse_upload_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        upload_url = _parse_upload_url(d.pop("upload_url", UNSET))

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
