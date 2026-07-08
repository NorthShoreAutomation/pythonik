from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.collection_keyframe_schema import CollectionKeyframeSchema
from ...models.post_collections_by_collection_id_custom_keyframe_by_poster_id_response_default import (
    PostCollectionsByCollectionIdCustomKeyframeByPosterIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    poster_id: str,
    *,
    overwrite: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["overwrite"] = overwrite

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/collections/{collection_id}/custom_keyframe/{poster_id}/".format(
            collection_id=quote(str(collection_id), safe=""),
            poster_id=quote(str(poster_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | CollectionKeyframeSchema
    | PostCollectionsByCollectionIdCustomKeyframeByPosterIdResponseDefault
):
    if response.status_code == 201:
        response_201 = CollectionKeyframeSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = (
        PostCollectionsByCollectionIdCustomKeyframeByPosterIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | CollectionKeyframeSchema
    | PostCollectionsByCollectionIdCustomKeyframeByPosterIdResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: str,
    poster_id: str,
    *,
    client: AuthenticatedClient | Client,
    overwrite: bool | Unset = UNSET,
) -> Response[
    Any
    | CollectionKeyframeSchema
    | PostCollectionsByCollectionIdCustomKeyframeByPosterIdResponseDefault
]:
    """Set keyframe of type poster as collection keyframe


    Required roles:
     - can_write_keyframes

    Args:
        collection_id (str):
        poster_id (str):
        overwrite (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionKeyframeSchema | PostCollectionsByCollectionIdCustomKeyframeByPosterIdResponseDefault]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        poster_id=poster_id,
        overwrite=overwrite,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    poster_id: str,
    *,
    client: AuthenticatedClient | Client,
    overwrite: bool | Unset = UNSET,
) -> (
    Any
    | CollectionKeyframeSchema
    | PostCollectionsByCollectionIdCustomKeyframeByPosterIdResponseDefault
    | None
):
    """Set keyframe of type poster as collection keyframe


    Required roles:
     - can_write_keyframes

    Args:
        collection_id (str):
        poster_id (str):
        overwrite (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionKeyframeSchema | PostCollectionsByCollectionIdCustomKeyframeByPosterIdResponseDefault
    """

    return sync_detailed(
        collection_id=collection_id,
        poster_id=poster_id,
        client=client,
        overwrite=overwrite,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    poster_id: str,
    *,
    client: AuthenticatedClient | Client,
    overwrite: bool | Unset = UNSET,
) -> Response[
    Any
    | CollectionKeyframeSchema
    | PostCollectionsByCollectionIdCustomKeyframeByPosterIdResponseDefault
]:
    """Set keyframe of type poster as collection keyframe


    Required roles:
     - can_write_keyframes

    Args:
        collection_id (str):
        poster_id (str):
        overwrite (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionKeyframeSchema | PostCollectionsByCollectionIdCustomKeyframeByPosterIdResponseDefault]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        poster_id=poster_id,
        overwrite=overwrite,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    poster_id: str,
    *,
    client: AuthenticatedClient | Client,
    overwrite: bool | Unset = UNSET,
) -> (
    Any
    | CollectionKeyframeSchema
    | PostCollectionsByCollectionIdCustomKeyframeByPosterIdResponseDefault
    | None
):
    """Set keyframe of type poster as collection keyframe


    Required roles:
     - can_write_keyframes

    Args:
        collection_id (str):
        poster_id (str):
        overwrite (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionKeyframeSchema | PostCollectionsByCollectionIdCustomKeyframeByPosterIdResponseDefault
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            poster_id=poster_id,
            client=client,
            overwrite=overwrite,
        )
    ).parsed
