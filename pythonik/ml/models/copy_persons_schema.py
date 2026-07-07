from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CopyPersonsSchema")


@_attrs_define
class CopyPersonsSchema:
    """
    Attributes:
        source_asset_id (UUID):
        source_version_id (UUID):
        target_asset_id (UUID):
        target_version_id (UUID):
    """

    source_asset_id: UUID
    source_version_id: UUID
    target_asset_id: UUID
    target_version_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_asset_id = str(self.source_asset_id)

        source_version_id = str(self.source_version_id)

        target_asset_id = str(self.target_asset_id)

        target_version_id = str(self.target_version_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source_asset_id": source_asset_id,
                "source_version_id": source_version_id,
                "target_asset_id": target_asset_id,
                "target_version_id": target_version_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source_asset_id = UUID(d.pop("source_asset_id"))

        source_version_id = UUID(d.pop("source_version_id"))

        target_asset_id = UUID(d.pop("target_asset_id"))

        target_version_id = UUID(d.pop("target_version_id"))

        copy_persons_schema = cls(
            source_asset_id=source_asset_id,
            source_version_id=source_version_id,
            target_asset_id=target_asset_id,
            target_version_id=target_version_id,
        )

        copy_persons_schema.additional_properties = d
        return copy_persons_schema

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
