from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_projects_by_project_id_response_default_type_0 import (
    DeleteProjectsByProjectIdResponseDefaultType0,
)
from ...models.delete_projects_by_project_id_response_default_type_1 import (
    DeleteProjectsByProjectIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    project_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/projects/{project_id}/".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteProjectsByProjectIdResponseDefaultType0
    | DeleteProjectsByProjectIdResponseDefaultType1
):
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

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
        DeleteProjectsByProjectIdResponseDefaultType0
        | DeleteProjectsByProjectIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                DeleteProjectsByProjectIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            DeleteProjectsByProjectIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteProjectsByProjectIdResponseDefaultType0
    | DeleteProjectsByProjectIdResponseDefaultType1
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
) -> Response[
    Any
    | DeleteProjectsByProjectIdResponseDefaultType0
    | DeleteProjectsByProjectIdResponseDefaultType1
]:
    """Delete a particular project by id


    Required roles:
     - can_delete_projects

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteProjectsByProjectIdResponseDefaultType0 | DeleteProjectsByProjectIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteProjectsByProjectIdResponseDefaultType0
    | DeleteProjectsByProjectIdResponseDefaultType1
    | None
):
    """Delete a particular project by id


    Required roles:
     - can_delete_projects

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteProjectsByProjectIdResponseDefaultType0 | DeleteProjectsByProjectIdResponseDefaultType1
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteProjectsByProjectIdResponseDefaultType0
    | DeleteProjectsByProjectIdResponseDefaultType1
]:
    """Delete a particular project by id


    Required roles:
     - can_delete_projects

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteProjectsByProjectIdResponseDefaultType0 | DeleteProjectsByProjectIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteProjectsByProjectIdResponseDefaultType0
    | DeleteProjectsByProjectIdResponseDefaultType1
    | None
):
    """Delete a particular project by id


    Required roles:
     - can_delete_projects

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteProjectsByProjectIdResponseDefaultType0 | DeleteProjectsByProjectIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
