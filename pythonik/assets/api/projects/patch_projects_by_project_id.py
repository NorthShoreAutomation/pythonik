from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.patch_projects_by_project_id_response_default import (
    PatchProjectsByProjectIdResponseDefault,
)
from ...models.project_schema import ProjectSchema
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ProjectSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/projects/{project_id}/".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchProjectsByProjectIdResponseDefault | ProjectSchema:
    if response.status_code == 200:
        response_200 = ProjectSchema.from_dict(response.json())

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

    response_default = PatchProjectsByProjectIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PatchProjectsByProjectIdResponseDefault | ProjectSchema]:
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
    body: ProjectSchema,
) -> Response[Any | PatchProjectsByProjectIdResponseDefault | ProjectSchema]:
    """Update project


    Required roles:
     - can_write_projects

    Args:
        project_id (str):
        body (ProjectSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchProjectsByProjectIdResponseDefault | ProjectSchema]
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
    body: ProjectSchema,
) -> Any | PatchProjectsByProjectIdResponseDefault | ProjectSchema | None:
    """Update project


    Required roles:
     - can_write_projects

    Args:
        project_id (str):
        body (ProjectSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchProjectsByProjectIdResponseDefault | ProjectSchema
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
    body: ProjectSchema,
) -> Response[Any | PatchProjectsByProjectIdResponseDefault | ProjectSchema]:
    """Update project


    Required roles:
     - can_write_projects

    Args:
        project_id (str):
        body (ProjectSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchProjectsByProjectIdResponseDefault | ProjectSchema]
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
    body: ProjectSchema,
) -> Any | PatchProjectsByProjectIdResponseDefault | ProjectSchema | None:
    """Update project


    Required roles:
     - can_write_projects

    Args:
        project_id (str):
        body (ProjectSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchProjectsByProjectIdResponseDefault | ProjectSchema
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
