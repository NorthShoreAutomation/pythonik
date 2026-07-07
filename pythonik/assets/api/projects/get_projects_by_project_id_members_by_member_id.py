from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_projects_by_project_id_members_by_member_id_response_default_type_0 import (
    GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0,
)
from ...models.get_projects_by_project_id_members_by_member_id_response_default_type_1 import (
    GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1,
)
from ...models.project_member_schema import ProjectMemberSchema
from ...types import Response


def _get_kwargs(
    project_id: str,
    member_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/members/{member_id}/".format(
            project_id=quote(str(project_id), safe=""),
            member_id=quote(str(member_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0
    | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1
    | ProjectMemberSchema
):
    if response.status_code == 200:
        response_200 = ProjectMemberSchema.from_dict(response.json())

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
        GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0
        | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0
    | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1
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
    member_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0
    | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1
    | ProjectMemberSchema
]:
    """Returns a particular project member by id


    Required roles:
     - can_read_projects

    Args:
        project_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0 | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1 | ProjectMemberSchema]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        member_id=member_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0
    | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1
    | ProjectMemberSchema
    | None
):
    """Returns a particular project member by id


    Required roles:
     - can_read_projects

    Args:
        project_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0 | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1 | ProjectMemberSchema
    """

    return sync_detailed(
        project_id=project_id,
        member_id=member_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0
    | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1
    | ProjectMemberSchema
]:
    """Returns a particular project member by id


    Required roles:
     - can_read_projects

    Args:
        project_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0 | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1 | ProjectMemberSchema]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        member_id=member_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0
    | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1
    | ProjectMemberSchema
    | None
):
    """Returns a particular project member by id


    Required roles:
     - can_read_projects

    Args:
        project_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType0 | GetProjectsByProjectIdMembersByMemberIdResponseDefaultType1 | ProjectMemberSchema
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            member_id=member_id,
            client=client,
        )
    ).parsed
