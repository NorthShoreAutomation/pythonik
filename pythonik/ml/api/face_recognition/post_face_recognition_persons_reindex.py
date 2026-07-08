from http import HTTPStatus
from typing import Any, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_reindex_persons_schema import BulkReindexPersonsSchema
from ...models.post_face_recognition_persons_reindex_response_default import (
    PostFaceRecognitionPersonsReindexResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkReindexPersonsSchema,
    sync_assets: bool | Unset = UNSET,
    low_priority_indexing: bool | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["sync_assets"] = sync_assets

    params["low_priority_indexing"] = low_priority_indexing

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/face_recognition/persons/reindex/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostFaceRecognitionPersonsReindexResponseDefault:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    response_default = PostFaceRecognitionPersonsReindexResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostFaceRecognitionPersonsReindexResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkReindexPersonsSchema,
    sync_assets: bool | Unset = UNSET,
    low_priority_indexing: bool | Unset = UNSET,
) -> Response[Any | PostFaceRecognitionPersonsReindexResponseDefault]:
    """Trigger reindexing of persons by IDs


    Required roles:
     - can_reindex_person

    Args:
        sync_assets (bool | Unset):
        low_priority_indexing (bool | Unset):
        body (BulkReindexPersonsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionPersonsReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        sync_assets=sync_assets,
        low_priority_indexing=low_priority_indexing,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BulkReindexPersonsSchema,
    sync_assets: bool | Unset = UNSET,
    low_priority_indexing: bool | Unset = UNSET,
) -> Any | PostFaceRecognitionPersonsReindexResponseDefault | None:
    """Trigger reindexing of persons by IDs


    Required roles:
     - can_reindex_person

    Args:
        sync_assets (bool | Unset):
        low_priority_indexing (bool | Unset):
        body (BulkReindexPersonsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionPersonsReindexResponseDefault
    """

    return sync_detailed(
        client=client,
        body=body,
        sync_assets=sync_assets,
        low_priority_indexing=low_priority_indexing,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkReindexPersonsSchema,
    sync_assets: bool | Unset = UNSET,
    low_priority_indexing: bool | Unset = UNSET,
) -> Response[Any | PostFaceRecognitionPersonsReindexResponseDefault]:
    """Trigger reindexing of persons by IDs


    Required roles:
     - can_reindex_person

    Args:
        sync_assets (bool | Unset):
        low_priority_indexing (bool | Unset):
        body (BulkReindexPersonsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostFaceRecognitionPersonsReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        body=body,
        sync_assets=sync_assets,
        low_priority_indexing=low_priority_indexing,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BulkReindexPersonsSchema,
    sync_assets: bool | Unset = UNSET,
    low_priority_indexing: bool | Unset = UNSET,
) -> Any | PostFaceRecognitionPersonsReindexResponseDefault | None:
    """Trigger reindexing of persons by IDs


    Required roles:
     - can_reindex_person

    Args:
        sync_assets (bool | Unset):
        low_priority_indexing (bool | Unset):
        body (BulkReindexPersonsSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostFaceRecognitionPersonsReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            sync_assets=sync_assets,
            low_priority_indexing=low_priority_indexing,
        )
    ).parsed
