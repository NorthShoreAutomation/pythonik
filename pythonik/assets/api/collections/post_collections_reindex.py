from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_collections_reindex_response_default_type_0 import (
    PostCollectionsReindexResponseDefaultType0,
)
from ...models.post_collections_reindex_response_default_type_1 import (
    PostCollectionsReindexResponseDefaultType1,
)
from ...models.reindex_all_collections_schema import ReindexAllCollectionsSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ReindexAllCollectionsSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/collections/reindex/",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | PostCollectionsReindexResponseDefaultType0
    | PostCollectionsReindexResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        PostCollectionsReindexResponseDefaultType0
        | PostCollectionsReindexResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostCollectionsReindexResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = PostCollectionsReindexResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostCollectionsReindexResponseDefaultType0
    | PostCollectionsReindexResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReindexAllCollectionsSchema | Unset = UNSET,
) -> Response[
    Any
    | PostCollectionsReindexResponseDefaultType0
    | PostCollectionsReindexResponseDefaultType1
]:
    """Trigger reindexing of all collections


    Required roles:
     - can_reindex_collections

    Args:
        body (ReindexAllCollectionsSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostCollectionsReindexResponseDefaultType0 | PostCollectionsReindexResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ReindexAllCollectionsSchema | Unset = UNSET,
) -> (
    Any
    | PostCollectionsReindexResponseDefaultType0
    | PostCollectionsReindexResponseDefaultType1
    | None
):
    """Trigger reindexing of all collections


    Required roles:
     - can_reindex_collections

    Args:
        body (ReindexAllCollectionsSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostCollectionsReindexResponseDefaultType0 | PostCollectionsReindexResponseDefaultType1
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReindexAllCollectionsSchema | Unset = UNSET,
) -> Response[
    Any
    | PostCollectionsReindexResponseDefaultType0
    | PostCollectionsReindexResponseDefaultType1
]:
    """Trigger reindexing of all collections


    Required roles:
     - can_reindex_collections

    Args:
        body (ReindexAllCollectionsSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostCollectionsReindexResponseDefaultType0 | PostCollectionsReindexResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ReindexAllCollectionsSchema | Unset = UNSET,
) -> (
    Any
    | PostCollectionsReindexResponseDefaultType0
    | PostCollectionsReindexResponseDefaultType1
    | None
):
    """Trigger reindexing of all collections


    Required roles:
     - can_reindex_collections

    Args:
        body (ReindexAllCollectionsSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostCollectionsReindexResponseDefaultType0 | PostCollectionsReindexResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
