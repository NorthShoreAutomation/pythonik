from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_search_saved_group_by_group_id_search_by_search_id_response_default import (
    DeleteSearchSavedGroupByGroupIdSearchBySearchIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    group_id: str,
    search_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/search/saved/group/{group_id}/search/{search_id}/".format(
            group_id=quote(str(group_id), safe=""),
            search_id=quote(str(search_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteSearchSavedGroupByGroupIdSearchBySearchIdResponseDefault:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

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

    response_default = (
        DeleteSearchSavedGroupByGroupIdSearchBySearchIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteSearchSavedGroupByGroupIdSearchBySearchIdResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteSearchSavedGroupByGroupIdSearchBySearchIdResponseDefault]:
    """Delete saved search from search group


    Required roles:
     - can_write_saved_searches

    Args:
        group_id (str):
        search_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSearchSavedGroupByGroupIdSearchBySearchIdResponseDefault]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        search_id=search_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteSearchSavedGroupByGroupIdSearchBySearchIdResponseDefault | None:
    """Delete saved search from search group


    Required roles:
     - can_write_saved_searches

    Args:
        group_id (str):
        search_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSearchSavedGroupByGroupIdSearchBySearchIdResponseDefault
    """

    return sync_detailed(
        group_id=group_id,
        search_id=search_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteSearchSavedGroupByGroupIdSearchBySearchIdResponseDefault]:
    """Delete saved search from search group


    Required roles:
     - can_write_saved_searches

    Args:
        group_id (str):
        search_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSearchSavedGroupByGroupIdSearchBySearchIdResponseDefault]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        search_id=search_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteSearchSavedGroupByGroupIdSearchBySearchIdResponseDefault | None:
    """Delete saved search from search group


    Required roles:
     - can_write_saved_searches

    Args:
        group_id (str):
        search_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSearchSavedGroupByGroupIdSearchBySearchIdResponseDefault
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            search_id=search_id,
            client=client,
        )
    ).parsed
