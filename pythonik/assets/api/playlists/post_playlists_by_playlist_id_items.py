from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.playlist_item_schema import PlaylistItemSchema
from ...models.post_playlists_by_playlist_id_items_response_default import (
    PostPlaylistsByPlaylistIdItemsResponseDefault,
)
from ...types import Response


def _get_kwargs(
    playlist_id: str,
    *,
    body: PlaylistItemSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/playlists/{playlist_id}/items/".format(
            playlist_id=quote(str(playlist_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PlaylistItemSchema | PostPlaylistsByPlaylistIdItemsResponseDefault:
    if response.status_code == 201:
        response_201 = PlaylistItemSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostPlaylistsByPlaylistIdItemsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PlaylistItemSchema | PostPlaylistsByPlaylistIdItemsResponseDefault]:
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
    body: PlaylistItemSchema,
) -> Response[Any | PlaylistItemSchema | PostPlaylistsByPlaylistIdItemsResponseDefault]:
    """Add an item to a playlist


    Required roles:
     - can_add_playlist_items

    Args:
        playlist_id (str):
        body (PlaylistItemSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PlaylistItemSchema | PostPlaylistsByPlaylistIdItemsResponseDefault]
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
    body: PlaylistItemSchema,
) -> Any | PlaylistItemSchema | PostPlaylistsByPlaylistIdItemsResponseDefault | None:
    """Add an item to a playlist


    Required roles:
     - can_add_playlist_items

    Args:
        playlist_id (str):
        body (PlaylistItemSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PlaylistItemSchema | PostPlaylistsByPlaylistIdItemsResponseDefault
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
    body: PlaylistItemSchema,
) -> Response[Any | PlaylistItemSchema | PostPlaylistsByPlaylistIdItemsResponseDefault]:
    """Add an item to a playlist


    Required roles:
     - can_add_playlist_items

    Args:
        playlist_id (str):
        body (PlaylistItemSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PlaylistItemSchema | PostPlaylistsByPlaylistIdItemsResponseDefault]
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
    body: PlaylistItemSchema,
) -> Any | PlaylistItemSchema | PostPlaylistsByPlaylistIdItemsResponseDefault | None:
    """Add an item to a playlist


    Required roles:
     - can_add_playlist_items

    Args:
        playlist_id (str):
        body (PlaylistItemSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PlaylistItemSchema | PostPlaylistsByPlaylistIdItemsResponseDefault
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
            body=body,
        )
    ).parsed
