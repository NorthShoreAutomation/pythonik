from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="VersionsSchema")


@_attrs_define
class VersionsSchema:
    """
    Attributes:
        asset_id (UUID):
        version_ids (list[UUID] | Unset):
    """

    asset_id: UUID
    version_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        version_ids: list[str] | Unset = UNSET
        if not isinstance(self.version_ids, Unset):
            version_ids = []
            for version_ids_item_data in self.version_ids:
                version_ids_item = str(version_ids_item_data)
                version_ids.append(version_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
            }
        )
        if version_ids is not UNSET:
            field_dict["version_ids"] = version_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        _version_ids = d.pop("version_ids", UNSET)
        version_ids: list[UUID] | Unset = UNSET
        if _version_ids is not UNSET:
            version_ids = []
            for version_ids_item_data in _version_ids:
                version_ids_item = UUID(version_ids_item_data)

                version_ids.append(version_ids_item)

        versions_schema = cls(
            asset_id=asset_id,
            version_ids=version_ids,
        )

        versions_schema.additional_properties = d
        return versions_schema

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
