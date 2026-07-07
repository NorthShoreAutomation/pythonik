from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.generate_collection_keyframe_schema import (
    GenerateCollectionKeyframeSchema,
)
from ...models.post_keyframes_collections_by_collection_id_response_default_type_0 import (
    PostKeyframesCollectionsByCollectionIdResponseDefaultType0,
)
from ...models.post_keyframes_collections_by_collection_id_response_default_type_1 import (
    PostKeyframesCollectionsByCollectionIdResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    *,
    body: GenerateCollectionKeyframeSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/keyframes/collections/{collection_id}/".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostKeyframesCollectionsByCollectionIdResponseDefaultType0
    | PostKeyframesCollectionsByCollectionIdResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
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
        PostKeyframesCollectionsByCollectionIdResponseDefaultType0
        | PostKeyframesCollectionsByCollectionIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostKeyframesCollectionsByCollectionIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostKeyframesCollectionsByCollectionIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostKeyframesCollectionsByCollectionIdResponseDefaultType0
    | PostKeyframesCollectionsByCollectionIdResponseDefaultType1
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
    body: GenerateCollectionKeyframeSchema | Unset = UNSET,
) -> Response[
    Any
    | PostKeyframesCollectionsByCollectionIdResponseDefaultType0
    | PostKeyframesCollectionsByCollectionIdResponseDefaultType1
]:
    """Start a job that creates a collection keyframe


    Required roles:
     - can_write_transcode_jobs

    Args:
        collection_id (str):
        body (GenerateCollectionKeyframeSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostKeyframesCollectionsByCollectionIdResponseDefaultType0 | PostKeyframesCollectionsByCollectionIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateCollectionKeyframeSchema | Unset = UNSET,
) -> (
    Any
    | PostKeyframesCollectionsByCollectionIdResponseDefaultType0
    | PostKeyframesCollectionsByCollectionIdResponseDefaultType1
    | None
):
    """Start a job that creates a collection keyframe


    Required roles:
     - can_write_transcode_jobs

    Args:
        collection_id (str):
        body (GenerateCollectionKeyframeSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostKeyframesCollectionsByCollectionIdResponseDefaultType0 | PostKeyframesCollectionsByCollectionIdResponseDefaultType1
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateCollectionKeyframeSchema | Unset = UNSET,
) -> Response[
    Any
    | PostKeyframesCollectionsByCollectionIdResponseDefaultType0
    | PostKeyframesCollectionsByCollectionIdResponseDefaultType1
]:
    """Start a job that creates a collection keyframe


    Required roles:
     - can_write_transcode_jobs

    Args:
        collection_id (str):
        body (GenerateCollectionKeyframeSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostKeyframesCollectionsByCollectionIdResponseDefaultType0 | PostKeyframesCollectionsByCollectionIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GenerateCollectionKeyframeSchema | Unset = UNSET,
) -> (
    Any
    | PostKeyframesCollectionsByCollectionIdResponseDefaultType0
    | PostKeyframesCollectionsByCollectionIdResponseDefaultType1
    | None
):
    """Start a job that creates a collection keyframe


    Required roles:
     - can_write_transcode_jobs

    Args:
        collection_id (str):
        body (GenerateCollectionKeyframeSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostKeyframesCollectionsByCollectionIdResponseDefaultType0 | PostKeyframesCollectionsByCollectionIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            body=body,
        )
    ).parsed
