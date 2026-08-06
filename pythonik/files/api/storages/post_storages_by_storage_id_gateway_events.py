from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.iconik_storage_gateway_event_schema import (
    IconikStorageGatewayEventSchema,
)
from ...models.post_storages_by_storage_id_gateway_events_response_default import (
    PostStoragesByStorageIdGatewayEventsResponseDefault,
)
from ...types import Response


def _get_kwargs(
    storage_id: str,
    *,
    body: IconikStorageGatewayEventSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/storages/{storage_id}/gateway/events/".format(
            storage_id=quote(str(storage_id), safe=""),
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
    | IconikStorageGatewayEventSchema
    | PostStoragesByStorageIdGatewayEventsResponseDefault
):
    if response.status_code == 201:
        response_201 = IconikStorageGatewayEventSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PostStoragesByStorageIdGatewayEventsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | IconikStorageGatewayEventSchema
    | PostStoragesByStorageIdGatewayEventsResponseDefault
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
    body: IconikStorageGatewayEventSchema,
) -> Response[
    Any
    | IconikStorageGatewayEventSchema
    | PostStoragesByStorageIdGatewayEventsResponseDefault
]:
    """Create new storage gateway event

    Args:
        storage_id (str):
        body (IconikStorageGatewayEventSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IconikStorageGatewayEventSchema | PostStoragesByStorageIdGatewayEventsResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IconikStorageGatewayEventSchema,
) -> (
    Any
    | IconikStorageGatewayEventSchema
    | PostStoragesByStorageIdGatewayEventsResponseDefault
    | None
):
    """Create new storage gateway event

    Args:
        storage_id (str):
        body (IconikStorageGatewayEventSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IconikStorageGatewayEventSchema | PostStoragesByStorageIdGatewayEventsResponseDefault
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IconikStorageGatewayEventSchema,
) -> Response[
    Any
    | IconikStorageGatewayEventSchema
    | PostStoragesByStorageIdGatewayEventsResponseDefault
]:
    """Create new storage gateway event

    Args:
        storage_id (str):
        body (IconikStorageGatewayEventSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IconikStorageGatewayEventSchema | PostStoragesByStorageIdGatewayEventsResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: IconikStorageGatewayEventSchema,
) -> (
    Any
    | IconikStorageGatewayEventSchema
    | PostStoragesByStorageIdGatewayEventsResponseDefault
    | None
):
    """Create new storage gateway event

    Args:
        storage_id (str):
        body (IconikStorageGatewayEventSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IconikStorageGatewayEventSchema | PostStoragesByStorageIdGatewayEventsResponseDefault
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            body=body,
        )
    ).parsed
