from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_delete_queue_collections_purge_all_response_default import (
    PostDeleteQueueCollectionsPurgeAllResponseDefault,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/delete_queue/collections/purge/all/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostDeleteQueueCollectionsPurgeAllResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    response_default = PostDeleteQueueCollectionsPurgeAllResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostDeleteQueueCollectionsPurgeAllResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PostDeleteQueueCollectionsPurgeAllResponseDefault]:
    """Purge all collections from delete queue (Permanently delete)


    Required roles:
     - can_purge_collections

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostDeleteQueueCollectionsPurgeAllResponseDefault]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Any | PostDeleteQueueCollectionsPurgeAllResponseDefault | None:
    """Purge all collections from delete queue (Permanently delete)


    Required roles:
     - can_purge_collections

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostDeleteQueueCollectionsPurgeAllResponseDefault
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PostDeleteQueueCollectionsPurgeAllResponseDefault]:
    """Purge all collections from delete queue (Permanently delete)


    Required roles:
     - can_purge_collections

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostDeleteQueueCollectionsPurgeAllResponseDefault]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | PostDeleteQueueCollectionsPurgeAllResponseDefault | None:
    """Purge all collections from delete queue (Permanently delete)


    Required roles:
     - can_purge_collections

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostDeleteQueueCollectionsPurgeAllResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
