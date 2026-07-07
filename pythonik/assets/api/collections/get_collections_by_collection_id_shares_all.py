from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.get_collections_by_collection_id_shares_all_response_default_type_0 import (
    GetCollectionsByCollectionIdSharesAllResponseDefaultType0,
)
from ...models.get_collections_by_collection_id_shares_all_response_default_type_1 import (
    GetCollectionsByCollectionIdSharesAllResponseDefaultType1,
)
from ...models.shares_elastic_schema import SharesElasticSchema
from ...types import Response


def _get_kwargs(
    collection_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/collections/{collection_id}/shares/all/".format(
            collection_id=quote(str(collection_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | GetCollectionsByCollectionIdSharesAllResponseDefaultType0
    | GetCollectionsByCollectionIdSharesAllResponseDefaultType1
    | SharesElasticSchema
):
    if response.status_code == 200:
        response_200 = SharesElasticSchema.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    def _parse_response_default(
        data: object,
    ) -> (
        GetCollectionsByCollectionIdSharesAllResponseDefaultType0
        | GetCollectionsByCollectionIdSharesAllResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = (
                GetCollectionsByCollectionIdSharesAllResponseDefaultType0.from_dict(
                    data
                )
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = (
            GetCollectionsByCollectionIdSharesAllResponseDefaultType1.from_dict(data)
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | GetCollectionsByCollectionIdSharesAllResponseDefaultType0
    | GetCollectionsByCollectionIdSharesAllResponseDefaultType1
    | SharesElasticSchema
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
) -> Response[
    Any
    | GetCollectionsByCollectionIdSharesAllResponseDefaultType0
    | GetCollectionsByCollectionIdSharesAllResponseDefaultType1
    | SharesElasticSchema
]:
    """Get list of collection's shares including all direct and indirect shares that were made by

     sharing collections that contain the collectionsharing collections that contain the collection
    Required roles:
     - can_read_shares

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCollectionsByCollectionIdSharesAllResponseDefaultType0 | GetCollectionsByCollectionIdSharesAllResponseDefaultType1 | SharesElasticSchema]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetCollectionsByCollectionIdSharesAllResponseDefaultType0
    | GetCollectionsByCollectionIdSharesAllResponseDefaultType1
    | SharesElasticSchema
    | None
):
    """Get list of collection's shares including all direct and indirect shares that were made by

     sharing collections that contain the collectionsharing collections that contain the collection
    Required roles:
     - can_read_shares

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCollectionsByCollectionIdSharesAllResponseDefaultType0 | GetCollectionsByCollectionIdSharesAllResponseDefaultType1 | SharesElasticSchema
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | GetCollectionsByCollectionIdSharesAllResponseDefaultType0
    | GetCollectionsByCollectionIdSharesAllResponseDefaultType1
    | SharesElasticSchema
]:
    """Get list of collection's shares including all direct and indirect shares that were made by

     sharing collections that contain the collectionsharing collections that contain the collection
    Required roles:
     - can_read_shares

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetCollectionsByCollectionIdSharesAllResponseDefaultType0 | GetCollectionsByCollectionIdSharesAllResponseDefaultType1 | SharesElasticSchema]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | GetCollectionsByCollectionIdSharesAllResponseDefaultType0
    | GetCollectionsByCollectionIdSharesAllResponseDefaultType1
    | SharesElasticSchema
    | None
):
    """Get list of collection's shares including all direct and indirect shares that were made by

     sharing collections that contain the collectionsharing collections that contain the collection
    Required roles:
     - can_read_shares

    Args:
        collection_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetCollectionsByCollectionIdSharesAllResponseDefaultType0 | GetCollectionsByCollectionIdSharesAllResponseDefaultType1 | SharesElasticSchema
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
        )
    ).parsed
