from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_archive_collection_request_schema import (
    BulkArchiveCollectionRequestSchema,
)
from ...models.post_collections_bulk_archive_response_default import (
    PostCollectionsBulkArchiveResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkArchiveCollectionRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allow_host_transfer"] = allow_host_transfer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/collections/bulk/archive/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostCollectionsBulkArchiveResponseDefault:
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

    response_default = PostCollectionsBulkArchiveResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostCollectionsBulkArchiveResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkArchiveCollectionRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[Any | PostCollectionsBulkArchiveResponseDefault]:
    """Archive multiple assets to a storage.


    Required roles:
     - can_archive_formats

    Args:
        allow_host_transfer (bool | Unset):
        body (BulkArchiveCollectionRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostCollectionsBulkArchiveResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BulkArchiveCollectionRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Any | PostCollectionsBulkArchiveResponseDefault | None:
    """Archive multiple assets to a storage.


    Required roles:
     - can_archive_formats

    Args:
        allow_host_transfer (bool | Unset):
        body (BulkArchiveCollectionRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostCollectionsBulkArchiveResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
        allow_host_transfer=allow_host_transfer,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkArchiveCollectionRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[Any | PostCollectionsBulkArchiveResponseDefault]:
    """Archive multiple assets to a storage.


    Required roles:
     - can_archive_formats

    Args:
        allow_host_transfer (bool | Unset):
        body (BulkArchiveCollectionRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostCollectionsBulkArchiveResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BulkArchiveCollectionRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Any | PostCollectionsBulkArchiveResponseDefault | None:
    """Archive multiple assets to a storage.


    Required roles:
     - can_archive_formats

    Args:
        allow_host_transfer (bool | Unset):
        body (BulkArchiveCollectionRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostCollectionsBulkArchiveResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )
    ).parsed
