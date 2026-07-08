from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_role_groups_by_group_id_response_default import (
    PutRoleGroupsByGroupIdResponseDefault,
)
from ...models.role_group_schema import RoleGroupSchema
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    body: RoleGroupSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/role_groups/{group_id}/".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PutRoleGroupsByGroupIdResponseDefault | RoleGroupSchema:
    if response.status_code == 200:
        response_200 = RoleGroupSchema.from_dict(response.json())

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

    response_default = PutRoleGroupsByGroupIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PutRoleGroupsByGroupIdResponseDefault | RoleGroupSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RoleGroupSchema,
) -> Response[Any | PutRoleGroupsByGroupIdResponseDefault | RoleGroupSchema]:
    """Update role group


    Required roles:
     - can_write_role_groups

    Args:
        group_id (str):
        body (RoleGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutRoleGroupsByGroupIdResponseDefault | RoleGroupSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RoleGroupSchema,
) -> Any | PutRoleGroupsByGroupIdResponseDefault | RoleGroupSchema | None:
    """Update role group


    Required roles:
     - can_write_role_groups

    Args:
        group_id (str):
        body (RoleGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutRoleGroupsByGroupIdResponseDefault | RoleGroupSchema
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RoleGroupSchema,
) -> Response[Any | PutRoleGroupsByGroupIdResponseDefault | RoleGroupSchema]:
    """Update role group


    Required roles:
     - can_write_role_groups

    Args:
        group_id (str):
        body (RoleGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutRoleGroupsByGroupIdResponseDefault | RoleGroupSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: RoleGroupSchema,
) -> Any | PutRoleGroupsByGroupIdResponseDefault | RoleGroupSchema | None:
    """Update role group


    Required roles:
     - can_write_role_groups

    Args:
        group_id (str):
        body (RoleGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutRoleGroupsByGroupIdResponseDefault | RoleGroupSchema
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
        )
    ).parsed
