from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.storage_permissions_schema_method import StoragePermissionsSchemaMethod
from ..models.storage_permissions_schema_purpose import StoragePermissionsSchemaPurpose

if TYPE_CHECKING:
    from ..models.storage_permissions_schema_settings import (
        StoragePermissionsSchemaSettings,
    )


T = TypeVar("T", bound="StoragePermissionsSchema")


@_attrs_define
class StoragePermissionsSchema:
    """
    Attributes:
        method (StoragePermissionsSchemaMethod):
        purpose (StoragePermissionsSchemaPurpose):
        settings (StoragePermissionsSchemaSettings):
    """

    method: StoragePermissionsSchemaMethod
    purpose: StoragePermissionsSchemaPurpose
    settings: StoragePermissionsSchemaSettings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        purpose = self.purpose.value

        settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "purpose": purpose,
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_permissions_schema_settings import (
            StoragePermissionsSchemaSettings,
        )

        d = dict(src_dict)
        method = StoragePermissionsSchemaMethod(d.pop("method"))

        purpose = StoragePermissionsSchemaPurpose(d.pop("purpose"))

        settings = StoragePermissionsSchemaSettings.from_dict(d.pop("settings"))

        storage_permissions_schema = cls(
            method=method,
            purpose=purpose,
            settings=settings,
        )

        storage_permissions_schema.additional_properties = d
        return storage_permissions_schema

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
