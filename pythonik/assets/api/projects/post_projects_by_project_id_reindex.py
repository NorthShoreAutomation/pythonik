from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_projects_by_project_id_reindex_response_default_type_0 import (
    PostProjectsByProjectIdReindexResponseDefaultType0,
)
from ...models.post_projects_by_project_id_reindex_response_default_type_1 import (
    PostProjectsByProjectIdReindexResponseDefaultType1,
)
from ...models.reindex_project_schema import ReindexProjectSchema
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: ReindexProjectSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/projects/{project_id}/reindex/".format(
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
    | PostProjectsByProjectIdReindexResponseDefaultType0
    | PostProjectsByProjectIdReindexResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PostProjectsByProjectIdReindexResponseDefaultType0
        | PostProjectsByProjectIdReindexResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostProjectsByProjectIdReindexResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostProjectsByProjectIdReindexResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostProjectsByProjectIdReindexResponseDefaultType0
    | PostProjectsByProjectIdReindexResponseDefaultType1
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
    body: ReindexProjectSchema,
) -> Response[
    Any
    | PostProjectsByProjectIdReindexResponseDefaultType0
    | PostProjectsByProjectIdReindexResponseDefaultType1
]:
    """Reindex the project


    Required roles:
     - can_reindex_projects

    Args:
        project_id (str):
        body (ReindexProjectSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostProjectsByProjectIdReindexResponseDefaultType0 | PostProjectsByProjectIdReindexResponseDefaultType1]
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
    body: ReindexProjectSchema,
) -> (
    Any
    | PostProjectsByProjectIdReindexResponseDefaultType0
    | PostProjectsByProjectIdReindexResponseDefaultType1
    | None
):
    """Reindex the project


    Required roles:
     - can_reindex_projects

    Args:
        project_id (str):
        body (ReindexProjectSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostProjectsByProjectIdReindexResponseDefaultType0 | PostProjectsByProjectIdReindexResponseDefaultType1
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
    body: ReindexProjectSchema,
) -> Response[
    Any
    | PostProjectsByProjectIdReindexResponseDefaultType0
    | PostProjectsByProjectIdReindexResponseDefaultType1
]:
    """Reindex the project


    Required roles:
     - can_reindex_projects

    Args:
        project_id (str):
        body (ReindexProjectSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostProjectsByProjectIdReindexResponseDefaultType0 | PostProjectsByProjectIdReindexResponseDefaultType1]
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
    body: ReindexProjectSchema,
) -> (
    Any
    | PostProjectsByProjectIdReindexResponseDefaultType0
    | PostProjectsByProjectIdReindexResponseDefaultType1
    | None
):
    """Reindex the project


    Required roles:
     - can_reindex_projects

    Args:
        project_id (str):
        body (ReindexProjectSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostProjectsByProjectIdReindexResponseDefaultType0 | PostProjectsByProjectIdReindexResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
