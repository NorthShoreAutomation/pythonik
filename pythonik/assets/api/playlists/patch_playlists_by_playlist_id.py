from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.patch_playlists_by_playlist_id_response_default_type_0 import (
    PatchPlaylistsByPlaylistIdResponseDefaultType0,
)
from ...models.patch_playlists_by_playlist_id_response_default_type_1 import (
    PatchPlaylistsByPlaylistIdResponseDefaultType1,
)
from ...models.playlist_schema import PlaylistSchema
from ...types import Response


def _get_kwargs(
    playlist_id: str,
    *,
    body: PlaylistSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/playlists/{playlist_id}/".format(
            playlist_id=quote(str(playlist_id), safe=""),
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
    | PatchPlaylistsByPlaylistIdResponseDefaultType0
    | PatchPlaylistsByPlaylistIdResponseDefaultType1
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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        PatchPlaylistsByPlaylistIdResponseDefaultType0
        | PatchPlaylistsByPlaylistIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PatchPlaylistsByPlaylistIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PatchPlaylistsByPlaylistIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PatchPlaylistsByPlaylistIdResponseDefaultType0
    | PatchPlaylistsByPlaylistIdResponseDefaultType1
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
    body: PlaylistSchema,
) -> Response[
    Any
    | PatchPlaylistsByPlaylistIdResponseDefaultType0
    | PatchPlaylistsByPlaylistIdResponseDefaultType1
    | PlaylistSchema
]:
    """Update a playlist


    Required roles:
     - can_write_playlists

    Args:
        playlist_id (str):
        body (PlaylistSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchPlaylistsByPlaylistIdResponseDefaultType0 | PatchPlaylistsByPlaylistIdResponseDefaultType1 | PlaylistSchema]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PlaylistSchema,
) -> (
    Any
    | PatchPlaylistsByPlaylistIdResponseDefaultType0
    | PatchPlaylistsByPlaylistIdResponseDefaultType1
    | PlaylistSchema
    | None
):
    """Update a playlist


    Required roles:
     - can_write_playlists

    Args:
        playlist_id (str):
        body (PlaylistSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchPlaylistsByPlaylistIdResponseDefaultType0 | PatchPlaylistsByPlaylistIdResponseDefaultType1 | PlaylistSchema
    """

    return sync_detailed(
        playlist_id=playlist_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PlaylistSchema,
) -> Response[
    Any
    | PatchPlaylistsByPlaylistIdResponseDefaultType0
    | PatchPlaylistsByPlaylistIdResponseDefaultType1
    | PlaylistSchema
]:
    """Update a playlist


    Required roles:
     - can_write_playlists

    Args:
        playlist_id (str):
        body (PlaylistSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchPlaylistsByPlaylistIdResponseDefaultType0 | PatchPlaylistsByPlaylistIdResponseDefaultType1 | PlaylistSchema]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PlaylistSchema,
) -> (
    Any
    | PatchPlaylistsByPlaylistIdResponseDefaultType0
    | PatchPlaylistsByPlaylistIdResponseDefaultType1
    | PlaylistSchema
    | None
):
    """Update a playlist


    Required roles:
     - can_write_playlists

    Args:
        playlist_id (str):
        body (PlaylistSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchPlaylistsByPlaylistIdResponseDefaultType0 | PatchPlaylistsByPlaylistIdResponseDefaultType1 | PlaylistSchema
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
            body=body,
        )
    ).parsed
