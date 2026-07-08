from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.device_token_schema_platform import DeviceTokenSchemaPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_token_schema_push_service_type_1 import (
        DeviceTokenSchemaPushServiceType1,
    )


T = TypeVar("T", bound="DeviceTokenSchema")


@_attrs_define
class DeviceTokenSchema:
    """
    Attributes:
        device_token (str):
        platform (DeviceTokenSchemaPlatform):
        app_bundle_id (None | str | Unset):
        app_version (None | str | Unset):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        device_name (None | str | Unset):
        failed_count (int | None | Unset):
        is_active (bool | None | Unset):
        last_failed_at (datetime.datetime | None | Unset):
        last_used_at (datetime.datetime | None | Unset):
        push_service (DeviceTokenSchemaPushServiceType1 | None | Unset):
        system_domain_id (None | Unset | UUID):
        user_id (None | Unset | UUID):
    """

    device_token: str
    platform: DeviceTokenSchemaPlatform
    app_bundle_id: None | str | Unset = UNSET
    app_version: None | str | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    device_name: None | str | Unset = UNSET
    failed_count: int | None | Unset = UNSET
    is_active: bool | None | Unset = UNSET
    last_failed_at: datetime.datetime | None | Unset = UNSET
    last_used_at: datetime.datetime | None | Unset = UNSET
    push_service: DeviceTokenSchemaPushServiceType1 | None | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    user_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.device_token_schema_push_service_type_1 import (
            DeviceTokenSchemaPushServiceType1,
        )

        device_token = self.device_token

        platform = self.platform.value

        app_bundle_id: None | str | Unset
        if isinstance(self.app_bundle_id, Unset):
            app_bundle_id = UNSET
        else:
            app_bundle_id = self.app_bundle_id

        app_version: None | str | Unset
        if isinstance(self.app_version, Unset):
            app_version = UNSET
        else:
            app_version = self.app_version

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

        device_name: None | str | Unset
        if isinstance(self.device_name, Unset):
            device_name = UNSET
        else:
            device_name = self.device_name

        failed_count: int | None | Unset
        if isinstance(self.failed_count, Unset):
            failed_count = UNSET
        else:
            failed_count = self.failed_count

        is_active: bool | None | Unset
        if isinstance(self.is_active, Unset):
            is_active = UNSET
        else:
            is_active = self.is_active

        last_failed_at: None | str | Unset
        if isinstance(self.last_failed_at, Unset):
            last_failed_at = UNSET
        elif isinstance(self.last_failed_at, datetime.datetime):
            last_failed_at = self.last_failed_at.isoformat()
        else:
            last_failed_at = self.last_failed_at

        last_used_at: None | str | Unset
        if isinstance(self.last_used_at, Unset):
            last_used_at = UNSET
        elif isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        push_service: dict[str, Any] | None | Unset
        if isinstance(self.push_service, Unset):
            push_service = UNSET
        elif isinstance(self.push_service, DeviceTokenSchemaPushServiceType1):
            push_service = self.push_service.to_dict()
        else:
            push_service = self.push_service

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

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
        from ..models.device_token_schema_push_service_type_1 import (
            DeviceTokenSchemaPushServiceType1,
        )

        d = dict(src_dict)
        device_token = d.pop("device_token")

        platform = DeviceTokenSchemaPlatform(d.pop("platform"))

        def _parse_app_bundle_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_bundle_id = _parse_app_bundle_id(d.pop("app_bundle_id", UNSET))

        def _parse_app_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        app_version = _parse_app_version(d.pop("app_version", UNSET))

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

        def _parse_device_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        device_name = _parse_device_name(d.pop("device_name", UNSET))

        def _parse_failed_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        failed_count = _parse_failed_count(d.pop("failed_count", UNSET))

        def _parse_is_active(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_active = _parse_is_active(d.pop("is_active", UNSET))

        def _parse_last_failed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_failed_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_failed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_failed_at = _parse_last_failed_at(d.pop("last_failed_at", UNSET))

        def _parse_last_used_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at", UNSET))

        def _parse_push_service(
            data: object,
        ) -> DeviceTokenSchemaPushServiceType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                push_service_type_1 = DeviceTokenSchemaPushServiceType1.from_dict(data)

                return push_service_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeviceTokenSchemaPushServiceType1 | None | Unset, data)

        push_service = _parse_push_service(d.pop("push_service", UNSET))

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
