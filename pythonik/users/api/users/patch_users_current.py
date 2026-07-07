from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.patch_users_current_response_default_type_0 import (
    PatchUsersCurrentResponseDefaultType0,
)
from ...models.patch_users_current_response_default_type_1 import (
    PatchUsersCurrentResponseDefaultType1,
)
from ...models.user_schema import UserSchema
from ...types import Response


def _get_kwargs(
    *,
    body: UserSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/users/current/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PatchUsersCurrentResponseDefaultType0
    | PatchUsersCurrentResponseDefaultType1
    | UserSchema
):
    if response.status_code == 200:
        response_200 = UserSchema.from_dict(response.json())

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
    ) -> PatchUsersCurrentResponseDefaultType0 | PatchUsersCurrentResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PatchUsersCurrentResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PatchUsersCurrentResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PatchUsersCurrentResponseDefaultType0
    | PatchUsersCurrentResponseDefaultType1
    | UserSchema
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
    body: UserSchema,
) -> Response[
    Any
    | PatchUsersCurrentResponseDefaultType0
    | PatchUsersCurrentResponseDefaultType1
    | UserSchema
]:
    """Update user

    Args:
        body (UserSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchUsersCurrentResponseDefaultType0 | PatchUsersCurrentResponseDefaultType1 | UserSchema]
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
    body: UserSchema,
) -> (
    Any
    | PatchUsersCurrentResponseDefaultType0
    | PatchUsersCurrentResponseDefaultType1
    | UserSchema
    | None
):
    """Update user

    Args:
        body (UserSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchUsersCurrentResponseDefaultType0 | PatchUsersCurrentResponseDefaultType1 | UserSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: UserSchema,
) -> Response[
    Any
    | PatchUsersCurrentResponseDefaultType0
    | PatchUsersCurrentResponseDefaultType1
    | UserSchema
]:
    """Update user

    Args:
        body (UserSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchUsersCurrentResponseDefaultType0 | PatchUsersCurrentResponseDefaultType1 | UserSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: UserSchema,
) -> (
    Any
    | PatchUsersCurrentResponseDefaultType0
    | PatchUsersCurrentResponseDefaultType1
    | UserSchema
    | None
):
    """Update user

    Args:
        body (UserSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchUsersCurrentResponseDefaultType0 | PatchUsersCurrentResponseDefaultType1 | UserSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
