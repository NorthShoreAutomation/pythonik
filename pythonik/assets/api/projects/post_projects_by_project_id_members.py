from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_projects_by_project_id_members_response_default_type_0 import (
    PostProjectsByProjectIdMembersResponseDefaultType0,
)
from ...models.post_projects_by_project_id_members_response_default_type_1 import (
    PostProjectsByProjectIdMembersResponseDefaultType1,
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
) -> (
    Any
    | PostProjectsByProjectIdMembersResponseDefaultType0
    | PostProjectsByProjectIdMembersResponseDefaultType1
    | ProjectMemberSchema
):
    if response.status_code == 201:
        response_201 = ProjectMemberSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostProjectsByProjectIdMembersResponseDefaultType0
        | PostProjectsByProjectIdMembersResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostProjectsByProjectIdMembersResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostProjectsByProjectIdMembersResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostProjectsByProjectIdMembersResponseDefaultType0
    | PostProjectsByProjectIdMembersResponseDefaultType1
    | ProjectMemberSchema
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
    Any
    | PostProjectsByProjectIdMembersResponseDefaultType0
    | PostProjectsByProjectIdMembersResponseDefaultType1
    | ProjectMemberSchema
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
        Response[Any | PostProjectsByProjectIdMembersResponseDefaultType0 | PostProjectsByProjectIdMembersResponseDefaultType1 | ProjectMemberSchema]
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
) -> (
    Any
    | PostProjectsByProjectIdMembersResponseDefaultType0
    | PostProjectsByProjectIdMembersResponseDefaultType1
    | ProjectMemberSchema
    | None
):
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
        Any | PostProjectsByProjectIdMembersResponseDefaultType0 | PostProjectsByProjectIdMembersResponseDefaultType1 | ProjectMemberSchema
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
    Any
    | PostProjectsByProjectIdMembersResponseDefaultType0
    | PostProjectsByProjectIdMembersResponseDefaultType1
    | ProjectMemberSchema
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
        Response[Any | PostProjectsByProjectIdMembersResponseDefaultType0 | PostProjectsByProjectIdMembersResponseDefaultType1 | ProjectMemberSchema]
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
) -> (
    Any
    | PostProjectsByProjectIdMembersResponseDefaultType0
    | PostProjectsByProjectIdMembersResponseDefaultType1
    | ProjectMemberSchema
    | None
):
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
        Any | PostProjectsByProjectIdMembersResponseDefaultType0 | PostProjectsByProjectIdMembersResponseDefaultType1 | ProjectMemberSchema
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
