from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_shares_allowlist_entries_by_entry_id_response_default_type_0 import (
    GetSharesAllowlistEntriesByEntryIdResponseDefaultType0,
)
from ...models.get_shares_allowlist_entries_by_entry_id_response_default_type_1 import (
    GetSharesAllowlistEntriesByEntryIdResponseDefaultType1,
)
from ...models.magic_link_allowlist_entry_schema import MagicLinkAllowlistEntrySchema
from ...types import Response


def _get_kwargs(
    entry_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/shares/allowlist/entries/{entry_id}/".format(
            entry_id=quote(str(entry_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSharesAllowlistEntriesByEntryIdResponseDefaultType0
    | GetSharesAllowlistEntriesByEntryIdResponseDefaultType1
    | MagicLinkAllowlistEntrySchema
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

    def _parse_response_default(
        data: object,
    ) -> (
        GetSharesAllowlistEntriesByEntryIdResponseDefaultType0
        | GetSharesAllowlistEntriesByEntryIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetSharesAllowlistEntriesByEntryIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetSharesAllowlistEntriesByEntryIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSharesAllowlistEntriesByEntryIdResponseDefaultType0
    | GetSharesAllowlistEntriesByEntryIdResponseDefaultType1
    | MagicLinkAllowlistEntrySchema
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
) -> Response[
    Any
    | GetSharesAllowlistEntriesByEntryIdResponseDefaultType0
    | GetSharesAllowlistEntriesByEntryIdResponseDefaultType1
    | MagicLinkAllowlistEntrySchema
]:
    """Get a single allowlist entry by ID.

    Args:
        entry_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesAllowlistEntriesByEntryIdResponseDefaultType0 | GetSharesAllowlistEntriesByEntryIdResponseDefaultType1 | MagicLinkAllowlistEntrySchema]
    """

    kwargs = _get_kwargs(
        entry_id=entry_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    entry_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetSharesAllowlistEntriesByEntryIdResponseDefaultType0
    | GetSharesAllowlistEntriesByEntryIdResponseDefaultType1
    | MagicLinkAllowlistEntrySchema
    | None
):
    """Get a single allowlist entry by ID.

    Args:
        entry_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesAllowlistEntriesByEntryIdResponseDefaultType0 | GetSharesAllowlistEntriesByEntryIdResponseDefaultType1 | MagicLinkAllowlistEntrySchema
    """

    return sync_detailed(
        entry_id=entry_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    entry_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetSharesAllowlistEntriesByEntryIdResponseDefaultType0
    | GetSharesAllowlistEntriesByEntryIdResponseDefaultType1
    | MagicLinkAllowlistEntrySchema
]:
    """Get a single allowlist entry by ID.

    Args:
        entry_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesAllowlistEntriesByEntryIdResponseDefaultType0 | GetSharesAllowlistEntriesByEntryIdResponseDefaultType1 | MagicLinkAllowlistEntrySchema]
    """

    kwargs = _get_kwargs(
        entry_id=entry_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    entry_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetSharesAllowlistEntriesByEntryIdResponseDefaultType0
    | GetSharesAllowlistEntriesByEntryIdResponseDefaultType1
    | MagicLinkAllowlistEntrySchema
    | None
):
    """Get a single allowlist entry by ID.

    Args:
        entry_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesAllowlistEntriesByEntryIdResponseDefaultType0 | GetSharesAllowlistEntriesByEntryIdResponseDefaultType1 | MagicLinkAllowlistEntrySchema
    """

    return (
        await asyncio_detailed(
            entry_id=entry_id,
            client=client,
        )
    ).parsed
