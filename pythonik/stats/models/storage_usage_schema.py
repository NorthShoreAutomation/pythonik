from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.storage_usage_schema_storage_type import StorageUsageSchemaStorageType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageUsageSchema")


@_attrs_define
class StorageUsageSchema:
    """
    Attributes:
        bucket_name (str):
        storage_type (StorageUsageSchemaStorageType):
        system_name (str):
        bytes_stored (int | Unset):
        date (datetime.datetime | Unset):
        id (UUID | Unset):
        system_domain_id (UUID | Unset):
    """

    bucket_name: str
    storage_type: StorageUsageSchemaStorageType
    system_name: str
    bytes_stored: int | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_name = self.bucket_name

        storage_type = self.storage_type.value

        system_name = self.system_name

        bytes_stored = self.bytes_stored

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bucket_name": bucket_name,
                "storage_type": storage_type,
                "system_name": system_name,
            }
        )
        if bytes_stored is not UNSET:
            field_dict["bytes_stored"] = bytes_stored
        if date is not UNSET:
            field_dict["date"] = date
        if id is not UNSET:
            field_dict["id"] = id
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket_name = d.pop("bucket_name")

        storage_type = StorageUsageSchemaStorageType(d.pop("storage_type"))

        system_name = d.pop("system_name")

        bytes_stored = d.pop("bytes_stored", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.datetime.fromisoformat(_date)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        storage_usage_schema = cls(
            bucket_name=bucket_name,
            storage_type=storage_type,
            system_name=system_name,
            bytes_stored=bytes_stored,
            date=date,
            id=id,
            system_domain_id=system_domain_id,
        )

        storage_usage_schema.additional_properties = d
        return storage_usage_schema

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
