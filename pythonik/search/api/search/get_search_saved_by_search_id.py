from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_search_saved_by_search_id_response_default_type_0 import (
    GetSearchSavedBySearchIdResponseDefaultType0,
)
from ...models.get_search_saved_by_search_id_response_default_type_1 import (
    GetSearchSavedBySearchIdResponseDefaultType1,
)
from ...models.get_search_saved_by_search_id_search_after_type_0 import (
    GetSearchSavedBySearchIdSearchAfterType0,
)
from ...models.saved_search_results_schema import SavedSearchResultsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    search_id: str,
    *,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    include_results: bool | Unset = True,
    generate_signed_download_url: bool | Unset = False,
    generate_signed_proxy_url: bool | Unset = False,
    scroll: bool | Unset = False,
    scroll_id: None | str | Unset = UNSET,
    search_after: GetSearchSavedBySearchIdSearchAfterType0 | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["page"] = page

    params["include_results"] = include_results

    params["generate_signed_download_url"] = generate_signed_download_url

    params["generate_signed_proxy_url"] = generate_signed_proxy_url

    params["scroll"] = scroll

    json_scroll_id: None | str | Unset
    if isinstance(scroll_id, Unset):
        json_scroll_id = UNSET
    else:
        json_scroll_id = scroll_id
    params["scroll_id"] = json_scroll_id

    json_search_after: dict[str, Any] | None | Unset
    if isinstance(search_after, Unset):
        json_search_after = UNSET
    elif isinstance(search_after, GetSearchSavedBySearchIdSearchAfterType0):
        json_search_after = search_after.to_dict()
    else:
        json_search_after = search_after
    params["search_after"] = json_search_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/search/saved/{search_id}/".format(
            search_id=quote(str(search_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetSearchSavedBySearchIdResponseDefaultType0
    | GetSearchSavedBySearchIdResponseDefaultType1
    | SavedSearchResultsSchema
):
    if response.status_code == 200:
        response_200 = SavedSearchResultsSchema.from_dict(response.json())

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
        GetSearchSavedBySearchIdResponseDefaultType0
        | GetSearchSavedBySearchIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetSearchSavedBySearchIdResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetSearchSavedBySearchIdResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetSearchSavedBySearchIdResponseDefaultType0
    | GetSearchSavedBySearchIdResponseDefaultType1
    | SavedSearchResultsSchema
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
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    include_results: bool | Unset = True,
    generate_signed_download_url: bool | Unset = False,
    generate_signed_proxy_url: bool | Unset = False,
    scroll: bool | Unset = False,
    scroll_id: None | str | Unset = UNSET,
    search_after: GetSearchSavedBySearchIdSearchAfterType0 | None | Unset = UNSET,
) -> Response[
    Any
    | GetSearchSavedBySearchIdResponseDefaultType0
    | GetSearchSavedBySearchIdResponseDefaultType1
    | SavedSearchResultsSchema
]:
    """Returns results of saved search


    Required roles:
     - can_read_saved_searches

    Args:
        search_id (str):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        include_results (bool | Unset):  Default: True.
        generate_signed_download_url (bool | Unset):  Default: False.
        generate_signed_proxy_url (bool | Unset):  Default: False.
        scroll (bool | Unset):  Default: False.
        scroll_id (None | str | Unset):
        search_after (GetSearchSavedBySearchIdSearchAfterType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchSavedBySearchIdResponseDefaultType0 | GetSearchSavedBySearchIdResponseDefaultType1 | SavedSearchResultsSchema]
    """

    kwargs = _get_kwargs(
        search_id=search_id,
        per_page=per_page,
        page=page,
        include_results=include_results,
        generate_signed_download_url=generate_signed_download_url,
        generate_signed_proxy_url=generate_signed_proxy_url,
        scroll=scroll,
        scroll_id=scroll_id,
        search_after=search_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    include_results: bool | Unset = True,
    generate_signed_download_url: bool | Unset = False,
    generate_signed_proxy_url: bool | Unset = False,
    scroll: bool | Unset = False,
    scroll_id: None | str | Unset = UNSET,
    search_after: GetSearchSavedBySearchIdSearchAfterType0 | None | Unset = UNSET,
) -> (
    Any
    | GetSearchSavedBySearchIdResponseDefaultType0
    | GetSearchSavedBySearchIdResponseDefaultType1
    | SavedSearchResultsSchema
    | None
):
    """Returns results of saved search


    Required roles:
     - can_read_saved_searches

    Args:
        search_id (str):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        include_results (bool | Unset):  Default: True.
        generate_signed_download_url (bool | Unset):  Default: False.
        generate_signed_proxy_url (bool | Unset):  Default: False.
        scroll (bool | Unset):  Default: False.
        scroll_id (None | str | Unset):
        search_after (GetSearchSavedBySearchIdSearchAfterType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchSavedBySearchIdResponseDefaultType0 | GetSearchSavedBySearchIdResponseDefaultType1 | SavedSearchResultsSchema
    """

    return sync_detailed(
        search_id=search_id,
        client=client,
        per_page=per_page,
        page=page,
        include_results=include_results,
        generate_signed_download_url=generate_signed_download_url,
        generate_signed_proxy_url=generate_signed_proxy_url,
        scroll=scroll,
        scroll_id=scroll_id,
        search_after=search_after,
    ).parsed


