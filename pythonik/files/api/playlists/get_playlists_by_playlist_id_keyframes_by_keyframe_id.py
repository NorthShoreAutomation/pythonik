from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_playlists_by_playlist_id_keyframes_by_keyframe_id_response_default import (
    GetPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefault,
)
from ...models.playlist_keyframe_schema import PlaylistKeyframeSchema
from ...types import Response


def _get_kwargs(
    playlist_id: str,
    keyframe_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/playlists/{playlist_id}/keyframes/{keyframe_id}/".format(
            playlist_id=quote(str(playlist_id), safe=""),
            keyframe_id=quote(str(keyframe_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefault
    | PlaylistKeyframeSchema
):
    if response.status_code == 200:
        response_200 = PlaylistKeyframeSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        GetPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefault
    | PlaylistKeyframeSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    playlist_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefault
    | PlaylistKeyframeSchema
]:
    """Get playlist's keyframe


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):
        keyframe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefault | PlaylistKeyframeSchema]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        keyframe_id=keyframe_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefault
    | PlaylistKeyframeSchema
    | None
):
    """Get playlist's keyframe


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):
        keyframe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefault | PlaylistKeyframeSchema
    """

    return sync_detailed(
        playlist_id=playlist_id,
        keyframe_id=keyframe_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefault
    | PlaylistKeyframeSchema
]:
    """Get playlist's keyframe


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):
        keyframe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefault | PlaylistKeyframeSchema]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        keyframe_id=keyframe_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefault
    | PlaylistKeyframeSchema
    | None
):
    """Get playlist's keyframe


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):
        keyframe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefault | PlaylistKeyframeSchema
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            keyframe_id=keyframe_id,
            client=client,
        )
    ).parsed
