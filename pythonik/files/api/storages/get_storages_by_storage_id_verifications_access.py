from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_storages_by_storage_id_verifications_access_response_200 import (
    GetStoragesByStorageIdVerificationsAccessResponse200,
)
from ...models.get_storages_by_storage_id_verifications_access_response_default import (
    GetStoragesByStorageIdVerificationsAccessResponseDefault,
)
from ...types import Response


def _get_kwargs(
    storage_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/{storage_id}/verifications/access/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetStoragesByStorageIdVerificationsAccessResponse200
    | GetStoragesByStorageIdVerificationsAccessResponseDefault
):
    if response.status_code == 200:
        response_200 = GetStoragesByStorageIdVerificationsAccessResponse200.from_dict(
            response.json()
        )

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
        GetStoragesByStorageIdVerificationsAccessResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetStoragesByStorageIdVerificationsAccessResponse200
    | GetStoragesByStorageIdVerificationsAccessResponseDefault
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
) -> Response[
    Any
    | GetStoragesByStorageIdVerificationsAccessResponse200
    | GetStoragesByStorageIdVerificationsAccessResponseDefault
]:
    """Verify storage access


    Required roles:
     - can_read_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdVerificationsAccessResponse200 | GetStoragesByStorageIdVerificationsAccessResponseDefault]
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
) -> (
    Any
    | GetStoragesByStorageIdVerificationsAccessResponse200
    | GetStoragesByStorageIdVerificationsAccessResponseDefault
    | None
):
    """Verify storage access


    Required roles:
     - can_read_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdVerificationsAccessResponse200 | GetStoragesByStorageIdVerificationsAccessResponseDefault
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetStoragesByStorageIdVerificationsAccessResponse200
    | GetStoragesByStorageIdVerificationsAccessResponseDefault
]:
    """Verify storage access


    Required roles:
     - can_read_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetStoragesByStorageIdVerificationsAccessResponse200 | GetStoragesByStorageIdVerificationsAccessResponseDefault]
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
) -> (
    Any
    | GetStoragesByStorageIdVerificationsAccessResponse200
    | GetStoragesByStorageIdVerificationsAccessResponseDefault
    | None
):
    """Verify storage access


    Required roles:
     - can_read_storages

    Args:
        storage_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetStoragesByStorageIdVerificationsAccessResponse200 | GetStoragesByStorageIdVerificationsAccessResponseDefault
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
        )
    ).parsed
