from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_create_schema_status import WebhookCreateSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_create_schema_headers_type_0 import (
        WebhookCreateSchemaHeadersType0,
    )


T = TypeVar("T", bound="WebhookCreateSchema")


@_attrs_define
class WebhookCreateSchema:
    """
    Attributes:
        event_type (str): Type of events. Example assets, collections Example: assets.
        status (WebhookCreateSchemaStatus):  Example: ENABLED.
        url (str): URL you want to be called when notification is appeared Example: https://example.com/webhook_handler.
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        deleted_at (datetime.datetime | None | Unset):
        description (None | str | Unset):
        first_failed_at (datetime.datetime | None | Unset):
        headers (None | Unset | WebhookCreateSchemaHeadersType0): Define the key-value pairs your third party provider
            requires here Example: {'AUTH-TOKEN': 'XYZ', 'S3_BUCKET_NAME': 'iconik-examples', 'S3_REGION': 'eu-west-1',
            'SECRET': 'asdad'}.
        id (None | Unset | UUID):
        last_error (None | str | Unset):
        last_payload (None | str | Unset):
        name (None | str | Unset):
        object_id (None | Unset | UUID): ID of a particular object you want to subscribe on Example:
            d7a5a7e8-4247-11ee-b3d8-a683e79fffaf.
        operation (None | str | Unset): Operation of event. Example create, update, delete Example: update.
        query (None | str | Unset): Adding a query allows filtering out messages so webhooks will be called only if for
            messages that match this query. Example: data.is_archived=false AND data.size>0 (data.status="CLOSED" OR
            data.status="DELETED") AND data.external_id!=null.
        realm (None | str | Unset): Realm of event. Example entity, contents, acls, metadata Example: metadata.
    """

    event_type: str
    status: WebhookCreateSchemaStatus
    url: str
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    deleted_at: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    first_failed_at: datetime.datetime | None | Unset = UNSET
    headers: None | Unset | WebhookCreateSchemaHeadersType0 = UNSET
    id: None | Unset | UUID = UNSET
    last_error: None | str | Unset = UNSET
    last_payload: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    object_id: None | Unset | UUID = UNSET
    operation: None | str | Unset = UNSET
    query: None | str | Unset = UNSET
    realm: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_create_schema_headers_type_0 import (
            WebhookCreateSchemaHeadersType0,
        )

        event_type = self.event_type

        status = self.status.value

        url = self.url

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

        deleted_at: None | str | Unset
        if isinstance(self.deleted_at, Unset):
            deleted_at = UNSET
        elif isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        first_failed_at: None | str | Unset
        if isinstance(self.first_failed_at, Unset):
            first_failed_at = UNSET
        elif isinstance(self.first_failed_at, datetime.datetime):
            first_failed_at = self.first_failed_at.isoformat()
        else:
            first_failed_at = self.first_failed_at

        headers: dict[str, Any] | None | Unset
        if isinstance(self.headers, Unset):
            headers = UNSET
        elif isinstance(self.headers, WebhookCreateSchemaHeadersType0):
            headers = self.headers.to_dict()
        else:
            headers = self.headers

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        last_error: None | str | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        else:
            last_error = self.last_error

        last_payload: None | str | Unset
        if isinstance(self.last_payload, Unset):
            last_payload = UNSET
        else:
            last_payload = self.last_payload

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        object_id: None | str | Unset
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        elif isinstance(self.object_id, UUID):
            object_id = str(self.object_id)
        else:
            object_id = self.object_id

        operation: None | str | Unset
        if isinstance(self.operation, Unset):
            operation = UNSET
        else:
            operation = self.operation

        query: None | str | Unset
        if isinstance(self.query, Unset):
            query = UNSET
        else:
            query = self.query

        realm: None | str | Unset
        if isinstance(self.realm, Unset):
            realm = UNSET
        else:
            realm = self.realm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "status": status,
                "url": url,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if deleted_at is not UNSET:
            field_dict["deleted_at"] = deleted_at
        if description is not UNSET:
            field_dict["description"] = description
        if first_failed_at is not UNSET:
            field_dict["first_failed_at"] = first_failed_at
        if headers is not UNSET:
            field_dict["headers"] = headers
        if id is not UNSET:
            field_dict["id"] = id
        if last_error is not UNSET:
            field_dict["last_error"] = last_error
        if last_payload is not UNSET:
            field_dict["last_payload"] = last_payload
        if name is not UNSET:
            field_dict["name"] = name
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if operation is not UNSET:
            field_dict["operation"] = operation
        if query is not UNSET:
            field_dict["query"] = query
        if realm is not UNSET:
            field_dict["realm"] = realm

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_create_schema_headers_type_0 import (
            WebhookCreateSchemaHeadersType0,
        )

        d = dict(src_dict)
        event_type = d.pop("event_type")

        status = WebhookCreateSchemaStatus(d.pop("status"))

        url = d.pop("url")

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

        def _parse_deleted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = datetime.datetime.fromisoformat(data)

                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_first_failed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_failed_at_type_0 = datetime.datetime.fromisoformat(data)

                return first_failed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_failed_at = _parse_first_failed_at(d.pop("first_failed_at", UNSET))

        def _parse_headers(
            data: object,
        ) -> None | Unset | WebhookCreateSchemaHeadersType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                headers_type_0 = WebhookCreateSchemaHeadersType0.from_dict(data)

                return headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WebhookCreateSchemaHeadersType0, data)

        headers = _parse_headers(d.pop("headers", UNSET))

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

        def _parse_last_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_error = _parse_last_error(d.pop("last_error", UNSET))

        def _parse_last_payload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_payload = _parse_last_payload(d.pop("last_payload", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_object_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_id_type_0 = UUID(data)

                return object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        object_id = _parse_object_id(d.pop("object_id", UNSET))

        def _parse_operation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operation = _parse_operation(d.pop("operation", UNSET))

        def _parse_query(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        query = _parse_query(d.pop("query", UNSET))

        def _parse_realm(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        realm = _parse_realm(d.pop("realm", UNSET))

        webhook_create_schema = cls(
            event_type=event_type,
            status=status,
            url=url,
            date_created=date_created,
            date_modified=date_modified,
            deleted_at=deleted_at,
            description=description,
            first_failed_at=first_failed_at,
            headers=headers,
            id=id,
            last_error=last_error,
            last_payload=last_payload,
            name=name,
            object_id=object_id,
            operation=operation,
            query=query,
            realm=realm,
        )

        webhook_create_schema.additional_properties = d
        return webhook_create_schema

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
