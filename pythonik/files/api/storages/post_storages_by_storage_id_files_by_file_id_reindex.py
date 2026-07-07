from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_storages_by_storage_id_files_by_file_id_reindex_response_default_type_0 import (
    PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0,
)
from ...models.post_storages_by_storage_id_files_by_file_id_reindex_response_default_type_1 import (
    PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    storage_id: str,
    file_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/storages/{storage_id}/files/{file_id}/reindex/".format(
            storage_id=quote(str(storage_id), safe=""),
            file_id=quote(str(file_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0
    | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0
        | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1.from_dict(
                data
            )
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0
    | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0
    | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1
]:
    """Trigger reindexing for a file on a storage


    Required roles:
     - can_reindex_storages

    Args:
        storage_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0 | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        file_id=file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0
    | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1
    | None
):
    """Trigger reindexing for a file on a storage


    Required roles:
     - can_reindex_storages

    Args:
        storage_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0 | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1
    """

    return sync_detailed(
        storage_id=storage_id,
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0
    | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1
]:
    """Trigger reindexing for a file on a storage


    Required roles:
     - can_reindex_storages

    Args:
        storage_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0 | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    file_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0
    | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1
    | None
):
    """Trigger reindexing for a file on a storage


    Required roles:
     - can_reindex_storages

    Args:
        storage_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType0 | PostStoragesByStorageIdFilesByFileIdReindexResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            file_id=file_id,
            client=client,
        )
    ).parsed
