from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_oauth_token_body import PostOauthTokenBody
from ...models.post_oauth_token_response_default import PostOauthTokenResponseDefault
from ...models.token_schema import TokenSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostOauthTokenBody,
    expires_in: int | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(authorization, Unset):
        headers["Authorization"] = authorization

    params: dict[str, Any] = {}

    params["expires_in"] = expires_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/oauth/token/",
        "params": params,
    }

    _kwargs["data"] = body.to_dict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostOauthTokenResponseDefault | TokenSchema:
    if response.status_code == 200:
        response_200 = TokenSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    response_default = PostOauthTokenResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostOauthTokenResponseDefault | TokenSchema]:
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
    expires_in: int | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[Any | PostOauthTokenResponseDefault | TokenSchema]:
    """Issue an OAuth token

    Args:
        expires_in (int | Unset):
        authorization (str | Unset):
        body (PostOauthTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostOauthTokenResponseDefault | TokenSchema]
    """

    kwargs = _get_kwargs(
        body=body,
        expires_in=expires_in,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostOauthTokenBody,
    expires_in: int | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Any | PostOauthTokenResponseDefault | TokenSchema | None:
    """Issue an OAuth token

    Args:
        expires_in (int | Unset):
        authorization (str | Unset):
        body (PostOauthTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostOauthTokenResponseDefault | TokenSchema
    """

    return sync_detailed(
        client=client,
        body=body,
        expires_in=expires_in,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostOauthTokenBody,
    expires_in: int | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Response[Any | PostOauthTokenResponseDefault | TokenSchema]:
    """Issue an OAuth token

    Args:
        expires_in (int | Unset):
        authorization (str | Unset):
        body (PostOauthTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostOauthTokenResponseDefault | TokenSchema]
    """

    kwargs = _get_kwargs(
        body=body,
        expires_in=expires_in,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostOauthTokenBody,
    expires_in: int | Unset = UNSET,
    authorization: str | Unset = UNSET,
) -> Any | PostOauthTokenResponseDefault | TokenSchema | None:
    """Issue an OAuth token

    Args:
        expires_in (int | Unset):
        authorization (str | Unset):
        body (PostOauthTokenBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostOauthTokenResponseDefault | TokenSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            expires_in=expires_in,
            authorization=authorization,
        )
    ).parsed
