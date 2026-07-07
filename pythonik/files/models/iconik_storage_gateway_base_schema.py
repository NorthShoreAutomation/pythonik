from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.isg_config_settings_schema import ISGConfigSettingsSchema


T = TypeVar("T", bound="IconikStorageGatewayBaseSchema")


@_attrs_define
class IconikStorageGatewayBaseSchema:
    """
    Attributes:
        enabled (bool): Application toggle. If turned off ISG will enter idle state waiting to get enabled again.
        name (str):
        date_created (datetime.datetime | Unset):
        date_modified (datetime.datetime | Unset):
        description (str | Unset):
        id (UUID | Unset):
        settings (ISGConfigSettingsSchema | None | Unset): Application configuration settings as key-value pairs
    """

    enabled: bool
    name: str
    date_created: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    description: str | Unset = UNSET
    id: UUID | Unset = UNSET
    settings: ISGConfigSettingsSchema | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.isg_config_settings_schema import ISGConfigSettingsSchema

        enabled = self.enabled

        name = self.name

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

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, ISGConfigSettingsSchema):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "name": name,
            }
        )
        if date_created is not UNSET:
            field_dict["date_created"] = date_created
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.isg_config_settings_schema import ISGConfigSettingsSchema

        d = dict(src_dict)
        enabled = d.pop("enabled")

        name = d.pop("name")

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

        iconik_storage_gateway_base_schema = cls(
            enabled=enabled,
            name=name,
            date_created=date_created,
            date_modified=date_modified,
            description=description,
            id=id,
            settings=settings,
        )

        iconik_storage_gateway_base_schema.additional_properties = d
        return iconik_storage_gateway_base_schema

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
