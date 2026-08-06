from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_search_saved_by_search_id_response_default import (
    DeleteSearchSavedBySearchIdResponseDefault,
)
from ...types import Response


def _get_kwargs(
    search_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/search/saved/{search_id}/".format(
            search_id=quote(str(search_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | DeleteSearchSavedBySearchIdResponseDefault:
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

    response_default = DeleteSearchSavedBySearchIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | DeleteSearchSavedBySearchIdResponseDefault]:
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
) -> Response[Any | DeleteSearchSavedBySearchIdResponseDefault]:
    """Delete a saved search by its id


    Required roles:
     - can_delete_saved_searches

    Args:
        search_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSearchSavedBySearchIdResponseDefault]
    """

    kwargs = _get_kwargs(
        search_id=search_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteSearchSavedBySearchIdResponseDefault | None:
    """Delete a saved search by its id


    Required roles:
     - can_delete_saved_searches

    Args:
        search_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSearchSavedBySearchIdResponseDefault
    """

    return sync_detailed(
        search_id=search_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any | DeleteSearchSavedBySearchIdResponseDefault]:
    """Delete a saved search by its id


    Required roles:
     - can_delete_saved_searches

    Args:
        search_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteSearchSavedBySearchIdResponseDefault]
    """

    kwargs = _get_kwargs(
        search_id=search_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Any | DeleteSearchSavedBySearchIdResponseDefault | None:
    """Delete a saved search by its id


    Required roles:
     - can_delete_saved_searches

    Args:
        search_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteSearchSavedBySearchIdResponseDefault
    """

    return (
        await asyncio_detailed(
            search_id=search_id,
            client=client,
        )
    ).parsed
