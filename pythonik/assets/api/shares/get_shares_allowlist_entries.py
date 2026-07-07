from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_shares_allowlist_entries_response_default_type_0 import (
    GetSharesAllowlistEntriesResponseDefaultType0,
)
from ...models.get_shares_allowlist_entries_response_default_type_1 import (
    GetSharesAllowlistEntriesResponseDefaultType1,
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
) -> (
    Any
    | GetSharesAllowlistEntriesResponseDefaultType0
    | GetSharesAllowlistEntriesResponseDefaultType1
    | MagicLinkAllowlistListSchema
):
    if response.status_code == 200:
        response_200 = MagicLinkAllowlistListSchema.from_dict(response.json())

        return response_200

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    def _parse_response_default(
        data: object,
    ) -> (
        GetSharesAllowlistEntriesResponseDefaultType0
        | GetSharesAllowlistEntriesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetSharesAllowlistEntriesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetSharesAllowlistEntriesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSharesAllowlistEntriesResponseDefaultType0
    | GetSharesAllowlistEntriesResponseDefaultType1
    | MagicLinkAllowlistListSchema
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
    Any
    | GetSharesAllowlistEntriesResponseDefaultType0
    | GetSharesAllowlistEntriesResponseDefaultType1
    | MagicLinkAllowlistListSchema
]:
    """Get all magic link allowlist entries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesAllowlistEntriesResponseDefaultType0 | GetSharesAllowlistEntriesResponseDefaultType1 | MagicLinkAllowlistListSchema]
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
    Any
    | GetSharesAllowlistEntriesResponseDefaultType0
    | GetSharesAllowlistEntriesResponseDefaultType1
    | MagicLinkAllowlistListSchema
    | None
):
    """Get all magic link allowlist entries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesAllowlistEntriesResponseDefaultType0 | GetSharesAllowlistEntriesResponseDefaultType1 | MagicLinkAllowlistListSchema
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetSharesAllowlistEntriesResponseDefaultType0
    | GetSharesAllowlistEntriesResponseDefaultType1
    | MagicLinkAllowlistListSchema
]:
    """Get all magic link allowlist entries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesAllowlistEntriesResponseDefaultType0 | GetSharesAllowlistEntriesResponseDefaultType1 | MagicLinkAllowlistListSchema]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetSharesAllowlistEntriesResponseDefaultType0
    | GetSharesAllowlistEntriesResponseDefaultType1
    | MagicLinkAllowlistListSchema
    | None
):
    """Get all magic link allowlist entries.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesAllowlistEntriesResponseDefaultType0 | GetSharesAllowlistEntriesResponseDefaultType1 | MagicLinkAllowlistListSchema
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
