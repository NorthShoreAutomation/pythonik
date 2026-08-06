from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_storages_by_storage_id_files_by_file_id_transcode_response_default import (
    DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault,
)
from ...types import Response


def _get_kwargs(
    storage_id: str,
    file_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/storages/{storage_id}/files/{file_id}/transcode/".format(
            storage_id=quote(str(storage_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault]:
    """Delete local storage transcode job.


    Required roles:
     - can_read_transcode_jobs

    Args:
        storage_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        file_id=file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault | None:
    """Delete local storage transcode job.


    Required roles:
     - can_read_transcode_jobs

    Args:
        storage_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault
    """

    return sync_detailed(
        storage_id=storage_id,
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault]:
    """Delete local storage transcode job.


    Required roles:
     - can_read_transcode_jobs

    Args:
        storage_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault | None:
    """Delete local storage transcode job.


    Required roles:
     - can_read_transcode_jobs

    Args:
        storage_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdFilesByFileIdTranscodeResponseDefault
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            file_id=file_id,
            client=client,
        )
    ).parsed
