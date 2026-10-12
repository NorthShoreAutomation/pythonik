from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.logo_create_schema_upload_credentials_type_0 import (
        LogoCreateSchemaUploadCredentialsType0,
    )
    from ..models.logo_create_schema_upload_headers_type_0 import (
        LogoCreateSchemaUploadHeadersType0,
    )


T = TypeVar("T", bound="LogoCreateSchema")


@_attrs_define
class LogoCreateSchema:
    """
    Attributes:
        name (str):
        content_type (None | str | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        filename (None | str | Unset):
        id (None | Unset | UUID):
        storage_id (None | Unset | UUID):
        storage_method (None | str | Unset):
        system_domain_id (None | Unset | UUID):
        upload_credentials (LogoCreateSchemaUploadCredentialsType0 | None | Unset):
        upload_headers (LogoCreateSchemaUploadHeadersType0 | None | Unset):
        upload_method (None | str | Unset):
        upload_url (None | str | Unset):
        url (None | str | Unset):
        user_id (None | Unset | UUID):
    """

    name: str
    content_type: None | str | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    filename: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    storage_id: None | Unset | UUID = UNSET
    storage_method: None | str | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    upload_credentials: LogoCreateSchemaUploadCredentialsType0 | None | Unset = UNSET
    upload_headers: LogoCreateSchemaUploadHeadersType0 | None | Unset = UNSET
    upload_method: None | str | Unset = UNSET
    upload_url: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.logo_create_schema_upload_credentials_type_0 import (
            LogoCreateSchemaUploadCredentialsType0,
        )
        from ..models.logo_create_schema_upload_headers_type_0 import (
            LogoCreateSchemaUploadHeadersType0,
        )

        name = self.name

        content_type: None | str | Unset
        if isinstance(self.content_type, Unset):
            content_type = UNSET
        else:
            content_type = self.content_type

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

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

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

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        upload_credentials: dict[str, Any] | None | Unset
        if isinstance(self.upload_credentials, Unset):
            upload_credentials = UNSET
        elif isinstance(
            self.upload_credentials, LogoCreateSchemaUploadCredentialsType0
        ):
            upload_credentials = self.upload_credentials.to_dict()
        else:
            upload_credentials = self.upload_credentials

        upload_headers: dict[str, Any] | None | Unset
        if isinstance(self.upload_headers, Unset):
            upload_headers = UNSET
        elif isinstance(self.upload_headers, LogoCreateSchemaUploadHeadersType0):
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

        user_id: None | str | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, UUID):
            user_id = str(self.user_id)
        else:
            user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if filename is not UNSET:
            field_dict["filename"] = filename
        if id is not UNSET:
            field_dict["id"] = id
        if storage_id is not UNSET:
            field_dict["storage_id"] = storage_id
        if storage_method is not UNSET:
            field_dict["storage_method"] = storage_method
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
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
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.logo_create_schema_upload_credentials_type_0 import (
            LogoCreateSchemaUploadCredentialsType0,
        )
        from ..models.logo_create_schema_upload_headers_type_0 import (
            LogoCreateSchemaUploadHeadersType0,
        )

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_content_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        content_type = _parse_content_type(d.pop("content_type", UNSET))

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

        def _parse_system_domain_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                system_domain_id_type_0 = UUID(data)

                return system_domain_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        system_domain_id = _parse_system_domain_id(d.pop("system_domain_id", UNSET))

        def _parse_upload_credentials(
            data: object,
        ) -> LogoCreateSchemaUploadCredentialsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upload_credentials_type_0 = (
                    LogoCreateSchemaUploadCredentialsType0.from_dict(data)
                )

                return upload_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogoCreateSchemaUploadCredentialsType0 | None | Unset, data)

        upload_credentials = _parse_upload_credentials(
            d.pop("upload_credentials", UNSET)
        )

        def _parse_upload_headers(
            data: object,
        ) -> LogoCreateSchemaUploadHeadersType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                upload_headers_type_0 = LogoCreateSchemaUploadHeadersType0.from_dict(
                    data
                )

                return upload_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LogoCreateSchemaUploadHeadersType0 | None | Unset, data)

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

        def _parse_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                user_id_type_0 = UUID(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        user_id = _parse_user_id(d.pop("user_id", UNSET))

        logo_create_schema = cls(
            name=name,
            content_type=content_type,
            date_created=date_created,
            date_modified=date_modified,
            filename=filename,
            id=id,
            storage_id=storage_id,
            storage_method=storage_method,
            system_domain_id=system_domain_id,
            upload_credentials=upload_credentials,
            upload_headers=upload_headers,
            upload_method=upload_method,
            upload_url=upload_url,
            url=url,
            user_id=user_id,
        )

        logo_create_schema.additional_properties = d
        return logo_create_schema

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
