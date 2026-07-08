from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_storages_by_storage_id_response_default import (
    DeleteStoragesByStorageIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    storage_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/storages/{storage_id}/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteStoragesByStorageIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = DeleteStoragesByStorageIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteStoragesByStorageIdResponseDefault]:
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
) -> Response[Any | DeleteStoragesByStorageIdResponseDefault]:
    """Delete a particular storage by id


    Required roles:
     - can_delete_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteStoragesByStorageIdResponseDefault | None:
    """Delete a particular storage by id


    Required roles:
     - can_delete_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdResponseDefault
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteStoragesByStorageIdResponseDefault]:
    """Delete a particular storage by id


    Required roles:
     - can_delete_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteStoragesByStorageIdResponseDefault | None:
    """Delete a particular storage by id


    Required roles:
     - can_delete_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdResponseDefault
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
        )
    ).parsed
