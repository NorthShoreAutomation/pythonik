from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_files_by_file_id_deletions_from_by_storage_id_response_default import (
    DeleteFilesByFileIdDeletionsFromByStorageIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    file_id: str,
    storage_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/files/{file_id}/deletions_from/{storage_id}/".format(
            file_id=quote(str(file_id), safe=""),
            storage_id=quote(str(storage_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteFilesByFileIdDeletionsFromByStorageIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        DeleteFilesByFileIdDeletionsFromByStorageIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteFilesByFileIdDeletionsFromByStorageIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteFilesByFileIdDeletionsFromByStorageIdResponseDefault]:
    """Delete file deletion job after handling it


    Required roles:
     - is_storage_worker

    Args:
        file_id (str):
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteFilesByFileIdDeletionsFromByStorageIdResponseDefault]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        storage_id=storage_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteFilesByFileIdDeletionsFromByStorageIdResponseDefault | None:
    """Delete file deletion job after handling it


    Required roles:
     - is_storage_worker

    Args:
        file_id (str):
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteFilesByFileIdDeletionsFromByStorageIdResponseDefault
    """

    return sync_detailed(
        file_id=file_id,
        storage_id=storage_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    file_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteFilesByFileIdDeletionsFromByStorageIdResponseDefault]:
    """Delete file deletion job after handling it


    Required roles:
     - is_storage_worker

    Args:
        file_id (str):
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteFilesByFileIdDeletionsFromByStorageIdResponseDefault]
    """

    kwargs = _get_kwargs(
        file_id=file_id,
        storage_id=storage_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteFilesByFileIdDeletionsFromByStorageIdResponseDefault | None:
    """Delete file deletion job after handling it


    Required roles:
     - is_storage_worker

    Args:
        file_id (str):
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteFilesByFileIdDeletionsFromByStorageIdResponseDefault
    """

    return (
        await asyncio_detailed(
            file_id=file_id,
            storage_id=storage_id,
            client=client,
        )
    ).parsed
