from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_discovery_default_entities_by_entity_id_response_default_type_0 import (
    DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0,
)
from ...models.delete_discovery_default_entities_by_entity_id_response_default_type_1 import (
    DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    entity_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/discovery/default/entities/{entity_id}/".format(
            entity_id=quote(str(entity_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0
    | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0
        | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0
    | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1
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
    Any
    | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0
    | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1
]:
    """Delete a discovery entity by id


    Required roles:
     - can_delete_discovery_entities

    Args:
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0 | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1]
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
    | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0
    | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1
    | None
):
    """Delete a discovery entity by id


    Required roles:
     - can_delete_discovery_entities

    Args:
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0 | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1
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
    Any
    | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0
    | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1
]:
    """Delete a discovery entity by id


    Required roles:
     - can_delete_discovery_entities

    Args:
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0 | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1]
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
    | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0
    | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1
    | None
):
    """Delete a discovery entity by id


    Required roles:
     - can_delete_discovery_entities

    Args:
        entity_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType0 | DeleteDiscoveryDefaultEntitiesByEntityIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            entity_id=entity_id,
            client=client,
        )
    ).parsed
