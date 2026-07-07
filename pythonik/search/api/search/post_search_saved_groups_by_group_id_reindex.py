from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_search_saved_groups_by_group_id_reindex_response_default_type_0 import (
    PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0,
)
from ...models.post_search_saved_groups_by_group_id_reindex_response_default_type_1 import (
    PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    group_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/search/saved/groups/{group_id}/reindex/".format(
            group_id=quote(str(group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0
    | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
        PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0
        | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0
    | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1
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
    Any
    | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0
    | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1
]:
    """Reindex a particular saved search group by id


    Required roles:
     - can_reindex_saved_searches

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0 | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1]
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
) -> (
    Any
    | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0
    | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1
    | None
):
    """Reindex a particular saved search group by id


    Required roles:
     - can_reindex_saved_searches

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0 | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1
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
    Any
    | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0
    | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1
]:
    """Reindex a particular saved search group by id


    Required roles:
     - can_reindex_saved_searches

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0 | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1]
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
) -> (
    Any
    | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0
    | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1
    | None
):
    """Reindex a particular saved search group by id


    Required roles:
     - can_reindex_saved_searches

    Args:
        group_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType0 | PostSearchSavedGroupsByGroupIdReindexResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
