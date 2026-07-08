from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_assets_segments_reindex_response_default import (
    PostAssetsSegmentsReindexResponseDefault,
)
from ...models.reindex_all_segments_schema import ReindexAllSegmentsSchema
from ...types import Response


def _get_kwargs(
    *,
    body: ReindexAllSegmentsSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/assets/segments/reindex/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostAssetsSegmentsReindexResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostAssetsSegmentsReindexResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostAssetsSegmentsReindexResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReindexAllSegmentsSchema,
) -> Response[Any | PostAssetsSegmentsReindexResponseDefault]:
    """Trigger reindexing of all segments


    Required roles:
     - can_reindex_segments

    Args:
        body (ReindexAllSegmentsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsSegmentsReindexResponseDefault]
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
    body: ReindexAllSegmentsSchema,
) -> Any | PostAssetsSegmentsReindexResponseDefault | None:
    """Trigger reindexing of all segments


    Required roles:
     - can_reindex_segments

    Args:
        body (ReindexAllSegmentsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsSegmentsReindexResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReindexAllSegmentsSchema,
) -> Response[Any | PostAssetsSegmentsReindexResponseDefault]:
    """Trigger reindexing of all segments


    Required roles:
     - can_reindex_segments

    Args:
        body (ReindexAllSegmentsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAssetsSegmentsReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ReindexAllSegmentsSchema,
) -> Any | PostAssetsSegmentsReindexResponseDefault | None:
    """Trigger reindexing of all segments


    Required roles:
     - can_reindex_segments

    Args:
        body (ReindexAllSegmentsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAssetsSegmentsReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
