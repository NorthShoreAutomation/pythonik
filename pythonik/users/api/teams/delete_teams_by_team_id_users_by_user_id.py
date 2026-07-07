from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_teams_by_team_id_users_by_user_id_response_default_type_0 import (
    DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0,
)
from ...models.delete_teams_by_team_id_users_by_user_id_response_default_type_1 import (
    DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1,
)
from ...models.user_with_separated_groups_schema import UserWithSeparatedGroupsSchema
from ...types import Response


def _get_kwargs(
    team_id: str,
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/teams/{team_id}/users/{user_id}/".format(
            team_id=quote(str(team_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0
    | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1
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
    ) -> (
        DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0
        | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0
    | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0
    | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
]:
    """Delete a user from team


    Required roles:
     - can_delete_teams

    Args:
        team_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0 | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1 | UserWithSeparatedGroupsSchema]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0
    | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
    | None
):
    """Delete a user from team


    Required roles:
     - can_delete_teams

    Args:
        team_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0 | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1 | UserWithSeparatedGroupsSchema
    """

    return sync_detailed(
        team_id=team_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0
    | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
]:
    """Delete a user from team


    Required roles:
     - can_delete_teams

    Args:
        team_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0 | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1 | UserWithSeparatedGroupsSchema]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0
    | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1
    | UserWithSeparatedGroupsSchema
    | None
):
    """Delete a user from team


    Required roles:
     - can_delete_teams

    Args:
        team_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType0 | DeleteTeamsByTeamIdUsersByUserIdResponseDefaultType1 | UserWithSeparatedGroupsSchema
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
