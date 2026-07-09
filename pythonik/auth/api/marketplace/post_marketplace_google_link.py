from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.marketplace_google_link_schema import MarketplaceGoogleLinkSchema
from ...models.post_marketplace_google_link_response_default import (
    PostMarketplaceGoogleLinkResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: MarketplaceGoogleLinkSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/marketplace/google/link/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostMarketplaceGoogleLinkResponseDefault:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    response_default = PostMarketplaceGoogleLinkResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostMarketplaceGoogleLinkResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MarketplaceGoogleLinkSchema,
) -> Response[Any | PostMarketplaceGoogleLinkResponseDefault]:
    """Google cloud marketplace link to existing system domain

    Args:
        body (MarketplaceGoogleLinkSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostMarketplaceGoogleLinkResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: MarketplaceGoogleLinkSchema,
) -> Any | PostMarketplaceGoogleLinkResponseDefault | None:
    """Google cloud marketplace link to existing system domain

    Args:
        body (MarketplaceGoogleLinkSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostMarketplaceGoogleLinkResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MarketplaceGoogleLinkSchema,
) -> Response[Any | PostMarketplaceGoogleLinkResponseDefault]:
    """Google cloud marketplace link to existing system domain

    Args:
        body (MarketplaceGoogleLinkSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostMarketplaceGoogleLinkResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MarketplaceGoogleLinkSchema,
) -> Any | PostMarketplaceGoogleLinkResponseDefault | None:
    """Google cloud marketplace link to existing system domain

    Args:
        body (MarketplaceGoogleLinkSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostMarketplaceGoogleLinkResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
