from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.embed_token_request_schema import EmbedTokenRequestSchema
from ...models.embed_token_response_schema import EmbedTokenResponseSchema
from ...models.post_auth_embed_token_response_default import (
    PostAuthEmbedTokenResponseDefault,
)
from ...types import Response


def _get_kwargs(
    *,
    body: EmbedTokenRequestSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/auth/embed/token/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | EmbedTokenResponseSchema | PostAuthEmbedTokenResponseDefault:
    if response.status_code == 201:
        response_201 = EmbedTokenResponseSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostAuthEmbedTokenResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | EmbedTokenResponseSchema | PostAuthEmbedTokenResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EmbedTokenRequestSchema,
) -> Response[Any | EmbedTokenResponseSchema | PostAuthEmbedTokenResponseDefault]:
    """Create a short lived, single use embed token for the logged in user

    Args:
        body (EmbedTokenRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmbedTokenResponseSchema | PostAuthEmbedTokenResponseDefault]
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
    body: EmbedTokenRequestSchema,
) -> Any | EmbedTokenResponseSchema | PostAuthEmbedTokenResponseDefault | None:
    """Create a short lived, single use embed token for the logged in user

    Args:
        body (EmbedTokenRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmbedTokenResponseSchema | PostAuthEmbedTokenResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: EmbedTokenRequestSchema,
) -> Response[Any | EmbedTokenResponseSchema | PostAuthEmbedTokenResponseDefault]:
    """Create a short lived, single use embed token for the logged in user

    Args:
        body (EmbedTokenRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EmbedTokenResponseSchema | PostAuthEmbedTokenResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: EmbedTokenRequestSchema,
) -> Any | EmbedTokenResponseSchema | PostAuthEmbedTokenResponseDefault | None:
    """Create a short lived, single use embed token for the logged in user

    Args:
        body (EmbedTokenRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EmbedTokenResponseSchema | PostAuthEmbedTokenResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
