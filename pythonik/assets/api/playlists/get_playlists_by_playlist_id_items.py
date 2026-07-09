from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_playlists_by_playlist_id_items_response_default import (
    GetPlaylistsByPlaylistIdItemsResponseDefault,
)
from ...models.playlist_items_schema import PlaylistItemsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    playlist_id: str,
    *,
    per_page: int | Unset = UNSET,
    ids: str | Unset = UNSET,
    page: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["ids"] = ids

    params["page"] = page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/playlists/{playlist_id}/items/".format(
            playlist_id=quote(str(playlist_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetPlaylistsByPlaylistIdItemsResponseDefault | PlaylistItemsSchema:
    if response.status_code == 200:
        response_200 = PlaylistItemsSchema.from_dict(response.json())

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

    response_default = GetPlaylistsByPlaylistIdItemsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetPlaylistsByPlaylistIdItemsResponseDefault | PlaylistItemsSchema]:
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
    per_page: int | Unset = UNSET,
    ids: str | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[Any | GetPlaylistsByPlaylistIdItemsResponseDefault | PlaylistItemsSchema]:
    """Get list of playlist's items


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):
        per_page (int | Unset):
        ids (str | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPlaylistsByPlaylistIdItemsResponseDefault | PlaylistItemsSchema]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        per_page=per_page,
        ids=ids,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    ids: str | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Any | GetPlaylistsByPlaylistIdItemsResponseDefault | PlaylistItemsSchema | None:
    """Get list of playlist's items


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):
        per_page (int | Unset):
        ids (str | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPlaylistsByPlaylistIdItemsResponseDefault | PlaylistItemsSchema
    """

    return sync_detailed(
        playlist_id=playlist_id,
        client=client,
        per_page=per_page,
        ids=ids,
        page=page,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    ids: str | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Response[Any | GetPlaylistsByPlaylistIdItemsResponseDefault | PlaylistItemsSchema]:
    """Get list of playlist's items


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):
        per_page (int | Unset):
        ids (str | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPlaylistsByPlaylistIdItemsResponseDefault | PlaylistItemsSchema]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        per_page=per_page,
        ids=ids,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    ids: str | Unset = UNSET,
    page: int | Unset = UNSET,
) -> Any | GetPlaylistsByPlaylistIdItemsResponseDefault | PlaylistItemsSchema | None:
    """Get list of playlist's items


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):
        per_page (int | Unset):
        ids (str | Unset):
        page (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPlaylistsByPlaylistIdItemsResponseDefault | PlaylistItemsSchema
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
            per_page=per_page,
            ids=ids,
            page=page,
        )
    ).parsed
