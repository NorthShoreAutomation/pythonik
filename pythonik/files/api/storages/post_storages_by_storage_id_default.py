from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_storages_by_storage_id_default_response_default import (
    PostStoragesByStorageIdDefaultResponseDefault,
)
from ...types import Response


def _get_kwargs(
    storage_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/storages/{storage_id}/default/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostStoragesByStorageIdDefaultResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostStoragesByStorageIdDefaultResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostStoragesByStorageIdDefaultResponseDefault]:
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
) -> Response[Any | PostStoragesByStorageIdDefaultResponseDefault]:
    """Set a storage to the default of its purpose


    Required roles:
     - can_write_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStoragesByStorageIdDefaultResponseDefault]
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
) -> Any | PostStoragesByStorageIdDefaultResponseDefault | None:
    """Set a storage to the default of its purpose


    Required roles:
     - can_write_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStoragesByStorageIdDefaultResponseDefault
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | PostStoragesByStorageIdDefaultResponseDefault]:
    """Set a storage to the default of its purpose


    Required roles:
     - can_write_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStoragesByStorageIdDefaultResponseDefault]
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
) -> Any | PostStoragesByStorageIdDefaultResponseDefault | None:
    """Set a storage to the default of its purpose


    Required roles:
     - can_write_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStoragesByStorageIdDefaultResponseDefault
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
        )
    ).parsed
