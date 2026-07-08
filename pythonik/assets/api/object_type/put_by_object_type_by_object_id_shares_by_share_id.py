from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_by_object_type_by_object_id_shares_by_share_id_response_default import (
    PutByObjectTypeByObjectIdSharesByShareIdResponseDefault,
)
from ...models.share_schema import ShareSchema
from ...types import Response


def _get_kwargs(
    object_type: str,
    object_id: str,
    share_id: str,
    *,
    body: ShareSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/{object_type}/{object_id}/shares/{share_id}/".format(
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
) -> Any | PutByObjectTypeByObjectIdSharesByShareIdResponseDefault | ShareSchema:
    if response.status_code == 200:
        response_200 = ShareSchema.from_dict(response.json())

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

    response_default = (
        PutByObjectTypeByObjectIdSharesByShareIdResponseDefault.from_dict(
            response.json()
        )
    )

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any | PutByObjectTypeByObjectIdSharesByShareIdResponseDefault | ShareSchema
]:
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
    body: ShareSchema,
) -> Response[
    Any | PutByObjectTypeByObjectIdSharesByShareIdResponseDefault | ShareSchema
]:
    """Update share


    Required roles:
     - can_write_shares

    Args:
        object_type (str):
        object_id (str):
        share_id (str):
        body (ShareSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutByObjectTypeByObjectIdSharesByShareIdResponseDefault | ShareSchema]
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
    body: ShareSchema,
) -> Any | PutByObjectTypeByObjectIdSharesByShareIdResponseDefault | ShareSchema | None:
    """Update share


    Required roles:
     - can_write_shares

    Args:
        object_type (str):
        object_id (str):
        share_id (str):
        body (ShareSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutByObjectTypeByObjectIdSharesByShareIdResponseDefault | ShareSchema
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
    body: ShareSchema,
) -> Response[
    Any | PutByObjectTypeByObjectIdSharesByShareIdResponseDefault | ShareSchema
]:
    """Update share


    Required roles:
     - can_write_shares

    Args:
        object_type (str):
        object_id (str):
        share_id (str):
        body (ShareSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PutByObjectTypeByObjectIdSharesByShareIdResponseDefault | ShareSchema]
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
    body: ShareSchema,
) -> Any | PutByObjectTypeByObjectIdSharesByShareIdResponseDefault | ShareSchema | None:
    """Update share


    Required roles:
     - can_write_shares

    Args:
        object_type (str):
        object_id (str):
        share_id (str):
        body (ShareSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PutByObjectTypeByObjectIdSharesByShareIdResponseDefault | ShareSchema
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
