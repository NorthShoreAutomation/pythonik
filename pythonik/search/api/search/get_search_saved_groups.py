from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_search_saved_groups_response_default_type_0 import (
    GetSearchSavedGroupsResponseDefaultType0,
)
from ...models.get_search_saved_groups_response_default_type_1 import (
    GetSearchSavedGroupsResponseDefaultType1,
)
from ...models.saved_search_groups_schema import SavedSearchGroupsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["ids"] = ids

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/search/saved/groups/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSearchSavedGroupsResponseDefaultType0
    | GetSearchSavedGroupsResponseDefaultType1
    | SavedSearchGroupsSchema
):
    if response.status_code == 200:
        response_200 = SavedSearchGroupsSchema.from_dict(response.json())

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
        GetSearchSavedGroupsResponseDefaultType0
        | GetSearchSavedGroupsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetSearchSavedGroupsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = GetSearchSavedGroupsResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSearchSavedGroupsResponseDefaultType0
    | GetSearchSavedGroupsResponseDefaultType1
    | SavedSearchGroupsSchema
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
    ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[
    Any
    | GetSearchSavedGroupsResponseDefaultType0
    | GetSearchSavedGroupsResponseDefaultType1
    | SavedSearchGroupsSchema
]:
    """Returns paginated list of search groups


    Required roles:
     - can_read_saved_searches

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        ids (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchSavedGroupsResponseDefaultType0 | GetSearchSavedGroupsResponseDefaultType1 | SavedSearchGroupsSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        ids=ids,
        sort=sort,
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
    ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> (
    Any
    | GetSearchSavedGroupsResponseDefaultType0
    | GetSearchSavedGroupsResponseDefaultType1
    | SavedSearchGroupsSchema
    | None
):
    """Returns paginated list of search groups


    Required roles:
     - can_read_saved_searches

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        ids (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchSavedGroupsResponseDefaultType0 | GetSearchSavedGroupsResponseDefaultType1 | SavedSearchGroupsSchema
    """

    return sync_detailed(
        client=client,
        per_page=per_page,
        page=page,
        ids=ids,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> Response[
    Any
    | GetSearchSavedGroupsResponseDefaultType0
    | GetSearchSavedGroupsResponseDefaultType1
    | SavedSearchGroupsSchema
]:
    """Returns paginated list of search groups


    Required roles:
     - can_read_saved_searches

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        ids (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchSavedGroupsResponseDefaultType0 | GetSearchSavedGroupsResponseDefaultType1 | SavedSearchGroupsSchema]
    """

    kwargs = _get_kwargs(
        per_page=per_page,
        page=page,
        ids=ids,
        sort=sort,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    ids: str | Unset = UNSET,
    sort: str | Unset = UNSET,
) -> (
    Any
    | GetSearchSavedGroupsResponseDefaultType0
    | GetSearchSavedGroupsResponseDefaultType1
    | SavedSearchGroupsSchema
    | None
):
    """Returns paginated list of search groups


    Required roles:
     - can_read_saved_searches

    Args:
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        ids (str | Unset):
        sort (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchSavedGroupsResponseDefaultType0 | GetSearchSavedGroupsResponseDefaultType1 | SavedSearchGroupsSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            per_page=per_page,
            page=page,
            ids=ids,
            sort=sort,
        )
    ).parsed
