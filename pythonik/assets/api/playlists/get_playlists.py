from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_playlists_response_default_type_0 import (
    GetPlaylistsResponseDefaultType0,
)
from ...models.get_playlists_response_default_type_1 import (
    GetPlaylistsResponseDefaultType1,
)
from ...models.playlists_schema import PlaylistsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    status: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["scroll"] = scroll

    params["scroll_id"] = scroll_id

    params["sort"] = sort

    params["status"] = status

    params["ids"] = ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/playlists/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetPlaylistsResponseDefaultType0
    | GetPlaylistsResponseDefaultType1
    | PlaylistsSchema
):
    if response.status_code == 200:
        response_200 = PlaylistsSchema.from_dict(response.json())

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
    ) -> GetPlaylistsResponseDefaultType0 | GetPlaylistsResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetPlaylistsResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetPlaylistsResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetPlaylistsResponseDefaultType0
    | GetPlaylistsResponseDefaultType1
    | PlaylistsSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    status: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Response[
    Any
    | GetPlaylistsResponseDefaultType0
    | GetPlaylistsResponseDefaultType1
    | PlaylistsSchema
]:
    """Get list of playlists


    Required roles:
     - can_read_playlists

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        status (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPlaylistsResponseDefaultType0 | GetPlaylistsResponseDefaultType1 | PlaylistsSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        status=status,
        ids=ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    status: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> (
    Any
    | GetPlaylistsResponseDefaultType0
    | GetPlaylistsResponseDefaultType1
    | PlaylistsSchema
    | None
):
    """Get list of playlists


    Required roles:
     - can_read_playlists

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        status (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPlaylistsResponseDefaultType0 | GetPlaylistsResponseDefaultType1 | PlaylistsSchema
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        status=status,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    status: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> Response[
    Any
    | GetPlaylistsResponseDefaultType0
    | GetPlaylistsResponseDefaultType1
    | PlaylistsSchema
]:
    """Get list of playlists


    Required roles:
     - can_read_playlists

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        status (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetPlaylistsResponseDefaultType0 | GetPlaylistsResponseDefaultType1 | PlaylistsSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        status=status,
        ids=ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    status: str | Unset = UNSET,
    ids: str | Unset = UNSET,
) -> (
    Any
    | GetPlaylistsResponseDefaultType0
    | GetPlaylistsResponseDefaultType1
    | PlaylistsSchema
    | None
):
    """Get list of playlists


    Required roles:
     - can_read_playlists

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        status (str | Unset):
        ids (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetPlaylistsResponseDefaultType0 | GetPlaylistsResponseDefaultType1 | PlaylistsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            status=status,
            ids=ids,
        )
    ).parsed
