from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.edge_transcode_worker_schema import EdgeTranscodeWorkerSchema
from ...models.post_edge_transcode_workers_response_default import (
    PostEdgeTranscodeWorkersResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: EdgeTranscodeWorkerSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/edge_transcode/workers/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EdgeTranscodeWorkerSchema | PostEdgeTranscodeWorkersResponseDefault:
    if response.status_code == 201:
        response_201 = EdgeTranscodeWorkerSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostEdgeTranscodeWorkersResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | EdgeTranscodeWorkerSchema | PostEdgeTranscodeWorkersResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EdgeTranscodeWorkerSchema,
) -> Response[
    Any | EdgeTranscodeWorkerSchema | PostEdgeTranscodeWorkersResponseDefault
]:
    """Create a new edge transcode worker


    Required roles:
     - is_storage_worker
    - can_write_transcoders

    Args:
        body (EdgeTranscodeWorkerSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EdgeTranscodeWorkerSchema | PostEdgeTranscodeWorkersResponseDefault]
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
    body: EdgeTranscodeWorkerSchema,
) -> Any | EdgeTranscodeWorkerSchema | PostEdgeTranscodeWorkersResponseDefault | None:
    """Create a new edge transcode worker


    Required roles:
     - is_storage_worker
    - can_write_transcoders

    Args:
        body (EdgeTranscodeWorkerSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EdgeTranscodeWorkerSchema | PostEdgeTranscodeWorkersResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EdgeTranscodeWorkerSchema,
) -> Response[
    Any | EdgeTranscodeWorkerSchema | PostEdgeTranscodeWorkersResponseDefault
]:
    """Create a new edge transcode worker


    Required roles:
     - is_storage_worker
    - can_write_transcoders

    Args:
        body (EdgeTranscodeWorkerSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EdgeTranscodeWorkerSchema | PostEdgeTranscodeWorkersResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: EdgeTranscodeWorkerSchema,
) -> Any | EdgeTranscodeWorkerSchema | PostEdgeTranscodeWorkersResponseDefault | None:
    """Create a new edge transcode worker


    Required roles:
     - is_storage_worker
    - can_write_transcoders

    Args:
        body (EdgeTranscodeWorkerSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EdgeTranscodeWorkerSchema | PostEdgeTranscodeWorkersResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
