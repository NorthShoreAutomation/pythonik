from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_playlists_by_playlist_id_keyframes_by_keyframe_id_response_default_type_0 import (
    DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0,
)
from ...models.delete_playlists_by_playlist_id_keyframes_by_keyframe_id_response_default_type_1 import (
    DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    playlist_id: str,
    keyframe_id: str,
    *,
    regenerate_keyframes: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["regenerate_keyframes"] = regenerate_keyframes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/playlists/{playlist_id}/keyframes/{keyframe_id}/".format(
            playlist_id=quote(str(playlist_id), safe=""),
            keyframe_id=quote(str(keyframe_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
    | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
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

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
        | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
    | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
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
    regenerate_keyframes: bool | Unset = UNSET,
) -> Response[
    Any
    | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
    | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
]:
    """Delete playlist's keyframe


    Required roles:
     - can_write_keyframes

    Args:
        playlist_id (str):
        keyframe_id (str):
        regenerate_keyframes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0 | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        keyframe_id=keyframe_id,
        regenerate_keyframes=regenerate_keyframes,
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
    regenerate_keyframes: bool | Unset = UNSET,
) -> (
    Any
    | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
    | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
    | None
):
    """Delete playlist's keyframe


    Required roles:
     - can_write_keyframes

    Args:
        playlist_id (str):
        keyframe_id (str):
        regenerate_keyframes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0 | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
    """

    return sync_detailed(
        playlist_id=playlist_id,
        keyframe_id=keyframe_id,
        client=client,
        regenerate_keyframes=regenerate_keyframes,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
    regenerate_keyframes: bool | Unset = UNSET,
) -> Response[
    Any
    | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
    | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
]:
    """Delete playlist's keyframe


    Required roles:
     - can_write_keyframes

    Args:
        playlist_id (str):
        keyframe_id (str):
        regenerate_keyframes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0 | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        keyframe_id=keyframe_id,
        regenerate_keyframes=regenerate_keyframes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    keyframe_id: str,
    *,
    client: AuthenticatedClient | Client,
    regenerate_keyframes: bool | Unset = UNSET,
) -> (
    Any
    | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0
    | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
    | None
):
    """Delete playlist's keyframe


    Required roles:
     - can_write_keyframes

    Args:
        playlist_id (str):
        keyframe_id (str):
        regenerate_keyframes (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType0 | DeletePlaylistsByPlaylistIdKeyframesByKeyframeIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            keyframe_id=keyframe_id,
            client=client,
            regenerate_keyframes=regenerate_keyframes,
        )
    ).parsed
