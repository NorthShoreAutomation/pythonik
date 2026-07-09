from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.proxy_file_update_schema_status import ProxyFileUpdateSchemaStatus

T = TypeVar("T", bound="ProxyFileUpdateSchema")


@_attrs_define
class ProxyFileUpdateSchema:
    """
    Attributes:
        status (ProxyFileUpdateSchemaStatus):
    """

    status: ProxyFileUpdateSchemaStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ProxyFileUpdateSchemaStatus(d.pop("status"))

        proxy_file_update_schema = cls(
            status=status,
        )

        proxy_file_update_schema.additional_properties = d
        return proxy_file_update_schema

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
