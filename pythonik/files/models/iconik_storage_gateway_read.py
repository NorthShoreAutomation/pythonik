from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.iconik_storage_gateway_read_roles_type_0_item import (
    IconikStorageGatewayReadRolesType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iconik_storage_gateway_read_status_type_1 import (
        IconikStorageGatewayReadStatusType1,
    )
    from ..models.iconik_storage_gateway_read_storages_type_0 import (
        IconikStorageGatewayReadStoragesType0,
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
        cluster_id (None | Unset | UUID):
        cluster_storage_ids (list[UUID] | None | Unset): Cluster storage IDs
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        dedicated_storage_ids (list[UUID] | None | Unset): Dedicated storage IDs
        description (None | str | Unset):
        id (None | Unset | UUID):
        merged_settings (ISGConfigClusterSettingsSchema | None | Unset): Application configuration settings merged with
            cluster settings
        public_identity (None | str | Unset):
        roles (list[IconikStorageGatewayReadRolesType0Item] | None | Unset): Set of roles this gateway can perform when
            part of cluster
        settings (ISGConfigSettingsSchema | None | Unset): Application configuration settings as key-value pairs
        status (IconikStorageGatewayReadStatusType1 | None | Unset):
        storage_addr (None | str | Unset): Server address for direct transfers between storage gateways
        storages (IconikStorageGatewayReadStoragesType0 | None | Unset): Storage mount points mapped by storage ID
        telemetry (IconikStorageGatewayTelemetry | None | Unset):
    """

    enabled: bool
    name: str
    cluster_id: None | Unset | UUID = UNSET
    cluster_storage_ids: list[UUID] | None | Unset = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    dedicated_storage_ids: list[UUID] | None | Unset = UNSET
    description: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    merged_settings: ISGConfigClusterSettingsSchema | None | Unset = UNSET
    public_identity: None | str | Unset = UNSET
    roles: list[IconikStorageGatewayReadRolesType0Item] | None | Unset = UNSET
    settings: ISGConfigSettingsSchema | None | Unset = UNSET
    status: IconikStorageGatewayReadStatusType1 | None | Unset = UNSET
    storage_addr: None | str | Unset = UNSET
    storages: IconikStorageGatewayReadStoragesType0 | None | Unset = UNSET
    telemetry: IconikStorageGatewayTelemetry | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.iconik_storage_gateway_read_status_type_1 import (
            IconikStorageGatewayReadStatusType1,
        )
        from ..models.iconik_storage_gateway_read_storages_type_0 import (
            IconikStorageGatewayReadStoragesType0,
        )
        from ..models.iconik_storage_gateway_telemetry import (
            IconikStorageGatewayTelemetry,
        )
        from ..models.isg_config_cluster_settings_schema import (
            ISGConfigClusterSettingsSchema,
        )
        from ..models.isg_config_settings_schema import ISGConfigSettingsSchema

        enabled = self.enabled

        name = self.name

        cluster_id: None | str | Unset
        if isinstance(self.cluster_id, Unset):
            cluster_id = UNSET
        elif isinstance(self.cluster_id, UUID):
            cluster_id = str(self.cluster_id)
        else:
            cluster_id = self.cluster_id

        cluster_storage_ids: list[str] | None | Unset
        if isinstance(self.cluster_storage_ids, Unset):
            cluster_storage_ids = UNSET
        elif isinstance(self.cluster_storage_ids, list):
            cluster_storage_ids = []
            for cluster_storage_ids_type_0_item_data in self.cluster_storage_ids:
                cluster_storage_ids_type_0_item = str(
                    cluster_storage_ids_type_0_item_data
                )
                cluster_storage_ids.append(cluster_storage_ids_type_0_item)

        else:
            cluster_storage_ids = self.cluster_storage_ids

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

        dedicated_storage_ids: list[str] | None | Unset
        if isinstance(self.dedicated_storage_ids, Unset):
            dedicated_storage_ids = UNSET
        elif isinstance(self.dedicated_storage_ids, list):
            dedicated_storage_ids = []
            for dedicated_storage_ids_type_0_item_data in self.dedicated_storage_ids:
                dedicated_storage_ids_type_0_item = str(
                    dedicated_storage_ids_type_0_item_data
                )
                dedicated_storage_ids.append(dedicated_storage_ids_type_0_item)

        else:
            dedicated_storage_ids = self.dedicated_storage_ids

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

        merged_settings: dict[str, Any] | None | Unset
        if isinstance(self.merged_settings, Unset):
            merged_settings = UNSET
        elif isinstance(self.merged_settings, ISGConfigClusterSettingsSchema):
            merged_settings = self.merged_settings.to_dict()
        else:
            merged_settings = self.merged_settings

        public_identity: None | str | Unset
        if isinstance(self.public_identity, Unset):
            public_identity = UNSET
        else:
            public_identity = self.public_identity

        roles: list[str] | None | Unset
        if isinstance(self.roles, Unset):
            roles = UNSET
        elif isinstance(self.roles, list):
            roles = []
            for roles_type_0_item_data in self.roles:
                roles_type_0_item = roles_type_0_item_data.value
                roles.append(roles_type_0_item)

        else:
            roles = self.roles

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, ISGConfigSettingsSchema):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        status: dict[str, Any] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, IconikStorageGatewayReadStatusType1):
            status = self.status.to_dict()
        else:
            status = self.status

        storage_addr: None | str | Unset
        if isinstance(self.storage_addr, Unset):
            storage_addr = UNSET
        else:
            storage_addr = self.storage_addr

        storages: dict[str, Any] | None | Unset
        if isinstance(self.storages, Unset):
            storages = UNSET
        elif isinstance(self.storages, IconikStorageGatewayReadStoragesType0):
            storages = self.storages.to_dict()
        else:
            storages = self.storages

        telemetry: dict[str, Any] | None | Unset
        if isinstance(self.telemetry, Unset):
            telemetry = UNSET
        elif isinstance(self.telemetry, IconikStorageGatewayTelemetry):
            telemetry = self.telemetry.to_dict()
        else:
            telemetry = self.telemetry

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
        from ..models.iconik_storage_gateway_read_status_type_1 import (
            IconikStorageGatewayReadStatusType1,
        )
        from ..models.iconik_storage_gateway_read_storages_type_0 import (
            IconikStorageGatewayReadStoragesType0,
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

        def _parse_cluster_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cluster_id_type_0 = UUID(data)

                return cluster_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        cluster_id = _parse_cluster_id(d.pop("cluster_id", UNSET))

        def _parse_cluster_storage_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                cluster_storage_ids_type_0 = []
                _cluster_storage_ids_type_0 = data
                for cluster_storage_ids_type_0_item_data in _cluster_storage_ids_type_0:
                    cluster_storage_ids_type_0_item = UUID(
                        cluster_storage_ids_type_0_item_data
                    )

                    cluster_storage_ids_type_0.append(cluster_storage_ids_type_0_item)

                return cluster_storage_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        cluster_storage_ids = _parse_cluster_storage_ids(
            d.pop("cluster_storage_ids", UNSET)
        )

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

        def _parse_dedicated_storage_ids(data: object) -> list[UUID] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                dedicated_storage_ids_type_0 = []
                _dedicated_storage_ids_type_0 = data
                for (
                    dedicated_storage_ids_type_0_item_data
                ) in _dedicated_storage_ids_type_0:
                    dedicated_storage_ids_type_0_item = UUID(
                        dedicated_storage_ids_type_0_item_data
                    )

                    dedicated_storage_ids_type_0.append(
                        dedicated_storage_ids_type_0_item
                    )

                return dedicated_storage_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UUID] | None | Unset, data)

        dedicated_storage_ids = _parse_dedicated_storage_ids(
            d.pop("dedicated_storage_ids", UNSET)
        )

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

        def _parse_merged_settings(
            data: object,
        ) -> ISGConfigClusterSettingsSchema | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                merged_settings_type_1 = ISGConfigClusterSettingsSchema.from_dict(data)

                return merged_settings_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ISGConfigClusterSettingsSchema | None | Unset, data)

        merged_settings = _parse_merged_settings(d.pop("merged_settings", UNSET))

        def _parse_public_identity(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        public_identity = _parse_public_identity(d.pop("public_identity", UNSET))

        def _parse_roles(
            data: object,
        ) -> list[IconikStorageGatewayReadRolesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                roles_type_0 = []
                _roles_type_0 = data
                for roles_type_0_item_data in _roles_type_0:
                    roles_type_0_item = IconikStorageGatewayReadRolesType0Item(
                        roles_type_0_item_data
                    )

                    roles_type_0.append(roles_type_0_item)

                return roles_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[IconikStorageGatewayReadRolesType0Item] | None | Unset, data
            )

        roles = _parse_roles(d.pop("roles", UNSET))

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

        def _parse_status(
            data: object,
        ) -> IconikStorageGatewayReadStatusType1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                status_type_1 = IconikStorageGatewayReadStatusType1.from_dict(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IconikStorageGatewayReadStatusType1 | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_storage_addr(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        storage_addr = _parse_storage_addr(d.pop("storage_addr", UNSET))

        def _parse_storages(
            data: object,
        ) -> IconikStorageGatewayReadStoragesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                storages_type_0 = IconikStorageGatewayReadStoragesType0.from_dict(data)

                return storages_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IconikStorageGatewayReadStoragesType0 | None | Unset, data)

        storages = _parse_storages(d.pop("storages", UNSET))

        def _parse_telemetry(
            data: object,
        ) -> IconikStorageGatewayTelemetry | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                telemetry_type_1 = IconikStorageGatewayTelemetry.from_dict(data)

                return telemetry_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IconikStorageGatewayTelemetry | None | Unset, data)

        telemetry = _parse_telemetry(d.pop("telemetry", UNSET))

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
