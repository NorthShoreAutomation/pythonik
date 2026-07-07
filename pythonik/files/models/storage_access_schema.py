from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.storage_access_schema_method import StorageAccessSchemaMethod

if TYPE_CHECKING:
    from ..models.storage_access_schema_settings import StorageAccessSchemaSettings


T = TypeVar("T", bound="StorageAccessSchema")


@_attrs_define
class StorageAccessSchema:
    """
    Attributes:
        method (StorageAccessSchemaMethod):
        settings (StorageAccessSchemaSettings):
    """

    method: StorageAccessSchemaMethod
    settings: StorageAccessSchemaSettings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "settings": settings,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.storage_access_schema_settings import StorageAccessSchemaSettings

        d = dict(src_dict)
        method = StorageAccessSchemaMethod(d.pop("method"))

        settings = StorageAccessSchemaSettings.from_dict(d.pop("settings"))

        storage_access_schema = cls(
            method=method,
            settings=settings,
        )

        storage_access_schema.additional_properties = d
        return storage_access_schema

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
