from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_drm_assets_by_asset_id_versions_by_version_id_proxies_by_proxy_id_auth_response_200 import (
    PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200,
)
from ...models.post_drm_assets_by_asset_id_versions_by_version_id_proxies_by_proxy_id_auth_response_default import (
    PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    version_id: str,
    proxy_id: str,
    *,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(drm, Unset):
        headers["DRM"] = drm

    if not isinstance(watermark, Unset):
        headers["WATERMARK"] = watermark

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/drm/assets/{asset_id}/versions/{version_id}/proxies/{proxy_id}/auth/".format(
            asset_id=quote(str(asset_id), safe=""),
            version_id=quote(str(version_id), safe=""),
            proxy_id=quote(str(proxy_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200
    | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponseDefault
):
    if response.status_code == 200:
        response_200 = PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200.from_dict(
            response.json()
        )

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200
    | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    version_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> Response[
    Any
    | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200
    | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponseDefault
]:
    """Get authentication token for a given asset proxy.


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        version_id (str):
        proxy_id (str):
        drm (str | Unset):
        watermark (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200 | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        proxy_id=proxy_id,
        drm=drm,
        watermark=watermark,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    version_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> (
    Any
    | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200
    | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponseDefault
    | None
):
    """Get authentication token for a given asset proxy.


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        version_id (str):
        proxy_id (str):
        drm (str | Unset):
        watermark (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200 | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        version_id=version_id,
        proxy_id=proxy_id,
        client=client,
        drm=drm,
        watermark=watermark,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    version_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> Response[
    Any
    | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200
    | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponseDefault
]:
    """Get authentication token for a given asset proxy.


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        version_id (str):
        proxy_id (str):
        drm (str | Unset):
        watermark (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200 | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        proxy_id=proxy_id,
        drm=drm,
        watermark=watermark,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    version_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> (
    Any
    | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200
    | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponseDefault
    | None
):
    """Get authentication token for a given asset proxy.


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        version_id (str):
        proxy_id (str):
        drm (str | Unset):
        watermark (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponse200 | PostDrmAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdAuthResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            version_id=version_id,
            proxy_id=proxy_id,
            client=client,
            drm=drm,
            watermark=watermark,
        )
    ).parsed
