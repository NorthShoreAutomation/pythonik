from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_by_asset_id_method_by_storage_method_proxies_response_default import (
    PostAssetsByAssetIdMethodByStorageMethodProxiesResponseDefault,
)
from ...models.proxy_create_schema import ProxyCreateSchema
from ...types import Response


def _get_kwargs(
    asset_id: str,
    storage_method: str,
    *,
    body: ProxyCreateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/{asset_id}/method/{storage_method}/proxies/".format(
            asset_id=quote(str(asset_id), safe=""),
            storage_method=quote(str(storage_method), safe=""),
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
    | PostAssetsByAssetIdMethodByStorageMethodProxiesResponseDefault
    | ProxyCreateSchema
):
    if response.status_code == 201:
        response_201 = ProxyCreateSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        PostAssetsByAssetIdMethodByStorageMethodProxiesResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostAssetsByAssetIdMethodByStorageMethodProxiesResponseDefault
    | ProxyCreateSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    asset_id: str,
    storage_method: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyCreateSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdMethodByStorageMethodProxiesResponseDefault
    | ProxyCreateSchema
]:
    """Create proxy and associate to asset


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        storage_method (str):
        body (ProxyCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdMethodByStorageMethodProxiesResponseDefault | ProxyCreateSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        storage_method=storage_method,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    asset_id: str,
    storage_method: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyCreateSchema,
) -> (
    Any
    | PostAssetsByAssetIdMethodByStorageMethodProxiesResponseDefault
    | ProxyCreateSchema
    | None
):
    """Create proxy and associate to asset


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        storage_method (str):
        body (ProxyCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdMethodByStorageMethodProxiesResponseDefault | ProxyCreateSchema
    """

    return sync_detailed(
        asset_id=asset_id,
        storage_method=storage_method,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    storage_method: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyCreateSchema,
) -> Response[
    Any
    | PostAssetsByAssetIdMethodByStorageMethodProxiesResponseDefault
    | ProxyCreateSchema
]:
    """Create proxy and associate to asset


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        storage_method (str):
        body (ProxyCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsByAssetIdMethodByStorageMethodProxiesResponseDefault | ProxyCreateSchema]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        storage_method=storage_method,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    asset_id: str,
    storage_method: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProxyCreateSchema,
) -> (
    Any
    | PostAssetsByAssetIdMethodByStorageMethodProxiesResponseDefault
    | ProxyCreateSchema
    | None
):
    """Create proxy and associate to asset


    Required roles:
     - can_write_proxies

    Args:
        asset_id (str):
        storage_method (str):
        body (ProxyCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsByAssetIdMethodByStorageMethodProxiesResponseDefault | ProxyCreateSchema
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            storage_method=storage_method,
            client=client,
            body=body,
        )
    ).parsed
