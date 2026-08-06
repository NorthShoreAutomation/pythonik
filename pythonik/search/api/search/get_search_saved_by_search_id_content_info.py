from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_search_saved_by_search_id_content_info_response_default import (
    GetSearchSavedBySearchIdContentInfoResponseDefault,
)
from ...models.search_content_info_schema import SearchContentInfoSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    search_id: str,
    *,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["format_name"] = format_name

    params["by_storage_id"] = by_storage_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/search/saved/{search_id}/content/info/".format(
            search_id=quote(str(search_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSearchSavedBySearchIdContentInfoResponseDefault | SearchContentInfoSchema:
    if response.status_code == 200:
        response_200 = SearchContentInfoSchema.from_dict(response.json())

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

    response_default = GetSearchSavedBySearchIdContentInfoResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetSearchSavedBySearchIdContentInfoResponseDefault | SearchContentInfoSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = UNSET,
) -> Response[
    Any | GetSearchSavedBySearchIdContentInfoResponseDefault | SearchContentInfoSchema
]:
    """Get aggregated information about saved search results

     <br/>The returned information includes count of assets and collections,<br/>total size of all assets
    (in bytes) and total duration of video and audio<br/>assets (in milliseconds).<br/>The returned
    information includes count of assets and collections,<br/>total size of all assets (in bytes) and
    total duration of video and audio<br/>assets (in milliseconds).
    Required roles:
     - can_read_saved_searches

    Args:
        search_id (str):
        format_name (str | Unset):
        by_storage_id (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchSavedBySearchIdContentInfoResponseDefault | SearchContentInfoSchema]
    """

    kwargs = _get_kwargs(
        search_id=search_id,
        format_name=format_name,
        by_storage_id=by_storage_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = UNSET,
) -> (
    Any
    | GetSearchSavedBySearchIdContentInfoResponseDefault
    | SearchContentInfoSchema
    | None
):
    """Get aggregated information about saved search results

     <br/>The returned information includes count of assets and collections,<br/>total size of all assets
    (in bytes) and total duration of video and audio<br/>assets (in milliseconds).<br/>The returned
    information includes count of assets and collections,<br/>total size of all assets (in bytes) and
    total duration of video and audio<br/>assets (in milliseconds).
    Required roles:
     - can_read_saved_searches

    Args:
        search_id (str):
        format_name (str | Unset):
        by_storage_id (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchSavedBySearchIdContentInfoResponseDefault | SearchContentInfoSchema
    """

    return sync_detailed(
        search_id=search_id,
        client=client,
        format_name=format_name,
        by_storage_id=by_storage_id,
    ).parsed


async def asyncio_detailed(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = UNSET,
) -> Response[
    Any | GetSearchSavedBySearchIdContentInfoResponseDefault | SearchContentInfoSchema
]:
    """Get aggregated information about saved search results

     <br/>The returned information includes count of assets and collections,<br/>total size of all assets
    (in bytes) and total duration of video and audio<br/>assets (in milliseconds).<br/>The returned
    information includes count of assets and collections,<br/>total size of all assets (in bytes) and
    total duration of video and audio<br/>assets (in milliseconds).
    Required roles:
     - can_read_saved_searches

    Args:
        search_id (str):
        format_name (str | Unset):
        by_storage_id (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchSavedBySearchIdContentInfoResponseDefault | SearchContentInfoSchema]
    """

    kwargs = _get_kwargs(
        search_id=search_id,
        format_name=format_name,
        by_storage_id=by_storage_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = UNSET,
) -> (
    Any
    | GetSearchSavedBySearchIdContentInfoResponseDefault
    | SearchContentInfoSchema
    | None
):
    """Get aggregated information about saved search results

     <br/>The returned information includes count of assets and collections,<br/>total size of all assets
    (in bytes) and total duration of video and audio<br/>assets (in milliseconds).<br/>The returned
    information includes count of assets and collections,<br/>total size of all assets (in bytes) and
    total duration of video and audio<br/>assets (in milliseconds).
    Required roles:
     - can_read_saved_searches

    Args:
        search_id (str):
        format_name (str | Unset):
        by_storage_id (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchSavedBySearchIdContentInfoResponseDefault | SearchContentInfoSchema
    """

    return (
        await asyncio_detailed(
            search_id=search_id,
            client=client,
            format_name=format_name,
            by_storage_id=by_storage_id,
        )
    ).parsed
