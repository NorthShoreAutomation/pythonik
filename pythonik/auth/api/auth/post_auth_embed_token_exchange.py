from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.cutting_room_token_response_schema import CuttingRoomTokenResponseSchema
from ...models.post_auth_embed_token_exchange_response_default import (
    PostAuthEmbedTokenExchangeResponseDefault,
)
from ...models.token_exchange_request_schema import TokenExchangeRequestSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: TokenExchangeRequestSchema,
    format_: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["format"] = format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/auth/embed/token/exchange/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CuttingRoomTokenResponseSchema | PostAuthEmbedTokenExchangeResponseDefault:
    if response.status_code == 200:
        response_200 = CuttingRoomTokenResponseSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostAuthEmbedTokenExchangeResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | CuttingRoomTokenResponseSchema | PostAuthEmbedTokenExchangeResponseDefault
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
    body: TokenExchangeRequestSchema,
    format_: str | Unset = UNSET,
) -> Response[
    Any | CuttingRoomTokenResponseSchema | PostAuthEmbedTokenExchangeResponseDefault
]:
    """Exchange an embed token for an iconik access token

    Args:
        format_ (str | Unset):
        body (TokenExchangeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CuttingRoomTokenResponseSchema | PostAuthEmbedTokenExchangeResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        format_=format_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: TokenExchangeRequestSchema,
    format_: str | Unset = UNSET,
) -> (
    Any
    | CuttingRoomTokenResponseSchema
    | PostAuthEmbedTokenExchangeResponseDefault
    | None
):
    """Exchange an embed token for an iconik access token

    Args:
        format_ (str | Unset):
        body (TokenExchangeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CuttingRoomTokenResponseSchema | PostAuthEmbedTokenExchangeResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TokenExchangeRequestSchema,
    format_: str | Unset = UNSET,
) -> Response[
    Any | CuttingRoomTokenResponseSchema | PostAuthEmbedTokenExchangeResponseDefault
]:
    """Exchange an embed token for an iconik access token

    Args:
        format_ (str | Unset):
        body (TokenExchangeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CuttingRoomTokenResponseSchema | PostAuthEmbedTokenExchangeResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        format_=format_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: TokenExchangeRequestSchema,
    format_: str | Unset = UNSET,
) -> (
    Any
    | CuttingRoomTokenResponseSchema
    | PostAuthEmbedTokenExchangeResponseDefault
    | None
):
    """Exchange an embed token for an iconik access token

    Args:
        format_ (str | Unset):
        body (TokenExchangeRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CuttingRoomTokenResponseSchema | PostAuthEmbedTokenExchangeResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            format_=format_,
        )
    ).parsed
