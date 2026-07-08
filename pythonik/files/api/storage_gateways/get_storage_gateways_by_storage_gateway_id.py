from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storage_gateways_by_storage_gateway_id_response_default import (
    GetStorageGatewaysByStorageGatewayIdResponseDefault,
)
from ...models.iconik_storage_gateway_read_schema import IconikStorageGatewayReadSchema
from ...types import Response


def _get_kwargs(
    storage_gateway_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storage_gateways/{storage_gateway_id}/".format(
            storage_gateway_id=quote(str(storage_gateway_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStorageGatewaysByStorageGatewayIdResponseDefault
    | IconikStorageGatewayReadSchema
):
    if response.status_code == 200:
        response_200 = IconikStorageGatewayReadSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetStorageGatewaysByStorageGatewayIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStorageGatewaysByStorageGatewayIdResponseDefault
    | IconikStorageGatewayReadSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_gateway_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetStorageGatewaysByStorageGatewayIdResponseDefault
    | IconikStorageGatewayReadSchema
]:
    """Get a specific storage gateway

    Args:
        storage_gateway_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStorageGatewaysByStorageGatewayIdResponseDefault | IconikStorageGatewayReadSchema]
    """

    kwargs = _get_kwargs(
        storage_gateway_id=storage_gateway_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_gateway_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetStorageGatewaysByStorageGatewayIdResponseDefault
    | IconikStorageGatewayReadSchema
    | None
):
    """Get a specific storage gateway

    Args:
        storage_gateway_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStorageGatewaysByStorageGatewayIdResponseDefault | IconikStorageGatewayReadSchema
    """

    return sync_detailed(
        storage_gateway_id=storage_gateway_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_gateway_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetStorageGatewaysByStorageGatewayIdResponseDefault
    | IconikStorageGatewayReadSchema
]:
    """Get a specific storage gateway

    Args:
        storage_gateway_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStorageGatewaysByStorageGatewayIdResponseDefault | IconikStorageGatewayReadSchema]
    """

    kwargs = _get_kwargs(
        storage_gateway_id=storage_gateway_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_gateway_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetStorageGatewaysByStorageGatewayIdResponseDefault
    | IconikStorageGatewayReadSchema
    | None
):
    """Get a specific storage gateway

    Args:
        storage_gateway_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStorageGatewaysByStorageGatewayIdResponseDefault | IconikStorageGatewayReadSchema
    """

    return (
        await asyncio_detailed(
            storage_gateway_id=storage_gateway_id,
            client=client,
        )
    ).parsed
