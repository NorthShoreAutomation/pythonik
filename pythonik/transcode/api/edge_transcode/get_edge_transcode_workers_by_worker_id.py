from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.edge_transcode_worker_schema import EdgeTranscodeWorkerSchema
from ...models.get_edge_transcode_workers_by_worker_id_response_default import (
    GetEdgeTranscodeWorkersByWorkerIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    worker_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/edge_transcode/workers/{worker_id}/".format(
            worker_id=quote(str(worker_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EdgeTranscodeWorkerSchema | GetEdgeTranscodeWorkersByWorkerIdResponseDefault:
    if response.status_code == 200:
        response_200 = EdgeTranscodeWorkerSchema.from_dict(response.json())

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

    response_default = GetEdgeTranscodeWorkersByWorkerIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | EdgeTranscodeWorkerSchema | GetEdgeTranscodeWorkersByWorkerIdResponseDefault
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
) -> Response[
    Any | EdgeTranscodeWorkerSchema | GetEdgeTranscodeWorkersByWorkerIdResponseDefault
]:
    """Get a edge transcode worker


    Required roles:
     - is_storage_worker
    - can_read_transcoders

    Args:
        worker_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EdgeTranscodeWorkerSchema | GetEdgeTranscodeWorkersByWorkerIdResponseDefault]
    """

    kwargs = _get_kwargs(
        worker_id=worker_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    worker_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | EdgeTranscodeWorkerSchema
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefault
    | None
):
    """Get a edge transcode worker


    Required roles:
     - is_storage_worker
    - can_read_transcoders

    Args:
        worker_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EdgeTranscodeWorkerSchema | GetEdgeTranscodeWorkersByWorkerIdResponseDefault
    """

    return sync_detailed(
        worker_id=worker_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    worker_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | EdgeTranscodeWorkerSchema | GetEdgeTranscodeWorkersByWorkerIdResponseDefault
]:
    """Get a edge transcode worker


    Required roles:
     - is_storage_worker
    - can_read_transcoders

    Args:
        worker_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EdgeTranscodeWorkerSchema | GetEdgeTranscodeWorkersByWorkerIdResponseDefault]
    """

    kwargs = _get_kwargs(
        worker_id=worker_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    worker_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | EdgeTranscodeWorkerSchema
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefault
    | None
):
    """Get a edge transcode worker


    Required roles:
     - is_storage_worker
    - can_read_transcoders

    Args:
        worker_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EdgeTranscodeWorkerSchema | GetEdgeTranscodeWorkersByWorkerIdResponseDefault
    """

    return (
        await asyncio_detailed(
            worker_id=worker_id,
            client=client,
        )
    ).parsed
