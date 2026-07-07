from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.file_existence_check_schema import FileExistenceCheckSchema
from ...models.post_files_storages_by_storage_id_response_default_type_0 import (
    PostFilesStoragesByStorageIdResponseDefaultType0,
)
from ...models.post_files_storages_by_storage_id_response_default_type_1 import (
    PostFilesStoragesByStorageIdResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    storage_id: str,
    *,
    body: FileExistenceCheckSchema,
    get_file_size: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["get_file_size"] = get_file_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/files/storages/{storage_id}/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostFilesStoragesByStorageIdResponseDefaultType0
    | PostFilesStoragesByStorageIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
        PostFilesStoragesByStorageIdResponseDefaultType0
        | PostFilesStoragesByStorageIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostFilesStoragesByStorageIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostFilesStoragesByStorageIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostFilesStoragesByStorageIdResponseDefaultType0
    | PostFilesStoragesByStorageIdResponseDefaultType1
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
    body: FileExistenceCheckSchema,
    get_file_size: bool | Unset = UNSET,
) -> Response[
    Any
    | PostFilesStoragesByStorageIdResponseDefaultType0
    | PostFilesStoragesByStorageIdResponseDefaultType1
]:
    """Check file is on storage


    Required roles:
     - can_read_files

    Args:
        storage_id (str):
        get_file_size (bool | Unset):
        body (FileExistenceCheckSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFilesStoragesByStorageIdResponseDefaultType0 | PostFilesStoragesByStorageIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
        get_file_size=get_file_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileExistenceCheckSchema,
    get_file_size: bool | Unset = UNSET,
) -> (
    Any
    | PostFilesStoragesByStorageIdResponseDefaultType0
    | PostFilesStoragesByStorageIdResponseDefaultType1
    | None
):
    """Check file is on storage


    Required roles:
     - can_read_files

    Args:
        storage_id (str):
        get_file_size (bool | Unset):
        body (FileExistenceCheckSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFilesStoragesByStorageIdResponseDefaultType0 | PostFilesStoragesByStorageIdResponseDefaultType1
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        body=body,
        get_file_size=get_file_size,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileExistenceCheckSchema,
    get_file_size: bool | Unset = UNSET,
) -> Response[
    Any
    | PostFilesStoragesByStorageIdResponseDefaultType0
    | PostFilesStoragesByStorageIdResponseDefaultType1
]:
    """Check file is on storage


    Required roles:
     - can_read_files

    Args:
        storage_id (str):
        get_file_size (bool | Unset):
        body (FileExistenceCheckSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFilesStoragesByStorageIdResponseDefaultType0 | PostFilesStoragesByStorageIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
        get_file_size=get_file_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: FileExistenceCheckSchema,
    get_file_size: bool | Unset = UNSET,
) -> (
    Any
    | PostFilesStoragesByStorageIdResponseDefaultType0
    | PostFilesStoragesByStorageIdResponseDefaultType1
    | None
):
    """Check file is on storage


    Required roles:
     - can_read_files

    Args:
        storage_id (str):
        get_file_size (bool | Unset):
        body (FileExistenceCheckSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFilesStoragesByStorageIdResponseDefaultType0 | PostFilesStoragesByStorageIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            body=body,
            get_file_size=get_file_size,
        )
    ).parsed
