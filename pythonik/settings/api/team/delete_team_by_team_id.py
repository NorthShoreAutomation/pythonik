from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_team_by_team_id_response_default_type_0 import (
    DeleteTeamByTeamIdResponseDefaultType0,
)
from ...models.delete_team_by_team_id_response_default_type_1 import (
    DeleteTeamByTeamIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    team_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/team/{team_id}/".format(
            team_id=quote(str(team_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteTeamByTeamIdResponseDefaultType0
    | DeleteTeamByTeamIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        DeleteTeamByTeamIdResponseDefaultType0 | DeleteTeamByTeamIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteTeamByTeamIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteTeamByTeamIdResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteTeamByTeamIdResponseDefaultType0
    | DeleteTeamByTeamIdResponseDefaultType1
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
) -> Response[
    Any
    | DeleteTeamByTeamIdResponseDefaultType0
    | DeleteTeamByTeamIdResponseDefaultType1
]:
    """Delete team settings


    Required roles:
     - can_write_teams

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteTeamByTeamIdResponseDefaultType0 | DeleteTeamByTeamIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteTeamByTeamIdResponseDefaultType0
    | DeleteTeamByTeamIdResponseDefaultType1
    | None
):
    """Delete team settings


    Required roles:
     - can_write_teams

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteTeamByTeamIdResponseDefaultType0 | DeleteTeamByTeamIdResponseDefaultType1
    """

    return sync_detailed(
        team_id=team_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteTeamByTeamIdResponseDefaultType0
    | DeleteTeamByTeamIdResponseDefaultType1
]:
    """Delete team settings


    Required roles:
     - can_write_teams

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteTeamByTeamIdResponseDefaultType0 | DeleteTeamByTeamIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        team_id=team_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteTeamByTeamIdResponseDefaultType0
    | DeleteTeamByTeamIdResponseDefaultType1
    | None
):
    """Delete team settings


    Required roles:
     - can_write_teams

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteTeamByTeamIdResponseDefaultType0 | DeleteTeamByTeamIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
        )
    ).parsed
