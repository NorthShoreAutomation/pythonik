from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_users_current_otp_configure_response_200 import (
    GetUsersCurrentOtpConfigureResponse200,
)
from ...models.get_users_current_otp_configure_response_default import (
    GetUsersCurrentOtpConfigureResponseDefault,
)
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/current/otp/configure/",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetUsersCurrentOtpConfigureResponse200
    | GetUsersCurrentOtpConfigureResponseDefault
):
    if response.status_code == 200:
        response_200 = GetUsersCurrentOtpConfigureResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = GetUsersCurrentOtpConfigureResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetUsersCurrentOtpConfigureResponse200
    | GetUsersCurrentOtpConfigureResponseDefault
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
    | GetUsersCurrentOtpConfigureResponse200
    | GetUsersCurrentOtpConfigureResponseDefault
]:
    """Get current otp settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersCurrentOtpConfigureResponse200 | GetUsersCurrentOtpConfigureResponseDefault]
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
    | GetUsersCurrentOtpConfigureResponse200
    | GetUsersCurrentOtpConfigureResponseDefault
    | None
):
    """Get current otp settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersCurrentOtpConfigureResponse200 | GetUsersCurrentOtpConfigureResponseDefault
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetUsersCurrentOtpConfigureResponse200
    | GetUsersCurrentOtpConfigureResponseDefault
]:
    """Get current otp settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersCurrentOtpConfigureResponse200 | GetUsersCurrentOtpConfigureResponseDefault]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetUsersCurrentOtpConfigureResponse200
    | GetUsersCurrentOtpConfigureResponseDefault
    | None
):
    """Get current otp settings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersCurrentOtpConfigureResponse200 | GetUsersCurrentOtpConfigureResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
