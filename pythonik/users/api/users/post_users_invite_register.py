from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_users_invite_register_response_default import (
    PostUsersInviteRegisterResponseDefault,
)
from ...models.user_invite_register_request_schema import (
    UserInviteRegisterRequestSchema,
)
from ...models.user_invite_register_response_schema import (
    UserInviteRegisterResponseSchema,
)
from ...types import Response


def _get_kwargs(
    *,
    body: UserInviteRegisterRequestSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/users/invite/register/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostUsersInviteRegisterResponseDefault | UserInviteRegisterResponseSchema:
    if response.status_code == 201:
        response_201 = UserInviteRegisterResponseSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    response_default = PostUsersInviteRegisterResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostUsersInviteRegisterResponseDefault | UserInviteRegisterResponseSchema
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
    body: UserInviteRegisterRequestSchema,
) -> Response[
    Any | PostUsersInviteRegisterResponseDefault | UserInviteRegisterResponseSchema
]:
    """Register a new user using an invite link token

    Args:
        body (UserInviteRegisterRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostUsersInviteRegisterResponseDefault | UserInviteRegisterResponseSchema]
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
    body: UserInviteRegisterRequestSchema,
) -> (
    Any
    | PostUsersInviteRegisterResponseDefault
    | UserInviteRegisterResponseSchema
    | None
):
    """Register a new user using an invite link token

    Args:
        body (UserInviteRegisterRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostUsersInviteRegisterResponseDefault | UserInviteRegisterResponseSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserInviteRegisterRequestSchema,
) -> Response[
    Any | PostUsersInviteRegisterResponseDefault | UserInviteRegisterResponseSchema
]:
    """Register a new user using an invite link token

    Args:
        body (UserInviteRegisterRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostUsersInviteRegisterResponseDefault | UserInviteRegisterResponseSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UserInviteRegisterRequestSchema,
) -> (
    Any
    | PostUsersInviteRegisterResponseDefault
    | UserInviteRegisterResponseSchema
    | None
):
    """Register a new user using an invite link token

    Args:
        body (UserInviteRegisterRequestSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostUsersInviteRegisterResponseDefault | UserInviteRegisterResponseSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
