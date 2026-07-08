from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.edge_transcode_worker_schema import EdgeTranscodeWorkerSchema
from ...models.get_edge_transcode_workers_by_worker_id_response_default_type_0 import (
    GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0,
)
from ...models.get_edge_transcode_workers_by_worker_id_response_default_type_1 import (
    GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1,
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
) -> (
    Any
    | EdgeTranscodeWorkerSchema
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1
):
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

    def _parse_response_default(
        data: object,
    ) -> (
        GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0
        | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | EdgeTranscodeWorkerSchema
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1
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
    Any
    | EdgeTranscodeWorkerSchema
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1
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
        Response[Any | EdgeTranscodeWorkerSchema | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0 | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1]
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
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1
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
        Any | EdgeTranscodeWorkerSchema | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0 | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1
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
    Any
    | EdgeTranscodeWorkerSchema
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1
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
        Response[Any | EdgeTranscodeWorkerSchema | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0 | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1]
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
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0
    | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1
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
        Any | EdgeTranscodeWorkerSchema | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType0 | GetEdgeTranscodeWorkersByWorkerIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            worker_id=worker_id,
            client=client,
        )
    ).parsed
