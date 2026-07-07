from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_search_saved_by_search_id_reindex_response_default_type_0 import (
    PostSearchSavedBySearchIdReindexResponseDefaultType0,
)
from ...models.post_search_saved_by_search_id_reindex_response_default_type_1 import (
    PostSearchSavedBySearchIdReindexResponseDefaultType1,
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
    | PostSearchSavedBySearchIdReindexResponseDefaultType0
    | PostSearchSavedBySearchIdReindexResponseDefaultType1
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
        PostSearchSavedBySearchIdReindexResponseDefaultType0
        | PostSearchSavedBySearchIdReindexResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostSearchSavedBySearchIdReindexResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostSearchSavedBySearchIdReindexResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostSearchSavedBySearchIdReindexResponseDefaultType0
    | PostSearchSavedBySearchIdReindexResponseDefaultType1
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
    | PostSearchSavedBySearchIdReindexResponseDefaultType0
    | PostSearchSavedBySearchIdReindexResponseDefaultType1
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
        Response[Any | PostSearchSavedBySearchIdReindexResponseDefaultType0 | PostSearchSavedBySearchIdReindexResponseDefaultType1]
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
    | PostSearchSavedBySearchIdReindexResponseDefaultType0
    | PostSearchSavedBySearchIdReindexResponseDefaultType1
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
        Any | PostSearchSavedBySearchIdReindexResponseDefaultType0 | PostSearchSavedBySearchIdReindexResponseDefaultType1
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
    | PostSearchSavedBySearchIdReindexResponseDefaultType0
    | PostSearchSavedBySearchIdReindexResponseDefaultType1
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
        Response[Any | PostSearchSavedBySearchIdReindexResponseDefaultType0 | PostSearchSavedBySearchIdReindexResponseDefaultType1]
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
    | PostSearchSavedBySearchIdReindexResponseDefaultType0
    | PostSearchSavedBySearchIdReindexResponseDefaultType1
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
        Any | PostSearchSavedBySearchIdReindexResponseDefaultType0 | PostSearchSavedBySearchIdReindexResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            search_id=search_id,
            client=client,
            body=body,
        )
    ).parsed
