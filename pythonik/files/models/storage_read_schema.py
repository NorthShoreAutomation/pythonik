from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.storage_read_schema_method import StorageReadSchemaMethod
from ..models.storage_read_schema_purpose import StorageReadSchemaPurpose
from ..models.storage_read_schema_status import StorageReadSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.storage_read_schema_settings import StorageReadSchemaSettings


T = TypeVar("T", bound="StorageReadSchema")


@_attrs_define
class StorageReadSchema:
    """
    Attributes:
        method (StorageReadSchemaMethod):
        name (str):
        purpose (StorageReadSchemaPurpose):
        settings (StorageReadSchemaSettings):
        default (bool | Unset):
        description (None | str | Unset):
        id (UUID | Unset):
        isg_version (str | Unset):
        last_scanned (datetime.datetime | None | Unset):
        scanner_status (None | str | Unset):
        status (StorageReadSchemaStatus | Unset):
        status_message (None | str | Unset):
        storage_gateway_cluster_id (UUID | Unset):
        storage_gateway_ids (list[UUID] | Unset):
        version (str | Unset):
    """

    method: StorageReadSchemaMethod
    name: str
    purpose: StorageReadSchemaPurpose
    settings: StorageReadSchemaSettings
    default: bool | Unset = UNSET
    description: None | str | Unset = UNSET
    id: UUID | Unset = UNSET
    isg_version: str | Unset = UNSET
    last_scanned: datetime.datetime | None | Unset = UNSET
    scanner_status: None | str | Unset = UNSET
    status: StorageReadSchemaStatus | Unset = UNSET
    status_message: None | str | Unset = UNSET
    storage_gateway_cluster_id: UUID | Unset = UNSET
    storage_gateway_ids: list[UUID] | Unset = UNSET
    version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        name = self.name

        purpose = self.purpose.value

        settings = self.settings.to_dict()

        default = self.default

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        isg_version = self.isg_version

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

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_message: None | str | Unset
        if isinstance(self.status_message, Unset):
            status_message = UNSET
        else:
            status_message = self.status_message

        storage_gateway_cluster_id: str | Unset = UNSET
        if not isinstance(self.storage_gateway_cluster_id, Unset):
            storage_gateway_cluster_id = str(self.storage_gateway_cluster_id)

        storage_gateway_ids: list[str] | Unset = UNSET
        if not isinstance(self.storage_gateway_ids, Unset):
            storage_gateway_ids = []
            for storage_gateway_ids_item_data in self.storage_gateway_ids:
                storage_gateway_ids_item = str(storage_gateway_ids_item_data)
                storage_gateway_ids.append(storage_gateway_ids_item)

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
        if isg_version is not UNSET:
            field_dict["isg_version"] = isg_version
        if last_scanned is not UNSET:
            field_dict["last_scanned"] = last_scanned
        if scanner_status is not UNSET:
            field_dict["scanner_status"] = scanner_status
        if status is not UNSET:
            field_dict["status"] = status
        if status_message is not UNSET:
            field_dict["status_message"] = status_message
        if storage_gateway_cluster_id is not UNSET:
            field_dict["storage_gateway_cluster_id"] = storage_gateway_cluster_id
        if storage_gateway_ids is not UNSET:
            field_dict["storage_gateway_ids"] = storage_gateway_ids
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_read_schema_settings import StorageReadSchemaSettings

        d = dict(src_dict)
        method = StorageReadSchemaMethod(d.pop("method"))

        name = d.pop("name")

        purpose = StorageReadSchemaPurpose(d.pop("purpose"))

        settings = StorageReadSchemaSettings.from_dict(d.pop("settings"))

        default = d.pop("default", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        isg_version = d.pop("isg_version", UNSET)

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

        _status = d.pop("status", UNSET)
        status: StorageReadSchemaStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StorageReadSchemaStatus(_status)

        def _parse_status_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_message = _parse_status_message(d.pop("status_message", UNSET))

        _storage_gateway_cluster_id = d.pop("storage_gateway_cluster_id", UNSET)
        storage_gateway_cluster_id: UUID | Unset
        if isinstance(_storage_gateway_cluster_id, Unset):
            storage_gateway_cluster_id = UNSET
        else:
            storage_gateway_cluster_id = UUID(_storage_gateway_cluster_id)

        _storage_gateway_ids = d.pop("storage_gateway_ids", UNSET)
        storage_gateway_ids: list[UUID] | Unset = UNSET
        if _storage_gateway_ids is not UNSET:
            storage_gateway_ids = []
            for storage_gateway_ids_item_data in _storage_gateway_ids:
                storage_gateway_ids_item = UUID(storage_gateway_ids_item_data)

                storage_gateway_ids.append(storage_gateway_ids_item)

        version = d.pop("version", UNSET)

        storage_read_schema = cls(
            method=method,
            name=name,
            purpose=purpose,
            settings=settings,
            default=default,
            description=description,
            id=id,
            isg_version=isg_version,
            last_scanned=last_scanned,
            scanner_status=scanner_status,
            status=status,
            status_message=status_message,
            storage_gateway_cluster_id=storage_gateway_cluster_id,
            storage_gateway_ids=storage_gateway_ids,
            version=version,
        )

        storage_read_schema.additional_properties = d
        return storage_read_schema

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
