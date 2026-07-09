from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_by_storage_id_transfers_from_by_transfer_id_response_default import (
    GetStoragesByStorageIdTransfersFromByTransferIdResponseDefault,
)
from ...models.transfer_from_storage_read_schema import TransferFromStorageReadSchema
from ...types import Response


def _get_kwargs(
    storage_id: str,
    transfer_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/{storage_id}/transfers_from/{transfer_id}/".format(
            storage_id=quote(str(storage_id), safe=""),
            transfer_id=quote(str(transfer_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStoragesByStorageIdTransfersFromByTransferIdResponseDefault
    | TransferFromStorageReadSchema
):
    if response.status_code == 200:
        response_200 = TransferFromStorageReadSchema.from_dict(response.json())

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

    response_default = (
        GetStoragesByStorageIdTransfersFromByTransferIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStoragesByStorageIdTransfersFromByTransferIdResponseDefault
    | TransferFromStorageReadSchema
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
) -> Response[
    Any
    | GetStoragesByStorageIdTransfersFromByTransferIdResponseDefault
    | TransferFromStorageReadSchema
]:
    """Get file set transfer record


    Required roles:
     - can_read_transfers

    Args:
        storage_id (str):
        transfer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdTransfersFromByTransferIdResponseDefault | TransferFromStorageReadSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        transfer_id=transfer_id,
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
) -> (
    Any
    | GetStoragesByStorageIdTransfersFromByTransferIdResponseDefault
    | TransferFromStorageReadSchema
    | None
):
    """Get file set transfer record


    Required roles:
     - can_read_transfers

    Args:
        storage_id (str):
        transfer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdTransfersFromByTransferIdResponseDefault | TransferFromStorageReadSchema
    """

    return sync_detailed(
        storage_id=storage_id,
        transfer_id=transfer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetStoragesByStorageIdTransfersFromByTransferIdResponseDefault
    | TransferFromStorageReadSchema
]:
    """Get file set transfer record


    Required roles:
     - can_read_transfers

    Args:
        storage_id (str):
        transfer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdTransfersFromByTransferIdResponseDefault | TransferFromStorageReadSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        transfer_id=transfer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    transfer_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetStoragesByStorageIdTransfersFromByTransferIdResponseDefault
    | TransferFromStorageReadSchema
    | None
):
    """Get file set transfer record


    Required roles:
     - can_read_transfers

    Args:
        storage_id (str):
        transfer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdTransfersFromByTransferIdResponseDefault | TransferFromStorageReadSchema
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            transfer_id=transfer_id,
            client=client,
        )
    ).parsed
