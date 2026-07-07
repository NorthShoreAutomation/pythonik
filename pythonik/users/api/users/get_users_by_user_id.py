from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_users_by_user_id_response_default_type_0 import (
    GetUsersByUserIdResponseDefaultType0,
)
from ...models.get_users_by_user_id_response_default_type_1 import (
    GetUsersByUserIdResponseDefaultType1,
)
from ...models.user_with_separated_groups_schema import UserWithSeparatedGroupsSchema
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetUsersByUserIdResponseDefaultType0
    | GetUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
):
    if response.status_code == 200:
        response_200 = UserWithSeparatedGroupsSchema.from_dict(response.json())

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
    ) -> GetUsersByUserIdResponseDefaultType0 | GetUsersByUserIdResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetUsersByUserIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetUsersByUserIdResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetUsersByUserIdResponseDefaultType0
    | GetUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetUsersByUserIdResponseDefaultType0
    | GetUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
]:
    """Returns a particular user by id


    Required roles:
     - can_read_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersByUserIdResponseDefaultType0 | GetUsersByUserIdResponseDefaultType1 | UserWithSeparatedGroupsSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetUsersByUserIdResponseDefaultType0
    | GetUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
    | None
):
    """Returns a particular user by id


    Required roles:
     - can_read_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersByUserIdResponseDefaultType0 | GetUsersByUserIdResponseDefaultType1 | UserWithSeparatedGroupsSchema
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetUsersByUserIdResponseDefaultType0
    | GetUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
]:
    """Returns a particular user by id


    Required roles:
     - can_read_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersByUserIdResponseDefaultType0 | GetUsersByUserIdResponseDefaultType1 | UserWithSeparatedGroupsSchema]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetUsersByUserIdResponseDefaultType0
    | GetUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
    | None
):
    """Returns a particular user by id


    Required roles:
     - can_read_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersByUserIdResponseDefaultType0 | GetUsersByUserIdResponseDefaultType1 | UserWithSeparatedGroupsSchema
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
