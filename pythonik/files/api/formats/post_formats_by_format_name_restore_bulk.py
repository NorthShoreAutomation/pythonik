from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_fileset_restore_schema import BulkFilesetRestoreSchema
from ...models.post_formats_by_format_name_restore_bulk_response_default import (
    PostFormatsByFormatNameRestoreBulkResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    format_name: str,
    *,
    body: BulkFilesetRestoreSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allow_host_transfer"] = allow_host_transfer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/formats/{format_name}/restore/bulk/".format(
            format_name=quote(str(format_name), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostFormatsByFormatNameRestoreBulkResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PostFormatsByFormatNameRestoreBulkResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostFormatsByFormatNameRestoreBulkResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    format_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkFilesetRestoreSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[Any | PostFormatsByFormatNameRestoreBulkResponseDefault]:
    """Queue bulk restore of previously archived assets, collections or saved_searches


    Required roles:
     - can_restore_archived_formats

    Args:
        format_name (str):
        allow_host_transfer (bool | Unset):
        body (BulkFilesetRestoreSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFormatsByFormatNameRestoreBulkResponseDefault]
    """

    kwargs = _get_kwargs(
        format_name=format_name,
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    format_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkFilesetRestoreSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Any | PostFormatsByFormatNameRestoreBulkResponseDefault | None:
    """Queue bulk restore of previously archived assets, collections or saved_searches


    Required roles:
     - can_restore_archived_formats

    Args:
        format_name (str):
        allow_host_transfer (bool | Unset):
        body (BulkFilesetRestoreSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFormatsByFormatNameRestoreBulkResponseDefault
    """

    return sync_detailed(
        format_name=format_name,
        client=client,
        body=body,
        allow_host_transfer=allow_host_transfer,
    ).parsed


async def asyncio_detailed(
    format_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkFilesetRestoreSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[Any | PostFormatsByFormatNameRestoreBulkResponseDefault]:
    """Queue bulk restore of previously archived assets, collections or saved_searches


    Required roles:
     - can_restore_archived_formats

    Args:
        format_name (str):
        allow_host_transfer (bool | Unset):
        body (BulkFilesetRestoreSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFormatsByFormatNameRestoreBulkResponseDefault]
    """

    kwargs = _get_kwargs(
        format_name=format_name,
        body=body,
        allow_host_transfer=allow_host_transfer,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    format_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkFilesetRestoreSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Any | PostFormatsByFormatNameRestoreBulkResponseDefault | None:
    """Queue bulk restore of previously archived assets, collections or saved_searches


    Required roles:
     - can_restore_archived_formats

    Args:
        format_name (str):
        allow_host_transfer (bool | Unset):
        body (BulkFilesetRestoreSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFormatsByFormatNameRestoreBulkResponseDefault
    """

    return (
        await asyncio_detailed(
            format_name=format_name,
            client=client,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )
    ).parsed
