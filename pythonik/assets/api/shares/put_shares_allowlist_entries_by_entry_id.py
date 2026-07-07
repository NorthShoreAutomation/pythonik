from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.magic_link_allowlist_entry_schema import MagicLinkAllowlistEntrySchema
from ...models.magic_link_allowlist_update_schema import MagicLinkAllowlistUpdateSchema
from ...models.put_shares_allowlist_entries_by_entry_id_response_default_type_0 import (
    PutSharesAllowlistEntriesByEntryIdResponseDefaultType0,
)
from ...models.put_shares_allowlist_entries_by_entry_id_response_default_type_1 import (
    PutSharesAllowlistEntriesByEntryIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    entry_id: str,
    *,
    body: MagicLinkAllowlistUpdateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/shares/allowlist/entries/{entry_id}/".format(
            entry_id=quote(str(entry_id), safe=""),
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
    | MagicLinkAllowlistEntrySchema
    | PutSharesAllowlistEntriesByEntryIdResponseDefaultType0
    | PutSharesAllowlistEntriesByEntryIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = MagicLinkAllowlistEntrySchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
        PutSharesAllowlistEntriesByEntryIdResponseDefaultType0
        | PutSharesAllowlistEntriesByEntryIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PutSharesAllowlistEntriesByEntryIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutSharesAllowlistEntriesByEntryIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | MagicLinkAllowlistEntrySchema
    | PutSharesAllowlistEntriesByEntryIdResponseDefaultType0
    | PutSharesAllowlistEntriesByEntryIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    entry_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkAllowlistUpdateSchema,
) -> Response[
    Any
    | MagicLinkAllowlistEntrySchema
    | PutSharesAllowlistEntriesByEntryIdResponseDefaultType0
    | PutSharesAllowlistEntriesByEntryIdResponseDefaultType1
]:
    """Update an allowlist entry.

    Args:
        entry_id (str):
        body (MagicLinkAllowlistUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MagicLinkAllowlistEntrySchema | PutSharesAllowlistEntriesByEntryIdResponseDefaultType0 | PutSharesAllowlistEntriesByEntryIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        entry_id=entry_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entry_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkAllowlistUpdateSchema,
) -> (
    Any
    | MagicLinkAllowlistEntrySchema
    | PutSharesAllowlistEntriesByEntryIdResponseDefaultType0
    | PutSharesAllowlistEntriesByEntryIdResponseDefaultType1
    | None
):
    """Update an allowlist entry.

    Args:
        entry_id (str):
        body (MagicLinkAllowlistUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MagicLinkAllowlistEntrySchema | PutSharesAllowlistEntriesByEntryIdResponseDefaultType0 | PutSharesAllowlistEntriesByEntryIdResponseDefaultType1
    """

    return sync_detailed(
        entry_id=entry_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    entry_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkAllowlistUpdateSchema,
) -> Response[
    Any
    | MagicLinkAllowlistEntrySchema
    | PutSharesAllowlistEntriesByEntryIdResponseDefaultType0
    | PutSharesAllowlistEntriesByEntryIdResponseDefaultType1
]:
    """Update an allowlist entry.

    Args:
        entry_id (str):
        body (MagicLinkAllowlistUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MagicLinkAllowlistEntrySchema | PutSharesAllowlistEntriesByEntryIdResponseDefaultType0 | PutSharesAllowlistEntriesByEntryIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        entry_id=entry_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entry_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: MagicLinkAllowlistUpdateSchema,
) -> (
    Any
    | MagicLinkAllowlistEntrySchema
    | PutSharesAllowlistEntriesByEntryIdResponseDefaultType0
    | PutSharesAllowlistEntriesByEntryIdResponseDefaultType1
    | None
):
    """Update an allowlist entry.

    Args:
        entry_id (str):
        body (MagicLinkAllowlistUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MagicLinkAllowlistEntrySchema | PutSharesAllowlistEntriesByEntryIdResponseDefaultType0 | PutSharesAllowlistEntriesByEntryIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            entry_id=entry_id,
            client=client,
            body=body,
        )
    ).parsed
