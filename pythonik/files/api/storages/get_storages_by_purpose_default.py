from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_by_purpose_default_response_default import (
    GetStoragesByPurposeDefaultResponseDefault,
)
from ...models.storage_schema import StorageSchema
from ...types import Response


def _get_kwargs(
    purpose: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/{purpose}/default/".format(
            purpose=quote(str(purpose), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetStoragesByPurposeDefaultResponseDefault | StorageSchema:
    if response.status_code == 200:
        response_200 = StorageSchema.from_dict(response.json())

        return response_200

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

    response_default = GetStoragesByPurposeDefaultResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetStoragesByPurposeDefaultResponseDefault | StorageSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    purpose: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetStoragesByPurposeDefaultResponseDefault | StorageSchema]:
    """Get a purpose default storage


    Required roles:
     - can_read_storages

    Args:
        purpose (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByPurposeDefaultResponseDefault | StorageSchema]
    """

    kwargs = _get_kwargs(
        purpose=purpose,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    purpose: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetStoragesByPurposeDefaultResponseDefault | StorageSchema | None:
    """Get a purpose default storage


    Required roles:
     - can_read_storages

    Args:
        purpose (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByPurposeDefaultResponseDefault | StorageSchema
    """

    return sync_detailed(
        purpose=purpose,
        client=client,
    ).parsed


async def asyncio_detailed(
    purpose: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetStoragesByPurposeDefaultResponseDefault | StorageSchema]:
    """Get a purpose default storage


    Required roles:
     - can_read_storages

    Args:
        purpose (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByPurposeDefaultResponseDefault | StorageSchema]
    """

    kwargs = _get_kwargs(
        purpose=purpose,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    purpose: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetStoragesByPurposeDefaultResponseDefault | StorageSchema | None:
    """Get a purpose default storage


    Required roles:
     - can_read_storages

    Args:
        purpose (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByPurposeDefaultResponseDefault | StorageSchema
    """

    return (
        await asyncio_detailed(
            purpose=purpose,
            client=client,
        )
    ).parsed
