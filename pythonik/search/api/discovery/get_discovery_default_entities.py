from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.discovery_entities_schema import DiscoveryEntitiesSchema
from ...models.get_discovery_default_entities_response_default_type_0 import (
    GetDiscoveryDefaultEntitiesResponseDefaultType0,
)
from ...models.get_discovery_default_entities_response_default_type_1 import (
    GetDiscoveryDefaultEntitiesResponseDefaultType1,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/discovery/default/entities/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DiscoveryEntitiesSchema
    | GetDiscoveryDefaultEntitiesResponseDefaultType0
    | GetDiscoveryDefaultEntitiesResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = DiscoveryEntitiesSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetDiscoveryDefaultEntitiesResponseDefaultType0
        | GetDiscoveryDefaultEntitiesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetDiscoveryDefaultEntitiesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetDiscoveryDefaultEntitiesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DiscoveryEntitiesSchema
    | GetDiscoveryDefaultEntitiesResponseDefaultType0
    | GetDiscoveryDefaultEntitiesResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DiscoveryEntitiesSchema
    | GetDiscoveryDefaultEntitiesResponseDefaultType0
    | GetDiscoveryDefaultEntitiesResponseDefaultType1
]:
    """Returns the discovery entities that are used to build the discovery view.


    Required roles:
     - can_read_discovery_entities

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DiscoveryEntitiesSchema | GetDiscoveryDefaultEntitiesResponseDefaultType0 | GetDiscoveryDefaultEntitiesResponseDefaultType1]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DiscoveryEntitiesSchema
    | GetDiscoveryDefaultEntitiesResponseDefaultType0
    | GetDiscoveryDefaultEntitiesResponseDefaultType1
    | None
):
    """Returns the discovery entities that are used to build the discovery view.


    Required roles:
     - can_read_discovery_entities

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DiscoveryEntitiesSchema | GetDiscoveryDefaultEntitiesResponseDefaultType0 | GetDiscoveryDefaultEntitiesResponseDefaultType1
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DiscoveryEntitiesSchema
    | GetDiscoveryDefaultEntitiesResponseDefaultType0
    | GetDiscoveryDefaultEntitiesResponseDefaultType1
]:
    """Returns the discovery entities that are used to build the discovery view.


    Required roles:
     - can_read_discovery_entities

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DiscoveryEntitiesSchema | GetDiscoveryDefaultEntitiesResponseDefaultType0 | GetDiscoveryDefaultEntitiesResponseDefaultType1]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DiscoveryEntitiesSchema
    | GetDiscoveryDefaultEntitiesResponseDefaultType0
    | GetDiscoveryDefaultEntitiesResponseDefaultType1
    | None
):
    """Returns the discovery entities that are used to build the discovery view.


    Required roles:
     - can_read_discovery_entities

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DiscoveryEntitiesSchema | GetDiscoveryDefaultEntitiesResponseDefaultType0 | GetDiscoveryDefaultEntitiesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
