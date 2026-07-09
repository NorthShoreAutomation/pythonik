from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_search_saved_by_search_id_reindex_response_201 import (
    PostSearchSavedBySearchIdReindexResponse201,
)
from ...models.post_search_saved_by_search_id_reindex_response_default import (
    PostSearchSavedBySearchIdReindexResponseDefault,
)
from ...models.reindex_saved_search_schema import ReindexSavedSearchSchema
from ...types import Response


def _get_kwargs(
    search_id: str,
    *,
    body: ReindexSavedSearchSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/search/saved/{search_id}/reindex/".format(
            search_id=quote(str(search_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostSearchSavedBySearchIdReindexResponse201
    | PostSearchSavedBySearchIdReindexResponseDefault
):
    if response.status_code == 201:
        response_201 = PostSearchSavedBySearchIdReindexResponse201.from_dict(
            response.json()
        )

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = PostSearchSavedBySearchIdReindexResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSearchSavedBySearchIdReindexResponse201
    | PostSearchSavedBySearchIdReindexResponseDefault
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
    body: ReindexSavedSearchSchema,
) -> Response[
    Any
    | PostSearchSavedBySearchIdReindexResponse201
    | PostSearchSavedBySearchIdReindexResponseDefault
]:
    """Reindex a particular saved search by id


    Required roles:
     - can_reindex_saved_searches

    Args:
        search_id (str):
        body (ReindexSavedSearchSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchSavedBySearchIdReindexResponse201 | PostSearchSavedBySearchIdReindexResponseDefault]
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
    body: ReindexSavedSearchSchema,
) -> (
    Any
    | PostSearchSavedBySearchIdReindexResponse201
    | PostSearchSavedBySearchIdReindexResponseDefault
    | None
):
    """Reindex a particular saved search by id


    Required roles:
     - can_reindex_saved_searches

    Args:
        search_id (str):
        body (ReindexSavedSearchSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchSavedBySearchIdReindexResponse201 | PostSearchSavedBySearchIdReindexResponseDefault
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
    body: ReindexSavedSearchSchema,
) -> Response[
    Any
    | PostSearchSavedBySearchIdReindexResponse201
    | PostSearchSavedBySearchIdReindexResponseDefault
]:
    """Reindex a particular saved search by id


    Required roles:
     - can_reindex_saved_searches

    Args:
        search_id (str):
        body (ReindexSavedSearchSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchSavedBySearchIdReindexResponse201 | PostSearchSavedBySearchIdReindexResponseDefault]
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
    body: ReindexSavedSearchSchema,
) -> (
    Any
    | PostSearchSavedBySearchIdReindexResponse201
    | PostSearchSavedBySearchIdReindexResponseDefault
    | None
):
    """Reindex a particular saved search by id


    Required roles:
     - can_reindex_saved_searches

    Args:
        search_id (str):
        body (ReindexSavedSearchSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchSavedBySearchIdReindexResponse201 | PostSearchSavedBySearchIdReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            search_id=search_id,
            client=client,
            body=body,
        )
    ).parsed
