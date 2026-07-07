from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_schema_status import NotificationSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_schema_context import NotificationSchemaContext


T = TypeVar("T", bound="NotificationSchema")


@_attrs_define
class NotificationSchema:
    """
    Attributes:
        event_type (str):
        message_long (str):
        message_short (str):
        object_id (UUID):
        object_type (str):
        recipient_id (UUID):
        sender_id (UUID):
        context (NotificationSchemaContext | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        exclude_users (list[UUID] | None | Unset):
        id (UUID | Unset):
        share_id (UUID | Unset):
        share_user_id (UUID | Unset):
        status (NotificationSchemaStatus | Unset):
        sub_object_id (UUID | Unset):
        sub_object_type (str | Unset):
        system_domain_id (UUID | Unset):
        user_id (UUID | Unset):
    """

    event_type: str
    message_long: str
    message_short: str
    object_id: UUID
    object_type: str
    recipient_id: UUID
    sender_id: UUID
    context: NotificationSchemaContext | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    exclude_users: list[UUID] | None | Unset = UNSET
    id: UUID | Unset = UNSET
    share_id: UUID | Unset = UNSET
    share_user_id: UUID | Unset = UNSET
    status: NotificationSchemaStatus | Unset = UNSET
    sub_object_id: UUID | Unset = UNSET
    sub_object_type: str | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    user_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type

        message_long = self.message_long

        message_short = self.message_short

        object_id = str(self.object_id)

        object_type = self.object_type

        recipient_id = str(self.recipient_id)

        sender_id = str(self.sender_id)

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

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

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        share_id: str | Unset = UNSET
        if not isinstance(self.share_id, Unset):
            share_id = str(self.share_id)

        share_user_id: str | Unset = UNSET
        if not isinstance(self.share_user_id, Unset):
            share_user_id = str(self.share_user_id)

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        sub_object_id: str | Unset = UNSET
        if not isinstance(self.sub_object_id, Unset):
            sub_object_id = str(self.sub_object_id)

        sub_object_type = self.sub_object_type

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "event_type": event_type,
                "message_long": message_long,
                "message_short": message_short,
                "object_id": object_id,
                "object_type": object_type,
                "recipient_id": recipient_id,
                "sender_id": sender_id,
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
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_schema_context import NotificationSchemaContext

        d = dict(src_dict)
        event_type = d.pop("event_type")

        message_long = d.pop("message_long")

        message_short = d.pop("message_short")

        object_id = UUID(d.pop("object_id"))

        object_type = d.pop("object_type")

        recipient_id = UUID(d.pop("recipient_id"))

        sender_id = UUID(d.pop("sender_id"))

        _context = d.pop("context", UNSET)
        context: NotificationSchemaContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = NotificationSchemaContext.from_dict(_context)

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

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _share_id = d.pop("share_id", UNSET)
        share_id: UUID | Unset
        if isinstance(_share_id, Unset):
            share_id = UNSET
        else:
            share_id = UUID(_share_id)

        _share_user_id = d.pop("share_user_id", UNSET)
        share_user_id: UUID | Unset
        if isinstance(_share_user_id, Unset):
            share_user_id = UNSET
        else:
            share_user_id = UUID(_share_user_id)

        _status = d.pop("status", UNSET)
        status: NotificationSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = NotificationSchemaStatus(_status)

        _sub_object_id = d.pop("sub_object_id", UNSET)
        sub_object_id: UUID | Unset
        if isinstance(_sub_object_id, Unset):
            sub_object_id = UNSET
        else:
            sub_object_id = UUID(_sub_object_id)

        sub_object_type = d.pop("sub_object_type", UNSET)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        notification_schema = cls(
            event_type=event_type,
            message_long=message_long,
            message_short=message_short,
            object_id=object_id,
            object_type=object_type,
            recipient_id=recipient_id,
            sender_id=sender_id,
            context=context,
            date_created=date_created,
            date_modified=date_modified,
            exclude_users=exclude_users,
            id=id,
            share_id=share_id,
            share_user_id=share_user_id,
            status=status,
            sub_object_id=sub_object_id,
            sub_object_type=sub_object_type,
            system_domain_id=system_domain_id,
            user_id=user_id,
        )

        notification_schema.additional_properties = d
        return notification_schema

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
