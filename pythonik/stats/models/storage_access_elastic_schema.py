from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageAccessElasticSchema")


@_attrs_define
class StorageAccessElasticSchema:
    """
    Attributes:
        bucket_name (str | Unset):
        bytes_received (int | Unset):
        bytes_sent (int | Unset):
        date (str | Unset):
        id (UUID | Unset):
        operations (int | Unset):
        system_domain_id (UUID | Unset):
    """

    bucket_name: str | Unset = UNSET
    bytes_received: int | Unset = UNSET
    bytes_sent: int | Unset = UNSET
    date: str | Unset = UNSET
    id: UUID | Unset = UNSET
    operations: int | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_name = self.bucket_name

        bytes_received = self.bytes_received

        bytes_sent = self.bytes_sent

        date = self.date

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        operations = self.operations

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_name is not UNSET:
            field_dict["bucket_name"] = bucket_name
        if bytes_received is not UNSET:
            field_dict["bytes_received"] = bytes_received
        if bytes_sent is not UNSET:
            field_dict["bytes_sent"] = bytes_sent
        if date is not UNSET:
            field_dict["date"] = date
        if id is not UNSET:
            field_dict["id"] = id
        if operations is not UNSET:
            field_dict["operations"] = operations
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bucket_name = d.pop("bucket_name", UNSET)

        bytes_received = d.pop("bytes_received", UNSET)

        bytes_sent = d.pop("bytes_sent", UNSET)

        date = d.pop("date", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        operations = d.pop("operations", UNSET)

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        storage_access_elastic_schema = cls(
            bucket_name=bucket_name,
            bytes_received=bytes_received,
            bytes_sent=bytes_sent,
            date=date,
            id=id,
            operations=operations,
            system_domain_id=system_domain_id,
        )

        storage_access_elastic_schema.additional_properties = d
        return storage_access_elastic_schema

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
