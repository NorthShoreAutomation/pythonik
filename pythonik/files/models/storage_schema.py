from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.storage_schema_method import StorageSchemaMethod
from ..models.storage_schema_purpose import StorageSchemaPurpose
from ..models.storage_schema_status import StorageSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_schema_settings import StorageSchemaSettings


T = TypeVar("T", bound="StorageSchema")


@_attrs_define
class StorageSchema:
    """
    Attributes:
        method (StorageSchemaMethod):
        name (str):
        purpose (StorageSchemaPurpose):
        settings (StorageSchemaSettings):
        default (bool | None | Unset):
        description (None | str | Unset):
        id (None | Unset | UUID):
        last_scanned (datetime.datetime | None | Unset):
        scanner_status (None | str | Unset):
        status (None | StorageSchemaStatus | Unset):
        status_message (None | str | Unset):
        version (None | str | Unset):
    """

    method: StorageSchemaMethod
    name: str
    purpose: StorageSchemaPurpose
    settings: StorageSchemaSettings
    default: bool | None | Unset = UNSET
    description: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    last_scanned: datetime.datetime | None | Unset = UNSET
    scanner_status: None | str | Unset = UNSET
    status: None | StorageSchemaStatus | Unset = UNSET
    status_message: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        name = self.name

        purpose = self.purpose.value

        settings = self.settings.to_dict()

        default: bool | None | Unset
        if isinstance(self.default, Unset):
            default = UNSET
        else:
            default = self.default

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        last_scanned: None | str | Unset
        if isinstance(self.last_scanned, Unset):
            last_scanned = UNSET
        elif isinstance(self.last_scanned, datetime.datetime):
            last_scanned = self.last_scanned.isoformat()
        else:
            last_scanned = self.last_scanned

        scanner_status: None | str | Unset
        if isinstance(self.scanner_status, Unset):
            scanner_status = UNSET
        else:
            scanner_status = self.scanner_status

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, StorageSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        status_message: None | str | Unset
        if isinstance(self.status_message, Unset):
            status_message = UNSET
        else:
            status_message = self.status_message

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "name": name,
                "purpose": purpose,
                "settings": settings,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if last_scanned is not UNSET:
            field_dict["last_scanned"] = last_scanned
        if scanner_status is not UNSET:
            field_dict["scanner_status"] = scanner_status
        if status is not UNSET:
            field_dict["status"] = status
        if status_message is not UNSET:
            field_dict["status_message"] = status_message
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_schema_settings import StorageSchemaSettings

        d = dict(src_dict)
        method = StorageSchemaMethod(d.pop("method"))

        name = d.pop("name")

        purpose = StorageSchemaPurpose(d.pop("purpose"))

        settings = StorageSchemaSettings.from_dict(d.pop("settings"))

        def _parse_default(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        default = _parse_default(d.pop("default", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

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

        def _parse_last_scanned(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_scanned_type_0 = datetime.datetime.fromisoformat(data)

                return last_scanned_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_scanned = _parse_last_scanned(d.pop("last_scanned", UNSET))

        def _parse_scanner_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        scanner_status = _parse_scanner_status(d.pop("scanner_status", UNSET))

        def _parse_status(data: object) -> None | StorageSchemaStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = StorageSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StorageSchemaStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_status_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_message = _parse_status_message(d.pop("status_message", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        storage_schema = cls(
            method=method,
            name=name,
            purpose=purpose,
            settings=settings,
            default=default,
            description=description,
            id=id,
            last_scanned=last_scanned,
            scanner_status=scanner_status,
            status=status,
            status_message=status_message,
            version=version,
        )

        storage_schema.additional_properties = d
        return storage_schema

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
