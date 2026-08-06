from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_users_by_user_id_roles_by_role_response_default import (
    GetUsersByUserIdRolesByRoleResponseDefault,
)
from ...types import Response


def _get_kwargs(
    user_id: str,
    role: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/roles/{role}/".format(
            user_id=quote(str(user_id), safe=""),
            role=quote(str(role), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetUsersByUserIdRolesByRoleResponseDefault:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetUsersByUserIdRolesByRoleResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetUsersByUserIdRolesByRoleResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    role: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetUsersByUserIdRolesByRoleResponseDefault]:
    """Returns user roles by user_id


    Required roles:
     - can_read_users

    Args:
        user_id (str):
        role (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersByUserIdRolesByRoleResponseDefault]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        role=role,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    role: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetUsersByUserIdRolesByRoleResponseDefault | None:
    """Returns user roles by user_id


    Required roles:
     - can_read_users

    Args:
        user_id (str):
        role (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersByUserIdRolesByRoleResponseDefault
    """

    return sync_detailed(
        user_id=user_id,
        role=role,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    role: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | GetUsersByUserIdRolesByRoleResponseDefault]:
    """Returns user roles by user_id


    Required roles:
     - can_read_users

    Args:
        user_id (str):
        role (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersByUserIdRolesByRoleResponseDefault]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        role=role,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    role: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetUsersByUserIdRolesByRoleResponseDefault | None:
    """Returns user roles by user_id


    Required roles:
     - can_read_users

    Args:
        user_id (str):
        role (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersByUserIdRolesByRoleResponseDefault
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            role=role,
            client=client,
        )
    ).parsed
