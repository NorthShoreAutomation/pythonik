from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_users_by_user_id_roles_response_default_type_0 import (
    GetUsersByUserIdRolesResponseDefaultType0,
)
from ...models.get_users_by_user_id_roles_response_default_type_1 import (
    GetUsersByUserIdRolesResponseDefaultType1,
)
from ...models.user_roles_schema import UserRolesSchema
from ...types import Response


def _get_kwargs(
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/users/{user_id}/roles/".format(
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetUsersByUserIdRolesResponseDefaultType0
    | GetUsersByUserIdRolesResponseDefaultType1
    | UserRolesSchema
):
    if response.status_code == 200:
        response_200 = UserRolesSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetUsersByUserIdRolesResponseDefaultType0
        | GetUsersByUserIdRolesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetUsersByUserIdRolesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetUsersByUserIdRolesResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetUsersByUserIdRolesResponseDefaultType0
    | GetUsersByUserIdRolesResponseDefaultType1
    | UserRolesSchema
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
    | GetUsersByUserIdRolesResponseDefaultType0
    | GetUsersByUserIdRolesResponseDefaultType1
    | UserRolesSchema
]:
    """Returns user roles by user_id


    Required roles:
     - can_read_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersByUserIdRolesResponseDefaultType0 | GetUsersByUserIdRolesResponseDefaultType1 | UserRolesSchema]
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
    | GetUsersByUserIdRolesResponseDefaultType0
    | GetUsersByUserIdRolesResponseDefaultType1
    | UserRolesSchema
    | None
):
    """Returns user roles by user_id


    Required roles:
     - can_read_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersByUserIdRolesResponseDefaultType0 | GetUsersByUserIdRolesResponseDefaultType1 | UserRolesSchema
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
    | GetUsersByUserIdRolesResponseDefaultType0
    | GetUsersByUserIdRolesResponseDefaultType1
    | UserRolesSchema
]:
    """Returns user roles by user_id


    Required roles:
     - can_read_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetUsersByUserIdRolesResponseDefaultType0 | GetUsersByUserIdRolesResponseDefaultType1 | UserRolesSchema]
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
    | GetUsersByUserIdRolesResponseDefaultType0
    | GetUsersByUserIdRolesResponseDefaultType1
    | UserRolesSchema
    | None
):
    """Returns user roles by user_id


    Required roles:
     - can_read_users

    Args:
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetUsersByUserIdRolesResponseDefaultType0 | GetUsersByUserIdRolesResponseDefaultType1 | UserRolesSchema
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
