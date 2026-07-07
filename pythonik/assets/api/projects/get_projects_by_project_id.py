from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_projects_by_project_id_response_default_type_0 import (
    GetProjectsByProjectIdResponseDefaultType0,
)
from ...models.get_projects_by_project_id_response_default_type_1 import (
    GetProjectsByProjectIdResponseDefaultType1,
)
from ...models.project_schema import ProjectSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    include_users: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_users"] = include_users

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/projects/{project_id}/".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetProjectsByProjectIdResponseDefaultType0
    | GetProjectsByProjectIdResponseDefaultType1
    | ProjectSchema
):
    if response.status_code == 200:
        response_200 = ProjectSchema.from_dict(response.json())

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
        GetProjectsByProjectIdResponseDefaultType0
        | GetProjectsByProjectIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetProjectsByProjectIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetProjectsByProjectIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetProjectsByProjectIdResponseDefaultType0
    | GetProjectsByProjectIdResponseDefaultType1
    | ProjectSchema
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
    include_users: bool | Unset = False,
) -> Response[
    Any
    | GetProjectsByProjectIdResponseDefaultType0
    | GetProjectsByProjectIdResponseDefaultType1
    | ProjectSchema
]:
    """Returns a particular project by id


    Required roles:
     - can_read_projects

    Args:
        project_id (str):
        include_users (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetProjectsByProjectIdResponseDefaultType0 | GetProjectsByProjectIdResponseDefaultType1 | ProjectSchema]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        include_users=include_users,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_users: bool | Unset = False,
) -> (
    Any
    | GetProjectsByProjectIdResponseDefaultType0
    | GetProjectsByProjectIdResponseDefaultType1
    | ProjectSchema
    | None
):
    """Returns a particular project by id


    Required roles:
     - can_read_projects

    Args:
        project_id (str):
        include_users (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetProjectsByProjectIdResponseDefaultType0 | GetProjectsByProjectIdResponseDefaultType1 | ProjectSchema
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        include_users=include_users,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_users: bool | Unset = False,
) -> Response[
    Any
    | GetProjectsByProjectIdResponseDefaultType0
    | GetProjectsByProjectIdResponseDefaultType1
    | ProjectSchema
]:
    """Returns a particular project by id


    Required roles:
     - can_read_projects

    Args:
        project_id (str):
        include_users (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetProjectsByProjectIdResponseDefaultType0 | GetProjectsByProjectIdResponseDefaultType1 | ProjectSchema]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        include_users=include_users,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_users: bool | Unset = False,
) -> (
    Any
    | GetProjectsByProjectIdResponseDefaultType0
    | GetProjectsByProjectIdResponseDefaultType1
    | ProjectSchema
    | None
):
    """Returns a particular project by id


    Required roles:
     - can_read_projects

    Args:
        project_id (str):
        include_users (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetProjectsByProjectIdResponseDefaultType0 | GetProjectsByProjectIdResponseDefaultType1 | ProjectSchema
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            include_users=include_users,
        )
    ).parsed
