from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.collection_contents_schema import CollectionContentsSchema
from ...models.get_collections_by_collection_id_contents_response_default import (
    GetCollectionsByCollectionIdContentsResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    *,
    object_types: str | Unset = UNSET,
    object_ids: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    include_keyframes: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["object_types"] = object_types

    params["object_ids"] = object_ids

    params["external_id"] = external_id

    params["per_page"] = per_page

    params["page"] = page

    params["sort"] = sort

    params["filter"] = filter_

    params["include_keyframes"] = include_keyframes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections/{collection_id}/contents/".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any | CollectionContentsSchema | GetCollectionsByCollectionIdContentsResponseDefault
):
    if response.status_code == 200:
        response_200 = CollectionContentsSchema.from_dict(response.json())

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

    response_default = GetCollectionsByCollectionIdContentsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | CollectionContentsSchema | GetCollectionsByCollectionIdContentsResponseDefault
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
    object_types: str | Unset = UNSET,
    object_ids: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    include_keyframes: bool | Unset = UNSET,
) -> Response[
    Any | CollectionContentsSchema | GetCollectionsByCollectionIdContentsResponseDefault
]:
    """Returns contents of a collection by id


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        object_types (str | Unset):
        object_ids (str | Unset):
        external_id (str | Unset):
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):
        filter_ (str | Unset):
        include_keyframes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionContentsSchema | GetCollectionsByCollectionIdContentsResponseDefault]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        object_types=object_types,
        object_ids=object_ids,
        external_id=external_id,
        per_page=per_page,
        page=page,
        sort=sort,
        filter_=filter_,
        include_keyframes=include_keyframes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    object_types: str | Unset = UNSET,
    object_ids: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    include_keyframes: bool | Unset = UNSET,
) -> (
    Any
    | CollectionContentsSchema
    | GetCollectionsByCollectionIdContentsResponseDefault
    | None
):
    """Returns contents of a collection by id


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        object_types (str | Unset):
        object_ids (str | Unset):
        external_id (str | Unset):
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):
        filter_ (str | Unset):
        include_keyframes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionContentsSchema | GetCollectionsByCollectionIdContentsResponseDefault
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        object_types=object_types,
        object_ids=object_ids,
        external_id=external_id,
        per_page=per_page,
        page=page,
        sort=sort,
        filter_=filter_,
        include_keyframes=include_keyframes,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    object_types: str | Unset = UNSET,
    object_ids: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    include_keyframes: bool | Unset = UNSET,
) -> Response[
    Any | CollectionContentsSchema | GetCollectionsByCollectionIdContentsResponseDefault
]:
    """Returns contents of a collection by id


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        object_types (str | Unset):
        object_ids (str | Unset):
        external_id (str | Unset):
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):
        filter_ (str | Unset):
        include_keyframes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionContentsSchema | GetCollectionsByCollectionIdContentsResponseDefault]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        object_types=object_types,
        object_ids=object_ids,
        external_id=external_id,
        per_page=per_page,
        page=page,
        sort=sort,
        filter_=filter_,
        include_keyframes=include_keyframes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    object_types: str | Unset = UNSET,
    object_ids: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    include_keyframes: bool | Unset = UNSET,
) -> (
    Any
    | CollectionContentsSchema
    | GetCollectionsByCollectionIdContentsResponseDefault
    | None
):
    """Returns contents of a collection by id


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        object_types (str | Unset):
        object_ids (str | Unset):
        external_id (str | Unset):
        per_page (int | Unset):
        page (int | Unset):
        sort (str | Unset):
        filter_ (str | Unset):
        include_keyframes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionContentsSchema | GetCollectionsByCollectionIdContentsResponseDefault
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            object_types=object_types,
            object_ids=object_ids,
            external_id=external_id,
            per_page=per_page,
            page=page,
            sort=sort,
            filter_=filter_,
            include_keyframes=include_keyframes,
        )
    ).parsed
