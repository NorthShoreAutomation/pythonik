from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        app_id (None | Unset | UUID):
        client_ip (None | str | Unset):
        date (datetime.date | None | Unset):
        id (None | Unset | UUID):
        is_acting_as_user (bool | None | Unset):
        metadata (None | str | Unset):
        operation_result (int | None | Unset):
        original_user_id (None | Unset | UUID):
        payload (None | str | Unset):
        request_id (None | str | Unset):
        resource (None | str | Unset):
        share_id (None | Unset | UUID):
        share_user_id (None | Unset | UUID):
        sudo (bool | None | Unset):
        system_domain_id (None | Unset | UUID):
        time (datetime.datetime | None | Unset):
        user_agent (None | str | Unset):
        user_id (None | Unset | UUID):
    """

    operation_type: UserAuditSchemaOperationType
    system_name: str
    app_id: None | Unset | UUID = UNSET
    client_ip: None | str | Unset = UNSET
    date: datetime.date | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    is_acting_as_user: bool | None | Unset = UNSET
    metadata: None | str | Unset = UNSET
    operation_result: int | None | Unset = UNSET
    original_user_id: None | Unset | UUID = UNSET
    payload: None | str | Unset = UNSET
    request_id: None | str | Unset = UNSET
    resource: None | str | Unset = UNSET
    share_id: None | Unset | UUID = UNSET
    share_user_id: None | Unset | UUID = UNSET
    sudo: bool | None | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    time: datetime.datetime | None | Unset = UNSET
    user_agent: None | str | Unset = UNSET
    user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        operation_type = self.operation_type.value

        system_name = self.system_name

        app_id: None | str | Unset
        if isinstance(self.app_id, Unset):
            app_id = UNSET
        elif isinstance(self.app_id, UUID):
            app_id = str(self.app_id)
        else:
            app_id = self.app_id

        client_ip: None | str | Unset
        if isinstance(self.client_ip, Unset):
            client_ip = UNSET
        else:
            client_ip = self.client_ip

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        is_acting_as_user: bool | None | Unset
        if isinstance(self.is_acting_as_user, Unset):
            is_acting_as_user = UNSET
        else:
            is_acting_as_user = self.is_acting_as_user

        metadata: None | str | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        else:
            metadata = self.metadata

        operation_result: int | None | Unset
        if isinstance(self.operation_result, Unset):
            operation_result = UNSET
        else:
            operation_result = self.operation_result

        original_user_id: None | str | Unset
        if isinstance(self.original_user_id, Unset):
            original_user_id = UNSET
        elif isinstance(self.original_user_id, UUID):
            original_user_id = str(self.original_user_id)
        else:
            original_user_id = self.original_user_id

        payload: None | str | Unset
        if isinstance(self.payload, Unset):
            payload = UNSET
        else:
            payload = self.payload

        request_id: None | str | Unset
        if isinstance(self.request_id, Unset):
            request_id = UNSET
        else:
            request_id = self.request_id

        resource: None | str | Unset
        if isinstance(self.resource, Unset):
            resource = UNSET
        else:
            resource = self.resource

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

        sudo: bool | None | Unset
        if isinstance(self.sudo, Unset):
            sudo = UNSET
        else:
            sudo = self.sudo

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        time: None | str | Unset
        if isinstance(self.time, Unset):
            time = UNSET
        elif isinstance(self.time, datetime.datetime):
            time = self.time.isoformat()
        else:
            time = self.time

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

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

        def _parse_app_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                app_id_type_0 = UUID(data)

                return app_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        app_id = _parse_app_id(d.pop("app_id", UNSET))

        def _parse_client_ip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_ip = _parse_client_ip(d.pop("client_ip", UNSET))

        def _parse_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = datetime.date.fromisoformat(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

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

        def _parse_is_acting_as_user(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_acting_as_user = _parse_is_acting_as_user(d.pop("is_acting_as_user", UNSET))

        def _parse_metadata(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_operation_result(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        operation_result = _parse_operation_result(d.pop("operation_result", UNSET))

        def _parse_original_user_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_user_id_type_0 = UUID(data)

                return original_user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        original_user_id = _parse_original_user_id(d.pop("original_user_id", UNSET))

        def _parse_payload(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payload = _parse_payload(d.pop("payload", UNSET))

        def _parse_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_id = _parse_request_id(d.pop("request_id", UNSET))

        def _parse_resource(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource = _parse_resource(d.pop("resource", UNSET))

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

        def _parse_sudo(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        sudo = _parse_sudo(d.pop("sudo", UNSET))

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

        def _parse_time(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                time_type_0 = datetime.datetime.fromisoformat(data)

                return time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        time = _parse_time(d.pop("time", UNSET))

        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("user_agent", UNSET))

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
