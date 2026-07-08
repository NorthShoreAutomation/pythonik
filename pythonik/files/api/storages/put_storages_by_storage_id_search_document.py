from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_storages_by_storage_id_search_document_response_default import (
    PutStoragesByStorageIdSearchDocumentResponseDefault,
)
from ...models.storage_schema import StorageSchema
from ...types import Response


def _get_kwargs(
    storage_id: str,
    *,
    body: StorageSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/storages/{storage_id}/search_document/".format(
            storage_id=quote(str(storage_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutStoragesByStorageIdSearchDocumentResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PutStoragesByStorageIdSearchDocumentResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutStoragesByStorageIdSearchDocumentResponseDefault]:
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
    body: StorageSchema,
) -> Response[Any | PutStoragesByStorageIdSearchDocumentResponseDefault]:
    """Update search document for storage


    Required roles:
     - can_reindex_storages

    Args:
        storage_id (str):
        body (StorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutStoragesByStorageIdSearchDocumentResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageSchema,
) -> Any | PutStoragesByStorageIdSearchDocumentResponseDefault | None:
    """Update search document for storage


    Required roles:
     - can_reindex_storages

    Args:
        storage_id (str):
        body (StorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutStoragesByStorageIdSearchDocumentResponseDefault
    """

    return sync_detailed(
        storage_id=storage_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageSchema,
) -> Response[Any | PutStoragesByStorageIdSearchDocumentResponseDefault]:
    """Update search document for storage


    Required roles:
     - can_reindex_storages

    Args:
        storage_id (str):
        body (StorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutStoragesByStorageIdSearchDocumentResponseDefault]
    """

    kwargs = _get_kwargs(
        storage_id=storage_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    storage_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: StorageSchema,
) -> Any | PutStoragesByStorageIdSearchDocumentResponseDefault | None:
    """Update search document for storage


    Required roles:
     - can_reindex_storages

    Args:
        storage_id (str):
        body (StorageSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutStoragesByStorageIdSearchDocumentResponseDefault
    """

    return (
        await asyncio_detailed(
            storage_id=storage_id,
            client=client,
            body=body,
        )
    ).parsed
