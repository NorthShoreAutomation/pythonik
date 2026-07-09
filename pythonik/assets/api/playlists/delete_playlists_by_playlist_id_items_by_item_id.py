from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_playlists_by_playlist_id_items_by_item_id_response_default import (
    DeletePlaylistsByPlaylistIdItemsByItemIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    playlist_id: str,
    item_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/playlists/{playlist_id}/items/{item_id}/".format(
            playlist_id=quote(str(playlist_id), safe=""),
            item_id=quote(str(item_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeletePlaylistsByPlaylistIdItemsByItemIdResponseDefault:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        DeletePlaylistsByPlaylistIdItemsByItemIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeletePlaylistsByPlaylistIdItemsByItemIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    playlist_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeletePlaylistsByPlaylistIdItemsByItemIdResponseDefault]:
    """Delete a particular playlist item by id


    Required roles:
     - can_delete_playlist_items

    Args:
        playlist_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeletePlaylistsByPlaylistIdItemsByItemIdResponseDefault]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        item_id=item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeletePlaylistsByPlaylistIdItemsByItemIdResponseDefault | None:
    """Delete a particular playlist item by id


    Required roles:
     - can_delete_playlist_items

    Args:
        playlist_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeletePlaylistsByPlaylistIdItemsByItemIdResponseDefault
    """

    return sync_detailed(
        playlist_id=playlist_id,
        item_id=item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeletePlaylistsByPlaylistIdItemsByItemIdResponseDefault]:
    """Delete a particular playlist item by id


    Required roles:
     - can_delete_playlist_items

    Args:
        playlist_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeletePlaylistsByPlaylistIdItemsByItemIdResponseDefault]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeletePlaylistsByPlaylistIdItemsByItemIdResponseDefault | None:
    """Delete a particular playlist item by id


    Required roles:
     - can_delete_playlist_items

    Args:
        playlist_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeletePlaylistsByPlaylistIdItemsByItemIdResponseDefault
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            item_id=item_id,
            client=client,
        )
    ).parsed