async def asyncio_detailed(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    include_results: bool | Unset = True,
    generate_signed_download_url: bool | Unset = False,
    generate_signed_proxy_url: bool | Unset = False,
    scroll: bool | Unset = False,
    scroll_id: None | str | Unset = UNSET,
    search_after: GetSearchSavedBySearchIdSearchAfterType0 | None | Unset = UNSET,
) -> Response[
    Any
    | GetSearchSavedBySearchIdResponseDefaultType0
    | GetSearchSavedBySearchIdResponseDefaultType1
    | SavedSearchResultsSchema
]:
    """Returns results of saved search


    Required roles:
     - can_read_saved_searches

    Args:
        search_id (str):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        include_results (bool | Unset):  Default: True.
        generate_signed_download_url (bool | Unset):  Default: False.
        generate_signed_proxy_url (bool | Unset):  Default: False.
        scroll (bool | Unset):  Default: False.
        scroll_id (None | str | Unset):
        search_after (GetSearchSavedBySearchIdSearchAfterType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchSavedBySearchIdResponseDefaultType0 | GetSearchSavedBySearchIdResponseDefaultType1 | SavedSearchResultsSchema]
    """

    kwargs = _get_kwargs(
        search_id=search_id,
        per_page=per_page,
        page=page,
        include_results=include_results,
        generate_signed_download_url=generate_signed_download_url,
        generate_signed_proxy_url=generate_signed_proxy_url,
        scroll=scroll,
        scroll_id=scroll_id,
        search_after=search_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    include_results: bool | Unset = True,
    generate_signed_download_url: bool | Unset = False,
    generate_signed_proxy_url: bool | Unset = False,
    scroll: bool | Unset = False,
    scroll_id: None | str | Unset = UNSET,
    search_after: GetSearchSavedBySearchIdSearchAfterType0 | None | Unset = UNSET,
) -> (
    Any
    | GetSearchSavedBySearchIdResponseDefaultType0
    | GetSearchSavedBySearchIdResponseDefaultType1
    | SavedSearchResultsSchema
    | None
):
    """Returns results of saved search


    Required roles:
     - can_read_saved_searches

    Args:
        search_id (str):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        include_results (bool | Unset):  Default: True.
        generate_signed_download_url (bool | Unset):  Default: False.
        generate_signed_proxy_url (bool | Unset):  Default: False.
        scroll (bool | Unset):  Default: False.
        scroll_id (None | str | Unset):
        search_after (GetSearchSavedBySearchIdSearchAfterType0 | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchSavedBySearchIdResponseDefaultType0 | GetSearchSavedBySearchIdResponseDefaultType1 | SavedSearchResultsSchema
    """

    return (
        await asyncio_detailed(
            search_id=search_id,
            client=client,
            per_page=per_page,
            page=page,
            include_results=include_results,
            generate_signed_download_url=generate_signed_download_url,
            generate_signed_proxy_url=generate_signed_proxy_url,
            scroll=scroll,
            scroll_id=scroll_id,
            search_after=search_after,
        )
    ).parsed
