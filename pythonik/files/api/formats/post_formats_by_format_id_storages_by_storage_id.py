from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_formats_by_format_id_storages_by_storage_id_response_default import (
    PostFormatsByFormatIdStoragesByStorageIdResponseDefault,
)
from ...models.transfer_from_storage_schema import TransferFromStorageSchema
from ...types import Response


def _get_kwargs(
    format_id: str,
    storage_id: str,
    *,
    body: TransferFromStorageSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/formats/{format_id}/storages/{storage_id}/".format(
            format_id=quote(str(format_id), safe=""),
            storage_id=quote(str(storage_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostFormatsByFormatIdStoragesByStorageIdResponseDefault:
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

    response_default = (
        PostFormatsByFormatIdStoragesByStorageIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostFormatsByFormatIdStoragesByStorageIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    format_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TransferFromStorageSchema,
) -> Response[Any | PostFormatsByFormatIdStoragesByStorageIdResponseDefault]:
    """Queue copying of a formats file sets with files from one storage to another


    Required roles:
     - can_read_formats
    - can_write_transfers

    Args:
        format_id (str):
        storage_id (str):
        body (TransferFromStorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFormatsByFormatIdStoragesByStorageIdResponseDefault]
    """

    kwargs = _get_kwargs(
        format_id=format_id,
        storage_id=storage_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    format_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TransferFromStorageSchema,
) -> Any | PostFormatsByFormatIdStoragesByStorageIdResponseDefault | None:
    """Queue copying of a formats file sets with files from one storage to another


    Required roles:
     - can_read_formats
    - can_write_transfers

    Args:
        format_id (str):
        storage_id (str):
        body (TransferFromStorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFormatsByFormatIdStoragesByStorageIdResponseDefault
    """

    return sync_detailed(
        format_id=format_id,
        storage_id=storage_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    format_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TransferFromStorageSchema,
) -> Response[Any | PostFormatsByFormatIdStoragesByStorageIdResponseDefault]:
    """Queue copying of a formats file sets with files from one storage to another


    Required roles:
     - can_read_formats
    - can_write_transfers

    Args:
        format_id (str):
        storage_id (str):
        body (TransferFromStorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFormatsByFormatIdStoragesByStorageIdResponseDefault]
    """

    kwargs = _get_kwargs(
        format_id=format_id,
        storage_id=storage_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    format_id: str,
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TransferFromStorageSchema,
) -> Any | PostFormatsByFormatIdStoragesByStorageIdResponseDefault | None:
    """Queue copying of a formats file sets with files from one storage to another


    Required roles:
     - can_read_formats
    - can_write_transfers

    Args:
        format_id (str):
        storage_id (str):
        body (TransferFromStorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFormatsByFormatIdStoragesByStorageIdResponseDefault
    """

    return (
        await asyncio_detailed(
            format_id=format_id,
            storage_id=storage_id,
            client=client,
            body=body,
        )
    ).parsed
