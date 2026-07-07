from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_storages_by_storage_id_by_object_type_files_response_default_type_0 import (
    DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0,
)
from ...models.delete_storages_by_storage_id_by_object_type_files_response_default_type_1 import (
    DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1,
)
from ...models.storage_files_delete_bulk_schema import StorageFilesDeleteBulkSchema
from ...types import Response


def _get_kwargs(
    storage_id: str,
    object_type: str,
    *,
    body: StorageFilesDeleteBulkSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/storages/{storage_id}/{object_type}/files/".format(
            storage_id=quote(str(storage_id), safe=""),
            object_type=quote(str(object_type), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0
    | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1
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

    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0
        | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1.from_dict(
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
    | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0
    | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    storage_id: str,
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageFilesDeleteBulkSchema,
) -> Response[
    Any
    | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0
    | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1
]:
    """Delete files from a particular storage from multiple objects


    Required roles:
     - can_read_storages
    - can_delete_files

    Args:
        storage_id (str):
        object_type (str):
        body (StorageFilesDeleteBulkSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0 | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        object_type=object_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageFilesDeleteBulkSchema,
) -> (
    Any
    | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0
    | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1
    | None
):
    """Delete files from a particular storage from multiple objects


    Required roles:
     - can_read_storages
    - can_delete_files

    Args:
        storage_id (str):
        object_type (str):
        body (StorageFilesDeleteBulkSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0 | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1
    """

    return sync_detailed(
        storage_id=storage_id,
        object_type=object_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageFilesDeleteBulkSchema,
) -> Response[
    Any
    | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0
    | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1
]:
    """Delete files from a particular storage from multiple objects


    Required roles:
     - can_read_storages
    - can_delete_files

    Args:
        storage_id (str):
        object_type (str):
        body (StorageFilesDeleteBulkSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0 | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        object_type=object_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageFilesDeleteBulkSchema,
) -> (
    Any
    | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0
    | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1
    | None
):
    """Delete files from a particular storage from multiple objects


    Required roles:
     - can_read_storages
    - can_delete_files

    Args:
        storage_id (str):
        object_type (str):
        body (StorageFilesDeleteBulkSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType0 | DeleteStoragesByStorageIdByObjectTypeFilesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            object_type=object_type,
            client=client,
            body=body,
        )
    ).parsed
