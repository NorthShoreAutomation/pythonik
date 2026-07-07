from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.files_schema import FilesSchema
from ...models.get_storages_by_storage_id_temporary_files_response_default_type_0 import (
    GetStoragesByStorageIdTemporaryFilesResponseDefaultType0,
)
from ...models.get_storages_by_storage_id_temporary_files_response_default_type_1 import (
    GetStoragesByStorageIdTemporaryFilesResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    per_page: int | Unset = 100,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/storages/{storage_id}/temporary_files/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | FilesSchema
    | GetStoragesByStorageIdTemporaryFilesResponseDefaultType0
    | GetStoragesByStorageIdTemporaryFilesResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = FilesSchema.from_dict(response.json())

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

    def _parse_response_default(
        data: object,
    ) -> (
        GetStoragesByStorageIdTemporaryFilesResponseDefaultType0
        | GetStoragesByStorageIdTemporaryFilesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetStoragesByStorageIdTemporaryFilesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetStoragesByStorageIdTemporaryFilesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | FilesSchema
    | GetStoragesByStorageIdTemporaryFilesResponseDefaultType0
    | GetStoragesByStorageIdTemporaryFilesResponseDefaultType1
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
    per_page: int | Unset = 100,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | FilesSchema
    | GetStoragesByStorageIdTemporaryFilesResponseDefaultType0
    | GetStoragesByStorageIdTemporaryFilesResponseDefaultType1
]:
    """Get storage's exported files


    Required roles:
     - can_read_storages

    Args:
        storage_id (str):
        per_page (int | Unset):  Default: 100.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FilesSchema | GetStoragesByStorageIdTemporaryFilesResponseDefaultType0 | GetStoragesByStorageIdTemporaryFilesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        per_page=per_page,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 100,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | FilesSchema
    | GetStoragesByStorageIdTemporaryFilesResponseDefaultType0
    | GetStoragesByStorageIdTemporaryFilesResponseDefaultType1
    | None
):
    """Get storage's exported files


    Required roles:
     - can_read_storages

    Args:
        storage_id (str):
        per_page (int | Unset):  Default: 100.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FilesSchema | GetStoragesByStorageIdTemporaryFilesResponseDefaultType0 | GetStoragesByStorageIdTemporaryFilesResponseDefaultType1
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        per_page=per_page,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 100,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | FilesSchema
    | GetStoragesByStorageIdTemporaryFilesResponseDefaultType0
    | GetStoragesByStorageIdTemporaryFilesResponseDefaultType1
]:
    """Get storage's exported files


    Required roles:
     - can_read_storages

    Args:
        storage_id (str):
        per_page (int | Unset):  Default: 100.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FilesSchema | GetStoragesByStorageIdTemporaryFilesResponseDefaultType0 | GetStoragesByStorageIdTemporaryFilesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        per_page=per_page,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 100,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | FilesSchema
    | GetStoragesByStorageIdTemporaryFilesResponseDefaultType0
    | GetStoragesByStorageIdTemporaryFilesResponseDefaultType1
    | None
):
    """Get storage's exported files


    Required roles:
     - can_read_storages

    Args:
        storage_id (str):
        per_page (int | Unset):  Default: 100.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FilesSchema | GetStoragesByStorageIdTemporaryFilesResponseDefaultType0 | GetStoragesByStorageIdTemporaryFilesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            per_page=per_page,
            last_id=last_id,
        )
    ).parsed
