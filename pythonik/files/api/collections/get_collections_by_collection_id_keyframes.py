from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.collection_keyframes_schema import CollectionKeyframesSchema
from ...models.get_collections_by_collection_id_keyframes_response_default_type_0 import (
    GetCollectionsByCollectionIdKeyframesResponseDefaultType0,
)
from ...models.get_collections_by_collection_id_keyframes_response_default_type_1 import (
    GetCollectionsByCollectionIdKeyframesResponseDefaultType1,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_id: str,
    *,
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    last_id: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["per_page"] = per_page

    params["generate_signed_url"] = generate_signed_url

    params["last_id"] = last_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections/{collection_id}/keyframes/".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | CollectionKeyframesSchema
    | GetCollectionsByCollectionIdKeyframesResponseDefaultType0
    | GetCollectionsByCollectionIdKeyframesResponseDefaultType1
):
    if response.status_code == 200:
        response_200 = CollectionKeyframesSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    def _parse_response_default(
        data: object,
    ) -> (
        GetCollectionsByCollectionIdKeyframesResponseDefaultType0
        | GetCollectionsByCollectionIdKeyframesResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetCollectionsByCollectionIdKeyframesResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetCollectionsByCollectionIdKeyframesResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | CollectionKeyframesSchema
    | GetCollectionsByCollectionIdKeyframesResponseDefaultType0
    | GetCollectionsByCollectionIdKeyframesResponseDefaultType1
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
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | CollectionKeyframesSchema
    | GetCollectionsByCollectionIdKeyframesResponseDefaultType0
    | GetCollectionsByCollectionIdKeyframesResponseDefaultType1
]:
    """Get all collection's keyframes


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        per_page (int | Unset):  Default: 10.
        generate_signed_url (bool | Unset):  Default: True.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionKeyframesSchema | GetCollectionsByCollectionIdKeyframesResponseDefaultType0 | GetCollectionsByCollectionIdKeyframesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        per_page=per_page,
        generate_signed_url=generate_signed_url,
        last_id=last_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | CollectionKeyframesSchema
    | GetCollectionsByCollectionIdKeyframesResponseDefaultType0
    | GetCollectionsByCollectionIdKeyframesResponseDefaultType1
    | None
):
    """Get all collection's keyframes


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        per_page (int | Unset):  Default: 10.
        generate_signed_url (bool | Unset):  Default: True.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionKeyframesSchema | GetCollectionsByCollectionIdKeyframesResponseDefaultType0 | GetCollectionsByCollectionIdKeyframesResponseDefaultType1
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        per_page=per_page,
        generate_signed_url=generate_signed_url,
        last_id=last_id,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    last_id: str | Unset = UNSET,
) -> Response[
    Any
    | CollectionKeyframesSchema
    | GetCollectionsByCollectionIdKeyframesResponseDefaultType0
    | GetCollectionsByCollectionIdKeyframesResponseDefaultType1
]:
    """Get all collection's keyframes


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        per_page (int | Unset):  Default: 10.
        generate_signed_url (bool | Unset):  Default: True.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CollectionKeyframesSchema | GetCollectionsByCollectionIdKeyframesResponseDefaultType0 | GetCollectionsByCollectionIdKeyframesResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        per_page=per_page,
        generate_signed_url=generate_signed_url,
        last_id=last_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 10,
    generate_signed_url: bool | Unset = True,
    last_id: str | Unset = UNSET,
) -> (
    Any
    | CollectionKeyframesSchema
    | GetCollectionsByCollectionIdKeyframesResponseDefaultType0
    | GetCollectionsByCollectionIdKeyframesResponseDefaultType1
    | None
):
    """Get all collection's keyframes


    Required roles:
     - can_read_collections

    Args:
        collection_id (str):
        per_page (int | Unset):  Default: 10.
        generate_signed_url (bool | Unset):  Default: True.
        last_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CollectionKeyframesSchema | GetCollectionsByCollectionIdKeyframesResponseDefaultType0 | GetCollectionsByCollectionIdKeyframesResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            per_page=per_page,
            generate_signed_url=generate_signed_url,
            last_id=last_id,
        )
    ).parsed
