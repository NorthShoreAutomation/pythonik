from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.collection_input_schema import CollectionInputSchema
from ...models.collection_schema import CollectionSchema
from ...models.put_collections_by_collection_id_response_default import (
    PutCollectionsByCollectionIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    *,
    body: CollectionInputSchema,
    change_parent_mode: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["change_parent_mode"] = change_parent_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/collections/{collection_id}/".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CollectionSchema | PutCollectionsByCollectionIdResponseDefault:
    if response.status_code == 200:
        response_200 = CollectionSchema.from_dict(response.json())

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

    response_default = PutCollectionsByCollectionIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CollectionSchema | PutCollectionsByCollectionIdResponseDefault]:
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
    body: CollectionInputSchema,
    change_parent_mode: str | Unset = UNSET,
) -> Response[Any | CollectionSchema | PutCollectionsByCollectionIdResponseDefault]:
    """Update collection


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        change_parent_mode (str | Unset):
        body (CollectionInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionSchema | PutCollectionsByCollectionIdResponseDefault]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
        change_parent_mode=change_parent_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionInputSchema,
    change_parent_mode: str | Unset = UNSET,
) -> Any | CollectionSchema | PutCollectionsByCollectionIdResponseDefault | None:
    """Update collection


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        change_parent_mode (str | Unset):
        body (CollectionInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionSchema | PutCollectionsByCollectionIdResponseDefault
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        body=body,
        change_parent_mode=change_parent_mode,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionInputSchema,
    change_parent_mode: str | Unset = UNSET,
) -> Response[Any | CollectionSchema | PutCollectionsByCollectionIdResponseDefault]:
    """Update collection


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        change_parent_mode (str | Unset):
        body (CollectionInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionSchema | PutCollectionsByCollectionIdResponseDefault]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
        change_parent_mode=change_parent_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionInputSchema,
    change_parent_mode: str | Unset = UNSET,
) -> Any | CollectionSchema | PutCollectionsByCollectionIdResponseDefault | None:
    """Update collection


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        change_parent_mode (str | Unset):
        body (CollectionInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionSchema | PutCollectionsByCollectionIdResponseDefault
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            body=body,
            change_parent_mode=change_parent_mode,
        )
    ).parsed
