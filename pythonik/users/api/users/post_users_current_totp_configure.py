from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.otp_schema import OtpSchema
from ...models.post_users_current_totp_configure_response_201 import (
    PostUsersCurrentTotpConfigureResponse201,
)
from ...models.post_users_current_totp_configure_response_default_type_0 import (
    PostUsersCurrentTotpConfigureResponseDefaultType0,
)
from ...models.post_users_current_totp_configure_response_default_type_1 import (
    PostUsersCurrentTotpConfigureResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: OtpSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/users/current/totp/configure/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostUsersCurrentTotpConfigureResponse201
    | PostUsersCurrentTotpConfigureResponseDefaultType0
    | PostUsersCurrentTotpConfigureResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = PostUsersCurrentTotpConfigureResponse201.from_dict(
            response.json()
        )

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    def _parse_response_default(
        data: object,
    ) -> (
        PostUsersCurrentTotpConfigureResponseDefaultType0
        | PostUsersCurrentTotpConfigureResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostUsersCurrentTotpConfigureResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostUsersCurrentTotpConfigureResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostUsersCurrentTotpConfigureResponse201
    | PostUsersCurrentTotpConfigureResponseDefaultType0
    | PostUsersCurrentTotpConfigureResponseDefaultType1
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
    body: OtpSchema | Unset = UNSET,
) -> Response[
    Any
    | PostUsersCurrentTotpConfigureResponse201
    | PostUsersCurrentTotpConfigureResponseDefaultType0
    | PostUsersCurrentTotpConfigureResponseDefaultType1
]:
    """Setup totp

    Args:
        body (OtpSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostUsersCurrentTotpConfigureResponse201 | PostUsersCurrentTotpConfigureResponseDefaultType0 | PostUsersCurrentTotpConfigureResponseDefaultType1]
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
    body: OtpSchema | Unset = UNSET,
) -> (
    Any
    | PostUsersCurrentTotpConfigureResponse201
    | PostUsersCurrentTotpConfigureResponseDefaultType0
    | PostUsersCurrentTotpConfigureResponseDefaultType1
    | None
):
    """Setup totp

    Args:
        body (OtpSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostUsersCurrentTotpConfigureResponse201 | PostUsersCurrentTotpConfigureResponseDefaultType0 | PostUsersCurrentTotpConfigureResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: OtpSchema | Unset = UNSET,
) -> Response[
    Any
    | PostUsersCurrentTotpConfigureResponse201
    | PostUsersCurrentTotpConfigureResponseDefaultType0
    | PostUsersCurrentTotpConfigureResponseDefaultType1
]:
    """Setup totp

    Args:
        body (OtpSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostUsersCurrentTotpConfigureResponse201 | PostUsersCurrentTotpConfigureResponseDefaultType0 | PostUsersCurrentTotpConfigureResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: OtpSchema | Unset = UNSET,
) -> (
    Any
    | PostUsersCurrentTotpConfigureResponse201
    | PostUsersCurrentTotpConfigureResponseDefaultType0
    | PostUsersCurrentTotpConfigureResponseDefaultType1
    | None
):
    """Setup totp

    Args:
        body (OtpSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostUsersCurrentTotpConfigureResponse201 | PostUsersCurrentTotpConfigureResponseDefaultType0 | PostUsersCurrentTotpConfigureResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
