from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_proxies_by_proxy_id_containers_by_container_id_files_response_default import (
    PostAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesResponseDefault,
)
from ...models.proxy_file_schema import ProxyFileSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    asset_id: str,
    proxy_id: str,
    container_id: str,
    *,
    body: ProxyFileSchema,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(drm, Unset):
        headers["DRM"] = drm

    if not isinstance(watermark, Unset):
        headers["Watermark"] = watermark

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/proxies/{proxy_id}/containers/{container_id}/files/".format(
            asset_id=quote(str(asset_id), safe=""),
            proxy_id=quote(str(proxy_id), safe=""),
            container_id=quote(str(container_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesResponseDefault
    | ProxyFileSchema
):
    if response.status_code == 201:
        response_201 = ProxyFileSchema.from_dict(response.json())

        return response_201

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

    response_default = PostAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesResponseDefault
    | ProxyFileSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    proxy_id: str,
    container_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyFileSchema,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> Response[
    Any
    | PostAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesResponseDefault
    | ProxyFileSchema
]:
    """Create Proxy file


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        container_id (str):
        drm (str | Unset):
        watermark (str | Unset):
        body (ProxyFileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesResponseDefault | ProxyFileSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
        container_id=container_id,
        body=body,
        drm=drm,
        watermark=watermark,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    proxy_id: str,
    container_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyFileSchema,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> (
    Any
    | PostAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesResponseDefault
    | ProxyFileSchema
    | None
):
    """Create Proxy file


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        container_id (str):
        drm (str | Unset):
        watermark (str | Unset):
        body (ProxyFileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesResponseDefault | ProxyFileSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        proxy_id=proxy_id,
        container_id=container_id,
        client=client,
        body=body,
        drm=drm,
        watermark=watermark,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    proxy_id: str,
    container_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyFileSchema,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> Response[
    Any
    | PostAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesResponseDefault
    | ProxyFileSchema
]:
    """Create Proxy file


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        container_id (str):
        drm (str | Unset):
        watermark (str | Unset):
        body (ProxyFileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesResponseDefault | ProxyFileSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
        container_id=container_id,
        body=body,
        drm=drm,
        watermark=watermark,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    proxy_id: str,
    container_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyFileSchema,
    drm: str | Unset = UNSET,
    watermark: str | Unset = UNSET,
) -> (
    Any
    | PostAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesResponseDefault
    | ProxyFileSchema
    | None
):
    """Create Proxy file


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        container_id (str):
        drm (str | Unset):
        watermark (str | Unset):
        body (ProxyFileSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesResponseDefault | ProxyFileSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            proxy_id=proxy_id,
            container_id=container_id,
            client=client,
            body=body,
            drm=drm,
            watermark=watermark,
        )
    ).parsed
