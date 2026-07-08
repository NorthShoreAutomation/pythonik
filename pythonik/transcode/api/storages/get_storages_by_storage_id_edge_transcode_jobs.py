from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.edge_transcode_jobs_schema import EdgeTranscodeJobsSchema
from ...models.get_storages_by_storage_id_edge_transcode_jobs_response_default import (
    GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/{storage_id}/edge_transcode/jobs/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | EdgeTranscodeJobsSchema
    | GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault
):
    if response.status_code == 200:
        response_200 = EdgeTranscodeJobsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | EdgeTranscodeJobsSchema
    | GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
) -> Response[
    Any
    | EdgeTranscodeJobsSchema
    | GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault
]:
    """Get a edge transcode jobs from the job queue


    Required roles:
     - can_read_transcode_jobs

    Args:
        storage_id (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EdgeTranscodeJobsSchema | GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
) -> (
    Any
    | EdgeTranscodeJobsSchema
    | GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault
    | None
):
    """Get a edge transcode jobs from the job queue


    Required roles:
     - can_read_transcode_jobs

    Args:
        storage_id (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EdgeTranscodeJobsSchema | GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
) -> Response[
    Any
    | EdgeTranscodeJobsSchema
    | GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault
]:
    """Get a edge transcode jobs from the job queue


    Required roles:
     - can_read_transcode_jobs

    Args:
        storage_id (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EdgeTranscodeJobsSchema | GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
) -> (
    Any
    | EdgeTranscodeJobsSchema
    | GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault
    | None
):
    """Get a edge transcode jobs from the job queue


    Required roles:
     - can_read_transcode_jobs

    Args:
        storage_id (str):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EdgeTranscodeJobsSchema | GetStoragesByStorageIdEdgeTranscodeJobsResponseDefault
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            limit=limit,
        )
    ).parsed
