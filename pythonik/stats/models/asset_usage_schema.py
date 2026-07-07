from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_usage_schema_asset_type import AssetUsageSchemaAssetType
from ..models.asset_usage_schema_operation_source import AssetUsageSchemaOperationSource
from ..models.asset_usage_schema_operation_type import AssetUsageSchemaOperationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetUsageSchema")


@_attrs_define
class AssetUsageSchema:
    """
    Attributes:
        asset_id (UUID):
        operation_type (AssetUsageSchemaOperationType):
        system_name (str):
        user_id (UUID):
        asset_type (AssetUsageSchemaAssetType | Unset):
        date (datetime.date | Unset):
        id (UUID | Unset):
        metadata (str | Unset):
        operation_source (AssetUsageSchemaOperationSource | Unset):
        system_domain_id (UUID | Unset):
        time (datetime.datetime | Unset):
    """

    asset_id: UUID
    operation_type: AssetUsageSchemaOperationType
    system_name: str
    user_id: UUID
    asset_type: AssetUsageSchemaAssetType | Unset = UNSET
    date: datetime.date | Unset = UNSET
    id: UUID | Unset = UNSET
    metadata: str | Unset = UNSET
    operation_source: AssetUsageSchemaOperationSource | Unset = UNSET
    system_domain_id: UUID | Unset = UNSET
    time: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        operation_type = self.operation_type.value

        system_name = self.system_name

        user_id = str(self.user_id)

        asset_type: str | Unset = UNSET
        if not isinstance(self.asset_type, Unset):
            asset_type = self.asset_type.value

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        metadata = self.metadata

        operation_source: str | Unset = UNSET
        if not isinstance(self.operation_source, Unset):
            operation_source = self.operation_source.value

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        time: str | Unset = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "operation_type": operation_type,
                "system_name": system_name,
                "user_id": user_id,
            }
        )
        if asset_type is not UNSET:
            field_dict["asset_type"] = asset_type
        if date is not UNSET:
            field_dict["date"] = date
        if id is not UNSET:
            field_dict["id"] = id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if operation_source is not UNSET:
            field_dict["operation_source"] = operation_source
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        operation_type = AssetUsageSchemaOperationType(d.pop("operation_type"))

        system_name = d.pop("system_name")

        user_id = UUID(d.pop("user_id"))

        _asset_type = d.pop("asset_type", UNSET)
        asset_type: AssetUsageSchemaAssetType | Unset
        if isinstance(_asset_type, Unset):
            asset_type = UNSET
        else:
            asset_type = AssetUsageSchemaAssetType(_asset_type)

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

        metadata = d.pop("metadata", UNSET)

        _operation_source = d.pop("operation_source", UNSET)
        operation_source: AssetUsageSchemaOperationSource | Unset
        if isinstance(_operation_source, Unset):
            operation_source = UNSET
        else:
            operation_source = AssetUsageSchemaOperationSource(_operation_source)

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

        asset_usage_schema = cls(
            asset_id=asset_id,
            operation_type=operation_type,
            system_name=system_name,
            user_id=user_id,
            asset_type=asset_type,
            date=date,
            id=id,
            metadata=metadata,
            operation_source=operation_source,
            system_domain_id=system_domain_id,
            time=time,
        )

        asset_usage_schema.additional_properties = d
        return asset_usage_schema

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
