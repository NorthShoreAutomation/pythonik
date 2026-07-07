from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_by_storage_id_transfers_from_response_default_type_0 import (
    GetStoragesByStorageIdTransfersFromResponseDefaultType0,
)
from ...models.get_storages_by_storage_id_transfers_from_response_default_type_1 import (
    GetStoragesByStorageIdTransfersFromResponseDefaultType1,
)
from ...models.transfers_from_storage_schema import TransfersFromStorageSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/{storage_id}/transfers_from/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetStoragesByStorageIdTransfersFromResponseDefaultType0
    | GetStoragesByStorageIdTransfersFromResponseDefaultType1
    | TransfersFromStorageSchema
):
    if response.status_code == 200:
        response_200 = TransfersFromStorageSchema.from_dict(response.json())

        return response_200

    def _parse_response_default(
        data: object,
    ) -> (
        GetStoragesByStorageIdTransfersFromResponseDefaultType0
        | GetStoragesByStorageIdTransfersFromResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetStoragesByStorageIdTransfersFromResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetStoragesByStorageIdTransfersFromResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetStoragesByStorageIdTransfersFromResponseDefaultType0
    | GetStoragesByStorageIdTransfersFromResponseDefaultType1
    | TransfersFromStorageSchema
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
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    GetStoragesByStorageIdTransfersFromResponseDefaultType0
    | GetStoragesByStorageIdTransfersFromResponseDefaultType1
    | TransfersFromStorageSchema
]:
    """Get pending transfers of file sets from a local storage


    Required roles:
     - can_read_transfers

    Args:
        storage_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStoragesByStorageIdTransfersFromResponseDefaultType0 | GetStoragesByStorageIdTransfersFromResponseDefaultType1 | TransfersFromStorageSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        per_page=per_page,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> (
    GetStoragesByStorageIdTransfersFromResponseDefaultType0
    | GetStoragesByStorageIdTransfersFromResponseDefaultType1
    | TransfersFromStorageSchema
    | None
):
    """Get pending transfers of file sets from a local storage


    Required roles:
     - can_read_transfers

    Args:
        storage_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStoragesByStorageIdTransfersFromResponseDefaultType0 | GetStoragesByStorageIdTransfersFromResponseDefaultType1 | TransfersFromStorageSchema
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        per_page=per_page,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> Response[
    GetStoragesByStorageIdTransfersFromResponseDefaultType0
    | GetStoragesByStorageIdTransfersFromResponseDefaultType1
    | TransfersFromStorageSchema
]:
    """Get pending transfers of file sets from a local storage


    Required roles:
     - can_read_transfers

    Args:
        storage_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetStoragesByStorageIdTransfersFromResponseDefaultType0 | GetStoragesByStorageIdTransfersFromResponseDefaultType1 | TransfersFromStorageSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        per_page=per_page,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    last_id: str | Unset = UNSET,
) -> (
    GetStoragesByStorageIdTransfersFromResponseDefaultType0
    | GetStoragesByStorageIdTransfersFromResponseDefaultType1
    | TransfersFromStorageSchema
    | None
):
    """Get pending transfers of file sets from a local storage


    Required roles:
     - can_read_transfers

    Args:
        storage_id (str):
        per_page (int | Unset):  Default: 10.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetStoragesByStorageIdTransfersFromResponseDefaultType0 | GetStoragesByStorageIdTransfersFromResponseDefaultType1 | TransfersFromStorageSchema
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            per_page=per_page,
            last_id=last_id,
        )
    ).parsed
