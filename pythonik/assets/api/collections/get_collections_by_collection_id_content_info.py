from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.collection_content_info_schema import CollectionContentInfoSchema
from ...models.get_collections_by_collection_id_content_info_response_default_type_0 import (
    GetCollectionsByCollectionIdContentInfoResponseDefaultType0,
)
from ...models.get_collections_by_collection_id_content_info_response_default_type_1 import (
    GetCollectionsByCollectionIdContentInfoResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    *,
    only_active: bool | Unset = True,
    include_subcollections: bool | Unset = True,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = True,
    types: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["only_active"] = only_active

    params["include_subcollections"] = include_subcollections

    params["format_name"] = format_name

    params["by_storage_id"] = by_storage_id

    params["types"] = types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections/{collection_id}/content/info/".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | CollectionContentInfoSchema
    | GetCollectionsByCollectionIdContentInfoResponseDefaultType0
    | GetCollectionsByCollectionIdContentInfoResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = CollectionContentInfoSchema.from_dict(response.json())

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
        GetCollectionsByCollectionIdContentInfoResponseDefaultType0
        | GetCollectionsByCollectionIdContentInfoResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetCollectionsByCollectionIdContentInfoResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetCollectionsByCollectionIdContentInfoResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | CollectionContentInfoSchema
    | GetCollectionsByCollectionIdContentInfoResponseDefaultType0
    | GetCollectionsByCollectionIdContentInfoResponseDefaultType1
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
    only_active: bool | Unset = True,
    include_subcollections: bool | Unset = True,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = True,
    types: bool | Unset = UNSET,
) -> Response[
    Any
    | CollectionContentInfoSchema
    | GetCollectionsByCollectionIdContentInfoResponseDefaultType0
    | GetCollectionsByCollectionIdContentInfoResponseDefaultType1
]:
    """Get aggregated information about collection

     <br/>The returned information includes count of assets and sub-collections,<br/>total size of all
    assets (in bytes) and total duration of video and audio<br/>assets (in milliseconds).<br/>The
    returned information includes count of assets and sub-collections,<br/>total size of all assets (in
    bytes) and total duration of video and audio<br/>assets (in milliseconds).
    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        only_active (bool | Unset):  Default: True.
        include_subcollections (bool | Unset):  Default: True.
        format_name (str | Unset):
        by_storage_id (bool | Unset):  Default: True.
        types (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionContentInfoSchema | GetCollectionsByCollectionIdContentInfoResponseDefaultType0 | GetCollectionsByCollectionIdContentInfoResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        only_active=only_active,
        include_subcollections=include_subcollections,
        format_name=format_name,
        by_storage_id=by_storage_id,
        types=types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    only_active: bool | Unset = True,
    include_subcollections: bool | Unset = True,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = True,
    types: bool | Unset = UNSET,
) -> (
    Any
    | CollectionContentInfoSchema
    | GetCollectionsByCollectionIdContentInfoResponseDefaultType0
    | GetCollectionsByCollectionIdContentInfoResponseDefaultType1
    | None
):
    """Get aggregated information about collection

     <br/>The returned information includes count of assets and sub-collections,<br/>total size of all
    assets (in bytes) and total duration of video and audio<br/>assets (in milliseconds).<br/>The
    returned information includes count of assets and sub-collections,<br/>total size of all assets (in
    bytes) and total duration of video and audio<br/>assets (in milliseconds).
    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        only_active (bool | Unset):  Default: True.
        include_subcollections (bool | Unset):  Default: True.
        format_name (str | Unset):
        by_storage_id (bool | Unset):  Default: True.
        types (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionContentInfoSchema | GetCollectionsByCollectionIdContentInfoResponseDefaultType0 | GetCollectionsByCollectionIdContentInfoResponseDefaultType1
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        only_active=only_active,
        include_subcollections=include_subcollections,
        format_name=format_name,
        by_storage_id=by_storage_id,
        types=types,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    only_active: bool | Unset = True,
    include_subcollections: bool | Unset = True,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = True,
    types: bool | Unset = UNSET,
) -> Response[
    Any
    | CollectionContentInfoSchema
    | GetCollectionsByCollectionIdContentInfoResponseDefaultType0
    | GetCollectionsByCollectionIdContentInfoResponseDefaultType1
]:
    """Get aggregated information about collection

     <br/>The returned information includes count of assets and sub-collections,<br/>total size of all
    assets (in bytes) and total duration of video and audio<br/>assets (in milliseconds).<br/>The
    returned information includes count of assets and sub-collections,<br/>total size of all assets (in
    bytes) and total duration of video and audio<br/>assets (in milliseconds).
    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        only_active (bool | Unset):  Default: True.
        include_subcollections (bool | Unset):  Default: True.
        format_name (str | Unset):
        by_storage_id (bool | Unset):  Default: True.
        types (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionContentInfoSchema | GetCollectionsByCollectionIdContentInfoResponseDefaultType0 | GetCollectionsByCollectionIdContentInfoResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        only_active=only_active,
        include_subcollections=include_subcollections,
        format_name=format_name,
        by_storage_id=by_storage_id,
        types=types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    only_active: bool | Unset = True,
    include_subcollections: bool | Unset = True,
    format_name: str | Unset = UNSET,
    by_storage_id: bool | Unset = True,
    types: bool | Unset = UNSET,
) -> (
    Any
    | CollectionContentInfoSchema
    | GetCollectionsByCollectionIdContentInfoResponseDefaultType0
    | GetCollectionsByCollectionIdContentInfoResponseDefaultType1
    | None
):
    """Get aggregated information about collection

     <br/>The returned information includes count of assets and sub-collections,<br/>total size of all
    assets (in bytes) and total duration of video and audio<br/>assets (in milliseconds).<br/>The
    returned information includes count of assets and sub-collections,<br/>total size of all assets (in
    bytes) and total duration of video and audio<br/>assets (in milliseconds).
    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        only_active (bool | Unset):  Default: True.
        include_subcollections (bool | Unset):  Default: True.
        format_name (str | Unset):
        by_storage_id (bool | Unset):  Default: True.
        types (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionContentInfoSchema | GetCollectionsByCollectionIdContentInfoResponseDefaultType0 | GetCollectionsByCollectionIdContentInfoResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            only_active=only_active,
            include_subcollections=include_subcollections,
            format_name=format_name,
            by_storage_id=by_storage_id,
            types=types,
        )
    ).parsed
