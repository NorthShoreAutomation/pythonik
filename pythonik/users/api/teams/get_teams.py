from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_teams_response_default import GetTeamsResponseDefault
from ...models.teams_schema import TeamsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    alias: str | Unset = UNSET,
    description: str | Unset = UNSET,
    name: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["sort"] = sort

    params["alias"] = alias

    params["description"] = description

    params["name"] = name

    params["date_created"] = date_created

    params["date_modified"] = date_modified

    params["query"] = query

    params["ids"] = ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/teams/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetTeamsResponseDefault | TeamsSchema:
    if response.status_code == 200:
        response_200 = TeamsSchema.from_dict(response.json())

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

    response_default = GetTeamsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetTeamsResponseDefault | TeamsSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    alias: str | Unset = UNSET,
    description: str | Unset = UNSET,
    name: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Response[Any | GetTeamsResponseDefault | TeamsSchema]:
    """List teams with details


    Required roles:
     - can_read_teams

    Args:
        page (int | Unset):
        per_page (int | Unset):
        sort (str | Unset):
        alias (str | Unset):
        description (str | Unset):
        name (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        query (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTeamsResponseDefault | TeamsSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        alias=alias,
        description=description,
        name=name,
        date_created=date_created,
        date_modified=date_modified,
        query=query,
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    alias: str | Unset = UNSET,
    description: str | Unset = UNSET,
    name: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Any | GetTeamsResponseDefault | TeamsSchema | None:
    """List teams with details


    Required roles:
     - can_read_teams

    Args:
        page (int | Unset):
        per_page (int | Unset):
        sort (str | Unset):
        alias (str | Unset):
        description (str | Unset):
        name (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        query (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTeamsResponseDefault | TeamsSchema
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        sort=sort,
        alias=alias,
        description=description,
        name=name,
        date_created=date_created,
        date_modified=date_modified,
        query=query,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    alias: str | Unset = UNSET,
    description: str | Unset = UNSET,
    name: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Response[Any | GetTeamsResponseDefault | TeamsSchema]:
    """List teams with details


    Required roles:
     - can_read_teams

    Args:
        page (int | Unset):
        per_page (int | Unset):
        sort (str | Unset):
        alias (str | Unset):
        description (str | Unset):
        name (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        query (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTeamsResponseDefault | TeamsSchema]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        sort=sort,
        alias=alias,
        description=description,
        name=name,
        date_created=date_created,
        date_modified=date_modified,
        query=query,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    sort: str | Unset = UNSET,
    alias: str | Unset = UNSET,
    description: str | Unset = UNSET,
    name: str | Unset = UNSET,
    date_created: str | Unset = UNSET,
    date_modified: str | Unset = UNSET,
    query: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Any | GetTeamsResponseDefault | TeamsSchema | None:
    """List teams with details


    Required roles:
     - can_read_teams

    Args:
        page (int | Unset):
        per_page (int | Unset):
        sort (str | Unset):
        alias (str | Unset):
        description (str | Unset):
        name (str | Unset):
        date_created (str | Unset):
        date_modified (str | Unset):
        query (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTeamsResponseDefault | TeamsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            sort=sort,
            alias=alias,
            description=description,
            name=name,
            date_created=date_created,
            date_modified=date_modified,
            query=query,
            ids=ids,
        )
    ).parsed
