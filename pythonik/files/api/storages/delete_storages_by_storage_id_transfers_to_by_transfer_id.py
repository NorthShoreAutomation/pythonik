from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_storages_by_storage_id_transfers_to_by_transfer_id_response_default_type_0 import (
    DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0,
)
from ...models.delete_storages_by_storage_id_transfers_to_by_transfer_id_response_default_type_1 import (
    DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1,
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
        "url": "/v1/storages/{storage_id}/transfers_to/{transfer_id}/".format(
            storage_id=quote(str(storage_id), safe=""),
            transfer_id=quote(str(transfer_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0
    | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0
        | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0
    | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1
]:
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
) -> Response[
    Any
    | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0
    | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1
]:
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
        Response[Any | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0 | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1]
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
) -> (
    Any
    | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0
    | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1
    | None
):
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
        Any | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0 | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1
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
) -> Response[
    Any
    | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0
    | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1
]:
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
        Response[Any | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0 | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1]
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
) -> (
    Any
    | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0
    | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1
    | None
):
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
        Any | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType0 | DeleteStoragesByStorageIdTransfersToByTransferIdResponseDefaultType1
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
