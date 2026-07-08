from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageUsagesElasticSchema")


@_attrs_define
class StorageUsagesElasticSchema:
    """
    Attributes:
        bucket_name (None | str | Unset):
        bytes_stored (int | None | Unset):
        date (None | str | Unset):
        id (None | Unset | UUID):
        system_domain_id (None | Unset | UUID):
    """

    bucket_name: None | str | Unset = UNSET
    bytes_stored: int | None | Unset = UNSET
    date: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bucket_name: None | str | Unset
        if isinstance(self.bucket_name, Unset):
            bucket_name = UNSET
        else:
            bucket_name = self.bucket_name

        bytes_stored: int | None | Unset
        if isinstance(self.bytes_stored, Unset):
            bytes_stored = UNSET
        else:
            bytes_stored = self.bytes_stored

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        else:
            date = self.date

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        elif isinstance(self.id, UUID):
            id = str(self.id)
        else:
            id = self.id

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bucket_name is not UNSET:
            field_dict["bucket_name"] = bucket_name
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

        def _parse_bucket_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bucket_name = _parse_bucket_name(d.pop("bucket_name", UNSET))

        def _parse_bytes_stored(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bytes_stored = _parse_bytes_stored(d.pop("bytes_stored", UNSET))

        def _parse_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

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

        storage_usages_elastic_schema = cls(
            bucket_name=bucket_name,
            bytes_stored=bytes_stored,
            date=date,
            id=id,
            system_domain_id=system_domain_id,
        )

        storage_usages_elastic_schema.additional_properties = d
        return storage_usages_elastic_schema

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
