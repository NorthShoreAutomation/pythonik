from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_auth_token_response_default import PostAuthTokenResponseDefault
from ...models.token_schema import TokenSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    expires_in: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["expires_in"] = expires_in

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/auth/token/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostAuthTokenResponseDefault | TokenSchema:
    if response.status_code == 201:
        response_201 = TokenSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostAuthTokenResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostAuthTokenResponseDefault | TokenSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    expires_in: int | Unset = UNSET,
) -> Response[Any | PostAuthTokenResponseDefault | TokenSchema]:
    """Create new token without invalidating the old one

    Args:
        expires_in (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAuthTokenResponseDefault | TokenSchema]
    """

    kwargs = _get_kwargs(
        expires_in=expires_in,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    expires_in: int | Unset = UNSET,
) -> Any | PostAuthTokenResponseDefault | TokenSchema | None:
    """Create new token without invalidating the old one

    Args:
        expires_in (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAuthTokenResponseDefault | TokenSchema
    """

    return sync_detailed(
        client=client,
        expires_in=expires_in,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    expires_in: int | Unset = UNSET,
) -> Response[Any | PostAuthTokenResponseDefault | TokenSchema]:
    """Create new token without invalidating the old one

    Args:
        expires_in (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostAuthTokenResponseDefault | TokenSchema]
    """

    kwargs = _get_kwargs(
        expires_in=expires_in,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    expires_in: int | Unset = UNSET,
) -> Any | PostAuthTokenResponseDefault | TokenSchema | None:
    """Create new token without invalidating the old one

    Args:
        expires_in (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostAuthTokenResponseDefault | TokenSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            expires_in=expires_in,
        )
    ).parsed
