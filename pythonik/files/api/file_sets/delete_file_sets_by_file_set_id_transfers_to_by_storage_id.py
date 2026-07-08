from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_file_sets_by_file_set_id_transfers_to_by_storage_id_response_default import (
    DeleteFileSetsByFileSetIdTransfersToByStorageIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    file_set_id: str,
    storage_id: str,
    *,
    failed: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["failed"] = failed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/file_sets/{file_set_id}/transfers_to/{storage_id}/".format(
            file_set_id=quote(str(file_set_id), safe=""),
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteFileSetsByFileSetIdTransfersToByStorageIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        DeleteFileSetsByFileSetIdTransfersToByStorageIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteFileSetsByFileSetIdTransfersToByStorageIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_set_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    failed: bool | Unset = UNSET,
) -> Response[Any | DeleteFileSetsByFileSetIdTransfersToByStorageIdResponseDefault]:
    """Delete file set transfer after handling it


    Required roles:
     - can_write_transfers

    Args:
        file_set_id (str):
        storage_id (str):
        failed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteFileSetsByFileSetIdTransfersToByStorageIdResponseDefault]
    """

    kwargs = _get_kwargs(
        file_set_id=file_set_id,
        storage_id=storage_id,
        failed=failed,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_set_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    failed: bool | Unset = UNSET,
) -> Any | DeleteFileSetsByFileSetIdTransfersToByStorageIdResponseDefault | None:
    """Delete file set transfer after handling it


    Required roles:
     - can_write_transfers

    Args:
        file_set_id (str):
        storage_id (str):
        failed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteFileSetsByFileSetIdTransfersToByStorageIdResponseDefault
    """

    return sync_detailed(
        file_set_id=file_set_id,
        storage_id=storage_id,
        client=client,
        failed=failed,
    ).parsed


async def asyncio_detailed(
    file_set_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    failed: bool | Unset = UNSET,
) -> Response[Any | DeleteFileSetsByFileSetIdTransfersToByStorageIdResponseDefault]:
    """Delete file set transfer after handling it


    Required roles:
     - can_write_transfers

    Args:
        file_set_id (str):
        storage_id (str):
        failed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteFileSetsByFileSetIdTransfersToByStorageIdResponseDefault]
    """

    kwargs = _get_kwargs(
        file_set_id=file_set_id,
        storage_id=storage_id,
        failed=failed,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_set_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    failed: bool | Unset = UNSET,
) -> Any | DeleteFileSetsByFileSetIdTransfersToByStorageIdResponseDefault | None:
    """Delete file set transfer after handling it


    Required roles:
     - can_write_transfers

    Args:
        file_set_id (str):
        storage_id (str):
        failed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteFileSetsByFileSetIdTransfersToByStorageIdResponseDefault
    """

    return (
        await asyncio_detailed(
            file_set_id=file_set_id,
            storage_id=storage_id,
            client=client,
            failed=failed,
        )
    ).parsed
