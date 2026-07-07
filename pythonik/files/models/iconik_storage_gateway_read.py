from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.iconik_storage_gateway_read_roles_item import (
    IconikStorageGatewayReadRolesItem,
)
from ..models.iconik_storage_gateway_read_status import IconikStorageGatewayReadStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iconik_storage_gateway_read_storages import (
        IconikStorageGatewayReadStorages,
    )
    from ..models.iconik_storage_gateway_telemetry import IconikStorageGatewayTelemetry
    from ..models.isg_config_cluster_settings_schema import (
        ISGConfigClusterSettingsSchema,
    )
    from ..models.isg_config_settings_schema import ISGConfigSettingsSchema


T = TypeVar("T", bound="IconikStorageGatewayRead")


@_attrs_define
class IconikStorageGatewayRead:
    """
    Attributes:
        enabled (bool): Application toggle. If turned off ISG will enter idle state waiting to get enabled again.
        name (str):
        cluster_id (UUID | Unset):
        cluster_storage_ids (list[UUID] | Unset): Cluster storage IDs
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        dedicated_storage_ids (list[UUID] | Unset): Dedicated storage IDs
        description (str | Unset):
        id (UUID | Unset):
        merged_settings (ISGConfigClusterSettingsSchema | Unset):
        public_identity (str | Unset):
        roles (list[IconikStorageGatewayReadRolesItem] | Unset): Set of roles this gateway can perform when part of
            cluster
        settings (ISGConfigSettingsSchema | None | Unset): Application configuration settings as key-value pairs
        status (IconikStorageGatewayReadStatus | Unset):
        storage_addr (str | Unset): Server address for direct transfers between storage gateways
        storages (IconikStorageGatewayReadStorages | Unset): Storage mount points mapped by storage ID
        telemetry (IconikStorageGatewayTelemetry | Unset):
    """

    enabled: bool
    name: str
    cluster_id: UUID | Unset = UNSET
    cluster_storage_ids: list[UUID] | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    dedicated_storage_ids: list[UUID] | Unset = UNSET
    description: str | Unset = UNSET
    id: UUID | Unset = UNSET
    merged_settings: ISGConfigClusterSettingsSchema | Unset = UNSET
    public_identity: str | Unset = UNSET
    roles: list[IconikStorageGatewayReadRolesItem] | Unset = UNSET
    settings: ISGConfigSettingsSchema | None | Unset = UNSET
    status: IconikStorageGatewayReadStatus | Unset = UNSET
    storage_addr: str | Unset = UNSET
    storages: IconikStorageGatewayReadStorages | Unset = UNSET
    telemetry: IconikStorageGatewayTelemetry | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.isg_config_settings_schema import ISGConfigSettingsSchema

        enabled = self.enabled

        name = self.name

        cluster_id: str | Unset = UNSET
        if not isinstance(self.cluster_id, Unset):
            cluster_id = str(self.cluster_id)

        cluster_storage_ids: list[str] | Unset = UNSET
        if not isinstance(self.cluster_storage_ids, Unset):
            cluster_storage_ids = []
            for cluster_storage_ids_item_data in self.cluster_storage_ids:
                cluster_storage_ids_item = str(cluster_storage_ids_item_data)
                cluster_storage_ids.append(cluster_storage_ids_item)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        dedicated_storage_ids: list[str] | Unset = UNSET
        if not isinstance(self.dedicated_storage_ids, Unset):
            dedicated_storage_ids = []
            for dedicated_storage_ids_item_data in self.dedicated_storage_ids:
                dedicated_storage_ids_item = str(dedicated_storage_ids_item_data)
                dedicated_storage_ids.append(dedicated_storage_ids_item)

        description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        merged_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merged_settings, Unset):
            merged_settings = self.merged_settings.to_dict()

        public_identity = self.public_identity

        roles: list[str] | Unset = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.value
                roles.append(roles_item)

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, ISGConfigSettingsSchema):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        storage_addr = self.storage_addr

        storages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storages, Unset):
            storages = self.storages.to_dict()

        telemetry: dict[str, Any] | Unset = UNSET
        if not isinstance(self.telemetry, Unset):
            telemetry = self.telemetry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "name": name,
            }
        )
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if cluster_storage_ids is not UNSET:
            field_dict["cluster_storage_ids"] = cluster_storage_ids
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if dedicated_storage_ids is not UNSET:
            field_dict["dedicated_storage_ids"] = dedicated_storage_ids
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if merged_settings is not UNSET:
            field_dict["merged_settings"] = merged_settings
        if public_identity is not UNSET:
            field_dict["public_identity"] = public_identity
        if roles is not UNSET:
            field_dict["roles"] = roles
        if settings is not UNSET:
            field_dict["settings"] = settings
        if status is not UNSET:
            field_dict["status"] = status
        if storage_addr is not UNSET:
            field_dict["storage_addr"] = storage_addr
        if storages is not UNSET:
            field_dict["storages"] = storages
        if telemetry is not UNSET:
            field_dict["telemetry"] = telemetry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iconik_storage_gateway_read_storages import (
            IconikStorageGatewayReadStorages,
        )
        from ..models.iconik_storage_gateway_telemetry import (
            IconikStorageGatewayTelemetry,
        )
        from ..models.isg_config_cluster_settings_schema import (
            ISGConfigClusterSettingsSchema,
        )
        from ..models.isg_config_settings_schema import ISGConfigSettingsSchema

        d = dict(src_dict)
        enabled = d.pop("enabled")

        name = d.pop("name")

        _cluster_id = d.pop("cluster_id", UNSET)
        cluster_id: UUID | Unset
        if isinstance(_cluster_id, Unset):
            cluster_id = UNSET
        else:
            cluster_id = UUID(_cluster_id)

        _cluster_storage_ids = d.pop("cluster_storage_ids", UNSET)
        cluster_storage_ids: list[UUID] | Unset = UNSET
        if _cluster_storage_ids is not UNSET:
            cluster_storage_ids = []
            for cluster_storage_ids_item_data in _cluster_storage_ids:
                cluster_storage_ids_item = UUID(cluster_storage_ids_item_data)

                cluster_storage_ids.append(cluster_storage_ids_item)

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

        _dedicated_storage_ids = d.pop("dedicated_storage_ids", UNSET)
        dedicated_storage_ids: list[UUID] | Unset = UNSET
        if _dedicated_storage_ids is not UNSET:
            dedicated_storage_ids = []
            for dedicated_storage_ids_item_data in _dedicated_storage_ids:
                dedicated_storage_ids_item = UUID(dedicated_storage_ids_item_data)

                dedicated_storage_ids.append(dedicated_storage_ids_item)

        description = d.pop("description", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _merged_settings = d.pop("merged_settings", UNSET)
        merged_settings: ISGConfigClusterSettingsSchema | Unset
        if isinstance(_merged_settings, Unset):
            merged_settings = UNSET
        else:
            merged_settings = ISGConfigClusterSettingsSchema.from_dict(_merged_settings)

        public_identity = d.pop("public_identity", UNSET)

        _roles = d.pop("roles", UNSET)
        roles: list[IconikStorageGatewayReadRolesItem] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = IconikStorageGatewayReadRolesItem(roles_item_data)

                roles.append(roles_item)

        def _parse_settings(data: object) -> ISGConfigSettingsSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_1 = ISGConfigSettingsSchema.from_dict(data)

                return settings_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ISGConfigSettingsSchema | None | Unset, data)

        settings = _parse_settings(d.pop("settings", UNSET))

        _status = d.pop("status", UNSET)
        status: IconikStorageGatewayReadStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IconikStorageGatewayReadStatus(_status)

        storage_addr = d.pop("storage_addr", UNSET)

        _storages = d.pop("storages", UNSET)
        storages: IconikStorageGatewayReadStorages | Unset
        if isinstance(_storages, Unset):
            storages = UNSET
        else:
            storages = IconikStorageGatewayReadStorages.from_dict(_storages)

        _telemetry = d.pop("telemetry", UNSET)
        telemetry: IconikStorageGatewayTelemetry | Unset
        if isinstance(_telemetry, Unset):
            telemetry = UNSET
        else:
            telemetry = IconikStorageGatewayTelemetry.from_dict(_telemetry)

        iconik_storage_gateway_read = cls(
            enabled=enabled,
            name=name,
            cluster_id=cluster_id,
            cluster_storage_ids=cluster_storage_ids,
            date_created=date_created,
            date_modified=date_modified,
            dedicated_storage_ids=dedicated_storage_ids,
            description=description,
            id=id,
            merged_settings=merged_settings,
            public_identity=public_identity,
            roles=roles,
            settings=settings,
            status=status,
            storage_addr=storage_addr,
            storages=storages,
            telemetry=telemetry,
        )

        iconik_storage_gateway_read.additional_properties = d
        return iconik_storage_gateway_read

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
