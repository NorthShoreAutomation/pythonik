from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_edge_transcode_workers_by_worker_id_response_default import (
    DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    worker_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/edge_transcode/workers/{worker_id}/".format(
            worker_id=quote(str(worker_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault:
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

    response_default = DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault]:
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
) -> Response[Any | DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault]:
    """Delete a edge transcode worker


    Required roles:
     - is_storage_worker
    - can_write_transcoders

    Args:
        worker_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault]
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
) -> Any | DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault | None:
    """Delete a edge transcode worker


    Required roles:
     - is_storage_worker
    - can_write_transcoders

    Args:
        worker_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault
    """

    return sync_detailed(
        worker_id=worker_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    worker_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault]:
    """Delete a edge transcode worker


    Required roles:
     - is_storage_worker
    - can_write_transcoders

    Args:
        worker_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault]
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
) -> Any | DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault | None:
    """Delete a edge transcode worker


    Required roles:
     - is_storage_worker
    - can_write_transcoders

    Args:
        worker_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteEdgeTranscodeWorkersByWorkerIdResponseDefault
    """

    return (
        await asyncio_detailed(
            worker_id=worker_id,
            client=client,
        )
    ).parsed
