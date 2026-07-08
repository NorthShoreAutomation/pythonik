from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_collections_by_collection_id_restore_response_202 import (
    PutCollectionsByCollectionIdRestoreResponse202,
)
from ...models.put_collections_by_collection_id_restore_response_default import (
    PutCollectionsByCollectionIdRestoreResponseDefault,
)
from ...types import Response


def _get_kwargs(
    collection_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/collections/{collection_id}/restore/".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PutCollectionsByCollectionIdRestoreResponse202
    | PutCollectionsByCollectionIdRestoreResponseDefault
):
    if response.status_code == 202:
        response_202 = PutCollectionsByCollectionIdRestoreResponse202.from_dict(
            response.json()
        )

        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PutCollectionsByCollectionIdRestoreResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PutCollectionsByCollectionIdRestoreResponse202
    | PutCollectionsByCollectionIdRestoreResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PutCollectionsByCollectionIdRestoreResponse202
    | PutCollectionsByCollectionIdRestoreResponseDefault
]:
    """Restore deleted collection by id


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutCollectionsByCollectionIdRestoreResponse202 | PutCollectionsByCollectionIdRestoreResponseDefault]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PutCollectionsByCollectionIdRestoreResponse202
    | PutCollectionsByCollectionIdRestoreResponseDefault
    | None
):
    """Restore deleted collection by id


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutCollectionsByCollectionIdRestoreResponse202 | PutCollectionsByCollectionIdRestoreResponseDefault
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PutCollectionsByCollectionIdRestoreResponse202
    | PutCollectionsByCollectionIdRestoreResponseDefault
]:
    """Restore deleted collection by id


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutCollectionsByCollectionIdRestoreResponse202 | PutCollectionsByCollectionIdRestoreResponseDefault]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PutCollectionsByCollectionIdRestoreResponse202
    | PutCollectionsByCollectionIdRestoreResponseDefault
    | None
):
    """Restore deleted collection by id


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutCollectionsByCollectionIdRestoreResponse202 | PutCollectionsByCollectionIdRestoreResponseDefault
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
        )
    ).parsed
