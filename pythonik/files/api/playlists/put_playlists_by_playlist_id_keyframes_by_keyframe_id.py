from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.playlist_keyframe_schema import PlaylistKeyframeSchema
from ...models.put_playlists_by_playlist_id_keyframes_by_keyframe_id_response_default_type_0 import (
    PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0,
)
from ...models.put_playlists_by_playlist_id_keyframes_by_keyframe_id_response_default_type_1 import (
    PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    playlist_id: str,
    keyframe_id: str,
    *,
    body: PlaylistKeyframeSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/playlists/{playlist_id}/keyframes/{keyframe_id}/".format(
            playlist_id=quote(str(playlist_id), safe=""),
            keyframe_id=quote(str(keyframe_id), safe=""),
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
    | PlaylistKeyframeSchema
    | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
    | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = PlaylistKeyframeSchema.from_dict(response.json())

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
        PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
        | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1.from_dict(
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
    | PlaylistKeyframeSchema
    | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
    | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
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
    body: PlaylistKeyframeSchema,
) -> Response[
    Any
    | PlaylistKeyframeSchema
    | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
    | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
]:
    """Update keyframe information


    Required roles:
     - can_write_keyframes

    Args:
        playlist_id (str):
        keyframe_id (str):
        body (PlaylistKeyframeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PlaylistKeyframeSchema | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0 | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        keyframe_id=keyframe_id,
        body=body,
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
    body: PlaylistKeyframeSchema,
) -> (
    Any
    | PlaylistKeyframeSchema
    | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
    | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
    | None
):
    """Update keyframe information


    Required roles:
     - can_write_keyframes

    Args:
        playlist_id (str):
        keyframe_id (str):
        body (PlaylistKeyframeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PlaylistKeyframeSchema | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0 | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
    """

    return sync_detailed(
        playlist_id=playlist_id,
        keyframe_id=keyframe_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PlaylistKeyframeSchema,
) -> Response[
    Any
    | PlaylistKeyframeSchema
    | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
    | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
]:
    """Update keyframe information


    Required roles:
     - can_write_keyframes

    Args:
        playlist_id (str):
        keyframe_id (str):
        body (PlaylistKeyframeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PlaylistKeyframeSchema | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0 | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        keyframe_id=keyframe_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PlaylistKeyframeSchema,
) -> (
    Any
    | PlaylistKeyframeSchema
    | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
    | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
    | None
):
    """Update keyframe information


    Required roles:
     - can_write_keyframes

    Args:
        playlist_id (str):
        keyframe_id (str):
        body (PlaylistKeyframeSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PlaylistKeyframeSchema | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0 | PutPlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            keyframe_id=keyframe_id,
            client=client,
            body=body,
        )
    ).parsed
