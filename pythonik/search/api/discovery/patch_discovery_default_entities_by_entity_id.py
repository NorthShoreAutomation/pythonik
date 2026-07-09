from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.discovery_entity_schema import DiscoveryEntitySchema
from ...models.patch_discovery_default_entities_by_entity_id_response_default import (
    PatchDiscoveryDefaultEntitiesByEntityIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    entity_id: str,
    *,
    body: DiscoveryEntitySchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/discovery/default/entities/{entity_id}/".format(
            entity_id=quote(str(entity_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchDiscoveryDefaultEntitiesByEntityIdResponseDefault:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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

    response_default = PatchDiscoveryDefaultEntitiesByEntityIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PatchDiscoveryDefaultEntitiesByEntityIdResponseDefault]:
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
    body: DiscoveryEntitySchema,
) -> Response[Any | PatchDiscoveryDefaultEntitiesByEntityIdResponseDefault]:
    """Update a discovery entity by id


    Required roles:
     - can_write_discovery_entities

    Args:
        entity_id (str):
        body (DiscoveryEntitySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchDiscoveryDefaultEntitiesByEntityIdResponseDefault]
    """

    kwargs = _get_kwargs(
        entity_id=entity_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DiscoveryEntitySchema,
) -> Any | PatchDiscoveryDefaultEntitiesByEntityIdResponseDefault | None:
    """Update a discovery entity by id


    Required roles:
     - can_write_discovery_entities

    Args:
        entity_id (str):
        body (DiscoveryEntitySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchDiscoveryDefaultEntitiesByEntityIdResponseDefault
    """

    return sync_detailed(
        entity_id=entity_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DiscoveryEntitySchema,
) -> Response[Any | PatchDiscoveryDefaultEntitiesByEntityIdResponseDefault]:
    """Update a discovery entity by id


    Required roles:
     - can_write_discovery_entities

    Args:
        entity_id (str):
        body (DiscoveryEntitySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchDiscoveryDefaultEntitiesByEntityIdResponseDefault]
    """

    kwargs = _get_kwargs(
        entity_id=entity_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entity_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: DiscoveryEntitySchema,
) -> Any | PatchDiscoveryDefaultEntitiesByEntityIdResponseDefault | None:
    """Update a discovery entity by id


    Required roles:
     - can_write_discovery_entities

    Args:
        entity_id (str):
        body (DiscoveryEntitySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchDiscoveryDefaultEntitiesByEntityIdResponseDefault
    """

    return (
        await asyncio_detailed(
            entity_id=entity_id,
            client=client,
            body=body,
        )
    ).parsed
