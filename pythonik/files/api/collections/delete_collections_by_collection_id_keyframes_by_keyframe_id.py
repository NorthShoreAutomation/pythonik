from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_collections_by_collection_id_keyframes_by_keyframe_id_response_default_type_0 import (
    DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0,
)
from ...models.delete_collections_by_collection_id_keyframes_by_keyframe_id_response_default_type_1 import (
    DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    keyframe_id: str,
    *,
    regenerate_keyframes: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["regenerate_keyframes"] = regenerate_keyframes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/collections/{collection_id}/keyframes/{keyframe_id}/".format(
            collection_id=quote(str(collection_id), safe=""),
            keyframe_id=quote(str(keyframe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0
    | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1
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
        DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0
        | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0
    | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
    regenerate_keyframes: bool | Unset = UNSET,
) -> Response[
    Any
    | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0
    | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1
]:
    """Delete collection's keyframe


    Required roles:
     - can_write_keyframes

    Args:
        collection_id (str):
        keyframe_id (str):
        regenerate_keyframes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0 | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        keyframe_id=keyframe_id,
        regenerate_keyframes=regenerate_keyframes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
    regenerate_keyframes: bool | Unset = UNSET,
) -> (
    Any
    | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0
    | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1
    | None
):
    """Delete collection's keyframe


    Required roles:
     - can_write_keyframes

    Args:
        collection_id (str):
        keyframe_id (str):
        regenerate_keyframes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0 | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1
    """

    return sync_detailed(
        collection_id=collection_id,
        keyframe_id=keyframe_id,
        client=client,
        regenerate_keyframes=regenerate_keyframes,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
    regenerate_keyframes: bool | Unset = UNSET,
) -> Response[
    Any
    | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0
    | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1
]:
    """Delete collection's keyframe


    Required roles:
     - can_write_keyframes

    Args:
        collection_id (str):
        keyframe_id (str):
        regenerate_keyframes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0 | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        keyframe_id=keyframe_id,
        regenerate_keyframes=regenerate_keyframes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
    regenerate_keyframes: bool | Unset = UNSET,
) -> (
    Any
    | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0
    | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1
    | None
):
    """Delete collection's keyframe


    Required roles:
     - can_write_keyframes

    Args:
        collection_id (str):
        keyframe_id (str):
        regenerate_keyframes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType0 | DeleteCollectionsByCollectionIdKeyframesByKeyframeIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            keyframe_id=keyframe_id,
            client=client,
            regenerate_keyframes=regenerate_keyframes,
        )
    ).parsed
