from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.device_token_schema_platform import DeviceTokenSchemaPlatform
from ..models.device_token_schema_push_service import DeviceTokenSchemaPushService
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceTokenSchema")


@_attrs_define
class DeviceTokenSchema:
    """
    Attributes:
        device_token (str):
        platform (DeviceTokenSchemaPlatform):
        app_bundle_id (str | Unset):
        app_version (str | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        device_name (str | Unset):
        failed_count (int | Unset):
        is_active (bool | Unset):
        last_failed_at (datetime.datetime | Unset):
        last_used_at (datetime.datetime | Unset):
        push_service (DeviceTokenSchemaPushService | Unset):
        system_domain_id (UUID | Unset):
        user_id (UUID | Unset):
    """

    device_token: str
    platform: DeviceTokenSchemaPlatform
    app_bundle_id: str | Unset = UNSET
    app_version: str | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    device_name: str | Unset = UNSET
    failed_count: int | Unset = UNSET
    is_active: bool | Unset = UNSET
    last_failed_at: datetime.datetime | Unset = UNSET
    last_used_at: datetime.datetime | Unset = UNSET
    push_service: DeviceTokenSchemaPushService | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    user_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_token = self.device_token

        platform = self.platform.value

        app_bundle_id = self.app_bundle_id

        app_version = self.app_version

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        device_name = self.device_name

        failed_count = self.failed_count

        is_active = self.is_active

        last_failed_at: str | Unset = UNSET
        if not isinstance(self.last_failed_at, Unset):
            last_failed_at = self.last_failed_at.isoformat()

        last_used_at: str | Unset = UNSET
        if not isinstance(self.last_used_at, Unset):
            last_used_at = self.last_used_at.isoformat()

        push_service: str | Unset = UNSET
        if not isinstance(self.push_service, Unset):
            push_service = self.push_service.value

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
                "device_token": device_token,
                "platform": platform,
            }
        )
        if app_bundle_id is not UNSET:
            field_dict["app_bundle_id"] = app_bundle_id
        if app_version is not UNSET:
            field_dict["app_version"] = app_version
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if device_name is not UNSET:
            field_dict["device_name"] = device_name
        if failed_count is not UNSET:
            field_dict["failed_count"] = failed_count
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if last_failed_at is not UNSET:
            field_dict["last_failed_at"] = last_failed_at
        if last_used_at is not UNSET:
            field_dict["last_used_at"] = last_used_at
        if push_service is not UNSET:
            field_dict["push_service"] = push_service
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        device_token = d.pop("device_token")

        platform = DeviceTokenSchemaPlatform(d.pop("platform"))

        app_bundle_id = d.pop("app_bundle_id", UNSET)

        app_version = d.pop("app_version", UNSET)

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

        device_name = d.pop("device_name", UNSET)

        failed_count = d.pop("failed_count", UNSET)

        is_active = d.pop("is_active", UNSET)

        _last_failed_at = d.pop("last_failed_at", UNSET)
        last_failed_at: datetime.datetime | Unset
        if isinstance(_last_failed_at, Unset):
            last_failed_at = UNSET
        else:
            last_failed_at = datetime.datetime.fromisoformat(_last_failed_at)

        _last_used_at = d.pop("last_used_at", UNSET)
        last_used_at: datetime.datetime | Unset
        if isinstance(_last_used_at, Unset):
            last_used_at = UNSET
        else:
            last_used_at = datetime.datetime.fromisoformat(_last_used_at)

        _push_service = d.pop("push_service", UNSET)
        push_service: DeviceTokenSchemaPushService | Unset
        if isinstance(_push_service, Unset):
            push_service = UNSET
        else:
            push_service = DeviceTokenSchemaPushService(_push_service)

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

        device_token_schema = cls(
            device_token=device_token,
            platform=platform,
            app_bundle_id=app_bundle_id,
            app_version=app_version,
            date_created=date_created,
            date_modified=date_modified,
            device_name=device_name,
            failed_count=failed_count,
            is_active=is_active,
            last_failed_at=last_failed_at,
            last_used_at=last_used_at,
            push_service=push_service,
            system_domain_id=system_domain_id,
            user_id=user_id,
        )

        device_token_schema.additional_properties = d
        return device_token_schema

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
