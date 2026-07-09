from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_storages_by_storage_id_files_response_default import (
    DeleteStoragesByStorageIdFilesResponseDefault,
)
from ...models.files_elastic_schema import FilesElasticSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    path: str | Unset = UNSET,
    path_separator: str | Unset = UNSET,
    directory_path: str | Unset = UNSET,
    checksum: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["path"] = path

    params["path_separator"] = path_separator

    params["directory_path"] = directory_path

    params["checksum"] = checksum

    params["id"] = id

    params["name"] = name

    params["type"] = type_

    params["status"] = status

    params["date_created"] = date_created

    params["date_modified"] = date_modified

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/storages/{storage_id}/files/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteStoragesByStorageIdFilesResponseDefault | FilesElasticSchema:
    if response.status_code == 200:
        response_200 = FilesElasticSchema.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = DeleteStoragesByStorageIdFilesResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteStoragesByStorageIdFilesResponseDefault | FilesElasticSchema]:
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
    path: str | Unset = UNSET,
    path_separator: str | Unset = UNSET,
    directory_path: str | Unset = UNSET,
    checksum: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
) -> Response[Any | DeleteStoragesByStorageIdFilesResponseDefault | FilesElasticSchema]:
    """DELETE files (with copies in different storages) from a storage folder, or a storage


    Required roles:
     - can_read_storages
    - can_delete_files

    Args:
        storage_id (str):
        path (str | Unset):
        path_separator (str | Unset):
        directory_path (str | Unset):
        checksum (str | Unset):
        id (str | Unset):
        name (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdFilesResponseDefault | FilesElasticSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        path=path,
        path_separator=path_separator,
        directory_path=directory_path,
        checksum=checksum,
        id=id,
        name=name,
        type_=type_,
        status=status,
        date_created=date_created,
        date_modified=date_modified,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = UNSET,
    path_separator: str | Unset = UNSET,
    directory_path: str | Unset = UNSET,
    checksum: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
) -> Any | DeleteStoragesByStorageIdFilesResponseDefault | FilesElasticSchema | None:
    """DELETE files (with copies in different storages) from a storage folder, or a storage


    Required roles:
     - can_read_storages
    - can_delete_files

    Args:
        storage_id (str):
        path (str | Unset):
        path_separator (str | Unset):
        directory_path (str | Unset):
        checksum (str | Unset):
        id (str | Unset):
        name (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdFilesResponseDefault | FilesElasticSchema
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        path=path,
        path_separator=path_separator,
        directory_path=directory_path,
        checksum=checksum,
        id=id,
        name=name,
        type_=type_,
        status=status,
        date_created=date_created,
        date_modified=date_modified,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = UNSET,
    path_separator: str | Unset = UNSET,
    directory_path: str | Unset = UNSET,
    checksum: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
) -> Response[Any | DeleteStoragesByStorageIdFilesResponseDefault | FilesElasticSchema]:
    """DELETE files (with copies in different storages) from a storage folder, or a storage


    Required roles:
     - can_read_storages
    - can_delete_files

    Args:
        storage_id (str):
        path (str | Unset):
        path_separator (str | Unset):
        directory_path (str | Unset):
        checksum (str | Unset):
        id (str | Unset):
        name (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdFilesResponseDefault | FilesElasticSchema]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        path=path,
        path_separator=path_separator,
        directory_path=directory_path,
        checksum=checksum,
        id=id,
        name=name,
        type_=type_,
        status=status,
        date_created=date_created,
        date_modified=date_modified,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    path: str | Unset = UNSET,
    path_separator: str | Unset = UNSET,
    directory_path: str | Unset = UNSET,
    checksum: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
) -> Any | DeleteStoragesByStorageIdFilesResponseDefault | FilesElasticSchema | None:
    """DELETE files (with copies in different storages) from a storage folder, or a storage


    Required roles:
     - can_read_storages
    - can_delete_files

    Args:
        storage_id (str):
        path (str | Unset):
        path_separator (str | Unset):
        directory_path (str | Unset):
        checksum (str | Unset):
        id (str | Unset):
        name (str | Unset):
        type_ (str | Unset):
        status (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdFilesResponseDefault | FilesElasticSchema
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            path=path,
            path_separator=path_separator,
            directory_path=directory_path,
            checksum=checksum,
            id=id,
            name=name,
            type_=type_,
            status=status,
            date_created=date_created,
            date_modified=date_modified,
        )
    ).parsed
