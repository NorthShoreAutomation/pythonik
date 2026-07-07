from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_users_invite_token_request_response_200 import (
    PostUsersInviteTokenRequestResponse200,
)
from ...models.post_users_invite_token_request_response_default_type_0 import (
    PostUsersInviteTokenRequestResponseDefaultType0,
)
from ...models.post_users_invite_token_request_response_default_type_1 import (
    PostUsersInviteTokenRequestResponseDefaultType1,
)
from ...models.user_invite_request_link_schema import UserInviteRequestLinkSchema
from ...types import Response


def _get_kwargs(
    *,
    body: UserInviteRequestLinkSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/users/invite/token/request/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostUsersInviteTokenRequestResponse200
    | PostUsersInviteTokenRequestResponseDefaultType0
    | PostUsersInviteTokenRequestResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = PostUsersInviteTokenRequestResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PostUsersInviteTokenRequestResponseDefaultType0
        | PostUsersInviteTokenRequestResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostUsersInviteTokenRequestResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostUsersInviteTokenRequestResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostUsersInviteTokenRequestResponse200
    | PostUsersInviteTokenRequestResponseDefaultType0
    | PostUsersInviteTokenRequestResponseDefaultType1
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
    body: UserInviteRequestLinkSchema,
) -> Response[
    Any
    | PostUsersInviteTokenRequestResponse200
    | PostUsersInviteTokenRequestResponseDefaultType0
    | PostUsersInviteTokenRequestResponseDefaultType1
]:
    """Request an invite link for user invitation.


    Required roles:
     - can_create_users

    Args:
        body (UserInviteRequestLinkSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostUsersInviteTokenRequestResponse200 | PostUsersInviteTokenRequestResponseDefaultType0 | PostUsersInviteTokenRequestResponseDefaultType1]
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
    body: UserInviteRequestLinkSchema,
) -> (
    Any
    | PostUsersInviteTokenRequestResponse200
    | PostUsersInviteTokenRequestResponseDefaultType0
    | PostUsersInviteTokenRequestResponseDefaultType1
    | None
):
    """Request an invite link for user invitation.


    Required roles:
     - can_create_users

    Args:
        body (UserInviteRequestLinkSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostUsersInviteTokenRequestResponse200 | PostUsersInviteTokenRequestResponseDefaultType0 | PostUsersInviteTokenRequestResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserInviteRequestLinkSchema,
) -> Response[
    Any
    | PostUsersInviteTokenRequestResponse200
    | PostUsersInviteTokenRequestResponseDefaultType0
    | PostUsersInviteTokenRequestResponseDefaultType1
]:
    """Request an invite link for user invitation.


    Required roles:
     - can_create_users

    Args:
        body (UserInviteRequestLinkSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostUsersInviteTokenRequestResponse200 | PostUsersInviteTokenRequestResponseDefaultType0 | PostUsersInviteTokenRequestResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UserInviteRequestLinkSchema,
) -> (
    Any
    | PostUsersInviteTokenRequestResponse200
    | PostUsersInviteTokenRequestResponseDefaultType0
    | PostUsersInviteTokenRequestResponseDefaultType1
    | None
):
    """Request an invite link for user invitation.


    Required roles:
     - can_create_users

    Args:
        body (UserInviteRequestLinkSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostUsersInviteTokenRequestResponse200 | PostUsersInviteTokenRequestResponseDefaultType0 | PostUsersInviteTokenRequestResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
