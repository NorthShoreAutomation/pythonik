from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.discovery_entity_schema import DiscoveryEntitySchema
from ...models.get_discovery_default_entities_by_entity_id_response_default import (
    GetDiscoveryDefaultEntitiesByEntityIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    entity_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/discovery/default/entities/{entity_id}/".format(
            entity_id=quote(str(entity_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DiscoveryEntitySchema | GetDiscoveryDefaultEntitiesByEntityIdResponseDefault:
    if response.status_code == 200:
        response_200 = DiscoveryEntitySchema.from_dict(response.json())

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

    response_default = GetDiscoveryDefaultEntitiesByEntityIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | DiscoveryEntitySchema | GetDiscoveryDefaultEntitiesByEntityIdResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | DiscoveryEntitySchema | GetDiscoveryDefaultEntitiesByEntityIdResponseDefault
]:
    """Returns discovery entity


    Required roles:
     - can_read_discovery_entities

    Args:
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DiscoveryEntitySchema | GetDiscoveryDefaultEntitiesByEntityIdResponseDefault]
    """

    kwargs = _get_kwargs(
        entity_id=entity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DiscoveryEntitySchema
    | GetDiscoveryDefaultEntitiesByEntityIdResponseDefault
    | None
):
    """Returns discovery entity


    Required roles:
     - can_read_discovery_entities

    Args:
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DiscoveryEntitySchema | GetDiscoveryDefaultEntitiesByEntityIdResponseDefault
    """

    return sync_detailed(
        entity_id=entity_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | DiscoveryEntitySchema | GetDiscoveryDefaultEntitiesByEntityIdResponseDefault
]:
    """Returns discovery entity


    Required roles:
     - can_read_discovery_entities

    Args:
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DiscoveryEntitySchema | GetDiscoveryDefaultEntitiesByEntityIdResponseDefault]
    """

    kwargs = _get_kwargs(
        entity_id=entity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DiscoveryEntitySchema
    | GetDiscoveryDefaultEntitiesByEntityIdResponseDefault
    | None
):
    """Returns discovery entity


    Required roles:
     - can_read_discovery_entities

    Args:
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DiscoveryEntitySchema | GetDiscoveryDefaultEntitiesByEntityIdResponseDefault
    """

    return (
        await asyncio_detailed(
            entity_id=entity_id,
            client=client,
        )
    ).parsed
