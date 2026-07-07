from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_shares_storages_by_storage_id_files_response_default_type_0 import (
    GetSharesStoragesByStorageIdFilesResponseDefaultType0,
)
from ...models.get_shares_storages_by_storage_id_files_response_default_type_1 import (
    GetSharesStoragesByStorageIdFilesResponseDefaultType1,
)
from ...types import UNSET, Response


def _get_kwargs(
    storage_id: str,
    *,
    directory_path: str,
    name: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["directory_path"] = directory_path

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/shares/storages/{storage_id}/files/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSharesStoragesByStorageIdFilesResponseDefaultType0
    | GetSharesStoragesByStorageIdFilesResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetSharesStoragesByStorageIdFilesResponseDefaultType0
        | GetSharesStoragesByStorageIdFilesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetSharesStoragesByStorageIdFilesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetSharesStoragesByStorageIdFilesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSharesStoragesByStorageIdFilesResponseDefaultType0
    | GetSharesStoragesByStorageIdFilesResponseDefaultType1
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
    directory_path: str,
    name: str,
) -> Response[
    Any
    | GetSharesStoragesByStorageIdFilesResponseDefaultType0
    | GetSharesStoragesByStorageIdFilesResponseDefaultType1
]:
    """Check if a specific file is already on the storage for shares


    Required roles:
     - can_write_files

    Args:
        storage_id (str):
        directory_path (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesStoragesByStorageIdFilesResponseDefaultType0 | GetSharesStoragesByStorageIdFilesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        directory_path=directory_path,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    directory_path: str,
    name: str,
) -> (
    Any
    | GetSharesStoragesByStorageIdFilesResponseDefaultType0
    | GetSharesStoragesByStorageIdFilesResponseDefaultType1
    | None
):
    """Check if a specific file is already on the storage for shares


    Required roles:
     - can_write_files

    Args:
        storage_id (str):
        directory_path (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesStoragesByStorageIdFilesResponseDefaultType0 | GetSharesStoragesByStorageIdFilesResponseDefaultType1
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        directory_path=directory_path,
        name=name,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    directory_path: str,
    name: str,
) -> Response[
    Any
    | GetSharesStoragesByStorageIdFilesResponseDefaultType0
    | GetSharesStoragesByStorageIdFilesResponseDefaultType1
]:
    """Check if a specific file is already on the storage for shares


    Required roles:
     - can_write_files

    Args:
        storage_id (str):
        directory_path (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesStoragesByStorageIdFilesResponseDefaultType0 | GetSharesStoragesByStorageIdFilesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        directory_path=directory_path,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    directory_path: str,
    name: str,
) -> (
    Any
    | GetSharesStoragesByStorageIdFilesResponseDefaultType0
    | GetSharesStoragesByStorageIdFilesResponseDefaultType1
    | None
):
    """Check if a specific file is already on the storage for shares


    Required roles:
     - can_write_files

    Args:
        storage_id (str):
        directory_path (str):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesStoragesByStorageIdFilesResponseDefaultType0 | GetSharesStoragesByStorageIdFilesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            directory_path=directory_path,
            name=name,
        )
    ).parsed
