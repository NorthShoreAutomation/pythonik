from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_shares_auth_token_response_default_type_0 import (
    GetSharesAuthTokenResponseDefaultType0,
)
from ...models.get_shares_auth_token_response_default_type_1 import (
    GetSharesAuthTokenResponseDefaultType1,
)
from ...models.share_token_schema import ShareTokenSchema
from ...types import Response


def _get_kwargs(
    *,
    share_auth_token: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Share-Auth-Token"] = share_auth_token

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/shares/auth/token/",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSharesAuthTokenResponseDefaultType0
    | GetSharesAuthTokenResponseDefaultType1
    | ShareTokenSchema
):
    if response.status_code == 200:
        response_200 = ShareTokenSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetSharesAuthTokenResponseDefaultType0 | GetSharesAuthTokenResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetSharesAuthTokenResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetSharesAuthTokenResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSharesAuthTokenResponseDefaultType0
    | GetSharesAuthTokenResponseDefaultType1
    | ShareTokenSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    share_auth_token: str,
) -> Response[
    Any
    | GetSharesAuthTokenResponseDefaultType0
    | GetSharesAuthTokenResponseDefaultType1
    | ShareTokenSchema
]:
    """Check if a token is valid

    Args:
        share_auth_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesAuthTokenResponseDefaultType0 | GetSharesAuthTokenResponseDefaultType1 | ShareTokenSchema]
    """

    kwargs = _get_kwargs(
        share_auth_token=share_auth_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    share_auth_token: str,
) -> (
    Any
    | GetSharesAuthTokenResponseDefaultType0
    | GetSharesAuthTokenResponseDefaultType1
    | ShareTokenSchema
    | None
):
    """Check if a token is valid

    Args:
        share_auth_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesAuthTokenResponseDefaultType0 | GetSharesAuthTokenResponseDefaultType1 | ShareTokenSchema
    """

    return sync_detailed(
        client=client,
        share_auth_token=share_auth_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    share_auth_token: str,
) -> Response[
    Any
    | GetSharesAuthTokenResponseDefaultType0
    | GetSharesAuthTokenResponseDefaultType1
    | ShareTokenSchema
]:
    """Check if a token is valid

    Args:
        share_auth_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSharesAuthTokenResponseDefaultType0 | GetSharesAuthTokenResponseDefaultType1 | ShareTokenSchema]
    """

    kwargs = _get_kwargs(
        share_auth_token=share_auth_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    share_auth_token: str,
) -> (
    Any
    | GetSharesAuthTokenResponseDefaultType0
    | GetSharesAuthTokenResponseDefaultType1
    | ShareTokenSchema
    | None
):
    """Check if a token is valid

    Args:
        share_auth_token (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSharesAuthTokenResponseDefaultType0 | GetSharesAuthTokenResponseDefaultType1 | ShareTokenSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            share_auth_token=share_auth_token,
        )
    ).parsed
