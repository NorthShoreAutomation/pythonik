from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_by_storage_id_gateway_events_response_default import (
    GetStoragesByStorageIdGatewayEventsResponseDefault,
)
from ...models.iconik_storage_gateway_events_schema import (
    IconikStorageGatewayEventsSchema,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/{storage_id}/gateway/events/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStoragesByStorageIdGatewayEventsResponseDefault
    | IconikStorageGatewayEventsSchema
):
    if response.status_code == 200:
        response_200 = IconikStorageGatewayEventsSchema.from_dict(response.json())

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

    response_default = GetStoragesByStorageIdGatewayEventsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStoragesByStorageIdGatewayEventsResponseDefault
    | IconikStorageGatewayEventsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetStoragesByStorageIdGatewayEventsResponseDefault
    | IconikStorageGatewayEventsSchema
]:
    """Get pending storage gateway events

    Args:
        storage_id (str):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdGatewayEventsResponseDefault | IconikStorageGatewayEventsSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetStoragesByStorageIdGatewayEventsResponseDefault
    | IconikStorageGatewayEventsSchema
    | None
):
    """Get pending storage gateway events

    Args:
        storage_id (str):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdGatewayEventsResponseDefault | IconikStorageGatewayEventsSchema
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetStoragesByStorageIdGatewayEventsResponseDefault
    | IconikStorageGatewayEventsSchema
]:
    """Get pending storage gateway events

    Args:
        storage_id (str):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdGatewayEventsResponseDefault | IconikStorageGatewayEventsSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetStoragesByStorageIdGatewayEventsResponseDefault
    | IconikStorageGatewayEventsSchema
    | None
):
    """Get pending storage gateway events

    Args:
        storage_id (str):
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdGatewayEventsResponseDefault | IconikStorageGatewayEventsSchema
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            last_id=last_id,
        )
    ).parsed
