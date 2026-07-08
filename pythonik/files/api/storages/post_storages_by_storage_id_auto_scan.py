from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_storages_by_storage_id_auto_scan_response_default import (
    PostStoragesByStorageIdAutoScanResponseDefault,
)
from ...models.storage_auto_scan_schema import StorageAutoScanSchema
from ...types import Response


def _get_kwargs(
    storage_id: str,
    *,
    body: StorageAutoScanSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/storages/{storage_id}/auto_scan/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostStoragesByStorageIdAutoScanResponseDefault | StorageAutoScanSchema:
    if response.status_code == 200:
        response_200 = StorageAutoScanSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PostStoragesByStorageIdAutoScanResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostStoragesByStorageIdAutoScanResponseDefault | StorageAutoScanSchema
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
    body: StorageAutoScanSchema,
) -> Response[
    Any | PostStoragesByStorageIdAutoScanResponseDefault | StorageAutoScanSchema
]:
    """Enable cloud storage auto scan


    Required roles:
     - can_scan_bucket

    Args:
        storage_id (str):
        body (StorageAutoScanSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStoragesByStorageIdAutoScanResponseDefault | StorageAutoScanSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageAutoScanSchema,
) -> (
    Any | PostStoragesByStorageIdAutoScanResponseDefault | StorageAutoScanSchema | None
):
    """Enable cloud storage auto scan


    Required roles:
     - can_scan_bucket

    Args:
        storage_id (str):
        body (StorageAutoScanSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStoragesByStorageIdAutoScanResponseDefault | StorageAutoScanSchema
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageAutoScanSchema,
) -> Response[
    Any | PostStoragesByStorageIdAutoScanResponseDefault | StorageAutoScanSchema
]:
    """Enable cloud storage auto scan


    Required roles:
     - can_scan_bucket

    Args:
        storage_id (str):
        body (StorageAutoScanSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStoragesByStorageIdAutoScanResponseDefault | StorageAutoScanSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageAutoScanSchema,
) -> (
    Any | PostStoragesByStorageIdAutoScanResponseDefault | StorageAutoScanSchema | None
):
    """Enable cloud storage auto scan


    Required roles:
     - can_scan_bucket

    Args:
        storage_id (str):
        body (StorageAutoScanSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStoragesByStorageIdAutoScanResponseDefault | StorageAutoScanSchema
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            body=body,
        )
    ).parsed
