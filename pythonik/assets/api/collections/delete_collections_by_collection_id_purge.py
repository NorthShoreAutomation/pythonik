from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_collections_by_collection_id_purge_response_default_type_0 import (
    DeleteCollectionsByCollectionIdPurgeResponseDefaultType0,
)
from ...models.delete_collections_by_collection_id_purge_response_default_type_1 import (
    DeleteCollectionsByCollectionIdPurgeResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    collection_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/collections/{collection_id}/purge/".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteCollectionsByCollectionIdPurgeResponseDefaultType0
    | DeleteCollectionsByCollectionIdPurgeResponseDefaultType1
):
    if response.status_code == 202:
        response_202 = cast(Any, None)
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

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteCollectionsByCollectionIdPurgeResponseDefaultType0
        | DeleteCollectionsByCollectionIdPurgeResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteCollectionsByCollectionIdPurgeResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteCollectionsByCollectionIdPurgeResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteCollectionsByCollectionIdPurgeResponseDefaultType0
    | DeleteCollectionsByCollectionIdPurgeResponseDefaultType1
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
    | DeleteCollectionsByCollectionIdPurgeResponseDefaultType0
    | DeleteCollectionsByCollectionIdPurgeResponseDefaultType1
]:
    """Purges deleted collection by id immediately


    Required roles:
     - can_purge_collections

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteCollectionsByCollectionIdPurgeResponseDefaultType0 | DeleteCollectionsByCollectionIdPurgeResponseDefaultType1]
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
    | DeleteCollectionsByCollectionIdPurgeResponseDefaultType0
    | DeleteCollectionsByCollectionIdPurgeResponseDefaultType1
    | None
):
    """Purges deleted collection by id immediately


    Required roles:
     - can_purge_collections

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteCollectionsByCollectionIdPurgeResponseDefaultType0 | DeleteCollectionsByCollectionIdPurgeResponseDefaultType1
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
    | DeleteCollectionsByCollectionIdPurgeResponseDefaultType0
    | DeleteCollectionsByCollectionIdPurgeResponseDefaultType1
]:
    """Purges deleted collection by id immediately


    Required roles:
     - can_purge_collections

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteCollectionsByCollectionIdPurgeResponseDefaultType0 | DeleteCollectionsByCollectionIdPurgeResponseDefaultType1]
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
    | DeleteCollectionsByCollectionIdPurgeResponseDefaultType0
    | DeleteCollectionsByCollectionIdPurgeResponseDefaultType1
    | None
):
    """Purges deleted collection by id immediately


    Required roles:
     - can_purge_collections

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteCollectionsByCollectionIdPurgeResponseDefaultType0 | DeleteCollectionsByCollectionIdPurgeResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
        )
    ).parsed
