from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_role_groups_response_default_type_0 import (
    PostRoleGroupsResponseDefaultType0,
)
from ...models.post_role_groups_response_default_type_1 import (
    PostRoleGroupsResponseDefaultType1,
)
from ...models.role_group_schema import RoleGroupSchema
from ...types import Response


def _get_kwargs(
    *,
    body: RoleGroupSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/role_groups/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostRoleGroupsResponseDefaultType0
    | PostRoleGroupsResponseDefaultType1
    | RoleGroupSchema
):
    if response.status_code == 201:
        response_201 = RoleGroupSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> PostRoleGroupsResponseDefaultType0 | PostRoleGroupsResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostRoleGroupsResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostRoleGroupsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostRoleGroupsResponseDefaultType0
    | PostRoleGroupsResponseDefaultType1
    | RoleGroupSchema
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
    body: RoleGroupSchema,
) -> Response[
    Any
    | PostRoleGroupsResponseDefaultType0
    | PostRoleGroupsResponseDefaultType1
    | RoleGroupSchema
]:
    """Create a new role group


    Required roles:
     - can_write_role_groups

    Args:
        body (RoleGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostRoleGroupsResponseDefaultType0 | PostRoleGroupsResponseDefaultType1 | RoleGroupSchema]
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
    body: RoleGroupSchema,
) -> (
    Any
    | PostRoleGroupsResponseDefaultType0
    | PostRoleGroupsResponseDefaultType1
    | RoleGroupSchema
    | None
):
    """Create a new role group


    Required roles:
     - can_write_role_groups

    Args:
        body (RoleGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostRoleGroupsResponseDefaultType0 | PostRoleGroupsResponseDefaultType1 | RoleGroupSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RoleGroupSchema,
) -> Response[
    Any
    | PostRoleGroupsResponseDefaultType0
    | PostRoleGroupsResponseDefaultType1
    | RoleGroupSchema
]:
    """Create a new role group


    Required roles:
     - can_write_role_groups

    Args:
        body (RoleGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostRoleGroupsResponseDefaultType0 | PostRoleGroupsResponseDefaultType1 | RoleGroupSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RoleGroupSchema,
) -> (
    Any
    | PostRoleGroupsResponseDefaultType0
    | PostRoleGroupsResponseDefaultType1
    | RoleGroupSchema
    | None
):
    """Create a new role group


    Required roles:
     - can_write_role_groups

    Args:
        body (RoleGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostRoleGroupsResponseDefaultType0 | PostRoleGroupsResponseDefaultType1 | RoleGroupSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
