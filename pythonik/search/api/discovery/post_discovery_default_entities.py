from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.discovery_entity_schema import DiscoveryEntitySchema
from ...models.post_discovery_default_entities_response_default_type_0 import (
    PostDiscoveryDefaultEntitiesResponseDefaultType0,
)
from ...models.post_discovery_default_entities_response_default_type_1 import (
    PostDiscoveryDefaultEntitiesResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    *,
    body: DiscoveryEntitySchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/discovery/default/entities/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DiscoveryEntitySchema
    | PostDiscoveryDefaultEntitiesResponseDefaultType0
    | PostDiscoveryDefaultEntitiesResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = DiscoveryEntitySchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostDiscoveryDefaultEntitiesResponseDefaultType0
        | PostDiscoveryDefaultEntitiesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostDiscoveryDefaultEntitiesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostDiscoveryDefaultEntitiesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DiscoveryEntitySchema
    | PostDiscoveryDefaultEntitiesResponseDefaultType0
    | PostDiscoveryDefaultEntitiesResponseDefaultType1
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
    body: DiscoveryEntitySchema,
) -> Response[
    Any
    | DiscoveryEntitySchema
    | PostDiscoveryDefaultEntitiesResponseDefaultType0
    | PostDiscoveryDefaultEntitiesResponseDefaultType1
]:
    """Adds a new discovery entity.

     <br/>This creates an entry for the discovery view to show collections and saved searches.<br/>Object
    Type should be one of COLLECTION, SAVED_SEARCH, ASSET, RECOMMENDATION or TRENDING<br/>Object ID is
    only needed in the case of COLLECTION, SAVED_SEARCH or ASSET<br/>metadata is for user defined extra
    data.<br/><br/>This creates an entry for the discovery view to show collections and saved
    searches.<br/>Object Type should be one of COLLECTION, SAVED_SEARCH, ASSET, RECOMMENDATION or
    TRENDING<br/>Object ID is only needed in the case of COLLECTION, SAVED_SEARCH or ASSET<br/>metadata
    is for user defined extra data.<br/>
    Required roles:
     - can_write_discovery_entities

    Args:
        body (DiscoveryEntitySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DiscoveryEntitySchema | PostDiscoveryDefaultEntitiesResponseDefaultType0 | PostDiscoveryDefaultEntitiesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: DiscoveryEntitySchema,
) -> (
    Any
    | DiscoveryEntitySchema
    | PostDiscoveryDefaultEntitiesResponseDefaultType0
    | PostDiscoveryDefaultEntitiesResponseDefaultType1
    | None
):
    """Adds a new discovery entity.

     <br/>This creates an entry for the discovery view to show collections and saved searches.<br/>Object
    Type should be one of COLLECTION, SAVED_SEARCH, ASSET, RECOMMENDATION or TRENDING<br/>Object ID is
    only needed in the case of COLLECTION, SAVED_SEARCH or ASSET<br/>metadata is for user defined extra
    data.<br/><br/>This creates an entry for the discovery view to show collections and saved
    searches.<br/>Object Type should be one of COLLECTION, SAVED_SEARCH, ASSET, RECOMMENDATION or
    TRENDING<br/>Object ID is only needed in the case of COLLECTION, SAVED_SEARCH or ASSET<br/>metadata
    is for user defined extra data.<br/>
    Required roles:
     - can_write_discovery_entities

    Args:
        body (DiscoveryEntitySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DiscoveryEntitySchema | PostDiscoveryDefaultEntitiesResponseDefaultType0 | PostDiscoveryDefaultEntitiesResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DiscoveryEntitySchema,
) -> Response[
    Any
    | DiscoveryEntitySchema
    | PostDiscoveryDefaultEntitiesResponseDefaultType0
    | PostDiscoveryDefaultEntitiesResponseDefaultType1
]:
    """Adds a new discovery entity.

     <br/>This creates an entry for the discovery view to show collections and saved searches.<br/>Object
    Type should be one of COLLECTION, SAVED_SEARCH, ASSET, RECOMMENDATION or TRENDING<br/>Object ID is
    only needed in the case of COLLECTION, SAVED_SEARCH or ASSET<br/>metadata is for user defined extra
    data.<br/><br/>This creates an entry for the discovery view to show collections and saved
    searches.<br/>Object Type should be one of COLLECTION, SAVED_SEARCH, ASSET, RECOMMENDATION or
    TRENDING<br/>Object ID is only needed in the case of COLLECTION, SAVED_SEARCH or ASSET<br/>metadata
    is for user defined extra data.<br/>
    Required roles:
     - can_write_discovery_entities

    Args:
        body (DiscoveryEntitySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DiscoveryEntitySchema | PostDiscoveryDefaultEntitiesResponseDefaultType0 | PostDiscoveryDefaultEntitiesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DiscoveryEntitySchema,
) -> (
    Any
    | DiscoveryEntitySchema
    | PostDiscoveryDefaultEntitiesResponseDefaultType0
    | PostDiscoveryDefaultEntitiesResponseDefaultType1
    | None
):
    """Adds a new discovery entity.

     <br/>This creates an entry for the discovery view to show collections and saved searches.<br/>Object
    Type should be one of COLLECTION, SAVED_SEARCH, ASSET, RECOMMENDATION or TRENDING<br/>Object ID is
    only needed in the case of COLLECTION, SAVED_SEARCH or ASSET<br/>metadata is for user defined extra
    data.<br/><br/>This creates an entry for the discovery view to show collections and saved
    searches.<br/>Object Type should be one of COLLECTION, SAVED_SEARCH, ASSET, RECOMMENDATION or
    TRENDING<br/>Object ID is only needed in the case of COLLECTION, SAVED_SEARCH or ASSET<br/>metadata
    is for user defined extra data.<br/>
    Required roles:
     - can_write_discovery_entities

    Args:
        body (DiscoveryEntitySchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DiscoveryEntitySchema | PostDiscoveryDefaultEntitiesResponseDefaultType0 | PostDiscoveryDefaultEntitiesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
