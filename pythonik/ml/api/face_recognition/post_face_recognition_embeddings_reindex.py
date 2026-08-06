from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_face_recognition_embeddings_reindex_response_default import (
    PostFaceRecognitionEmbeddingsReindexResponseDefault,
)
from ...models.reindex_all_embeddings_schema import ReindexAllEmbeddingsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ReindexAllEmbeddingsSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/face_recognition/embeddings/reindex/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostFaceRecognitionEmbeddingsReindexResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostFaceRecognitionEmbeddingsReindexResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostFaceRecognitionEmbeddingsReindexResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReindexAllEmbeddingsSchema | Unset = UNSET,
) -> Response[Any | PostFaceRecognitionEmbeddingsReindexResponseDefault]:
    """Trigger reindexing of all embeddings


    Required roles:
     - can_reindex_person

    Args:
        body (ReindexAllEmbeddingsSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionEmbeddingsReindexResponseDefault]
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
    body: ReindexAllEmbeddingsSchema | Unset = UNSET,
) -> Any | PostFaceRecognitionEmbeddingsReindexResponseDefault | None:
    """Trigger reindexing of all embeddings


    Required roles:
     - can_reindex_person

    Args:
        body (ReindexAllEmbeddingsSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionEmbeddingsReindexResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReindexAllEmbeddingsSchema | Unset = UNSET,
) -> Response[Any | PostFaceRecognitionEmbeddingsReindexResponseDefault]:
    """Trigger reindexing of all embeddings


    Required roles:
     - can_reindex_person

    Args:
        body (ReindexAllEmbeddingsSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionEmbeddingsReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ReindexAllEmbeddingsSchema | Unset = UNSET,
) -> Any | PostFaceRecognitionEmbeddingsReindexResponseDefault | None:
    """Trigger reindexing of all embeddings


    Required roles:
     - can_reindex_person

    Args:
        body (ReindexAllEmbeddingsSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionEmbeddingsReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
