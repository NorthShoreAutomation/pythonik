from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_archive_saved_search_request_schema import (
    BulkArchiveSavedSearchRequestSchema,
)
from ...models.post_saved_searches_bulk_archive_response_default import (
    PostSavedSearchesBulkArchiveResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkArchiveSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allow_host_transfer"] = allow_host_transfer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/saved_searches/bulk/archive/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostSavedSearchesBulkArchiveResponseDefault:
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

    response_default = PostSavedSearchesBulkArchiveResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostSavedSearchesBulkArchiveResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkArchiveSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[Any | PostSavedSearchesBulkArchiveResponseDefault]:
    """Transfer multiple objects.


    Required roles:
     - can_archive_formats

    Args:
        allow_host_transfer (bool | Unset):
        body (BulkArchiveSavedSearchRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSavedSearchesBulkArchiveResponseDefault]
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
    body: BulkArchiveSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Any | PostSavedSearchesBulkArchiveResponseDefault | None:
    """Transfer multiple objects.


    Required roles:
     - can_archive_formats

    Args:
        allow_host_transfer (bool | Unset):
        body (BulkArchiveSavedSearchRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSavedSearchesBulkArchiveResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
        allow_host_transfer=allow_host_transfer,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkArchiveSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[Any | PostSavedSearchesBulkArchiveResponseDefault]:
    """Transfer multiple objects.


    Required roles:
     - can_archive_formats

    Args:
        allow_host_transfer (bool | Unset):
        body (BulkArchiveSavedSearchRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSavedSearchesBulkArchiveResponseDefault]
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
    body: BulkArchiveSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Any | PostSavedSearchesBulkArchiveResponseDefault | None:
    """Transfer multiple objects.


    Required roles:
     - can_archive_formats

    Args:
        allow_host_transfer (bool | Unset):
        body (BulkArchiveSavedSearchRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSavedSearchesBulkArchiveResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )
    ).parsed
