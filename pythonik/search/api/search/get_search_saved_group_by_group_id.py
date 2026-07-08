from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_search_saved_group_by_group_id_response_default import (
    GetSearchSavedGroupByGroupIdResponseDefault,
)
from ...models.saved_search_group_schema import SavedSearchGroupSchema
from ...types import Response


def _get_kwargs(
    group_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/search/saved/group/{group_id}/".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetSearchSavedGroupByGroupIdResponseDefault | SavedSearchGroupSchema:
    if response.status_code == 200:
        response_200 = SavedSearchGroupSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = GetSearchSavedGroupByGroupIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | GetSearchSavedGroupByGroupIdResponseDefault | SavedSearchGroupSchema
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetSearchSavedGroupByGroupIdResponseDefault | SavedSearchGroupSchema
]:
    """Returns saved search group data


    Required roles:
     - can_read_saved_searches

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchSavedGroupByGroupIdResponseDefault | SavedSearchGroupSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSearchSavedGroupByGroupIdResponseDefault | SavedSearchGroupSchema | None:
    """Returns saved search group data


    Required roles:
     - can_read_saved_searches

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchSavedGroupByGroupIdResponseDefault | SavedSearchGroupSchema
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any | GetSearchSavedGroupByGroupIdResponseDefault | SavedSearchGroupSchema
]:
    """Returns saved search group data


    Required roles:
     - can_read_saved_searches

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetSearchSavedGroupByGroupIdResponseDefault | SavedSearchGroupSchema]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | GetSearchSavedGroupByGroupIdResponseDefault | SavedSearchGroupSchema | None:
    """Returns saved search group data


    Required roles:
     - can_read_saved_searches

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetSearchSavedGroupByGroupIdResponseDefault | SavedSearchGroupSchema
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
