from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.proxy_file_schema import ProxyFileSchema
from ...models.proxy_file_update_schema import ProxyFileUpdateSchema
from ...models.put_assets_by_asset_id_proxies_by_proxy_id_containers_by_container_id_files_by_file_id_response_default import (
    PutAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesByFileIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    asset_id: str,
    proxy_id: str,
    container_id: str,
    file_id: str,
    *,
    body: ProxyFileUpdateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/assets/{asset_id}/proxies/{proxy_id}/containers/{container_id}/files/{file_id}/".format(
            asset_id=quote(str(asset_id), safe=""),
            proxy_id=quote(str(proxy_id), safe=""),
            container_id=quote(str(container_id), safe=""),
            file_id=quote(str(file_id), safe=""),
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
    | ProxyFileSchema
    | PutAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesByFileIdResponseDefault
):
    if response.status_code == 200:
        response_200 = ProxyFileSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PutAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesByFileIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ProxyFileSchema
    | PutAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesByFileIdResponseDefault
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
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyFileUpdateSchema,
) -> Response[
    Any
    | ProxyFileSchema
    | PutAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesByFileIdResponseDefault
]:
    """Update proxy file status


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        container_id (str):
        file_id (str):
        body (ProxyFileUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProxyFileSchema | PutAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesByFileIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
        container_id=container_id,
        file_id=file_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    proxy_id: str,
    container_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyFileUpdateSchema,
) -> (
    Any
    | ProxyFileSchema
    | PutAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesByFileIdResponseDefault
    | None
):
    """Update proxy file status


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        container_id (str):
        file_id (str):
        body (ProxyFileUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProxyFileSchema | PutAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesByFileIdResponseDefault
    """

    return sync_detailed(
        asset_id=asset_id,
        proxy_id=proxy_id,
        container_id=container_id,
        file_id=file_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    proxy_id: str,
    container_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyFileUpdateSchema,
) -> Response[
    Any
    | ProxyFileSchema
    | PutAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesByFileIdResponseDefault
]:
    """Update proxy file status


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        container_id (str):
        file_id (str):
        body (ProxyFileUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProxyFileSchema | PutAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesByFileIdResponseDefault]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        proxy_id=proxy_id,
        container_id=container_id,
        file_id=file_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    proxy_id: str,
    container_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyFileUpdateSchema,
) -> (
    Any
    | ProxyFileSchema
    | PutAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesByFileIdResponseDefault
    | None
):
    """Update proxy file status


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        proxy_id (str):
        container_id (str):
        file_id (str):
        body (ProxyFileUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProxyFileSchema | PutAssetsByAssetIdProxiesByProxyIdContainersByContainerIdFilesByFileIdResponseDefault
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            proxy_id=proxy_id,
            container_id=container_id,
            file_id=file_id,
            client=client,
            body=body,
        )
    ).parsed
