from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_playlists_by_playlist_id_response_default_type_0 import (
    GetPlaylistsByPlaylistIdResponseDefaultType0,
)
from ...models.get_playlists_by_playlist_id_response_default_type_1 import (
    GetPlaylistsByPlaylistIdResponseDefaultType1,
)
from ...models.playlist_schema import PlaylistSchema
from ...types import Response


def _get_kwargs(
    playlist_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/playlists/{playlist_id}/".format(
            playlist_id=quote(str(playlist_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetPlaylistsByPlaylistIdResponseDefaultType0
    | GetPlaylistsByPlaylistIdResponseDefaultType1
    | PlaylistSchema
):
    if response.status_code == 200:
        response_200 = PlaylistSchema.from_dict(response.json())

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
        GetPlaylistsByPlaylistIdResponseDefaultType0
        | GetPlaylistsByPlaylistIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetPlaylistsByPlaylistIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetPlaylistsByPlaylistIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetPlaylistsByPlaylistIdResponseDefaultType0
    | GetPlaylistsByPlaylistIdResponseDefaultType1
    | PlaylistSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetPlaylistsByPlaylistIdResponseDefaultType0
    | GetPlaylistsByPlaylistIdResponseDefaultType1
    | PlaylistSchema
]:
    """Returns a particular playlist by id


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPlaylistsByPlaylistIdResponseDefaultType0 | GetPlaylistsByPlaylistIdResponseDefaultType1 | PlaylistSchema]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetPlaylistsByPlaylistIdResponseDefaultType0
    | GetPlaylistsByPlaylistIdResponseDefaultType1
    | PlaylistSchema
    | None
):
    """Returns a particular playlist by id


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPlaylistsByPlaylistIdResponseDefaultType0 | GetPlaylistsByPlaylistIdResponseDefaultType1 | PlaylistSchema
    """

    return sync_detailed(
        playlist_id=playlist_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetPlaylistsByPlaylistIdResponseDefaultType0
    | GetPlaylistsByPlaylistIdResponseDefaultType1
    | PlaylistSchema
]:
    """Returns a particular playlist by id


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPlaylistsByPlaylistIdResponseDefaultType0 | GetPlaylistsByPlaylistIdResponseDefaultType1 | PlaylistSchema]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetPlaylistsByPlaylistIdResponseDefaultType0
    | GetPlaylistsByPlaylistIdResponseDefaultType1
    | PlaylistSchema
    | None
):
    """Returns a particular playlist by id


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPlaylistsByPlaylistIdResponseDefaultType0 | GetPlaylistsByPlaylistIdResponseDefaultType1 | PlaylistSchema
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
        )
    ).parsed
