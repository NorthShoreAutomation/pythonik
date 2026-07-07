from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.assets_schema import AssetsSchema
from ...models.get_collections_by_collection_id_contents_response_default_type_0 import (
    GetCollectionsByCollectionIdContentsResponseDefaultType0,
)
from ...models.get_collections_by_collection_id_contents_response_default_type_1 import (
    GetCollectionsByCollectionIdContentsResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    *,
    object_types: str | Unset = UNSET,
    object_ids: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    include_keyframes: bool | Unset = True,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["object_types"] = object_types

    params["object_ids"] = object_ids

    params["external_id"] = external_id

    params["per_page"] = per_page

    params["page"] = page

    params["sort"] = sort

    params["filter"] = filter_

    params["include_keyframes"] = include_keyframes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections/{collection_id}/contents/".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | AssetsSchema
    | GetCollectionsByCollectionIdContentsResponseDefaultType0
    | GetCollectionsByCollectionIdContentsResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = AssetsSchema.from_dict(response.json())

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
        GetCollectionsByCollectionIdContentsResponseDefaultType0
        | GetCollectionsByCollectionIdContentsResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetCollectionsByCollectionIdContentsResponseDefaultType0.from_dict(data)
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetCollectionsByCollectionIdContentsResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | AssetsSchema
    | GetCollectionsByCollectionIdContentsResponseDefaultType0
    | GetCollectionsByCollectionIdContentsResponseDefaultType1
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
    object_types: str | Unset = UNSET,
    object_ids: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    include_keyframes: bool | Unset = True,
) -> Response[
    Any
    | AssetsSchema
    | GetCollectionsByCollectionIdContentsResponseDefaultType0
    | GetCollectionsByCollectionIdContentsResponseDefaultType1
]:
    """Returns contents of a collection by id


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        object_types (str | Unset):
        object_ids (str | Unset):
        external_id (str | Unset):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        filter_ (str | Unset):
        include_keyframes (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetsSchema | GetCollectionsByCollectionIdContentsResponseDefaultType0 | GetCollectionsByCollectionIdContentsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        object_types=object_types,
        object_ids=object_ids,
        external_id=external_id,
        per_page=per_page,
        page=page,
        sort=sort,
        filter_=filter_,
        include_keyframes=include_keyframes,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    object_types: str | Unset = UNSET,
    object_ids: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    include_keyframes: bool | Unset = True,
) -> (
    Any
    | AssetsSchema
    | GetCollectionsByCollectionIdContentsResponseDefaultType0
    | GetCollectionsByCollectionIdContentsResponseDefaultType1
    | None
):
    """Returns contents of a collection by id


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        object_types (str | Unset):
        object_ids (str | Unset):
        external_id (str | Unset):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        filter_ (str | Unset):
        include_keyframes (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetsSchema | GetCollectionsByCollectionIdContentsResponseDefaultType0 | GetCollectionsByCollectionIdContentsResponseDefaultType1
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        object_types=object_types,
        object_ids=object_ids,
        external_id=external_id,
        per_page=per_page,
        page=page,
        sort=sort,
        filter_=filter_,
        include_keyframes=include_keyframes,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    object_types: str | Unset = UNSET,
    object_ids: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    include_keyframes: bool | Unset = True,
) -> Response[
    Any
    | AssetsSchema
    | GetCollectionsByCollectionIdContentsResponseDefaultType0
    | GetCollectionsByCollectionIdContentsResponseDefaultType1
]:
    """Returns contents of a collection by id


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        object_types (str | Unset):
        object_ids (str | Unset):
        external_id (str | Unset):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        filter_ (str | Unset):
        include_keyframes (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AssetsSchema | GetCollectionsByCollectionIdContentsResponseDefaultType0 | GetCollectionsByCollectionIdContentsResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        object_types=object_types,
        object_ids=object_ids,
        external_id=external_id,
        per_page=per_page,
        page=page,
        sort=sort,
        filter_=filter_,
        include_keyframes=include_keyframes,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    object_types: str | Unset = UNSET,
    object_ids: str | Unset = UNSET,
    external_id: str | Unset = UNSET,
    per_page: int | Unset = UNSET,
    page: int | Unset = 1,
    sort: str | Unset = UNSET,
    filter_: str | Unset = UNSET,
    include_keyframes: bool | Unset = True,
) -> (
    Any
    | AssetsSchema
    | GetCollectionsByCollectionIdContentsResponseDefaultType0
    | GetCollectionsByCollectionIdContentsResponseDefaultType1
    | None
):
    """Returns contents of a collection by id


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        object_types (str | Unset):
        object_ids (str | Unset):
        external_id (str | Unset):
        per_page (int | Unset):
        page (int | Unset):  Default: 1.
        sort (str | Unset):
        filter_ (str | Unset):
        include_keyframes (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AssetsSchema | GetCollectionsByCollectionIdContentsResponseDefaultType0 | GetCollectionsByCollectionIdContentsResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            object_types=object_types,
            object_ids=object_ids,
            external_id=external_id,
            per_page=per_page,
            page=page,
            sort=sort,
            filter_=filter_,
            include_keyframes=include_keyframes,
        )
    ).parsed
