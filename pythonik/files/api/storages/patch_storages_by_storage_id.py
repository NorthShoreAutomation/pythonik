from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.patch_storages_by_storage_id_response_default import (
    PatchStoragesByStorageIdResponseDefault,
)
from ...models.storage_schema import StorageSchema
from ...types import Response


def _get_kwargs(
    storage_id: str,
    *,
    body: StorageSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/storages/{storage_id}/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchStoragesByStorageIdResponseDefault | StorageSchema:
    if response.status_code == 200:
        response_200 = StorageSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PatchStoragesByStorageIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PatchStoragesByStorageIdResponseDefault | StorageSchema]:
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
    body: StorageSchema,
) -> Response[Any | PatchStoragesByStorageIdResponseDefault | StorageSchema]:
    """Update storage


    Required roles:
     - can_write_storages

    Args:
        storage_id (str):
        body (StorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchStoragesByStorageIdResponseDefault | StorageSchema]
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
    body: StorageSchema,
) -> Any | PatchStoragesByStorageIdResponseDefault | StorageSchema | None:
    """Update storage


    Required roles:
     - can_write_storages

    Args:
        storage_id (str):
        body (StorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchStoragesByStorageIdResponseDefault | StorageSchema
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
    body: StorageSchema,
) -> Response[Any | PatchStoragesByStorageIdResponseDefault | StorageSchema]:
    """Update storage


    Required roles:
     - can_write_storages

    Args:
        storage_id (str):
        body (StorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchStoragesByStorageIdResponseDefault | StorageSchema]
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
    body: StorageSchema,
) -> Any | PatchStoragesByStorageIdResponseDefault | StorageSchema | None:
    """Update storage


    Required roles:
     - can_write_storages

    Args:
        storage_id (str):
        body (StorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchStoragesByStorageIdResponseDefault | StorageSchema
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            body=body,
        )
    ).parsed
