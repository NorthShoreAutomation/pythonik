from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_fileset_archive_schema import BulkFilesetArchiveSchema
from ...models.post_formats_by_format_name_archive_bulk_response_default_type_0 import (
    PostFormatsByFormatNameArchiveBulkResponseDefaultType0,
)
from ...models.post_formats_by_format_name_archive_bulk_response_default_type_1 import (
    PostFormatsByFormatNameArchiveBulkResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    format_name: str,
    *,
    body: BulkFilesetArchiveSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allow_host_transfer"] = allow_host_transfer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/formats/{format_name}/archive/bulk/".format(
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
) -> (
    Any
    | PostFormatsByFormatNameArchiveBulkResponseDefaultType0
    | PostFormatsByFormatNameArchiveBulkResponseDefaultType1
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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PostFormatsByFormatNameArchiveBulkResponseDefaultType0
        | PostFormatsByFormatNameArchiveBulkResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostFormatsByFormatNameArchiveBulkResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostFormatsByFormatNameArchiveBulkResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostFormatsByFormatNameArchiveBulkResponseDefaultType0
    | PostFormatsByFormatNameArchiveBulkResponseDefaultType1
]:
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
    body: BulkFilesetArchiveSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any
    | PostFormatsByFormatNameArchiveBulkResponseDefaultType0
    | PostFormatsByFormatNameArchiveBulkResponseDefaultType1
]:
    """Queue bulk archiving of assets, collections and saved_searches


    Required roles:
     - can_archive_formats

    Args:
        format_name (str):
        allow_host_transfer (bool | Unset):
        body (BulkFilesetArchiveSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFormatsByFormatNameArchiveBulkResponseDefaultType0 | PostFormatsByFormatNameArchiveBulkResponseDefaultType1]
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
    body: BulkFilesetArchiveSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostFormatsByFormatNameArchiveBulkResponseDefaultType0
    | PostFormatsByFormatNameArchiveBulkResponseDefaultType1
    | None
):
    """Queue bulk archiving of assets, collections and saved_searches


    Required roles:
     - can_archive_formats

    Args:
        format_name (str):
        allow_host_transfer (bool | Unset):
        body (BulkFilesetArchiveSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFormatsByFormatNameArchiveBulkResponseDefaultType0 | PostFormatsByFormatNameArchiveBulkResponseDefaultType1
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
    body: BulkFilesetArchiveSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any
    | PostFormatsByFormatNameArchiveBulkResponseDefaultType0
    | PostFormatsByFormatNameArchiveBulkResponseDefaultType1
]:
    """Queue bulk archiving of assets, collections and saved_searches


    Required roles:
     - can_archive_formats

    Args:
        format_name (str):
        allow_host_transfer (bool | Unset):
        body (BulkFilesetArchiveSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFormatsByFormatNameArchiveBulkResponseDefaultType0 | PostFormatsByFormatNameArchiveBulkResponseDefaultType1]
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
    body: BulkFilesetArchiveSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostFormatsByFormatNameArchiveBulkResponseDefaultType0
    | PostFormatsByFormatNameArchiveBulkResponseDefaultType1
    | None
):
    """Queue bulk archiving of assets, collections and saved_searches


    Required roles:
     - can_archive_formats

    Args:
        format_name (str):
        allow_host_transfer (bool | Unset):
        body (BulkFilesetArchiveSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFormatsByFormatNameArchiveBulkResponseDefaultType0 | PostFormatsByFormatNameArchiveBulkResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            format_name=format_name,
            client=client,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )
    ).parsed
