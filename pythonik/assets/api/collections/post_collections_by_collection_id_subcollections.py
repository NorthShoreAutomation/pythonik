from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.collection_content_schema import CollectionContentSchema
from ...models.collection_schema import CollectionSchema
from ...models.post_collections_by_collection_id_subcollections_response_default_type_0 import (
    PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0,
)
from ...models.post_collections_by_collection_id_subcollections_response_default_type_1 import (
    PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    *,
    body: CollectionContentSchema,
    copy_acl: str | Unset = UNSET,
    copy_keyframes: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["copy_acl"] = copy_acl

    params["copy_keyframes"] = copy_keyframes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/collections/{collection_id}/subcollections/".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | CollectionSchema
    | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0
    | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1
):
    if response.status_code == 201:
        response_201 = CollectionSchema.from_dict(response.json())

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
        PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0
        | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1.from_dict(
                data
            )
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | CollectionSchema
    | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0
    | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1
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
    copy_acl: str | Unset = UNSET,
    copy_keyframes: str | Unset = UNSET,
) -> Response[
    Any
    | CollectionSchema
    | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0
    | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1
]:
    """Copy a collection (recursively) in to another collection


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        copy_acl (str | Unset):
        copy_keyframes (str | Unset):
        body (CollectionContentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionSchema | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0 | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
        copy_acl=copy_acl,
        copy_keyframes=copy_keyframes,
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
    copy_acl: str | Unset = UNSET,
    copy_keyframes: str | Unset = UNSET,
) -> (
    Any
    | CollectionSchema
    | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0
    | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1
    | None
):
    """Copy a collection (recursively) in to another collection


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        copy_acl (str | Unset):
        copy_keyframes (str | Unset):
        body (CollectionContentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionSchema | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0 | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        body=body,
        copy_acl=copy_acl,
        copy_keyframes=copy_keyframes,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionContentSchema,
    copy_acl: str | Unset = UNSET,
    copy_keyframes: str | Unset = UNSET,
) -> Response[
    Any
    | CollectionSchema
    | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0
    | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1
]:
    """Copy a collection (recursively) in to another collection


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        copy_acl (str | Unset):
        copy_keyframes (str | Unset):
        body (CollectionContentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionSchema | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0 | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
        copy_acl=copy_acl,
        copy_keyframes=copy_keyframes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CollectionContentSchema,
    copy_acl: str | Unset = UNSET,
    copy_keyframes: str | Unset = UNSET,
) -> (
    Any
    | CollectionSchema
    | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0
    | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1
    | None
):
    """Copy a collection (recursively) in to another collection


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        copy_acl (str | Unset):
        copy_keyframes (str | Unset):
        body (CollectionContentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionSchema | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType0 | PostCollectionsByCollectionIdSubcollectionsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            body=body,
            copy_acl=copy_acl,
            copy_keyframes=copy_keyframes,
        )
    ).parsed
