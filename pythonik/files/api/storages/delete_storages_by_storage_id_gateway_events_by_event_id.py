from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_storages_by_storage_id_gateway_events_by_event_id_response_default import (
    DeleteStoragesByStorageIdGatewayEventsByEventIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    storage_id: str,
    event_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/storages/{storage_id}/gateway/events/{event_id}/".format(
            storage_id=quote(str(storage_id), safe=""),
            event_id=quote(str(event_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteStoragesByStorageIdGatewayEventsByEventIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        DeleteStoragesByStorageIdGatewayEventsByEventIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteStoragesByStorageIdGatewayEventsByEventIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteStoragesByStorageIdGatewayEventsByEventIdResponseDefault]:
    """Delete storage gateway event

    Args:
        storage_id (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdGatewayEventsByEventIdResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        event_id=event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteStoragesByStorageIdGatewayEventsByEventIdResponseDefault | None:
    """Delete storage gateway event

    Args:
        storage_id (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdGatewayEventsByEventIdResponseDefault
    """

    return sync_detailed(
        storage_id=storage_id,
        event_id=event_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteStoragesByStorageIdGatewayEventsByEventIdResponseDefault]:
    """Delete storage gateway event

    Args:
        storage_id (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdGatewayEventsByEventIdResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        event_id=event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    event_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteStoragesByStorageIdGatewayEventsByEventIdResponseDefault | None:
    """Delete storage gateway event

    Args:
        storage_id (str):
        event_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdGatewayEventsByEventIdResponseDefault
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            event_id=event_id,
            client=client,
        )
    ).parsed
