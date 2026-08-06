from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
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
        asset_type (AssetUsageSchemaAssetType | None | Unset):
        date (datetime.date | None | Unset):
        id (None | Unset | UUID):
        metadata (None | str | Unset):
        operation_source (AssetUsageSchemaOperationSource | None | Unset):
        system_domain_id (None | Unset | UUID):
        time (datetime.datetime | None | Unset):
    """

    asset_id: UUID
    operation_type: AssetUsageSchemaOperationType
    system_name: str
    user_id: UUID
    asset_type: AssetUsageSchemaAssetType | None | Unset = UNSET
    date: datetime.date | None | Unset = UNSET
    id: None | Unset | UUID = UNSET
    metadata: None | str | Unset = UNSET
    operation_source: AssetUsageSchemaOperationSource | None | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    time: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        operation_type = self.operation_type.value

        system_name = self.system_name

        user_id = str(self.user_id)

        asset_type: None | str | Unset
        if isinstance(self.asset_type, Unset):
            asset_type = UNSET
        elif isinstance(self.asset_type, AssetUsageSchemaAssetType):
            asset_type = self.asset_type.value
        else:
            asset_type = self.asset_type

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

        metadata: None | str | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        else:
            metadata = self.metadata

        operation_source: None | str | Unset
        if isinstance(self.operation_source, Unset):
            operation_source = UNSET
        elif isinstance(self.operation_source, AssetUsageSchemaOperationSource):
            operation_source = self.operation_source.value
        else:
            operation_source = self.operation_source

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

        def _parse_asset_type(data: object) -> AssetUsageSchemaAssetType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                asset_type_type_1 = AssetUsageSchemaAssetType(data)

                return asset_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetUsageSchemaAssetType | None | Unset, data)

        asset_type = _parse_asset_type(d.pop("asset_type", UNSET))

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

        def _parse_metadata(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_operation_source(
            data: object,
        ) -> AssetUsageSchemaOperationSource | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operation_source_type_1 = AssetUsageSchemaOperationSource(data)

                return operation_source_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetUsageSchemaOperationSource | None | Unset, data)

        operation_source = _parse_operation_source(d.pop("operation_source", UNSET))

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
