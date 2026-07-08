from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.system_notification_schema_status import SystemNotificationSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_notification_schema_context_type_0 import (
        SystemNotificationSchemaContextType0,
    )


T = TypeVar("T", bound="SystemNotificationSchema")


@_attrs_define
class SystemNotificationSchema:
    """
    Attributes:
        event_type (str):
        message_long (str):
        message_short (str):
        object_type (str):
        recipient_id (UUID):
        sender_id (UUID):
        system_domain_id (UUID):
        context (None | SystemNotificationSchemaContextType0 | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        exclude_users (list[UUID] | None | Unset):
        id (None | Unset | UUID):
        object_id (None | Unset | UUID):
        share_id (None | Unset | UUID):
        share_user_id (None | Unset | UUID):
        status (None | SystemNotificationSchemaStatus | Unset):
        sub_object_id (None | Unset | UUID):
        sub_object_type (None | str | Unset):
        user_id (None | Unset | UUID):
    """

    event_type: str
    message_long: str
    message_short: str
    object_type: str
    recipient_id: UUID
    sender_id: UUID
    system_domain_id: UUID
    context: None | SystemNotificationSchemaContextType0 | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    exclude_users: list[UUID] | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    object_id: None | Unset | UUID = UNSET
    share_id: None | Unset | UUID = UNSET
    share_user_id: None | Unset | UUID = UNSET
    status: None | SystemNotificationSchemaStatus | Unset = UNSET
    sub_object_id: None | Unset | UUID = UNSET
    sub_object_type: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.system_notification_schema_context_type_0 import (
            SystemNotificationSchemaContextType0,
        )

        event_type = self.event_type

        message_long = self.message_long

        message_short = self.message_short

        object_type = self.object_type

        recipient_id = str(self.recipient_id)

        sender_id = str(self.sender_id)

        system_domain_id = str(self.system_domain_id)

        context: dict[str, Any] | None | Unset
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, SystemNotificationSchemaContextType0):
            context = self.context.to_dict()
        else:
            context = self.context

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

        exclude_users: list[str] | None | Unset
        if isinstance(self.exclude_users, Unset):
            exclude_users = UNSET
        elif isinstance(self.exclude_users, list):
            exclude_users = []
            for exclude_users_type_0_item_data in self.exclude_users:
                exclude_users_type_0_item = str(exclude_users_type_0_item_data)
                exclude_users.append(exclude_users_type_0_item)

        else:
            exclude_users = self.exclude_users

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        object_id: None | str | Unset
        if isinstance(self.object_id, Unset):
            object_id = UNSET
        elif isinstance(self.object_id, UUID):
            object_id = str(self.object_id)
        else:
            object_id = self.object_id

        share_id: None | str | Unset
        if isinstance(self.share_id, Unset):
            share_id = UNSET
        elif isinstance(self.share_id, UUID):
            share_id = str(self.share_id)
        else:
            share_id = self.share_id

        share_user_id: None | str | Unset
        if isinstance(self.share_user_id, Unset):
            share_user_id = UNSET
        elif isinstance(self.share_user_id, UUID):
            share_user_id = str(self.share_user_id)
        else:
            share_user_id = self.share_user_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, SystemNotificationSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        sub_object_id: None | str | Unset
        if isinstance(self.sub_object_id, Unset):
            sub_object_id = UNSET
        elif isinstance(self.sub_object_id, UUID):
            sub_object_id = str(self.sub_object_id)
        else:
            sub_object_id = self.sub_object_id

        sub_object_type: None | str | Unset
        if isinstance(self.sub_object_type, Unset):
            sub_object_type = UNSET
        else:
            sub_object_type = self.sub_object_type

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
                "event_type": event_type,
                "message_long": message_long,
                "message_short": message_short,
                "object_type": object_type,
                "recipient_id": recipient_id,
                "sender_id": sender_id,
                "system_domain_id": system_domain_id,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if exclude_users is not UNSET:
            field_dict["exclude_users"] = exclude_users
        if id is not UNSET:
            field_dict["id"] = id
        if object_id is not UNSET:
            field_dict["object_id"] = object_id
        if share_id is not UNSET:
            field_dict["share_id"] = share_id
        if share_user_id is not UNSET:
            field_dict["share_user_id"] = share_user_id
        if status is not UNSET:
            field_dict["status"] = status
        if sub_object_id is not UNSET:
            field_dict["sub_object_id"] = sub_object_id
        if sub_object_type is not UNSET:
            field_dict["sub_object_type"] = sub_object_type
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.system_notification_schema_context_type_0 import (
            SystemNotificationSchemaContextType0,
        )

        d = dict(src_dict)
        event_type = d.pop("event_type")

        message_long = d.pop("message_long")

        message_short = d.pop("message_short")

        object_type = d.pop("object_type")

        recipient_id = UUID(d.pop("recipient_id"))

        sender_id = UUID(d.pop("sender_id"))

        system_domain_id = UUID(d.pop("system_domain_id"))

        def _parse_context(
            data: object,
        ) -> None | SystemNotificationSchemaContextType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = SystemNotificationSchemaContextType0.from_dict(data)

                return context_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemNotificationSchemaContextType0 | Unset, data)

        context = _parse_context(d.pop("context", UNSET))

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

        def _parse_exclude_users(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exclude_users_type_0 = []
                _exclude_users_type_0 = data
                for exclude_users_type_0_item_data in _exclude_users_type_0:
                    exclude_users_type_0_item = UUID(exclude_users_type_0_item_data)

                    exclude_users_type_0.append(exclude_users_type_0_item)

                return exclude_users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        exclude_users = _parse_exclude_users(d.pop("exclude_users", UNSET))

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

        def _parse_share_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                share_id_type_0 = UUID(data)

                return share_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        share_id = _parse_share_id(d.pop("share_id", UNSET))

        def _parse_share_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                share_user_id_type_0 = UUID(data)

                return share_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        share_user_id = _parse_share_user_id(d.pop("share_user_id", UNSET))

        def _parse_status(
            data: object,
        ) -> None | SystemNotificationSchemaStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = SystemNotificationSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SystemNotificationSchemaStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_sub_object_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sub_object_id_type_0 = UUID(data)

                return sub_object_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        sub_object_id = _parse_sub_object_id(d.pop("sub_object_id", UNSET))

        def _parse_sub_object_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sub_object_type = _parse_sub_object_type(d.pop("sub_object_type", UNSET))

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

        system_notification_schema = cls(
            event_type=event_type,
            message_long=message_long,
            message_short=message_short,
            object_type=object_type,
            recipient_id=recipient_id,
            sender_id=sender_id,
            system_domain_id=system_domain_id,
            context=context,
            date_created=date_created,
            date_modified=date_modified,
            exclude_users=exclude_users,
            id=id,
            object_id=object_id,
            share_id=share_id,
            share_user_id=share_user_id,
            status=status,
            sub_object_id=sub_object_id,
            sub_object_type=sub_object_type,
            user_id=user_id,
        )

        system_notification_schema.additional_properties = d
        return system_notification_schema

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
