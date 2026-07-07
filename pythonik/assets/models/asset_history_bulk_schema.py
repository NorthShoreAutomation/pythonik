from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.asset_history_bulk_schema_operation_type import (
    AssetHistoryBulkSchemaOperationType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.asset_history_bulk_schema_assets_jobs_map import (
        AssetHistoryBulkSchemaAssetsJobsMap,
    )


T = TypeVar("T", bound="AssetHistoryBulkSchema")


@_attrs_define
class AssetHistoryBulkSchema:
    """
    Attributes:
        asset_ids (list[UUID]):
        operation_type (AssetHistoryBulkSchemaOperationType):
        assets_jobs_map (AssetHistoryBulkSchemaAssetsJobsMap | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        id (UUID | Unset):
        job_id (None | Unset | UUID):
        operation_description (None | str | Unset):
        share_id (None | Unset | UUID):
        share_user_id (None | Unset | UUID):
        system_domain_id (UUID | Unset):
        user_id (UUID | Unset):
        version_id (UUID | Unset):
    """

    asset_ids: list[UUID]
    operation_type: AssetHistoryBulkSchemaOperationType
    assets_jobs_map: AssetHistoryBulkSchemaAssetsJobsMap | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    id: UUID | Unset = UNSET
    job_id: None | Unset | UUID = UNSET
    operation_description: None | str | Unset = UNSET
    share_id: None | Unset | UUID = UNSET
    share_user_id: None | Unset | UUID = UNSET
    system_domain_id: UUID | Unset = UNSET
    user_id: UUID | Unset = UNSET
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_ids = []
        for asset_ids_item_data in self.asset_ids:
            asset_ids_item = str(asset_ids_item_data)
            asset_ids.append(asset_ids_item)

        operation_type = self.operation_type.value

        assets_jobs_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.assets_jobs_map, Unset):
            assets_jobs_map = self.assets_jobs_map.to_dict()

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        job_id: None | str | Unset
        if isinstance(self.job_id, Unset):
            job_id = UNSET
        elif isinstance(self.job_id, UUID):
            job_id = str(self.job_id)
        else:
            job_id = self.job_id

        operation_description: None | str | Unset
        if isinstance(self.operation_description, Unset):
            operation_description = UNSET
        else:
            operation_description = self.operation_description

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

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        user_id: str | Unset = UNSET
        if not isinstance(self.user_id, Unset):
            user_id = str(self.user_id)

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_ids": asset_ids,
                "operation_type": operation_type,
            }
        )
        if assets_jobs_map is not UNSET:
            field_dict["assets_jobs_map"] = assets_jobs_map
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if id is not UNSET:
            field_dict["id"] = id
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if operation_description is not UNSET:
            field_dict["operation_description"] = operation_description
        if share_id is not UNSET:
            field_dict["share_id"] = share_id
        if share_user_id is not UNSET:
            field_dict["share_user_id"] = share_user_id
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_history_bulk_schema_assets_jobs_map import (
            AssetHistoryBulkSchemaAssetsJobsMap,
        )

        d = dict(src_dict)
        asset_ids = []
        _asset_ids = d.pop("asset_ids")
        for asset_ids_item_data in _asset_ids:
            asset_ids_item = UUID(asset_ids_item_data)

            asset_ids.append(asset_ids_item)

        operation_type = AssetHistoryBulkSchemaOperationType(d.pop("operation_type"))

        _assets_jobs_map = d.pop("assets_jobs_map", UNSET)
        assets_jobs_map: AssetHistoryBulkSchemaAssetsJobsMap | Unset
        if isinstance(_assets_jobs_map, Unset):
            assets_jobs_map = UNSET
        else:
            assets_jobs_map = AssetHistoryBulkSchemaAssetsJobsMap.from_dict(
                _assets_jobs_map
            )

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

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        def _parse_job_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                job_id_type_0 = UUID(data)

                return job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        job_id = _parse_job_id(d.pop("job_id", UNSET))

        def _parse_operation_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operation_description = _parse_operation_description(
            d.pop("operation_description", UNSET)
        )

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

        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id, Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)

        asset_history_bulk_schema = cls(
            asset_ids=asset_ids,
            operation_type=operation_type,
            assets_jobs_map=assets_jobs_map,
            date_created=date_created,
            date_modified=date_modified,
            id=id,
            job_id=job_id,
            operation_description=operation_description,
            share_id=share_id,
            share_user_id=share_user_id,
            system_domain_id=system_domain_id,
            user_id=user_id,
            version_id=version_id,
        )

        asset_history_bulk_schema.additional_properties = d
        return asset_history_bulk_schema

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
