from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_playlists_by_playlist_id_keyframes_response_default_type_0 import (
    PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0,
)
from ...models.post_playlists_by_playlist_id_keyframes_response_default_type_1 import (
    PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1,
)
from ...models.synchronize_collection_keyframes_schema import (
    SynchronizeCollectionKeyframesSchema,
)
from ...types import Response


def _get_kwargs(
    playlist_id: str,
    *,
    body: SynchronizeCollectionKeyframesSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/playlists/{playlist_id}/keyframes/".format(
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
    | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0
    | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1
):
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

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
        PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0
        | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0
    | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1
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
    body: SynchronizeCollectionKeyframesSchema,
) -> Response[
    Any
    | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0
    | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1
]:
    """Pick up to three asset_ids for playlist keyframes


    Required roles:
     - can_reindex_playlists

    Args:
        playlist_id (str):
        body (SynchronizeCollectionKeyframesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0 | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1]
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
    body: SynchronizeCollectionKeyframesSchema,
) -> (
    Any
    | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0
    | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1
    | None
):
    """Pick up to three asset_ids for playlist keyframes


    Required roles:
     - can_reindex_playlists

    Args:
        playlist_id (str):
        body (SynchronizeCollectionKeyframesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0 | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1
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
    body: SynchronizeCollectionKeyframesSchema,
) -> Response[
    Any
    | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0
    | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1
]:
    """Pick up to three asset_ids for playlist keyframes


    Required roles:
     - can_reindex_playlists

    Args:
        playlist_id (str):
        body (SynchronizeCollectionKeyframesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0 | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1]
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
    body: SynchronizeCollectionKeyframesSchema,
) -> (
    Any
    | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0
    | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1
    | None
):
    """Pick up to three asset_ids for playlist keyframes


    Required roles:
     - can_reindex_playlists

    Args:
        playlist_id (str):
        body (SynchronizeCollectionKeyframesSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType0 | PostPlaylistsByPlaylistIdKeyframesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            playlist_id=playlist_id,
            client=client,
            body=body,
        )
    ).parsed
