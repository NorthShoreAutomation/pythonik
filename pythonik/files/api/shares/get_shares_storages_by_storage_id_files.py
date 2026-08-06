from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_shares_storages_by_storage_id_files_response_default import (
    GetSharesStoragesByStorageIdFilesResponseDefault,
)
from ...types import UNSET, Response


def _get_kwargs(
    storage_id: str,
    *,
    directory_path: str,
    name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["directory_path"] = directory_path

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/shares/storages/{storage_id}/files/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSharesStoragesByStorageIdFilesResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetSharesStoragesByStorageIdFilesResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetSharesStoragesByStorageIdFilesResponseDefault]:
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
    directory_path: str,
    name: str,
) -> Response[Any | GetSharesStoragesByStorageIdFilesResponseDefault]:
    """Check if a specific file is already on the storage for shares


    Required roles:
     - can_write_files

    Args:
        storage_id (str):
        directory_path (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesStoragesByStorageIdFilesResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        directory_path=directory_path,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    directory_path: str,
    name: str,
) -> Any | GetSharesStoragesByStorageIdFilesResponseDefault | None:
    """Check if a specific file is already on the storage for shares


    Required roles:
     - can_write_files

    Args:
        storage_id (str):
        directory_path (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesStoragesByStorageIdFilesResponseDefault
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        directory_path=directory_path,
        name=name,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    directory_path: str,
    name: str,
) -> Response[Any | GetSharesStoragesByStorageIdFilesResponseDefault]:
    """Check if a specific file is already on the storage for shares


    Required roles:
     - can_write_files

    Args:
        storage_id (str):
        directory_path (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesStoragesByStorageIdFilesResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        directory_path=directory_path,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    directory_path: str,
    name: str,
) -> Any | GetSharesStoragesByStorageIdFilesResponseDefault | None:
    """Check if a specific file is already on the storage for shares


    Required roles:
     - can_write_files

    Args:
        storage_id (str):
        directory_path (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesStoragesByStorageIdFilesResponseDefault
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            directory_path=directory_path,
            name=name,
        )
    ).parsed
