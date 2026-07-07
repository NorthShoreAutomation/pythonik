from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_transfer_saved_search_request_schema import (
    BulkTransferSavedSearchRequestSchema,
)
from ...models.post_saved_searches_storages_by_storage_id_bulk_transfer_response_default_type_0 import (
    PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0,
)
from ...models.post_saved_searches_storages_by_storage_id_bulk_transfer_response_default_type_1 import (
    PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    body: BulkTransferSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allow_host_transfer"] = allow_host_transfer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/saved_searches/storages/{storage_id}/bulk/transfer/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0
    | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1
):
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    def _parse_response_default(
        data: object,
    ) -> (
        PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0
        | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0
    | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1
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
    body: BulkTransferSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any
    | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0
    | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1
]:
    """Transfer multiple objects.


    Required roles:
     - can_write_transfers

    Args:
        storage_id (str):
        allow_host_transfer (bool | Unset):
        body (BulkTransferSavedSearchRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0 | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkTransferSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0
    | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1
    | None
):
    """Transfer multiple objects.


    Required roles:
     - can_write_transfers

    Args:
        storage_id (str):
        allow_host_transfer (bool | Unset):
        body (BulkTransferSavedSearchRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0 | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        body=body,
        allow_host_transfer=allow_host_transfer,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkTransferSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any
    | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0
    | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1
]:
    """Transfer multiple objects.


    Required roles:
     - can_write_transfers

    Args:
        storage_id (str):
        allow_host_transfer (bool | Unset):
        body (BulkTransferSavedSearchRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0 | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkTransferSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0
    | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1
    | None
):
    """Transfer multiple objects.


    Required roles:
     - can_write_transfers

    Args:
        storage_id (str):
        allow_host_transfer (bool | Unset):
        body (BulkTransferSavedSearchRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType0 | PostSavedSearchesStoragesByStorageIdBulkTransferResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )
    ).parsed
