from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_search_saved_groups_by_group_id_reindex_body import (
    PostSearchSavedGroupsByGroupIdReindexBody,
)
from ...models.post_search_saved_groups_by_group_id_reindex_response_201 import (
    PostSearchSavedGroupsByGroupIdReindexResponse201,
)
from ...models.post_search_saved_groups_by_group_id_reindex_response_default import (
    PostSearchSavedGroupsByGroupIdReindexResponseDefault,
)
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    body: PostSearchSavedGroupsByGroupIdReindexBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/search/saved/groups/{group_id}/reindex/".format(
            group_id=quote(str(group_id), safe=""),
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
    | PostSearchSavedGroupsByGroupIdReindexResponse201
    | PostSearchSavedGroupsByGroupIdReindexResponseDefault
):
    if response.status_code == 201:
        response_201 = PostSearchSavedGroupsByGroupIdReindexResponse201.from_dict(
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

    response_default = PostSearchSavedGroupsByGroupIdReindexResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSearchSavedGroupsByGroupIdReindexResponse201
    | PostSearchSavedGroupsByGroupIdReindexResponseDefault
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
    body: PostSearchSavedGroupsByGroupIdReindexBody,
) -> Response[
    Any
    | PostSearchSavedGroupsByGroupIdReindexResponse201
    | PostSearchSavedGroupsByGroupIdReindexResponseDefault
]:
    """Reindex a particular saved search group by id


    Required roles:
     - can_reindex_saved_searches

    Args:
        group_id (str):
        body (PostSearchSavedGroupsByGroupIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchSavedGroupsByGroupIdReindexResponse201 | PostSearchSavedGroupsByGroupIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSearchSavedGroupsByGroupIdReindexBody,
) -> (
    Any
    | PostSearchSavedGroupsByGroupIdReindexResponse201
    | PostSearchSavedGroupsByGroupIdReindexResponseDefault
    | None
):
    """Reindex a particular saved search group by id


    Required roles:
     - can_reindex_saved_searches

    Args:
        group_id (str):
        body (PostSearchSavedGroupsByGroupIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchSavedGroupsByGroupIdReindexResponse201 | PostSearchSavedGroupsByGroupIdReindexResponseDefault
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSearchSavedGroupsByGroupIdReindexBody,
) -> Response[
    Any
    | PostSearchSavedGroupsByGroupIdReindexResponse201
    | PostSearchSavedGroupsByGroupIdReindexResponseDefault
]:
    """Reindex a particular saved search group by id


    Required roles:
     - can_reindex_saved_searches

    Args:
        group_id (str):
        body (PostSearchSavedGroupsByGroupIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchSavedGroupsByGroupIdReindexResponse201 | PostSearchSavedGroupsByGroupIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: PostSearchSavedGroupsByGroupIdReindexBody,
) -> (
    Any
    | PostSearchSavedGroupsByGroupIdReindexResponse201
    | PostSearchSavedGroupsByGroupIdReindexResponseDefault
    | None
):
    """Reindex a particular saved search group by id


    Required roles:
     - can_reindex_saved_searches

    Args:
        group_id (str):
        body (PostSearchSavedGroupsByGroupIdReindexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchSavedGroupsByGroupIdReindexResponse201 | PostSearchSavedGroupsByGroupIdReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
        )
    ).parsed
