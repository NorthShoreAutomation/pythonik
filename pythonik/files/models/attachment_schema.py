from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.attachment_schema_status import AttachmentSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.attachment_schema_upload_credentials_type_0 import (
        AttachmentSchemaUploadCredentialsType0,
    )
    from ..models.attachment_schema_upload_headers_type_0 import (
        AttachmentSchemaUploadHeadersType0,
    )


T = TypeVar("T", bound="AttachmentSchema")


@_attrs_define
class AttachmentSchema:
    """
    Attributes:
        asset_id (None | Unset | UUID):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        filename (None | str | Unset):
        format_ (None | str | Unset):
        id (None | Unset | UUID):
        name (None | str | Unset):
        segment_id (None | Unset | UUID):
        size (int | None | Unset):
        status (AttachmentSchemaStatus | None | Unset):
        storage_id (None | Unset | UUID):
        storage_method (None | str | Unset):
        upload_credentials (AttachmentSchemaUploadCredentialsType0 | None | Unset):
        upload_headers (AttachmentSchemaUploadHeadersType0 | None | Unset):
        upload_method (None | str | Unset):
        upload_url (None | str | Unset):
        url (None | str | Unset):
    """

    asset_id: None | Unset | UUID = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    filename: None | str | Unset = UNSET
    format_: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    segment_id: None | Unset | UUID = UNSET
    size: int | None | Unset = UNSET
    status: AttachmentSchemaStatus | None | Unset = UNSET
    storage_id: None | Unset | UUID = UNSET
    storage_method: None | str | Unset = UNSET
    upload_credentials: AttachmentSchemaUploadCredentialsType0 | None | Unset = UNSET
    upload_headers: AttachmentSchemaUploadHeadersType0 | None | Unset = UNSET
    upload_method: None | str | Unset = UNSET
    upload_url: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.attachment_schema_upload_credentials_type_0 import (
            AttachmentSchemaUploadCredentialsType0,
        )
        from ..models.attachment_schema_upload_headers_type_0 import (
            AttachmentSchemaUploadHeadersType0,
        )

        asset_id: None | str | Unset
        if isinstance(self.asset_id, Unset):
            asset_id = UNSET
        elif isinstance(self.asset_id, UUID):
            asset_id = str(self.asset_id)
        else:
            asset_id = self.asset_id

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

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        segment_id: None | str | Unset
        if isinstance(self.segment_id, Unset):
            segment_id = UNSET
        elif isinstance(self.segment_id, UUID):
            segment_id = str(self.segment_id)
        else:
            segment_id = self.segment_id

        size: int | None | Unset
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, AttachmentSchemaStatus):
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

        storage_method: None | str | Unset
        if isinstance(self.storage_method, Unset):
            storage_method = UNSET
        else:
            storage_method = self.storage_method

        upload_credentials: dict[str, Any] | None | Unset
        if isinstance(self.upload_credentials, Unset):
            upload_credentials = UNSET
        elif isinstance(
            self.upload_credentials, AttachmentSchemaUploadCredentialsType0
        ):
            upload_credentials = self.upload_credentials.to_dict()
        else:
            upload_credentials = self.upload_credentials

        upload_headers: dict[str, Any] | None | Unset
        if isinstance(self.upload_headers, Unset):
            upload_headers = UNSET
        elif isinstance(self.upload_headers, AttachmentSchemaUploadHeadersType0):
            upload_headers = self.upload_headers.to_dict()
        else:
            upload_headers = self.upload_headers

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asset_id is not UNSET:
            field_dict["asset_id"] = asset_id
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
        if name is not UNSET:
            field_dict["name"] = name
        if segment_id is not UNSET:
            field_dict["segment_id"] = segment_id
        if size is not UNSET:
            field_dict["size"] = size
        if status is not UNSET:
            field_dict["status"] = status
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if storage_method is not UNSET:
            field_dict["storage_method"] = storage_method
        if upload_credentials is not UNSET:
            field_dict["upload_credentials"] = upload_credentials
        if upload_headers is not UNSET:
            field_dict["upload_headers"] = upload_headers
        if upload_method is not UNSET:
            field_dict["upload_method"] = upload_method
        if upload_url is not UNSET:
            field_dict["upload_url"] = upload_url
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attachment_schema_upload_credentials_type_0 import (
            AttachmentSchemaUploadCredentialsType0,
        )
        from ..models.attachment_schema_upload_headers_type_0 import (
            AttachmentSchemaUploadHeadersType0,
        )

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

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_segment_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                segment_id_type_0 = UUID(data)

                return segment_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        segment_id = _parse_segment_id(d.pop("segment_id", UNSET))

        def _parse_size(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_status(data: object) -> AttachmentSchemaStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = AttachmentSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AttachmentSchemaStatus | None | Unset, data)

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

        def _parse_upload_credentials(
            data: object,
        ) -> AttachmentSchemaUploadCredentialsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upload_credentials_type_0 = (
                    AttachmentSchemaUploadCredentialsType0.from_dict(data)
                )

                return upload_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AttachmentSchemaUploadCredentialsType0 | None | Unset, data)

        upload_credentials = _parse_upload_credentials(
            d.pop("upload_credentials", UNSET)
        )

        def _parse_upload_headers(
            data: object,
        ) -> AttachmentSchemaUploadHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upload_headers_type_0 = AttachmentSchemaUploadHeadersType0.from_dict(
                    data
                )

                return upload_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AttachmentSchemaUploadHeadersType0 | None | Unset, data)

        upload_headers = _parse_upload_headers(d.pop("upload_headers", UNSET))

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

        attachment_schema = cls(
            asset_id=asset_id,
            date_created=date_created,
            date_modified=date_modified,
            filename=filename,
            format_=format_,
            id=id,
            name=name,
            segment_id=segment_id,
            size=size,
            status=status,
            storage_id=storage_id,
            storage_method=storage_method,
            upload_credentials=upload_credentials,
            upload_headers=upload_headers,
            upload_method=upload_method,
            upload_url=upload_url,
            url=url,
        )

        attachment_schema.additional_properties = d
        return attachment_schema

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
