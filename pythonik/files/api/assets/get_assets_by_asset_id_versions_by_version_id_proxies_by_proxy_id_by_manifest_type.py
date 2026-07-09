from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_assets_by_asset_id_versions_by_version_id_proxies_by_proxy_id_by_manifest_type_response_default import (
    GetAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdByManifestTypeResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    version_id: str,
    proxy_id: str,
    manifest_type: str,
    *,
    path: str | Unset = UNSET,
    relative: bool | Unset = UNSET,
    presigned: bool | Unset = UNSET,
    recreate: bool | Unset = UNSET,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(drm, Unset):
        headers["DRM"] = drm

    if not isinstance(watermark, Unset):
        headers["Watermark"] = watermark

    params: dict[str, Any] = {}

    params["path"] = path

    params["relative"] = relative

    params["presigned"] = presigned

    params["recreate"] = recreate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/assets/{asset_id}/versions/{version_id}/proxies/{proxy_id}/{manifest_type}/".format(
            asset_id=quote(str(asset_id), safe=""),
            version_id=quote(str(version_id), safe=""),
            proxy_id=quote(str(proxy_id), safe=""),
            manifest_type=quote(str(manifest_type), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdByManifestTypeResponseDefault
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 425:
        response_425 = cast(Any, None)
        return response_425

    response_default = GetAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdByManifestTypeResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdByManifestTypeResponseDefault
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
    manifest_type: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = UNSET,
    relative: bool | Unset = UNSET,
    presigned: bool | Unset = UNSET,
    recreate: bool | Unset = UNSET,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdByManifestTypeResponseDefault
]:
    """Retrieve manifest/playlist for asset proxy


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        version_id (str):
        proxy_id (str):
        manifest_type (str):
        path (str | Unset):
        relative (bool | Unset):
        presigned (bool | Unset):
        recreate (bool | Unset):
        drm (str | Unset):
        watermark (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdByManifestTypeResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        proxy_id=proxy_id,
        manifest_type=manifest_type,
        path=path,
        relative=relative,
        presigned=presigned,
        recreate=recreate,
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
    manifest_type: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = UNSET,
    relative: bool | Unset = UNSET,
    presigned: bool | Unset = UNSET,
    recreate: bool | Unset = UNSET,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdByManifestTypeResponseDefault
    | None
):
    """Retrieve manifest/playlist for asset proxy


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        version_id (str):
        proxy_id (str):
        manifest_type (str):
        path (str | Unset):
        relative (bool | Unset):
        presigned (bool | Unset):
        recreate (bool | Unset):
        drm (str | Unset):
        watermark (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdByManifestTypeResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        version_id=version_id,
        proxy_id=proxy_id,
        manifest_type=manifest_type,
        client=client,
        path=path,
        relative=relative,
        presigned=presigned,
        recreate=recreate,
        drm=drm,
        watermark=watermark,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    version_id: str,
    proxy_id: str,
    manifest_type: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = UNSET,
    relative: bool | Unset = UNSET,
    presigned: bool | Unset = UNSET,
    recreate: bool | Unset = UNSET,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> Response[
    Any
    | GetAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdByManifestTypeResponseDefault
]:
    """Retrieve manifest/playlist for asset proxy


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        version_id (str):
        proxy_id (str):
        manifest_type (str):
        path (str | Unset):
        relative (bool | Unset):
        presigned (bool | Unset):
        recreate (bool | Unset):
        drm (str | Unset):
        watermark (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdByManifestTypeResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        version_id=version_id,
        proxy_id=proxy_id,
        manifest_type=manifest_type,
        path=path,
        relative=relative,
        presigned=presigned,
        recreate=recreate,
        drm=drm,
        watermark=watermark,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    version_id: str,
    proxy_id: str,
    manifest_type: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = UNSET,
    relative: bool | Unset = UNSET,
    presigned: bool | Unset = UNSET,
    recreate: bool | Unset = UNSET,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> (
    Any
    | GetAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdByManifestTypeResponseDefault
    | None
):
    """Retrieve manifest/playlist for asset proxy


    Required roles:
     - can_read_proxies

    Args:
        asset_id (str):
        version_id (str):
        proxy_id (str):
        manifest_type (str):
        path (str | Unset):
        relative (bool | Unset):
        presigned (bool | Unset):
        recreate (bool | Unset):
        drm (str | Unset):
        watermark (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetAssetsByAssetIdVersionsByVersionIdProxiesByProxyIdByManifestTypeResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            version_id=version_id,
            proxy_id=proxy_id,
            manifest_type=manifest_type,
            client=client,
            path=path,
            relative=relative,
            presigned=presigned,
            recreate=recreate,
            drm=drm,
            watermark=watermark,
        )
    ).parsed
