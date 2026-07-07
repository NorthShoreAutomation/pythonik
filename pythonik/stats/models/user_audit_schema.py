from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_audit_schema_operation_type import UserAuditSchemaOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserAuditSchema")


@_attrs_define
class UserAuditSchema:
    """
    Attributes:
        operation_type (UserAuditSchemaOperationType):
        system_name (str):
        app_id (UUID | Unset):
        client_ip (str | Unset):
        date (datetime.date | Unset):
        id (UUID | Unset):
        is_acting_as_user (bool | Unset):
        metadata (str | Unset):
        operation_result (int | Unset):
        original_user_id (UUID | Unset):
        payload (str | Unset):
        request_id (str | Unset):
        resource (str | Unset):
        share_id (UUID | Unset):
        share_user_id (UUID | Unset):
        sudo (bool | Unset):
        system_domain_id (UUID | Unset):
        time (datetime.datetime | Unset):
        user_agent (str | Unset):
        user_id (UUID | Unset):
    """

    operation_type: UserAuditSchemaOperationType
    system_name: str
    app_id: UUID | Unset = UNSET
    client_ip: str | Unset = UNSET
    date: datetime.date | Unset = UNSET
    id: UUID | Unset = UNSET
    is_acting_as_user: bool | Unset = UNSET
    metadata: str | Unset = UNSET
    operation_result: int | Unset = UNSET
    original_user_id: UUID | Unset = UNSET
    payload: str | Unset = UNSET
    request_id: str | Unset = UNSET
    resource: str | Unset = UNSET
    share_id: UUID | Unset = UNSET
    share_user_id: UUID | Unset = UNSET
    sudo: bool | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    user_agent: str | Unset = UNSET
    user_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation_type = self.operation_type.value

        system_name = self.system_name

        app_id: str | Unset = UNSET
        if not isinstance(self.app_id, Unset):
            app_id = str(self.app_id)

        client_ip = self.client_ip

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        is_acting_as_user = self.is_acting_as_user

        metadata = self.metadata

        operation_result = self.operation_result

        original_user_id: str | Unset = UNSET
        if not isinstance(self.original_user_id, Unset):
            original_user_id = str(self.original_user_id)

        payload = self.payload

        request_id = self.request_id

        resource = self.resource

        share_id: str | Unset = UNSET
        if not isinstance(self.share_id, Unset):
            share_id = str(self.share_id)

        share_user_id: str | Unset = UNSET
        if not isinstance(self.share_user_id, Unset):
            share_user_id = str(self.share_user_id)

        sudo = self.sudo

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        user_agent = self.user_agent

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "operation_type": operation_type,
                "system_name": system_name,
            }
        )
        if app_id is not UNSET:
            field_dict["app_id"] = app_id
        if client_ip is not UNSET:
            field_dict["client_ip"] = client_ip
        if date is not UNSET:
            field_dict["date"] = date
        if id is not UNSET:
            field_dict["id"] = id
        if is_acting_as_user is not UNSET:
            field_dict["is_acting_as_user"] = is_acting_as_user
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if operation_result is not UNSET:
            field_dict["operation_result"] = operation_result
        if original_user_id is not UNSET:
            field_dict["original_user_id"] = original_user_id
        if payload is not UNSET:
            field_dict["payload"] = payload
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if resource is not UNSET:
            field_dict["resource"] = resource
        if share_id is not UNSET:
            field_dict["share_id"] = share_id
        if share_user_id is not UNSET:
            field_dict["share_user_id"] = share_user_id
        if sudo is not UNSET:
            field_dict["sudo"] = sudo
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if time is not UNSET:
            field_dict["time"] = time
        if user_agent is not UNSET:
            field_dict["user_agent"] = user_agent
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        operation_type = UserAuditSchemaOperationType(d.pop("operation_type"))

        system_name = d.pop("system_name")

        _app_id = d.pop("app_id", UNSET)
        app_id: UUID | Unset
        if isinstance(_app_id, Unset):
            app_id = UNSET
        else:
            app_id = UUID(_app_id)

        client_ip = d.pop("client_ip", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        is_acting_as_user = d.pop("is_acting_as_user", UNSET)

        metadata = d.pop("metadata", UNSET)

        operation_result = d.pop("operation_result", UNSET)

        _original_user_id = d.pop("original_user_id", UNSET)
        original_user_id: UUID | Unset
        if isinstance(_original_user_id, Unset):
            original_user_id = UNSET
        else:
            original_user_id = UUID(_original_user_id)

        payload = d.pop("payload", UNSET)

        request_id = d.pop("request_id", UNSET)

        resource = d.pop("resource", UNSET)

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

        sudo = d.pop("sudo", UNSET)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        _time = d.pop("time", UNSET)
        time: datetime.datetime | Unset
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = datetime.datetime.fromisoformat(_time)

        user_agent = d.pop("user_agent", UNSET)

        _user_id = d.pop("user_id", UNSET)
        user_id: UUID | Unset
        if isinstance(_user_id, Unset):
            user_id = UNSET
        else:
            user_id = UUID(_user_id)

        user_audit_schema = cls(
            operation_type=operation_type,
            system_name=system_name,
            app_id=app_id,
            client_ip=client_ip,
            date=date,
            id=id,
            is_acting_as_user=is_acting_as_user,
            metadata=metadata,
            operation_result=operation_result,
            original_user_id=original_user_id,
            payload=payload,
            request_id=request_id,
            resource=resource,
            share_id=share_id,
            share_user_id=share_user_id,
            sudo=sudo,
            system_domain_id=system_domain_id,
            time=time,
            user_agent=user_agent,
            user_id=user_id,
        )

        user_audit_schema.additional_properties = d
        return user_audit_schema

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
