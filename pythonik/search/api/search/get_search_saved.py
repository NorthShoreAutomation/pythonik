from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_search_saved_response_default_type_0 import (
    GetSearchSavedResponseDefaultType0,
)
from ...models.get_search_saved_response_default_type_1 import (
    GetSearchSavedResponseDefaultType1,
)
from ...models.saved_searches_schema import SavedSearchesSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    favorites: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["scroll"] = scroll

    params["scroll_id"] = scroll_id

    params["sort"] = sort

    params["group_id"] = group_id

    params["ids"] = ids

    params["query"] = query

    params["favorites"] = favorites

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/search/saved/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSearchSavedResponseDefaultType0
    | GetSearchSavedResponseDefaultType1
    | SavedSearchesSchema
):
    if response.status_code == 200:
        response_200 = SavedSearchesSchema.from_dict(response.json())

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
    ) -> GetSearchSavedResponseDefaultType0 | GetSearchSavedResponseDefaultType1:
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = GetSearchSavedResponseDefaultType0.from_dict(data)

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetSearchSavedResponseDefaultType1.from_dict(data)

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSearchSavedResponseDefaultType0
    | GetSearchSavedResponseDefaultType1
    | SavedSearchesSchema
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
    group_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    favorites: bool | Unset = UNSET,
) -> Response[
    Any
    | GetSearchSavedResponseDefaultType0
    | GetSearchSavedResponseDefaultType1
    | SavedSearchesSchema
]:
    """Returns list of saved searches


    Required roles:
     - can_read_saved_searches

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        group_id (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        favorites (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchSavedResponseDefaultType0 | GetSearchSavedResponseDefaultType1 | SavedSearchesSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        group_id=group_id,
        ids=ids,
        query=query,
        favorites=favorites,
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
    group_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    favorites: bool | Unset = UNSET,
) -> (
    Any
    | GetSearchSavedResponseDefaultType0
    | GetSearchSavedResponseDefaultType1
    | SavedSearchesSchema
    | None
):
    """Returns list of saved searches


    Required roles:
     - can_read_saved_searches

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        group_id (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        favorites (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchSavedResponseDefaultType0 | GetSearchSavedResponseDefaultType1 | SavedSearchesSchema
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        group_id=group_id,
        ids=ids,
        query=query,
        favorites=favorites,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    scroll: bool | Unset = UNSET,
    scroll_id: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    group_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    favorites: bool | Unset = UNSET,
) -> Response[
    Any
    | GetSearchSavedResponseDefaultType0
    | GetSearchSavedResponseDefaultType1
    | SavedSearchesSchema
]:
    """Returns list of saved searches


    Required roles:
     - can_read_saved_searches

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        group_id (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        favorites (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchSavedResponseDefaultType0 | GetSearchSavedResponseDefaultType1 | SavedSearchesSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        scroll=scroll,
        scroll_id=scroll_id,
        sort=sort,
        group_id=group_id,
        ids=ids,
        query=query,
        favorites=favorites,
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
    group_id: str | Unset = UNSET,
    ids: str | Unset = UNSET,
    query: str | Unset = UNSET,
    favorites: bool | Unset = UNSET,
) -> (
    Any
    | GetSearchSavedResponseDefaultType0
    | GetSearchSavedResponseDefaultType1
    | SavedSearchesSchema
    | None
):
    """Returns list of saved searches


    Required roles:
     - can_read_saved_searches

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        scroll (bool | Unset):
        scroll_id (str | Unset):
        sort (str | Unset):
        group_id (str | Unset):
        ids (str | Unset):
        query (str | Unset):
        favorites (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchSavedResponseDefaultType0 | GetSearchSavedResponseDefaultType1 | SavedSearchesSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            scroll=scroll,
            scroll_id=scroll_id,
            sort=sort,
            group_id=group_id,
            ids=ids,
            query=query,
            favorites=favorites,
        )
    ).parsed
