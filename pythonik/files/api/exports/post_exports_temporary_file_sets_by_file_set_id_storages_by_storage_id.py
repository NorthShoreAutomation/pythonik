from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.complete_export_to_local_storage_schema import (
    CompleteExportToLocalStorageSchema,
)
from ...models.post_exports_temporary_file_sets_by_file_set_id_storages_by_storage_id_response_default import (
    PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    file_set_id: str,
    storage_id: str,
    *,
    body: CompleteExportToLocalStorageSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/exports/temporary_file_sets/{file_set_id}/storages/{storage_id}/".format(
            file_set_id=quote(str(file_set_id), safe=""),
            storage_id=quote(str(storage_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefault:
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

    response_default = PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefault
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
    body: CompleteExportToLocalStorageSchema,
) -> Response[
    Any | PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefault
]:
    """Queue export job completion between local storages


    Required roles:
     - can_read_files
    - can_write_transfers

    Args:
        file_set_id (str):
        storage_id (str):
        body (CompleteExportToLocalStorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefault]
    """

    kwargs = _get_kwargs(
        file_set_id=file_set_id,
        storage_id=storage_id,
        body=body,
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
    body: CompleteExportToLocalStorageSchema,
) -> (
    Any
    | PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefault
    | None
):
    """Queue export job completion between local storages


    Required roles:
     - can_read_files
    - can_write_transfers

    Args:
        file_set_id (str):
        storage_id (str):
        body (CompleteExportToLocalStorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefault
    """

    return sync_detailed(
        file_set_id=file_set_id,
        storage_id=storage_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    file_set_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CompleteExportToLocalStorageSchema,
) -> Response[
    Any | PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefault
]:
    """Queue export job completion between local storages


    Required roles:
     - can_read_files
    - can_write_transfers

    Args:
        file_set_id (str):
        storage_id (str):
        body (CompleteExportToLocalStorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefault]
    """

    kwargs = _get_kwargs(
        file_set_id=file_set_id,
        storage_id=storage_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    file_set_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CompleteExportToLocalStorageSchema,
) -> (
    Any
    | PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefault
    | None
):
    """Queue export job completion between local storages


    Required roles:
     - can_read_files
    - can_write_transfers

    Args:
        file_set_id (str):
        storage_id (str):
        body (CompleteExportToLocalStorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostExportsTemporaryFileSetsByFileSetIdStoragesByStorageIdResponseDefault
    """

    return (
        await asyncio_detailed(
            file_set_id=file_set_id,
            storage_id=storage_id,
            client=client,
            body=body,
        )
    ).parsed
