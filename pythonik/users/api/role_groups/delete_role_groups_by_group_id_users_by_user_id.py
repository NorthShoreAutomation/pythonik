from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_role_groups_by_group_id_users_by_user_id_response_default import (
    DeleteRoleGroupsByGroupIdUsersByUserIdResponseDefault,
)
from ...models.user_with_separated_groups_schema import UserWithSeparatedGroupsSchema
from ...types import Response


def _get_kwargs(
    group_id: str,
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
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
    | DeleteRoleGroupsByGroupIdUsersByUserIdResponseDefault
    | UserWithSeparatedGroupsSchema
):
    if response.status_code == 200:
        response_200 = UserWithSeparatedGroupsSchema.from_dict(response.json())

        return response_200

    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = DeleteRoleGroupsByGroupIdUsersByUserIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteRoleGroupsByGroupIdUsersByUserIdResponseDefault
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
    | DeleteRoleGroupsByGroupIdUsersByUserIdResponseDefault
    | UserWithSeparatedGroupsSchema
]:
    """Delete a user from role group


    Required roles:
     - can_delete_role_groups

    Args:
        group_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteRoleGroupsByGroupIdUsersByUserIdResponseDefault | UserWithSeparatedGroupsSchema]
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
    | DeleteRoleGroupsByGroupIdUsersByUserIdResponseDefault
    | UserWithSeparatedGroupsSchema
    | None
):
    """Delete a user from role group


    Required roles:
     - can_delete_role_groups

    Args:
        group_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteRoleGroupsByGroupIdUsersByUserIdResponseDefault | UserWithSeparatedGroupsSchema
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
    | DeleteRoleGroupsByGroupIdUsersByUserIdResponseDefault
    | UserWithSeparatedGroupsSchema
]:
    """Delete a user from role group


    Required roles:
     - can_delete_role_groups

    Args:
        group_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteRoleGroupsByGroupIdUsersByUserIdResponseDefault | UserWithSeparatedGroupsSchema]
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
    | DeleteRoleGroupsByGroupIdUsersByUserIdResponseDefault
    | UserWithSeparatedGroupsSchema
    | None
):
    """Delete a user from role group


    Required roles:
     - can_delete_role_groups

    Args:
        group_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteRoleGroupsByGroupIdUsersByUserIdResponseDefault | UserWithSeparatedGroupsSchema
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
