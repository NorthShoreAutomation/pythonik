from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_shares_allowlist_entries_response_default import (
    GetSharesAllowlistEntriesResponseDefault,
)
from ...models.magic_link_allowlist_list_schema import MagicLinkAllowlistListSchema
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/shares/allowlist/entries/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSharesAllowlistEntriesResponseDefault | MagicLinkAllowlistListSchema:
    if response.status_code == 200:
        response_200 = MagicLinkAllowlistListSchema.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    response_default = GetSharesAllowlistEntriesResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetSharesAllowlistEntriesResponseDefault | MagicLinkAllowlistListSchema
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
) -> Response[
    Any | GetSharesAllowlistEntriesResponseDefault | MagicLinkAllowlistListSchema
]:
    """Get all magic link allowlist entries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesAllowlistEntriesResponseDefault | MagicLinkAllowlistListSchema]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any | GetSharesAllowlistEntriesResponseDefault | MagicLinkAllowlistListSchema | None
):
    """Get all magic link allowlist entries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesAllowlistEntriesResponseDefault | MagicLinkAllowlistListSchema
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetSharesAllowlistEntriesResponseDefault | MagicLinkAllowlistListSchema
]:
    """Get all magic link allowlist entries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesAllowlistEntriesResponseDefault | MagicLinkAllowlistListSchema]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any | GetSharesAllowlistEntriesResponseDefault | MagicLinkAllowlistListSchema | None
):
    """Get all magic link allowlist entries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesAllowlistEntriesResponseDefault | MagicLinkAllowlistListSchema
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
