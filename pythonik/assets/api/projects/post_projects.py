from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_projects_response_default_type_0 import (
    PostProjectsResponseDefaultType0,
)
from ...models.post_projects_response_default_type_1 import (
    PostProjectsResponseDefaultType1,
)
from ...models.project_create_schema import ProjectCreateSchema
from ...models.project_schema import ProjectSchema
from ...types import Response


def _get_kwargs(
    *,
    body: ProjectCreateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostProjectsResponseDefaultType0
    | PostProjectsResponseDefaultType1
    | ProjectSchema
):
    if response.status_code == 201:
        response_201 = ProjectSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> PostProjectsResponseDefaultType0 | PostProjectsResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostProjectsResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostProjectsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostProjectsResponseDefaultType0
    | PostProjectsResponseDefaultType1
    | ProjectSchema
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
    body: ProjectCreateSchema,
) -> Response[
    Any
    | PostProjectsResponseDefaultType0
    | PostProjectsResponseDefaultType1
    | ProjectSchema
]:
    """Create a new project


    Required roles:
     - can_create_projects

    Args:
        body (ProjectCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostProjectsResponseDefaultType0 | PostProjectsResponseDefaultType1 | ProjectSchema]
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
    body: ProjectCreateSchema,
) -> (
    Any
    | PostProjectsResponseDefaultType0
    | PostProjectsResponseDefaultType1
    | ProjectSchema
    | None
):
    """Create a new project


    Required roles:
     - can_create_projects

    Args:
        body (ProjectCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostProjectsResponseDefaultType0 | PostProjectsResponseDefaultType1 | ProjectSchema
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ProjectCreateSchema,
) -> Response[
    Any
    | PostProjectsResponseDefaultType0
    | PostProjectsResponseDefaultType1
    | ProjectSchema
]:
    """Create a new project


    Required roles:
     - can_create_projects

    Args:
        body (ProjectCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostProjectsResponseDefaultType0 | PostProjectsResponseDefaultType1 | ProjectSchema]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ProjectCreateSchema,
) -> (
    Any
    | PostProjectsResponseDefaultType0
    | PostProjectsResponseDefaultType1
    | ProjectSchema
    | None
):
    """Create a new project


    Required roles:
     - can_create_projects

    Args:
        body (ProjectCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostProjectsResponseDefaultType0 | PostProjectsResponseDefaultType1 | ProjectSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
