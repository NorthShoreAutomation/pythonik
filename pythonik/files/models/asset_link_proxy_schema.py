from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetLinkProxySchema")


@_attrs_define
class AssetLinkProxySchema:
    """
    Attributes:
        asset_id (UUID):
        url (str):
        version_id (UUID):
        filename (None | str | Unset):
        name (None | str | Unset):
    """

    asset_id: UUID
    url: str
    version_id: UUID
    filename: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        asset_id = str(self.asset_id)

        url = self.url

        version_id = str(self.version_id)

        filename: None | str | Unset
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset_id": asset_id,
                "url": url,
                "version_id": version_id,
            }
        )
        if filename is not UNSET:
            field_dict["filename"] = filename
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        asset_id = UUID(d.pop("asset_id"))

        url = d.pop("url")

        version_id = UUID(d.pop("version_id"))

        def _parse_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filename = _parse_filename(d.pop("filename", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        asset_link_proxy_schema = cls(
            asset_id=asset_id,
            url=url,
            version_id=version_id,
            filename=filename,
            name=name,
        )

        asset_link_proxy_schema.additional_properties = d
        return asset_link_proxy_schema

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
