from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.edge_transcode_worker_schema import EdgeTranscodeWorkerSchema
from ...models.put_edge_transcode_workers_by_worker_id_response_default import (
    PutEdgeTranscodeWorkersByWorkerIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    worker_id: str,
    *,
    body: EdgeTranscodeWorkerSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/edge_transcode/workers/{worker_id}/".format(
            worker_id=quote(str(worker_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EdgeTranscodeWorkerSchema | PutEdgeTranscodeWorkersByWorkerIdResponseDefault:
    if response.status_code == 201:
        response_201 = EdgeTranscodeWorkerSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PutEdgeTranscodeWorkersByWorkerIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | EdgeTranscodeWorkerSchema | PutEdgeTranscodeWorkersByWorkerIdResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    worker_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EdgeTranscodeWorkerSchema,
) -> Response[
    Any | EdgeTranscodeWorkerSchema | PutEdgeTranscodeWorkersByWorkerIdResponseDefault
]:
    """Update a edge transcode worker


    Required roles:
     - is_storage_worker
    - can_write_transcoders

    Args:
        worker_id (str):
        body (EdgeTranscodeWorkerSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EdgeTranscodeWorkerSchema | PutEdgeTranscodeWorkersByWorkerIdResponseDefault]
    """

    kwargs = _get_kwargs(
        worker_id=worker_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    worker_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EdgeTranscodeWorkerSchema,
) -> (
    Any
    | EdgeTranscodeWorkerSchema
    | PutEdgeTranscodeWorkersByWorkerIdResponseDefault
    | None
):
    """Update a edge transcode worker


    Required roles:
     - is_storage_worker
    - can_write_transcoders

    Args:
        worker_id (str):
        body (EdgeTranscodeWorkerSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EdgeTranscodeWorkerSchema | PutEdgeTranscodeWorkersByWorkerIdResponseDefault
    """

    return sync_detailed(
        worker_id=worker_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    worker_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EdgeTranscodeWorkerSchema,
) -> Response[
    Any | EdgeTranscodeWorkerSchema | PutEdgeTranscodeWorkersByWorkerIdResponseDefault
]:
    """Update a edge transcode worker


    Required roles:
     - is_storage_worker
    - can_write_transcoders

    Args:
        worker_id (str):
        body (EdgeTranscodeWorkerSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EdgeTranscodeWorkerSchema | PutEdgeTranscodeWorkersByWorkerIdResponseDefault]
    """

    kwargs = _get_kwargs(
        worker_id=worker_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    worker_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: EdgeTranscodeWorkerSchema,
) -> (
    Any
    | EdgeTranscodeWorkerSchema
    | PutEdgeTranscodeWorkersByWorkerIdResponseDefault
    | None
):
    """Update a edge transcode worker


    Required roles:
     - is_storage_worker
    - can_write_transcoders

    Args:
        worker_id (str):
        body (EdgeTranscodeWorkerSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EdgeTranscodeWorkerSchema | PutEdgeTranscodeWorkersByWorkerIdResponseDefault
    """

    return (
        await asyncio_detailed(
            worker_id=worker_id,
            client=client,
            body=body,
        )
    ).parsed
