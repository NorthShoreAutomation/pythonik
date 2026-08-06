from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...models.bulk_share_create_schema import BulkShareCreateSchema
from ...models.post_share_by_object_type_response_default import (
    PostShareByObjectTypeResponseDefault,
)
from ...models.share_schema import ShareSchema
from ...types import Response


def _get_kwargs(
    object_type: str,
    *,
    body: BulkShareCreateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/share/{object_type}/".format(
            object_type=quote(str(object_type), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | PostShareByObjectTypeResponseDefault | ShareSchema:
    if response.status_code == 201:
        response_201 = ShareSchema.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    response_default = PostShareByObjectTypeResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | PostShareByObjectTypeResponseDefault | ShareSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkShareCreateSchema,
) -> Response[Any | PostShareByObjectTypeResponseDefault | ShareSchema]:
    """Create a new share of multiple objects (currently only assets are supported)


    Required roles:
     - can_write_shares

    Args:
        object_type (str):
        body (BulkShareCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostShareByObjectTypeResponseDefault | ShareSchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkShareCreateSchema,
) -> Any | PostShareByObjectTypeResponseDefault | ShareSchema | None:
    """Create a new share of multiple objects (currently only assets are supported)


    Required roles:
     - can_write_shares

    Args:
        object_type (str):
        body (BulkShareCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostShareByObjectTypeResponseDefault | ShareSchema
    """

    return sync_detailed(
        object_type=object_type,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkShareCreateSchema,
) -> Response[Any | PostShareByObjectTypeResponseDefault | ShareSchema]:
    """Create a new share of multiple objects (currently only assets are supported)


    Required roles:
     - can_write_shares

    Args:
        object_type (str):
        body (BulkShareCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PostShareByObjectTypeResponseDefault | ShareSchema]
    """

    kwargs = _get_kwargs(
        object_type=object_type,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    object_type: str,
    *,
    client: AuthenticatedClient | Client,
    body: BulkShareCreateSchema,
) -> Any | PostShareByObjectTypeResponseDefault | ShareSchema | None:
    """Create a new share of multiple objects (currently only assets are supported)


    Required roles:
     - can_write_shares

    Args:
        object_type (str):
        body (BulkShareCreateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PostShareByObjectTypeResponseDefault | ShareSchema
    """

    return (
        await asyncio_detailed(
            object_type=object_type,
            client=client,
            body=body,
        )
    ).parsed
