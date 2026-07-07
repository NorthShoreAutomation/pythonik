from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.collection_content_schema import CollectionContentSchema
from ...models.post_collections_by_collection_id_contents_response_default_type_0 import (
    PostCollectionsByCollectionIdContentsResponseDefaultType0,
)
from ...models.post_collections_by_collection_id_contents_response_default_type_1 import (
    PostCollectionsByCollectionIdContentsResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    collection_id: str,
    *,
    body: CollectionContentSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/collections/{collection_id}/contents/".format(
            collection_id=quote(str(collection_id), safe=""),
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
    | PostCollectionsByCollectionIdContentsResponseDefaultType0
    | PostCollectionsByCollectionIdContentsResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = cast(Any, None)
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

    def _parse_response_default(
        data: object,
    ) -> (
        PostCollectionsByCollectionIdContentsResponseDefaultType0
        | PostCollectionsByCollectionIdContentsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                PostCollectionsByCollectionIdContentsResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostCollectionsByCollectionIdContentsResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | PostCollectionsByCollectionIdContentsResponseDefaultType0
    | PostCollectionsByCollectionIdContentsResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionContentSchema,
) -> Response[
    Any
    | PostCollectionsByCollectionIdContentsResponseDefaultType0
    | PostCollectionsByCollectionIdContentsResponseDefaultType1
]:
    """Add an object to a collection


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        body (CollectionContentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostCollectionsByCollectionIdContentsResponseDefaultType0 | PostCollectionsByCollectionIdContentsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionContentSchema,
) -> (
    Any
    | PostCollectionsByCollectionIdContentsResponseDefaultType0
    | PostCollectionsByCollectionIdContentsResponseDefaultType1
    | None
):
    """Add an object to a collection


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        body (CollectionContentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostCollectionsByCollectionIdContentsResponseDefaultType0 | PostCollectionsByCollectionIdContentsResponseDefaultType1
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionContentSchema,
) -> Response[
    Any
    | PostCollectionsByCollectionIdContentsResponseDefaultType0
    | PostCollectionsByCollectionIdContentsResponseDefaultType1
]:
    """Add an object to a collection


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        body (CollectionContentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostCollectionsByCollectionIdContentsResponseDefaultType0 | PostCollectionsByCollectionIdContentsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionContentSchema,
) -> (
    Any
    | PostCollectionsByCollectionIdContentsResponseDefaultType0
    | PostCollectionsByCollectionIdContentsResponseDefaultType1
    | None
):
    """Add an object to a collection


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        body (CollectionContentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostCollectionsByCollectionIdContentsResponseDefaultType0 | PostCollectionsByCollectionIdContentsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            body=body,
        )
    ).parsed
