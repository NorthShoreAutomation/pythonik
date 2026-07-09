from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_proxies_by_proxy_id_public_response_default import (
    PostAssetsByAssetIdProxiesByProxyIdPublicResponseDefault,
)
from ...models.proxy_schema import ProxySchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    proxy_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/proxies/{proxy_id}/public/".format(
            asset_id=quote(str(asset_id), safe=""),
            proxy_id=quote(str(proxy_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostAssetsByAssetIdProxiesByProxyIdPublicResponseDefault | ProxySchema:
    if response.status_code == 201:
        response_201 = ProxySchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        PostAssetsByAssetIdProxiesByProxyIdPublicResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostAssetsByAssetIdProxiesByProxyIdPublicResponseDefault | ProxySchema
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
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | PostAssetsByAssetIdProxiesByProxyIdPublicResponseDefault | ProxySchema
]:
    """Make the proxy link public


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdProxiesByProxyIdPublicResponseDefault | ProxySchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any | PostAssetsByAssetIdProxiesByProxyIdPublicResponseDefault | ProxySchema | None
):
    """Make the proxy link public


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdProxiesByProxyIdPublicResponseDefault | ProxySchema
    """

    return sync_detailed(
        asset_id=asset_id,
        proxy_id=proxy_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | PostAssetsByAssetIdProxiesByProxyIdPublicResponseDefault | ProxySchema
]:
    """Make the proxy link public


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdProxiesByProxyIdPublicResponseDefault | ProxySchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    proxy_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any | PostAssetsByAssetIdProxiesByProxyIdPublicResponseDefault | ProxySchema | None
):
    """Make the proxy link public


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdProxiesByProxyIdPublicResponseDefault | ProxySchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            proxy_id=proxy_id,
            client=client,
        )
    ).parsed
