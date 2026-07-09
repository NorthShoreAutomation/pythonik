from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.collection_size_schema import CollectionSizeSchema
from ...models.get_collections_by_collection_id_size_response_default import (
    GetCollectionsByCollectionIdSizeResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    *,
    format_name: str | Unset = UNSET,
    include_subcollections: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["format_name"] = format_name

    params["include_subcollections"] = include_subcollections

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections/{collection_id}/size/".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CollectionSizeSchema | GetCollectionsByCollectionIdSizeResponseDefault:
    if response.status_code == 200:
        response_200 = CollectionSizeSchema.from_dict(response.json())

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

    response_default = GetCollectionsByCollectionIdSizeResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | CollectionSizeSchema | GetCollectionsByCollectionIdSizeResponseDefault
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
    format_name: str | Unset = UNSET,
    include_subcollections: bool | Unset = UNSET,
) -> Response[
    Any | CollectionSizeSchema | GetCollectionsByCollectionIdSizeResponseDefault
]:
    """Returns the size of all the collection's assets in bytes


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        format_name (str | Unset):
        include_subcollections (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionSizeSchema | GetCollectionsByCollectionIdSizeResponseDefault]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        format_name=format_name,
        include_subcollections=include_subcollections,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    format_name: str | Unset = UNSET,
    include_subcollections: bool | Unset = UNSET,
) -> (
    Any | CollectionSizeSchema | GetCollectionsByCollectionIdSizeResponseDefault | None
):
    """Returns the size of all the collection's assets in bytes


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        format_name (str | Unset):
        include_subcollections (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionSizeSchema | GetCollectionsByCollectionIdSizeResponseDefault
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        format_name=format_name,
        include_subcollections=include_subcollections,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    format_name: str | Unset = UNSET,
    include_subcollections: bool | Unset = UNSET,
) -> Response[
    Any | CollectionSizeSchema | GetCollectionsByCollectionIdSizeResponseDefault
]:
    """Returns the size of all the collection's assets in bytes


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        format_name (str | Unset):
        include_subcollections (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionSizeSchema | GetCollectionsByCollectionIdSizeResponseDefault]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        format_name=format_name,
        include_subcollections=include_subcollections,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    format_name: str | Unset = UNSET,
    include_subcollections: bool | Unset = UNSET,
) -> (
    Any | CollectionSizeSchema | GetCollectionsByCollectionIdSizeResponseDefault | None
):
    """Returns the size of all the collection's assets in bytes


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        format_name (str | Unset):
        include_subcollections (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionSizeSchema | GetCollectionsByCollectionIdSizeResponseDefault
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            format_name=format_name,
            include_subcollections=include_subcollections,
        )
    ).parsed
