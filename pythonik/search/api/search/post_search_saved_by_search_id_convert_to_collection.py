from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_search_saved_by_search_id_convert_to_collection_response_default import (
    PostSearchSavedBySearchIdConvertToCollectionResponseDefault,
)
from ...models.saved_search_convert_collection_schema import (
    SavedSearchConvertCollectionSchema,
)
from ...types import Response


def _get_kwargs(
    search_id: str,
    *,
    body: SavedSearchConvertCollectionSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/search/saved/{search_id}/convert_to_collection/".format(
            search_id=quote(str(search_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostSearchSavedBySearchIdConvertToCollectionResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        PostSearchSavedBySearchIdConvertToCollectionResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostSearchSavedBySearchIdConvertToCollectionResponseDefault]:
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
    body: SavedSearchConvertCollectionSchema,
) -> Response[Any | PostSearchSavedBySearchIdConvertToCollectionResponseDefault]:
    """Converts the saved search to a collection


    Required roles:
     - can_read_saved_searches
    - can_create_collections
    - can_write_collections

    Args:
        search_id (str):
        body (SavedSearchConvertCollectionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchSavedBySearchIdConvertToCollectionResponseDefault]
    """

    kwargs = _get_kwargs(
        search_id=search_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SavedSearchConvertCollectionSchema,
) -> Any | PostSearchSavedBySearchIdConvertToCollectionResponseDefault | None:
    """Converts the saved search to a collection


    Required roles:
     - can_read_saved_searches
    - can_create_collections
    - can_write_collections

    Args:
        search_id (str):
        body (SavedSearchConvertCollectionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchSavedBySearchIdConvertToCollectionResponseDefault
    """

    return sync_detailed(
        search_id=search_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SavedSearchConvertCollectionSchema,
) -> Response[Any | PostSearchSavedBySearchIdConvertToCollectionResponseDefault]:
    """Converts the saved search to a collection


    Required roles:
     - can_read_saved_searches
    - can_create_collections
    - can_write_collections

    Args:
        search_id (str):
        body (SavedSearchConvertCollectionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchSavedBySearchIdConvertToCollectionResponseDefault]
    """

    kwargs = _get_kwargs(
        search_id=search_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    search_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SavedSearchConvertCollectionSchema,
) -> Any | PostSearchSavedBySearchIdConvertToCollectionResponseDefault | None:
    """Converts the saved search to a collection


    Required roles:
     - can_read_saved_searches
    - can_create_collections
    - can_write_collections

    Args:
        search_id (str):
        body (SavedSearchConvertCollectionSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchSavedBySearchIdConvertToCollectionResponseDefault
    """

    return (
        await asyncio_detailed(
            search_id=search_id,
            client=client,
            body=body,
        )
    ).parsed
