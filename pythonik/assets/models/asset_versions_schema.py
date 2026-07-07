from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edit_asset_version import EditAssetVersion


T = TypeVar("T", bound="AssetVersionsSchema")


@_attrs_define
class AssetVersionsSchema:
    """
    Attributes:
        asset_id (UUID):
        system_domain_id (UUID | Unset):
        versions (list[EditAssetVersion] | Unset):
    """

    asset_id: UUID
    system_domain_id: UUID | Unset = UNSET
    versions: list[EditAssetVersion] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        system_domain_id: str | Unset = UNSET
        if not isinstance(self.system_domain_id, Unset):
            system_domain_id = str(self.system_domain_id)

        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
            }
        )
        if system_domain_id is not UNSET:
            field_dict["system_domain_id"] = system_domain_id
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_asset_version import EditAssetVersion

        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        _system_domain_id = d.pop("system_domain_id", UNSET)
        system_domain_id: UUID | Unset
        if isinstance(_system_domain_id, Unset):
            system_domain_id = UNSET
        else:
            system_domain_id = UUID(_system_domain_id)

        _versions = d.pop("versions", UNSET)
        versions: list[EditAssetVersion] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = EditAssetVersion.from_dict(versions_item_data)

                versions.append(versions_item)

        asset_versions_schema = cls(
            asset_id=asset_id,
            system_domain_id=system_domain_id,
            versions=versions,
        )

        asset_versions_schema.additional_properties = d
        return asset_versions_schema

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
