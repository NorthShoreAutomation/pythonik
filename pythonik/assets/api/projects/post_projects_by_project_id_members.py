from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_projects_by_project_id_members_response_default import (
    PostProjectsByProjectIdMembersResponseDefault,
)
from ...models.project_member_create_schema import ProjectMemberCreateSchema
from ...models.project_member_schema import ProjectMemberSchema
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ProjectMemberCreateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/members/".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostProjectsByProjectIdMembersResponseDefault | ProjectMemberSchema:
    if response.status_code == 201:
        response_201 = ProjectMemberSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostProjectsByProjectIdMembersResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostProjectsByProjectIdMembersResponseDefault | ProjectMemberSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectMemberCreateSchema,
) -> Response[
    Any | PostProjectsByProjectIdMembersResponseDefault | ProjectMemberSchema
]:
    """Add a member to a project


    Required roles:
     - can_add_project_members

    Args:
        project_id (str):
        body (ProjectMemberCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostProjectsByProjectIdMembersResponseDefault | ProjectMemberSchema]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectMemberCreateSchema,
) -> Any | PostProjectsByProjectIdMembersResponseDefault | ProjectMemberSchema | None:
    """Add a member to a project


    Required roles:
     - can_add_project_members

    Args:
        project_id (str):
        body (ProjectMemberCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostProjectsByProjectIdMembersResponseDefault | ProjectMemberSchema
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectMemberCreateSchema,
) -> Response[
    Any | PostProjectsByProjectIdMembersResponseDefault | ProjectMemberSchema
]:
    """Add a member to a project


    Required roles:
     - can_add_project_members

    Args:
        project_id (str):
        body (ProjectMemberCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostProjectsByProjectIdMembersResponseDefault | ProjectMemberSchema]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ProjectMemberCreateSchema,
) -> Any | PostProjectsByProjectIdMembersResponseDefault | ProjectMemberSchema | None:
    """Add a member to a project


    Required roles:
     - can_add_project_members

    Args:
        project_id (str):
        body (ProjectMemberCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostProjectsByProjectIdMembersResponseDefault | ProjectMemberSchema
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
