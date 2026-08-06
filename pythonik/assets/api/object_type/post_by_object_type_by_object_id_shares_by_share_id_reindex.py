from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.post_by_object_type_by_object_id_shares_by_share_id_reindex_response_default import (
    PostByObjectTypeByObjectIdSharesByShareIdReindexResponseDefault,
)
from ...models.reindex_share_schema import ReindexShareSchema
from ...types import Response


def _get_kwargs(
    object_type: str,
    object_id: str,
    share_id: str,
    *,
    body: ReindexShareSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/{object_type}/{object_id}/shares/{share_id}/reindex/".format(
            object_type=quote(str(object_type), safe=""),
            object_id=quote(str(object_id), safe=""),
            share_id=quote(str(share_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostByObjectTypeByObjectIdSharesByShareIdReindexResponseDefault:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    response_default = (
        PostByObjectTypeByObjectIdSharesByShareIdReindexResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostByObjectTypeByObjectIdSharesByShareIdReindexResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    object_id: str,
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexShareSchema,
) -> Response[Any | PostByObjectTypeByObjectIdSharesByShareIdReindexResponseDefault]:
    """Reindex the share


    Required roles:
     - can_reindex_shares

    Args:
        object_type (str):
        object_id (str):
        share_id (str):
        body (ReindexShareSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostByObjectTypeByObjectIdSharesByShareIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        share_id=share_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    object_id: str,
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexShareSchema,
) -> Any | PostByObjectTypeByObjectIdSharesByShareIdReindexResponseDefault | None:
    """Reindex the share


    Required roles:
     - can_reindex_shares

    Args:
        object_type (str):
        object_id (str):
        share_id (str):
        body (ReindexShareSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostByObjectTypeByObjectIdSharesByShareIdReindexResponseDefault
    """

    return sync_detailed(
        object_type=object_type,
        object_id=object_id,
        share_id=share_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    object_id: str,
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexShareSchema,
) -> Response[Any | PostByObjectTypeByObjectIdSharesByShareIdReindexResponseDefault]:
    """Reindex the share


    Required roles:
     - can_reindex_shares

    Args:
        object_type (str):
        object_id (str):
        share_id (str):
        body (ReindexShareSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostByObjectTypeByObjectIdSharesByShareIdReindexResponseDefault]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        object_id=object_id,
        share_id=share_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    object_id: str,
    share_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ReindexShareSchema,
) -> Any | PostByObjectTypeByObjectIdSharesByShareIdReindexResponseDefault | None:
    """Reindex the share


    Required roles:
     - can_reindex_shares

    Args:
        object_type (str):
        object_id (str):
        share_id (str):
        body (ReindexShareSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostByObjectTypeByObjectIdSharesByShareIdReindexResponseDefault
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            object_id=object_id,
            share_id=share_id,
            client=client,
            body=body,
        )
    ).parsed
