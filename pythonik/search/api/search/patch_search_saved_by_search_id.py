from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.patch_search_saved_by_search_id_response_default import (
    PatchSearchSavedBySearchIdResponseDefault,
)
from ...models.saved_search_schema import SavedSearchSchema
from ...models.search_documents_schema import SearchDocumentsSchema
from ...types import Response


def _get_kwargs(
    search_id: str,
    *,
    body: SavedSearchSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/search/saved/{search_id}/".format(
            search_id=quote(str(search_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PatchSearchSavedBySearchIdResponseDefault | SearchDocumentsSchema:
    if response.status_code == 200:
        response_200 = SearchDocumentsSchema.from_dict(response.json())

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

    response_default = PatchSearchSavedBySearchIdResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PatchSearchSavedBySearchIdResponseDefault | SearchDocumentsSchema]:
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
    body: SavedSearchSchema,
) -> Response[Any | PatchSearchSavedBySearchIdResponseDefault | SearchDocumentsSchema]:
    """Search and save this search


    Required roles:
     - can_write_saved_searches

    Args:
        search_id (str):
        body (SavedSearchSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchSearchSavedBySearchIdResponseDefault | SearchDocumentsSchema]
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
    body: SavedSearchSchema,
) -> Any | PatchSearchSavedBySearchIdResponseDefault | SearchDocumentsSchema | None:
    """Search and save this search


    Required roles:
     - can_write_saved_searches

    Args:
        search_id (str):
        body (SavedSearchSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchSearchSavedBySearchIdResponseDefault | SearchDocumentsSchema
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
    body: SavedSearchSchema,
) -> Response[Any | PatchSearchSavedBySearchIdResponseDefault | SearchDocumentsSchema]:
    """Search and save this search


    Required roles:
     - can_write_saved_searches

    Args:
        search_id (str):
        body (SavedSearchSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PatchSearchSavedBySearchIdResponseDefault | SearchDocumentsSchema]
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
    body: SavedSearchSchema,
) -> Any | PatchSearchSavedBySearchIdResponseDefault | SearchDocumentsSchema | None:
    """Search and save this search


    Required roles:
     - can_write_saved_searches

    Args:
        search_id (str):
        body (SavedSearchSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PatchSearchSavedBySearchIdResponseDefault | SearchDocumentsSchema
    """

    return (
        await asyncio_detailed(
            search_id=search_id,
            client=client,
            body=body,
        )
    ).parsed
