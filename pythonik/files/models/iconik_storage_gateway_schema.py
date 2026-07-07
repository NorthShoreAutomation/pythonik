from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.iconik_storage_gateway_schema_roles_item import (
    IconikStorageGatewaySchemaRolesItem,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iconik_storage_gateway_schema_storages import (
        IconikStorageGatewaySchemaStorages,
    )
    from ..models.isg_config_settings_schema import ISGConfigSettingsSchema


T = TypeVar("T", bound="IconikStorageGatewaySchema")


@_attrs_define
class IconikStorageGatewaySchema:
    """
    Attributes:
        enabled (bool): Application toggle. If turned off ISG will enter idle state waiting to get enabled again.
        name (str):
        cluster_id (UUID | Unset):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        description (str | Unset):
        id (UUID | Unset):
        public_identity (str | Unset):
        roles (list[IconikStorageGatewaySchemaRolesItem] | Unset): Set of roles this gateway can perform when part of
            cluster
        settings (ISGConfigSettingsSchema | None | Unset): Application configuration settings as key-value pairs
        storage_addr (str | Unset): Server address for direct transfers between storage gateways
        storages (IconikStorageGatewaySchemaStorages | Unset): Storage mount points mapped by storage ID
    """

    enabled: bool
    name: str
    cluster_id: UUID | Unset = UNSET
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    id: UUID | Unset = UNSET
    public_identity: str | Unset = UNSET
    roles: list[IconikStorageGatewaySchemaRolesItem] | Unset = UNSET
    settings: ISGConfigSettingsSchema | None | Unset = UNSET
    storage_addr: str | Unset = UNSET
    storages: IconikStorageGatewaySchemaStorages | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.isg_config_settings_schema import ISGConfigSettingsSchema

        enabled = self.enabled

        name = self.name

        cluster_id: str | Unset = UNSET
        if not isinstance(self.cluster_id, Unset):
            cluster_id = str(self.cluster_id)

        date_created: str | Unset = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        description = self.description

        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

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

        storage_addr = self.storage_addr

        storages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.storages, Unset):
            storages = self.storages.to_dict()

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
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if public_identity is not UNSET:
            field_dict["public_identity"] = public_identity
        if roles is not UNSET:
            field_dict["roles"] = roles
        if settings is not UNSET:
            field_dict["settings"] = settings
        if storage_addr is not UNSET:
            field_dict["storage_addr"] = storage_addr
        if storages is not UNSET:
            field_dict["storages"] = storages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.iconik_storage_gateway_schema_storages import (
            IconikStorageGatewaySchemaStorages,
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

        description = d.pop("description", UNSET)

        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        public_identity = d.pop("public_identity", UNSET)

        _roles = d.pop("roles", UNSET)
        roles: list[IconikStorageGatewaySchemaRolesItem] | Unset = UNSET
        if _roles is not UNSET:
            roles = []
            for roles_item_data in _roles:
                roles_item = IconikStorageGatewaySchemaRolesItem(roles_item_data)

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

        storage_addr = d.pop("storage_addr", UNSET)

        _storages = d.pop("storages", UNSET)
        storages: IconikStorageGatewaySchemaStorages | Unset
        if isinstance(_storages, Unset):
            storages = UNSET
        else:
            storages = IconikStorageGatewaySchemaStorages.from_dict(_storages)

        iconik_storage_gateway_schema = cls(
            enabled=enabled,
            name=name,
            cluster_id=cluster_id,
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            id=id,
            public_identity=public_identity,
            roles=roles,
            settings=settings,
            storage_addr=storage_addr,
            storages=storages,
        )

        iconik_storage_gateway_schema.additional_properties = d
        return iconik_storage_gateway_schema

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
