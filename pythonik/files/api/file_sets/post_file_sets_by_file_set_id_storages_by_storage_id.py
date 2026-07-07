from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_file_sets_by_file_set_id_storages_by_storage_id_response_default_type_0 import (
    PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0,
)
from ...models.post_file_sets_by_file_set_id_storages_by_storage_id_response_default_type_1 import (
    PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1,
)
from ...models.transfer_from_storage_schema import TransferFromStorageSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    file_set_id: str,
    storage_id: str,
    *,
    body: TransferFromStorageSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allow_host_transfer"] = allow_host_transfer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/file_sets/{file_set_id}/storages/{storage_id}/".format(
            file_set_id=quote(str(file_set_id), safe=""),
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
    | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0
    | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1
):
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    def _parse_response_default(
        data: object,
    ) -> (
        PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0
        | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1.from_dict(
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
    | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0
    | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_set_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TransferFromStorageSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any
    | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0
    | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1
]:
    """Queue copying of a file set with files from one storage to another


    Required roles:
     - can_read_files
    - can_write_transfers

    Args:
        file_set_id (str):
        storage_id (str):
        allow_host_transfer (bool | Unset):
        body (TransferFromStorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0 | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        file_set_id=file_set_id,
        storage_id=storage_id,
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    file_set_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TransferFromStorageSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0
    | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1
    | None
):
    """Queue copying of a file set with files from one storage to another


    Required roles:
     - can_read_files
    - can_write_transfers

    Args:
        file_set_id (str):
        storage_id (str):
        allow_host_transfer (bool | Unset):
        body (TransferFromStorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0 | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1
    """

    return sync_detailed(
        file_set_id=file_set_id,
        storage_id=storage_id,
        client=client,
        body=body,
        allow_host_transfer=allow_host_transfer,
    ).parsed


async def asyncio_detailed(
    file_set_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TransferFromStorageSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any
    | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0
    | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1
]:
    """Queue copying of a file set with files from one storage to another


    Required roles:
     - can_read_files
    - can_write_transfers

    Args:
        file_set_id (str):
        storage_id (str):
        allow_host_transfer (bool | Unset):
        body (TransferFromStorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0 | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        file_set_id=file_set_id,
        storage_id=storage_id,
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_set_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TransferFromStorageSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0
    | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1
    | None
):
    """Queue copying of a file set with files from one storage to another


    Required roles:
     - can_read_files
    - can_write_transfers

    Args:
        file_set_id (str):
        storage_id (str):
        allow_host_transfer (bool | Unset):
        body (TransferFromStorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType0 | PostFileSetsByFileSetIdStoragesByStorageIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            file_set_id=file_set_id,
            storage_id=storage_id,
            client=client,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )
    ).parsed
