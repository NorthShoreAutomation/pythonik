from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_playlists_by_playlist_id_keyframes_response_default_type_0 import (
    GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0,
)
from ...models.get_playlists_by_playlist_id_keyframes_response_default_type_1 import (
    GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1,
)
from ...models.playlist_keyframes_schema import PlaylistKeyframesSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    playlist_id: str,
    *,
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["generate_signed_url"] = generate_signed_url

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/playlists/{playlist_id}/keyframes/".format(
            playlist_id=quote(str(playlist_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0
    | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1
    | PlaylistKeyframesSchema
):
    if response.status_code == 200:
        response_200 = PlaylistKeyframesSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0
        | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0
    | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1
    | PlaylistKeyframesSchema
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
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0
    | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1
    | PlaylistKeyframesSchema
]:
    """Get all playlist's keyframes


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):
        per_page (int | Unset):  Default: 10.
        generate_signed_url (bool | Unset):  Default: True.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0 | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1 | PlaylistKeyframesSchema]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        per_page=per_page,
        generate_signed_url=generate_signed_url,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0
    | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1
    | PlaylistKeyframesSchema
    | None
):
    """Get all playlist's keyframes


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):
        per_page (int | Unset):  Default: 10.
        generate_signed_url (bool | Unset):  Default: True.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0 | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1 | PlaylistKeyframesSchema
    """

    return sync_detailed(
        playlist_id=playlist_id,
        client=client,
        per_page=per_page,
        generate_signed_url=generate_signed_url,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0
    | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1
    | PlaylistKeyframesSchema
]:
    """Get all playlist's keyframes


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):
        per_page (int | Unset):  Default: 10.
        generate_signed_url (bool | Unset):  Default: True.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0 | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1 | PlaylistKeyframesSchema]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        per_page=per_page,
        generate_signed_url=generate_signed_url,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    playlist_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0
    | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1
    | PlaylistKeyframesSchema
    | None
):
    """Get all playlist's keyframes


    Required roles:
     - can_read_playlists

    Args:
        playlist_id (str):
        per_page (int | Unset):  Default: 10.
        generate_signed_url (bool | Unset):  Default: True.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType0 | GetPlaylistsByPlaylistIdKeyframesResponseDefaultType1 | PlaylistKeyframesSchema
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
            per_page=per_page,
            generate_signed_url=generate_signed_url,
            last_id=last_id,
        )
    ).parsed
