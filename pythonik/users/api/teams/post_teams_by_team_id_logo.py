from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_teams_by_team_id_logo_body import PostTeamsByTeamIdLogoBody
from ...models.post_teams_by_team_id_logo_response_200 import (
    PostTeamsByTeamIdLogoResponse200,
)
from ...models.post_teams_by_team_id_logo_response_default import (
    PostTeamsByTeamIdLogoResponseDefault,
)
from ...types import Response


def _get_kwargs(
    team_id: str,
    *,
    body: PostTeamsByTeamIdLogoBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/teams/{team_id}/logo/".format(
            team_id=quote(str(team_id), safe=""),
        ),
    }

    _kwargs["content"] = body.payload
    headers["Content-Type"] = "image/*"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostTeamsByTeamIdLogoResponse200 | PostTeamsByTeamIdLogoResponseDefault:
    if response.status_code == 200:
        response_200 = PostTeamsByTeamIdLogoResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PostTeamsByTeamIdLogoResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PostTeamsByTeamIdLogoResponse200 | PostTeamsByTeamIdLogoResponseDefault
]:
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
    body: PostTeamsByTeamIdLogoBody,
) -> Response[
    Any | PostTeamsByTeamIdLogoResponse200 | PostTeamsByTeamIdLogoResponseDefault
]:
    """Upload team logo image


    Required roles:
     - can_write_teams

    Args:
        team_id (str):
        body (PostTeamsByTeamIdLogoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostTeamsByTeamIdLogoResponse200 | PostTeamsByTeamIdLogoResponseDefault]
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
    body: PostTeamsByTeamIdLogoBody,
) -> (
    Any | PostTeamsByTeamIdLogoResponse200 | PostTeamsByTeamIdLogoResponseDefault | None
):
    """Upload team logo image


    Required roles:
     - can_write_teams

    Args:
        team_id (str):
        body (PostTeamsByTeamIdLogoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostTeamsByTeamIdLogoResponse200 | PostTeamsByTeamIdLogoResponseDefault
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
    body: PostTeamsByTeamIdLogoBody,
) -> Response[
    Any | PostTeamsByTeamIdLogoResponse200 | PostTeamsByTeamIdLogoResponseDefault
]:
    """Upload team logo image


    Required roles:
     - can_write_teams

    Args:
        team_id (str):
        body (PostTeamsByTeamIdLogoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostTeamsByTeamIdLogoResponse200 | PostTeamsByTeamIdLogoResponseDefault]
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
    body: PostTeamsByTeamIdLogoBody,
) -> (
    Any | PostTeamsByTeamIdLogoResponse200 | PostTeamsByTeamIdLogoResponseDefault | None
):
    """Upload team logo image


    Required roles:
     - can_write_teams

    Args:
        team_id (str):
        body (PostTeamsByTeamIdLogoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostTeamsByTeamIdLogoResponse200 | PostTeamsByTeamIdLogoResponseDefault
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            body=body,
        )
    ).parsed
