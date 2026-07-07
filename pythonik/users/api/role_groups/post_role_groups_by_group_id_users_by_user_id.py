from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_role_groups_by_group_id_users_by_user_id_response_default_type_0 import (
    PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0,
)
from ...models.post_role_groups_by_group_id_users_by_user_id_response_default_type_1 import (
    PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1,
)
from ...models.user_with_separated_groups_schema import UserWithSeparatedGroupsSchema
from ...types import Response


def _get_kwargs(
    group_id: str,
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/role_groups/{group_id}/users/{user_id}/".format(
            group_id=quote(str(group_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0
    | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
):
    if response.status_code == 201:
        response_201 = UserWithSeparatedGroupsSchema.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0
        | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0
    | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0
    | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
]:
    """Add user into a role group


    Required roles:
     - can_write_role_groups

    Args:
        group_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0 | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1 | UserWithSeparatedGroupsSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0
    | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
    | None
):
    """Add user into a role group


    Required roles:
     - can_write_role_groups

    Args:
        group_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0 | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1 | UserWithSeparatedGroupsSchema
    """

    return sync_detailed(
        group_id=group_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0
    | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
]:
    """Add user into a role group


    Required roles:
     - can_write_role_groups

    Args:
        group_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0 | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1 | UserWithSeparatedGroupsSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0
    | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
    | None
):
    """Add user into a role group


    Required roles:
     - can_write_role_groups

    Args:
        group_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType0 | PostRoleGroupsByGroupIdUsersByUserIdResponseDefaultType1 | UserWithSeparatedGroupsSchema
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
