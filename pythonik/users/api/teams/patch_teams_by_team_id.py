from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.patch_teams_by_team_id_response_default import (
    PatchTeamsByTeamIdResponseDefault,
)
from ...models.team_schema import TeamSchema
from ...types import Response


def _get_kwargs(
    team_id: str,
    *,
    body: TeamSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/teams/{team_id}/".format(
            team_id=quote(str(team_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchTeamsByTeamIdResponseDefault | TeamSchema:
    if response.status_code == 200:
        response_200 = TeamSchema.from_dict(response.json())

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

    response_default = PatchTeamsByTeamIdResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PatchTeamsByTeamIdResponseDefault | TeamSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TeamSchema,
) -> Response[Any | PatchTeamsByTeamIdResponseDefault | TeamSchema]:
    """Update team


    Required roles:
     - can_write_teams

    Args:
        team_id (str):
        body (TeamSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchTeamsByTeamIdResponseDefault | TeamSchema]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TeamSchema,
) -> Any | PatchTeamsByTeamIdResponseDefault | TeamSchema | None:
    """Update team


    Required roles:
     - can_write_teams

    Args:
        team_id (str):
        body (TeamSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchTeamsByTeamIdResponseDefault | TeamSchema
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TeamSchema,
) -> Response[Any | PatchTeamsByTeamIdResponseDefault | TeamSchema]:
    """Update team


    Required roles:
     - can_write_teams

    Args:
        team_id (str):
        body (TeamSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchTeamsByTeamIdResponseDefault | TeamSchema]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: TeamSchema,
) -> Any | PatchTeamsByTeamIdResponseDefault | TeamSchema | None:
    """Update team


    Required roles:
     - can_write_teams

    Args:
        team_id (str):
        body (TeamSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchTeamsByTeamIdResponseDefault | TeamSchema
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            body=body,
        )
    ).parsed
