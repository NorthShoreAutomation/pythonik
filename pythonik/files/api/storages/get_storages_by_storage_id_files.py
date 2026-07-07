from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.files_elastic_schema import FilesElasticSchema
from ...models.get_storages_by_storage_id_files_response_default_type_0 import (
    GetStoragesByStorageIdFilesResponseDefaultType0,
)
from ...models.get_storages_by_storage_id_files_response_default_type_1 import (
    GetStoragesByStorageIdFilesResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    path: str | Unset = UNSET,
    path_separator: str | Unset = UNSET,
    directory_path: str | Unset = UNSET,
    checksum: str | Unset = UNSET,
    per_page: int | Unset = 10,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
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

    params["per_page"] = per_page

    params["page"] = page

    params["scroll"] = scroll

    params["scroll_id"] = scroll_id

    params["sort"] = sort

    params["id"] = id

    params["name"] = name

    params["type"] = type_

    params["status"] = status

    params["date_created"] = date_created

    params["date_modified"] = date_modified

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/{storage_id}/files/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | FilesElasticSchema
    | GetStoragesByStorageIdFilesResponseDefaultType0
    | GetStoragesByStorageIdFilesResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = FilesElasticSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetStoragesByStorageIdFilesResponseDefaultType0
        | GetStoragesByStorageIdFilesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetStoragesByStorageIdFilesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetStoragesByStorageIdFilesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | FilesElasticSchema
    | GetStoragesByStorageIdFilesResponseDefaultType0
    | GetStoragesByStorageIdFilesResponseDefaultType1
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
    path: str | Unset = UNSET,
    path_separator: str | Unset = UNSET,
    directory_path: str | Unset = UNSET,
    checksum: str | Unset = UNSET,
    per_page: int | Unset = 10,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
) -> Response[
    Any
    | FilesElasticSchema
    | GetStoragesByStorageIdFilesResponseDefaultType0
    | GetStoragesByStorageIdFilesResponseDefaultType1
]:
    """Get files in a storage folder, or all files on a storage


    Required roles:
     - can_list_storage_files

    Args:
        storage_id (str):
        path (str | Unset):
        path_separator (str | Unset):
        directory_path (str | Unset):
        checksum (str | Unset):
        per_page (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
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
        Response[Any | FilesElasticSchema | GetStoragesByStorageIdFilesResponseDefaultType0 | GetStoragesByStorageIdFilesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        path=path,
        path_separator=path_separator,
        directory_path=directory_path,
        checksum=checksum,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
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
    per_page: int | Unset = 10,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
) -> (
    Any
    | FilesElasticSchema
    | GetStoragesByStorageIdFilesResponseDefaultType0
    | GetStoragesByStorageIdFilesResponseDefaultType1
    | None
):
    """Get files in a storage folder, or all files on a storage


    Required roles:
     - can_list_storage_files

    Args:
        storage_id (str):
        path (str | Unset):
        path_separator (str | Unset):
        directory_path (str | Unset):
        checksum (str | Unset):
        per_page (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
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
        Any | FilesElasticSchema | GetStoragesByStorageIdFilesResponseDefaultType0 | GetStoragesByStorageIdFilesResponseDefaultType1
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        path=path,
        path_separator=path_separator,
        directory_path=directory_path,
        checksum=checksum,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
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
    per_page: int | Unset = 10,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
) -> Response[
    Any
    | FilesElasticSchema
    | GetStoragesByStorageIdFilesResponseDefaultType0
    | GetStoragesByStorageIdFilesResponseDefaultType1
]:
    """Get files in a storage folder, or all files on a storage


    Required roles:
     - can_list_storage_files

    Args:
        storage_id (str):
        path (str | Unset):
        path_separator (str | Unset):
        directory_path (str | Unset):
        checksum (str | Unset):
        per_page (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
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
        Response[Any | FilesElasticSchema | GetStoragesByStorageIdFilesResponseDefaultType0 | GetStoragesByStorageIdFilesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        path=path,
        path_separator=path_separator,
        directory_path=directory_path,
        checksum=checksum,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
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
    per_page: int | Unset = 10,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    id: str | Unset = UNSET,
    name: str | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
) -> (
    Any
    | FilesElasticSchema
    | GetStoragesByStorageIdFilesResponseDefaultType0
    | GetStoragesByStorageIdFilesResponseDefaultType1
    | None
):
    """Get files in a storage folder, or all files on a storage


    Required roles:
     - can_list_storage_files

    Args:
        storage_id (str):
        path (str | Unset):
        path_separator (str | Unset):
        directory_path (str | Unset):
        checksum (str | Unset):
        per_page (int | Unset):  Default: 10.
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
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
        Any | FilesElasticSchema | GetStoragesByStorageIdFilesResponseDefaultType0 | GetStoragesByStorageIdFilesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            path=path,
            path_separator=path_separator,
            directory_path=directory_path,
            checksum=checksum,
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            id=id,
            name=name,
            type_=type_,
            status=status,
            date_created=date_created,
            date_modified=date_modified,
        )
    ).parsed
