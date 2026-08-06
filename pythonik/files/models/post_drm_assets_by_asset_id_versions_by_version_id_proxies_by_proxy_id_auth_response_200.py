from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200",
)


@_attrs_define
class PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200:
    """
    Attributes:
        server_url (None | str | Unset):
        token (None | str | Unset):
    """

    server_url: None | str | Unset = UNSET
    token: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_url: None | str | Unset
        if isinstance(self.server_url, Unset):
            server_url = UNSET
        else:
            server_url = self.server_url

        token: None | str | Unset
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if server_url is not UNSET:
            field_dict["server_url"] = server_url
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_server_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server_url = _parse_server_url(d.pop("server_url", UNSET))

        def _parse_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        token = _parse_token(d.pop("token", UNSET))

        post_drm_assets_by_asset_id_versions_by_version_id_proxies_by_proxy_id_auth_response_200 = cls(
            server_url=server_url,
            token=token,
        )

        post_drm_assets_by_asset_id_versions_by_version_id_proxies_by_proxy_id_auth_response_200.additional_properties = d
        return post_drm_assets_by_asset_id_versions_by_version_id_proxies_by_proxy_id_auth_response_200

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
