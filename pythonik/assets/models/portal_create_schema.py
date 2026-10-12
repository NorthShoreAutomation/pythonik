from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.portal_create_schema_status import PortalCreateSchemaStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portal_config_schema import PortalConfigSchema
    from ..models.portal_create_schema_keyframes_type_0_item import (
        PortalCreateSchemaKeyframesType0Item,
    )


T = TypeVar("T", bound="PortalCreateSchema")


@_attrs_define
class PortalCreateSchema:
    """
    Attributes:
        name (str):
        playlist_id (UUID):
        config (None | PortalConfigSchema | Unset):
        created_by_user (None | Unset | UUID):
        date_created (datetime.datetime | None | Unset):
        date_modified (datetime.datetime | None | Unset):
        description (None | str | Unset):
        id (None | Unset | UUID):
        keyframes (list[PortalCreateSchemaKeyframesType0Item] | None | Unset):
        logo (None | str | Unset):
        logo_storage_id (None | Unset | UUID):
        status (None | PortalCreateSchemaStatus | Unset):
        system_domain_id (None | Unset | UUID):
    """

    name: str
    playlist_id: UUID
    config: None | PortalConfigSchema | Unset = UNSET
    created_by_user: None | Unset | UUID = UNSET
    date_created: datetime.datetime | None | Unset = UNSET
    date_modified: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET
    id: None | Unset | UUID = UNSET
    keyframes: list[PortalCreateSchemaKeyframesType0Item] | None | Unset = UNSET
    logo: None | str | Unset = UNSET
    logo_storage_id: None | Unset | UUID = UNSET
    status: None | PortalCreateSchemaStatus | Unset = UNSET
    system_domain_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.portal_config_schema import PortalConfigSchema

        name = self.name

        playlist_id = str(self.playlist_id)

        config: dict[str, Any] | None | Unset
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, PortalConfigSchema):
            config = self.config.to_dict()
        else:
            config = self.config

        created_by_user: None | str | Unset
        if isinstance(self.created_by_user, Unset):
            created_by_user = UNSET
        elif isinstance(self.created_by_user, UUID):
            created_by_user = str(self.created_by_user)
        else:
            created_by_user = self.created_by_user

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

        keyframes: list[dict[str, Any]] | None | Unset
        if isinstance(self.keyframes, Unset):
            keyframes = UNSET
        elif isinstance(self.keyframes, list):
            keyframes = []
            for keyframes_type_0_item_data in self.keyframes:
                keyframes_type_0_item = keyframes_type_0_item_data.to_dict()
                keyframes.append(keyframes_type_0_item)

        else:
            keyframes = self.keyframes

        logo: None | str | Unset
        if isinstance(self.logo, Unset):
            logo = UNSET
        else:
            logo = self.logo

        logo_storage_id: None | str | Unset
        if isinstance(self.logo_storage_id, Unset):
            logo_storage_id = UNSET
        elif isinstance(self.logo_storage_id, UUID):
            logo_storage_id = str(self.logo_storage_id)
        else:
            logo_storage_id = self.logo_storage_id

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, PortalCreateSchemaStatus):
            status = self.status.value
        else:
            status = self.status

        system_domain_id: None | str | Unset
        if isinstance(self.system_domain_id, Unset):
            system_domain_id = UNSET
        elif isinstance(self.system_domain_id, UUID):
            system_domain_id = str(self.system_domain_id)
        else:
            system_domain_id = self.system_domain_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "playlist_id": playlist_id,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if created_by_user is not UNSET:
            field_dict["created_by_user"] = created_by_user
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if keyframes is not UNSET:
            field_dict["keyframes"] = keyframes
        if logo is not UNSET:
            field_dict["logo"] = logo
        if logo_storage_id is not UNSET:
            field_dict["logo_storage_id"] = logo_storage_id
        if status is not UNSET:
            field_dict["status"] = status
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portal_config_schema import PortalConfigSchema
        from ..models.portal_create_schema_keyframes_type_0_item import (
            PortalCreateSchemaKeyframesType0Item,
        )

        d = dict(src_dict)
        name = d.pop("name")

        playlist_id = UUID(d.pop("playlist_id"))

        def _parse_config(data: object) -> None | PortalConfigSchema | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_1 = PortalConfigSchema.from_dict(data)

                return config_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PortalConfigSchema | Unset, data)

        config = _parse_config(d.pop("config", UNSET))

        def _parse_created_by_user(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_by_user_type_0 = UUID(data)

                return created_by_user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        created_by_user = _parse_created_by_user(d.pop("created_by_user", UNSET))

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

        def _parse_keyframes(
            data: object,
        ) -> list[PortalCreateSchemaKeyframesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                keyframes_type_0 = []
                _keyframes_type_0 = data
                for keyframes_type_0_item_data in _keyframes_type_0:
                    keyframes_type_0_item = (
                        PortalCreateSchemaKeyframesType0Item.from_dict(
                            keyframes_type_0_item_data
                        )
                    )

                    keyframes_type_0.append(keyframes_type_0_item)

                return keyframes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PortalCreateSchemaKeyframesType0Item] | None | Unset, data)

        keyframes = _parse_keyframes(d.pop("keyframes", UNSET))

        def _parse_logo(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo = _parse_logo(d.pop("logo", UNSET))

        def _parse_logo_storage_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                logo_storage_id_type_0 = UUID(data)

                return logo_storage_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        logo_storage_id = _parse_logo_storage_id(d.pop("logo_storage_id", UNSET))

        def _parse_status(data: object) -> None | PortalCreateSchemaStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = PortalCreateSchemaStatus(data)

                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PortalCreateSchemaStatus | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

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

        portal_create_schema = cls(
            name=name,
            playlist_id=playlist_id,
            config=config,
            created_by_user=created_by_user,
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            id=id,
            keyframes=keyframes,
            logo=logo,
            logo_storage_id=logo_storage_id,
            status=status,
            system_domain_id=system_domain_id,
        )

        portal_create_schema.additional_properties = d
        return portal_create_schema

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
