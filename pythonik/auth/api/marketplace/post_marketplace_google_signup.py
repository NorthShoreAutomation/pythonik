from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.marketplace_google_signup_schema import MarketplaceGoogleSignupSchema
from ...models.post_marketplace_google_signup_response_default import (
    PostMarketplaceGoogleSignupResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MarketplaceGoogleSignupSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/marketplace/google/signup/",
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostMarketplaceGoogleSignupResponseDefault:
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    response_default = PostMarketplaceGoogleSignupResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostMarketplaceGoogleSignupResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MarketplaceGoogleSignupSchema | Unset = UNSET,
) -> Response[Any | PostMarketplaceGoogleSignupResponseDefault]:
    """Google cloud marketplace signup

    Args:
        body (MarketplaceGoogleSignupSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostMarketplaceGoogleSignupResponseDefault]
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
    body: MarketplaceGoogleSignupSchema | Unset = UNSET,
) -> Any | PostMarketplaceGoogleSignupResponseDefault | None:
    """Google cloud marketplace signup

    Args:
        body (MarketplaceGoogleSignupSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostMarketplaceGoogleSignupResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MarketplaceGoogleSignupSchema | Unset = UNSET,
) -> Response[Any | PostMarketplaceGoogleSignupResponseDefault]:
    """Google cloud marketplace signup

    Args:
        body (MarketplaceGoogleSignupSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostMarketplaceGoogleSignupResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MarketplaceGoogleSignupSchema | Unset = UNSET,
) -> Any | PostMarketplaceGoogleSignupResponseDefault | None:
    """Google cloud marketplace signup

    Args:
        body (MarketplaceGoogleSignupSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostMarketplaceGoogleSignupResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
