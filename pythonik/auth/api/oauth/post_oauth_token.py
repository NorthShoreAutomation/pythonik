from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_oauth_token_body import PostOauthTokenBody
from ...models.post_oauth_token_response_default_type_0 import (
    PostOauthTokenResponseDefaultType0,
)
from ...models.post_oauth_token_response_default_type_1 import (
    PostOauthTokenResponseDefaultType1,
)
from ...models.token_schema import TokenSchema
from ...types import Response


def _get_kwargs(
    *,
    body: PostOauthTokenBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/oauth/token/",
    }

    _kwargs["data"] = body.to_dict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostOauthTokenResponseDefaultType0
    | PostOauthTokenResponseDefaultType1
    | TokenSchema
):
    if response.status_code == 200:
        response_200 = TokenSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    def _parse_response_default(
        data: object,
    ) -> PostOauthTokenResponseDefaultType0 | PostOauthTokenResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostOauthTokenResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostOauthTokenResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostOauthTokenResponseDefaultType0
    | PostOauthTokenResponseDefaultType1
    | TokenSchema
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
    body: PostOauthTokenBody,
) -> Response[
    Any
    | PostOauthTokenResponseDefaultType0
    | PostOauthTokenResponseDefaultType1
    | TokenSchema
]:
    """Issue an OAuth token

    Args:
        body (PostOauthTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostOauthTokenResponseDefaultType0 | PostOauthTokenResponseDefaultType1 | TokenSchema]
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
    body: PostOauthTokenBody,
) -> (
    Any
    | PostOauthTokenResponseDefaultType0
    | PostOauthTokenResponseDefaultType1
    | TokenSchema
    | None
):
    """Issue an OAuth token

    Args:
        body (PostOauthTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostOauthTokenResponseDefaultType0 | PostOauthTokenResponseDefaultType1 | TokenSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostOauthTokenBody,
) -> Response[
    Any
    | PostOauthTokenResponseDefaultType0
    | PostOauthTokenResponseDefaultType1
    | TokenSchema
]:
    """Issue an OAuth token

    Args:
        body (PostOauthTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostOauthTokenResponseDefaultType0 | PostOauthTokenResponseDefaultType1 | TokenSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostOauthTokenBody,
) -> (
    Any
    | PostOauthTokenResponseDefaultType0
    | PostOauthTokenResponseDefaultType1
    | TokenSchema
    | None
):
    """Issue an OAuth token

    Args:
        body (PostOauthTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostOauthTokenResponseDefaultType0 | PostOauthTokenResponseDefaultType1 | TokenSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
