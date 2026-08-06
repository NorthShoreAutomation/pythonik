from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_storages_by_storage_id_transfers_from_by_transfer_id_response_default import (
    DeleteStoragesByStorageIdTransfersFromByTransferIdResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    transfer_id: str,
    *,
    failed: bool | Unset = UNSET,
    completed: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["failed"] = failed

    params["completed"] = completed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/storages/{storage_id}/transfers_from/{transfer_id}/".format(
            storage_id=quote(str(storage_id), safe=""),
            transfer_id=quote(str(transfer_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteStoragesByStorageIdTransfersFromByTransferIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        DeleteStoragesByStorageIdTransfersFromByTransferIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteStoragesByStorageIdTransfersFromByTransferIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
    failed: bool | Unset = UNSET,
    completed: bool | Unset = UNSET,
) -> Response[Any | DeleteStoragesByStorageIdTransfersFromByTransferIdResponseDefault]:
    """Delete file set transfer after handling it


    Required roles:
     - can_write_transfers

    Args:
        storage_id (str):
        transfer_id (str):
        failed (bool | Unset):
        completed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdTransfersFromByTransferIdResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        transfer_id=transfer_id,
        failed=failed,
        completed=completed,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
    failed: bool | Unset = UNSET,
    completed: bool | Unset = UNSET,
) -> Any | DeleteStoragesByStorageIdTransfersFromByTransferIdResponseDefault | None:
    """Delete file set transfer after handling it


    Required roles:
     - can_write_transfers

    Args:
        storage_id (str):
        transfer_id (str):
        failed (bool | Unset):
        completed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdTransfersFromByTransferIdResponseDefault
    """

    return sync_detailed(
        storage_id=storage_id,
        transfer_id=transfer_id,
        client=client,
        failed=failed,
        completed=completed,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
    failed: bool | Unset = UNSET,
    completed: bool | Unset = UNSET,
) -> Response[Any | DeleteStoragesByStorageIdTransfersFromByTransferIdResponseDefault]:
    """Delete file set transfer after handling it


    Required roles:
     - can_write_transfers

    Args:
        storage_id (str):
        transfer_id (str):
        failed (bool | Unset):
        completed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdTransfersFromByTransferIdResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        transfer_id=transfer_id,
        failed=failed,
        completed=completed,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
    failed: bool | Unset = UNSET,
    completed: bool | Unset = UNSET,
) -> Any | DeleteStoragesByStorageIdTransfersFromByTransferIdResponseDefault | None:
    """Delete file set transfer after handling it


    Required roles:
     - can_write_transfers

    Args:
        storage_id (str):
        transfer_id (str):
        failed (bool | Unset):
        completed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdTransfersFromByTransferIdResponseDefault
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            transfer_id=transfer_id,
            client=client,
            failed=failed,
            completed=completed,
        )
    ).parsed
