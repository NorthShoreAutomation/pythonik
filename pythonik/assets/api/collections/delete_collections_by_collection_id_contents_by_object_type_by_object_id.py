from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.delete_collections_by_collection_id_contents_by_object_type_by_object_id_response_default_type_0 import (
    DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0,
)
from ...models.delete_collections_by_collection_id_contents_by_object_type_by_object_id_response_default_type_1 import (
    DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1,
)
from ...types import Response


def _get_kwargs(
    collection_id: str,
    object_type: str,
    object_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/collections/{collection_id}/contents/{object_type}/{object_id}/".format(
            collection_id=quote(str(collection_id), safe=""),
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0
    | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1
):
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
        DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0
        | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1
    ):
        try:
            if not isinstance(data, dict):
                raise TypeError()
            response_default_type_0 = DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0.from_dict(
                data
            )

            return response_default_type_0
        except (TypeError, ValueError, AttributeError, KeyError):
            pass
        if not isinstance(data, dict):
            raise TypeError()
        response_default_type_1 = DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1.from_dict(
            data
        )

        return response_default_type_1

    response_default = _parse_response_default(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0
    | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: str,
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0
    | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1
]:
    """Delete a particular content object in a collection by id


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        object_type (str):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0 | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        object_type=object_type,
        object_id=object_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0
    | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1
    | None
):
    """Delete a particular content object in a collection by id


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        object_type (str):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0 | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1
    """

    return sync_detailed(
        collection_id=collection_id,
        object_type=object_type,
        object_id=object_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Any
    | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0
    | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1
]:
    """Delete a particular content object in a collection by id


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        object_type (str):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0 | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        object_type=object_type,
        object_id=object_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    object_type: str,
    object_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Any
    | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0
    | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1
    | None
):
    """Delete a particular content object in a collection by id


    Required roles:
     - can_write_collections

    Args:
        collection_id (str):
        object_type (str):
        object_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType0 | DeleteCollectionsByCollectionIdContentsByObjectTypeByObjectIdResponseDefaultType1
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            object_type=object_type,
            object_id=object_id,
            client=client,
        )
    ).parsed
