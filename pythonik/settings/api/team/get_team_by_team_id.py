from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_team_by_team_id_response_default_type_0 import (
    GetTeamByTeamIdResponseDefaultType0,
)
from ...models.get_team_by_team_id_response_default_type_1 import (
    GetTeamByTeamIdResponseDefaultType1,
)
from ...models.group_setting_public_schema import GroupSettingPublicSchema
from ...types import Response


def _get_kwargs(
    team_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/team/{team_id}/".format(
            team_id=quote(str(team_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetTeamByTeamIdResponseDefaultType0
    | GetTeamByTeamIdResponseDefaultType1
    | GroupSettingPublicSchema
):
    if response.status_code == 200:
        response_200 = GroupSettingPublicSchema.from_dict(response.json())

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

    def _parse_response_default(
        data: object,
    ) -> GetTeamByTeamIdResponseDefaultType0 | GetTeamByTeamIdResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetTeamByTeamIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetTeamByTeamIdResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetTeamByTeamIdResponseDefaultType0
    | GetTeamByTeamIdResponseDefaultType1
    | GroupSettingPublicSchema
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
    | GetTeamByTeamIdResponseDefaultType0
    | GetTeamByTeamIdResponseDefaultType1
    | GroupSettingPublicSchema
]:
    """Team settings

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTeamByTeamIdResponseDefaultType0 | GetTeamByTeamIdResponseDefaultType1 | GroupSettingPublicSchema]
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
    | GetTeamByTeamIdResponseDefaultType0
    | GetTeamByTeamIdResponseDefaultType1
    | GroupSettingPublicSchema
    | None
):
    """Team settings

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTeamByTeamIdResponseDefaultType0 | GetTeamByTeamIdResponseDefaultType1 | GroupSettingPublicSchema
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
    | GetTeamByTeamIdResponseDefaultType0
    | GetTeamByTeamIdResponseDefaultType1
    | GroupSettingPublicSchema
]:
    """Team settings

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetTeamByTeamIdResponseDefaultType0 | GetTeamByTeamIdResponseDefaultType1 | GroupSettingPublicSchema]
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
    | GetTeamByTeamIdResponseDefaultType0
    | GetTeamByTeamIdResponseDefaultType1
    | GroupSettingPublicSchema
    | None
):
    """Team settings

    Args:
        team_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetTeamByTeamIdResponseDefaultType0 | GetTeamByTeamIdResponseDefaultType1 | GroupSettingPublicSchema
    """

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
        )
    ).parsed
