from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.playlist_item_schema import PlaylistItemSchema
from ...models.playlist_item_update_position_schema import (
    PlaylistItemUpdatePositionSchema,
)
from ...models.put_playlists_by_playlist_id_items_by_item_id_position_response_default_type_0 import (
    PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0,
)
from ...models.put_playlists_by_playlist_id_items_by_item_id_position_response_default_type_1 import (
    PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    playlist_id: str,
    item_id: str,
    *,
    body: PlaylistItemUpdatePositionSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/playlists/{playlist_id}/items/{item_id}/position/".format(
            playlist_id=quote(str(playlist_id), safe=""),
            item_id=quote(str(item_id), safe=""),
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
    | PlaylistItemSchema
    | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0
    | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = PlaylistItemSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0
        | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1.from_dict(
                data
            )
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PlaylistItemSchema
    | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0
    | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1
]:
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
    body: PlaylistItemUpdatePositionSchema,
) -> Response[
    Any
    | PlaylistItemSchema
    | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0
    | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1
]:
    """Update a playlist item position


    Required roles:
     - can_update_playlist_items_position

    Args:
        playlist_id (str):
        item_id (str):
        body (PlaylistItemUpdatePositionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PlaylistItemSchema | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0 | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        item_id=item_id,
        body=body,
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
    body: PlaylistItemUpdatePositionSchema,
) -> (
    Any
    | PlaylistItemSchema
    | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0
    | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1
    | None
):
    """Update a playlist item position


    Required roles:
     - can_update_playlist_items_position

    Args:
        playlist_id (str):
        item_id (str):
        body (PlaylistItemUpdatePositionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PlaylistItemSchema | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0 | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1
    """

    return sync_detailed(
        playlist_id=playlist_id,
        item_id=item_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PlaylistItemUpdatePositionSchema,
) -> Response[
    Any
    | PlaylistItemSchema
    | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0
    | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1
]:
    """Update a playlist item position


    Required roles:
     - can_update_playlist_items_position

    Args:
        playlist_id (str):
        item_id (str):
        body (PlaylistItemUpdatePositionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PlaylistItemSchema | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0 | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        item_id=item_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PlaylistItemUpdatePositionSchema,
) -> (
    Any
    | PlaylistItemSchema
    | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0
    | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1
    | None
):
    """Update a playlist item position


    Required roles:
     - can_update_playlist_items_position

    Args:
        playlist_id (str):
        item_id (str):
        body (PlaylistItemUpdatePositionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PlaylistItemSchema | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType0 | PutPlaylistsByPlaylistIdItemsByItemIdPositionResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            item_id=item_id,
            client=client,
            body=body,
        )
    ).parsed
