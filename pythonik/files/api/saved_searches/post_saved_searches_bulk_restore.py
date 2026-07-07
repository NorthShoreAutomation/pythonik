from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_restore_saved_search_request_schema import (
    BulkRestoreSavedSearchRequestSchema,
)
from ...models.post_saved_searches_bulk_restore_response_default_type_0 import (
    PostSavedSearchesBulkRestoreResponseDefaultType0,
)
from ...models.post_saved_searches_bulk_restore_response_default_type_1 import (
    PostSavedSearchesBulkRestoreResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkRestoreSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["allow_host_transfer"] = allow_host_transfer

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/saved_searches/bulk/restore/",
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
    | PostSavedSearchesBulkRestoreResponseDefaultType0
    | PostSavedSearchesBulkRestoreResponseDefaultType1
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
        PostSavedSearchesBulkRestoreResponseDefaultType0
        | PostSavedSearchesBulkRestoreResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostSavedSearchesBulkRestoreResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostSavedSearchesBulkRestoreResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSavedSearchesBulkRestoreResponseDefaultType0
    | PostSavedSearchesBulkRestoreResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkRestoreSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any
    | PostSavedSearchesBulkRestoreResponseDefaultType0
    | PostSavedSearchesBulkRestoreResponseDefaultType1
]:
    """Restore multiple saved searches.


    Required roles:
     - can_restore_archived_formats

    Args:
        allow_host_transfer (bool | Unset):
        body (BulkRestoreSavedSearchRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSavedSearchesBulkRestoreResponseDefaultType0 | PostSavedSearchesBulkRestoreResponseDefaultType1]
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
    body: BulkRestoreSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostSavedSearchesBulkRestoreResponseDefaultType0
    | PostSavedSearchesBulkRestoreResponseDefaultType1
    | None
):
    """Restore multiple saved searches.


    Required roles:
     - can_restore_archived_formats

    Args:
        allow_host_transfer (bool | Unset):
        body (BulkRestoreSavedSearchRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSavedSearchesBulkRestoreResponseDefaultType0 | PostSavedSearchesBulkRestoreResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
        allow_host_transfer=allow_host_transfer,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkRestoreSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> Response[
    Any
    | PostSavedSearchesBulkRestoreResponseDefaultType0
    | PostSavedSearchesBulkRestoreResponseDefaultType1
]:
    """Restore multiple saved searches.


    Required roles:
     - can_restore_archived_formats

    Args:
        allow_host_transfer (bool | Unset):
        body (BulkRestoreSavedSearchRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSavedSearchesBulkRestoreResponseDefaultType0 | PostSavedSearchesBulkRestoreResponseDefaultType1]
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
    body: BulkRestoreSavedSearchRequestSchema,
    allow_host_transfer: bool | Unset = UNSET,
) -> (
    Any
    | PostSavedSearchesBulkRestoreResponseDefaultType0
    | PostSavedSearchesBulkRestoreResponseDefaultType1
    | None
):
    """Restore multiple saved searches.


    Required roles:
     - can_restore_archived_formats

    Args:
        allow_host_transfer (bool | Unset):
        body (BulkRestoreSavedSearchRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSavedSearchesBulkRestoreResponseDefaultType0 | PostSavedSearchesBulkRestoreResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            allow_host_transfer=allow_host_transfer,
        )
    ).parsed
